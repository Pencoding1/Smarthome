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

delay_sending = 10
def PIR():
  global delay_sending
  if delay_sending >= 10:
    if not cam() and pin20.read_digital()==1:
        http_response = urequests.get((''.join([str(x) for x in ['https://api.telegram.org/bot', TOKEN, '/sendMessage?text=', 'có người vào nhà', '&chat_id=', ID]])))
        http_response.close()
    elif cam() == "NL" and pin20.read_digital()==1:
        http_response = urequests.get((''.join([str(x) for x in ['https://api.telegram.org/bot', TOKEN, '/sendMessage?text=', 'có người vào nhà', '&chat_id=', ID]])))
        http_response.close()
    else:
      tiny_rgb.show(0, hex_to_rgb('#323E42'))
    delay_sending = 0
  delay_sending += 1
  print(delay_sending)

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

# Mô tả hàm này...
def cam():
  global cam_input
  cam_input = cam_input
  if cam_input == 'NQ':
    return True
  elif cam_input == 'NL':
    return "NL"
  return False
  print(cam_input)
  

# Khóa cửa
fail, counting = 0, 0
def door():
  global fail, counting
  locked = False
  if fail >= 8 and counting < 30:
    locked = True
    counting += 1

  elif counting >= 30:
    locked = False
    counting = 0
    fail = 0
    print(fail)
  print(f"counting: {counting}, fail: {fail}, locked: {locked}")
    
  if not locked:

    if cam() == True:
      pin4.servo_write(60)
      time.sleep_ms(3000)
      pin4.servo_write(0)
    elif cam() == "NL":
      fail += 1
  
  
if True:
  wifi.connect_wifi('LMHT', '0916628391')
  mqtt.connect_wifi('LMHT', '0916628391')
  mqtt.connect_broker(server='io.adafruit.com', port=1883, username='Pen215', password='aio_MJpt91Ige2Y8WtNHLeXQr7wgbsQB')
  gc.collect()
  pass

while True:
  mqtt.check_message()
  cam()
  door()
  PIR()
  time.sleep_ms(1000)
  
