from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
from homebit3_rgbled import RGBLed
import time

tiny_rgb = RGBLed(pin1.pin, 4)
tiny_rgb2 = RGBLed(pin10.pin, 4)
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
def light():
  print(light_level(),":1")
  if light_level() <= 20:
    tiny_rgb.show(0, hex_to_rgb('#ffffff'))
  else:
    tiny_rgb.show(0, hex_to_rgb('#000000'))

def light2():
  print(round(translate((pin0.read_analog()), 0, 4095, 0, 100)),":2")
  if round(translate((pin0.read_analog()), 0, 4095, 0, 100)) <= 20:
    tiny_rgb2.show(0, hex_to_rgb('#ffffff'))
    tiny_rgb.show(0, hex_to_rgb('#ffffff'))
  else:
    tiny_rgb2.show(0, hex_to_rgb('#000000'))
    tiny_rgb.show(0, hex_to_rgb('#000000'))

def fan():
  print(temperature())
  if 25 <= round(temperature()) <= 28:
    pin2.write_analog(round(translate(70, 0, 100, 0, 1023)))
  elif round(temperature()) > 32:
    pin2.write_analog(round(translate(100, 0, 100, 0, 1023)))
if True:
  pass

while True:
  light2()
  time.sleep_ms(1000)
