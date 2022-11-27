from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
from homebit3_rgbled import RGBLed

tiny_rgb = RGBLed(pin14.pin, 4)
# round(translate((pin0.read_analog()), 0, 4095, 0, 100)): light sensor
# light_level(): light sensor
# pin10.write_analog(round(translate(70,0,100,0,1023))): Fan
# temperature(): temperature sensor
# tiny_rgb.show(0, hex_to_rgb('#ff0000'))
def l_C3_A0m_g_C3_AC__C4_91_C3_B3():
  global tiny_rgb
  if light_level() == 0:
    tiny_rgb.show(0, hex_to_rgb('#ff0000'))
  elif (round(translate((pin0.read_analog()), 0, 4095, 0, 100))) == '':
    pin10.write_analog(round(translate(70, 0, 100, 0, 1023)))
  elif temperature() == 0:
    pass
def light():
  if light_level() <= 30:
    tiny_rgb.show(0, hex_to_rgb('#ffffff'))
  else:
    tiny_rgb.show(0, hex_to_rgb('#000000'))

def fan():
  if temperature() > 30:
    pin10.write_analog(round(translate(70, 0, 100, 0, 1023)))

while True:
    pass
