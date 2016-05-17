#!/usr/bin/env python

import socket
from time import sleep
import collections

ip = '192.168.0.104'
port = 80

delay = 1
brightness = b = 0.25
pixels = 75
banner_size = 6

red_pixel = [0*b, 255*b, 0*b]
green_pixel = [255*b, 0*b, 0*b]

pattern = []

while len(pattern) <= pixels * 3:
    if (len(pattern) / banner_size) % 2 == 0:
        pattern += red_pixel * banner_size
    else:
        pattern += green_pixel * banner_size

deque = collections.deque(pattern)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Rotate for 1 RGB position
    deque.rotate(3)

    # Compose and send the RGB message
    message = ''.join(chr(int(i)) for i in deque)
    s.sendto(message, (ip, port))

    sleep(delay)

s.close()
