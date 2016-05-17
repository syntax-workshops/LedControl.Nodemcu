#!/usr/bin/env python

import socket
from time import sleep

IP = '192.168.1.154'
PORT = 80

def string_char(*args):
    return ''.join(chr(int(i)) for i in args)

# The following is a shameless Python port of:
# https://github.com/geekscape/nodemcu_esp8266/blob/master/examples/ws2812.lua

BRIGHT     = 1.0
ON         = BRIGHT * 255
PIXELS     = 75
DELAY      = 0.01

def colourWheel(index):
    if index < 85:
        return string_char(index * 3 * BRIGHT, (255 - index * 3) * BRIGHT, 0)
    elif index < 170 :
        index = index - 85
        return string_char((255 - index * 3) * BRIGHT, 0, index * 3 * BRIGHT)
    else:
        index = index - 170
        return string_char(0, index * 3 * BRIGHT, (255 - index * 3) * BRIGHT)

rainbow_speed = 4

def rainbow(index):
  buffer = ""
  for pixel in range(0, PIXELS):
      buffer = buffer + colourWheel((index + pixel * rainbow_speed) % 256)
  return buffer

rainbow_index = 0

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while 1:
        message = rainbow(rainbow_index)
        rainbow_index = (rainbow_index + 1) % 256
        s.sendto(message, (IP, PORT))
        sleep(DELAY)
except:
    s.close()
    print(" LED rainbow Exiting")
