from yolobit import *
from homebit3_rgbled import RGBLed
import time
from mqtt import *

tiny_rgb = RGBLed(pin1.pin, 4)
tiny_rgb2 = RGBLed(pin10.pin, 4)
auto = True
# round(translate((pin0.read_analog()), 0, 4095, 0, 100)): light sensor
# light_level(): light sensor
# pin10.write_analog(round(translate(70,0,100,0,1023))): Fan
# temperature(): temperature sensor
# tiny_rgb.show(0, hex_to_rgb('#ff0000'))
# def l_C3_A0m_g_C3_AC__C4_91_C3_B3():
#   global tiny_rgb
#   if light_level() == 0:
#     tiny_rgb.show(0, hex_to_rgb('#ff0000'))
#   elif (round(translate((pin0.read_analog()), 0, 4095, 0, 100))) == '':
#     pin10.write_analog(round(translate(70, 0, 100, 0, 1023)))
#   elif temperature() == 0:
#     pass
def on_mqtt_message_receive_callback__auto_(info):
  """Điều khiển IOT"""
  global auto
  if info == "1":
    auto = True
  else:
    auto = False
  


def light():
  print(light_level(),":1")
  # if light_level() <= 20:
  if True:
    tiny_rgb.show(0, hex_to_rgb('#ffffff'))
  else:
    tiny_rgb.show(0, hex_to_rgb('#000000'))

def light2():
  print(round(translate((pin0.read_analog()), 0, 4095, 0, 100)),":2")
  # if round(translate((pin0.read_analog()), 0, 4095, 0, 100)) <= 20:
  if True:
    tiny_rgb2.show(0, hex_to_rgb('#ffffff'))
    tiny_rgb.show(0, hex_to_rgb('#ffffff'))
  else:
    tiny_rgb2.show(0, hex_to_rgb('#000000'))
    tiny_rgb.show(0, hex_to_rgb('#000000'))

def fan():
  print(temperature())
  # if 25 <= round(temperature()) <= 28:
  if True:
    pin14.write_analog(round(translate(70, 0, 100, 0, 1023)))
  elif round(temperature()) > 32:
    pin14.write_analog(round(translate(100, 0, 100, 0, 1023)))

def fan2():
  print(temperature())
  # if 25 <= round(temperature()) <= 28:
  if True:
    pin2.write_analog(round(translate(70, 0, 100, 0, 1023)))
  elif round(temperature()) > 32:
    pin2.write_analog(round(translate(0, 0, 100, 0, 1023)))


if __name__ == "__main__":
  if True:
      mqtt.connect_wifi('LMHT', '0916628391')
      mqtt.connect_broker(server='io.adafruit.com', port=1883, username='Pen215', password='aio_LmGo95rUINBj0MRsqTIOMEKHoaWo')
      mqtt.on_receive_message('auto', on_mqtt_message_receive_callback__auto_)
  
  while True:
    mqtt.check_message()
    fan()
    fan2()
    light2()
    light()
    time.sleep_ms(1000)
