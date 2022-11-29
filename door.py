from yolobit_wifi import *
from mqtt import *
import urequests
import gc
import time
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
import sys
import uselect
from homebit3_rgbled import RGBLed

tiny_rgb = RGBLed(pin0.pin, 4)
TOKEN = "5955181205:AAHsgeilXg28sIMwDXmc77wmiQgYro3eN9I"
ID = "-895508981"

def read_terminal_input():
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
  global delay_sending, sending_excution_time
  sending_time = 0
  
  if delay_sending >= 20:
    if not mode:
      start = round(time.time())
      http_response = urequests.get((''.join([str(x) for x in ['https://api.telegram.org/bot', TOKEN, '/sendMessage?text=', 'có người lạ đứng trước cửa', '&chat_id=', ID]])))
      http_response.close()
      sending_time = (round(time.time()) - start)
      print(f"sending_time: {sending_time}")
    
    elif mode == 2:
      return
    
    else:
      start = round(time.time())
      http_response = urequests.get((''.join([str(x) for x in ['https://api.telegram.org/bot', TOKEN, '/sendMessage?text=', 'có người vào nhà', '&chat_id=', ID]])))
      http_response.close()
      sending_time = (round(time.time()) - start)
      print(f"sending_time: {sending_time}")
    
    delay_sending = 0
  
  delay_sending += (1 + sending_time)
  sending_excution_time = sending_time
  sending_time = 0
  print("delay_sending: {}".format(delay_sending))


def PIR(cam=None, off=None):
  if pin20.read_digital()!= 1:
  
    if not cam:
      sending_mess(1)
  
    elif cam == "NL":
      sending_mess(1)
    else:
      return



def cam():
  global cam_input
  cam_input = "NQ"
  
  if cam_input == 'NQ':
    return True
  
  elif cam_input == 'NL':
    return "NL"
  
  print(cam_input)
  return False
  
  

# Khóa cửa
def door():
  global delay_sending
  pin4.servo_write(60)
  time.sleep_ms(5000)
  delay_sending += 5
  pin4.servo_write(180)

fail, counting, delay = 0, 0, 5
def security_system(permision):
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
    
    print(fail)
  
  print(f"counting: {counting}, fail: {fail}, locked: {locked}")
    
  if not locked and delay>=5:

    if permision and permision != "NL":
      door()
    
    elif permision == "NL":
      fail += 1
    delay = 0
  print(delay)
  delay += 1
  
  
if __name__ == "__main__":
  if True:
    wifi.connect_wifi('LMHT', '0916628391')
    mqtt.connect_wifi('LMHT', '0916628391')
    mqtt.connect_broker(server='io.adafruit.com', port=1883, username='Pen215', password='aio_MJpt91Ige2Y8WtNHLeXQr7wgbsQB')
    gc.collect()

  while True:
    mqtt.check_message()
    sending_mess(2)
    camera = cam()
    security_system(camera)
    PIR(cam=camera)
    time.sleep_ms(1000)
  
