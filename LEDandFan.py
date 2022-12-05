from yolobit import *
from homebit3_rgbled import RGBLed
import time
from mqtt import *

tiny_rgb = RGBLed(pin1.pin, 4)
tiny_rgb2 = RGBLed(pin10.pin, 4)
# pin2.write_analog(round(translate(0, 0, 100, 0, 1023)))
# tiny_rgb.show(0, hex_to_rgb('#ff0000'))
# pin14.write_analog(round(translate(100, 0, 100, 0, 1023)))

def on_mqtt_message_receive_callback__V1_(info):
  if int(info):
    print(info, "LED 2")
    tiny_rgb.show(0, hex_to_rgb('#ffffff'))
  else:
    tiny_rgb.show(0, hex_to_rgb('#000000'))

def on_mqtt_message_receive_callback__V2_(info):
  if int(info):
    print(info, "LED 2")
    tiny_rgb2.show(0, hex_to_rgb('#ffffff'))
  else:
    tiny_rgb2.show(0, hex_to_rgb('#000000'))

def on_mqtt_message_receive_callback__V3_(info):
  print(info, "Fan 1")
  pin2.write_analog(round(translate(int(info), 0, 100, 0, 1023)))
    
def on_mqtt_message_receive_callback__V4_(info):
  print(info, "Fan 2")
  pin14.write_analog(round(translate(int(info), 0, 100, 0, 1023)))

if __name__ == "__main__":
  if True:
      mqtt.connect_wifi('LMHT', '0916628391')
      mqtt.connect_broker(server='mqtt.ohstem.vn', port=1883, username='Pen215', password='')
      mqtt.on_receive_message('V1', on_mqtt_message_receive_callback__V1_) # LED 1
      mqtt.on_receive_message('V2', on_mqtt_message_receive_callback__V2_) # LED 2
      mqtt.on_receive_message('V3', on_mqtt_message_receive_callback__V3_) # Fan 1
      mqtt.on_receive_message('V4', on_mqtt_message_receive_callback__V4_) # Fan 2
  
  while True:
    mqtt.check_message()
    time.sleep_ms(1000)
