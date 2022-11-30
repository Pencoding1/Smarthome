from yolobit_wifi import *
from mqtt import *
import urequests
import gc
import time
from yolobit import *
import sys
import uselect
from homebit3_rgbled import RGBLed

tiny_rgb = RGBLed(pin0.pin, 4)
TOKEN = "5955181205:AAHsgeilXg28sIMwDXmc77wmiQgYro3eN9I"
ID = "-895508981"
Wifi = "LMHT"
password = "0916628391"


def read_terminal_input():
  """Đọc thông tin từ camera"""
  spoll=uselect.poll()        # Set up an input polling object.
  spoll.register(sys.stdin, uselect.POLLIN)    # Register polling object.

  input = ''
  if spoll.poll(0):
    input = sys.stdin.read(1)

    while spoll.poll(0):
      input = input + sys.stdin.read(1)

  spoll.unregister(sys.stdin)
  return input


delay_sending = 20
def sending_mess(mode):
  """Gửi tin nhắn về telegram"""
  global delay_sending, sending_excution_time
  sending_time = 0
  
  if delay_sending >= 20:
    if not mode:
      start = round(time.time())
      http_response = urequests.get((''.join([str(x) for x in ['https://api.telegram.org/bot', TOKEN, '/sendMessage?text=', 'có người lạ đứng trước cửa', '&chat_id=', ID]])))
      http_response.close()
      sending_time = (round(time.time()) - start)
      # print(f"sending_time: {sending_time}")
    
    elif mode == 2:
      return
    
    else:
      start = round(time.time())
      http_response = urequests.get((''.join([str(x) for x in ['https://api.telegram.org/bot', TOKEN, '/sendMessage?text=', 'có người vào nhà', '&chat_id=', ID]])))
      http_response.close()
      sending_time = (round(time.time()) - start)
      # print(f"sending_time: {sending_time}")
    
    delay_sending = 0
  
  delay_sending += (1 + sending_time)
  sending_excution_time = sending_time
  sending_time = 0
  # print("delay_sending: {}".format(delay_sending))


def PIR(cam=None, off=None):
  """Điều khiển PIR"""
  if not off:
    if pin20.read_digital()!= 1:
    
      if not cam:
        sending_mess(1)
    
      elif cam == "NL":
        sending_mess(1)
      else:
        return
  else:
    return


def cam():
  """Nhận diện khuôn mặt"""
  global cam_input
  cam_input = "NQ"
  
  if cam_input == 'NQ':
    return True
  
  elif cam_input == 'NL':
    return "NL"
  
  # print(cam_input)
  return False


def door():
  """Hệ thống cửa tự động"""
  global delay_sending
  pin4.servo_write(60)
  time.sleep_ms(5000)
  delay_sending += 5
  pin4.servo_write(180)

fail, counting, delay = 0, 0, 5
def security_system(permision):
  """Hệ thống bảo mật của cửa"""
  global fail, delay,counting, delay_sending, sending_excution_time
  locked = False
  sending = True
  
  if fail >= 8 and counting < 30:
    
    if sending:
      sending_mess(0)
      sending = False
    locked = True
    counting += (1 + sending_excution_time)
    sending_excution_time = 0

  elif counting >= 30:
    
    fail = 0
    sending = True
    locked = False
    counting = 0
    
    # print(fail)
  
  # print(f"counting: {counting}, fail: {fail}, locked: {locked}")
    
  if not locked and delay>=5:

    if permision and permision != "NL":
      door()
    
    elif permision == "NL":
      fail += 1
    delay = 0
  # print(delay)
  delay += 1
  

def on_mqtt_message_receive_callback__work_please_(info):
  """Điều khiển IOT"""
  global delay
  if info == "1":
    PIR(off=True)
    door()
    PIR(off=False)
    delay -= 2
  else:
    return
  
  
if __name__ == "__main__":
  if True:
    wifi.connect_wifi(Wifi, password)
    mqtt.connect_wifi(Wifi, password)
    mqtt.connect_broker(server='io.adafruit.com', port=1883, username='Pen215', password='aio_LmGo95rUINBj0MRsqTIOMEKHoaWo')
    mqtt.on_receive_message('work-please', on_mqtt_message_receive_callback__work_please_)
    gc.collect()

  while True:
    if not turn_off:
      mqtt.check_message()
      sending_mess(2)
      camera = cam()
      security_system(camera)
      PIR(cam=camera)
    time.sleep_ms(1000)