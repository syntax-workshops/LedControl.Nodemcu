#!/usr/bin/env python

import sys
import socket
from time import sleep

ip = '192.168.1.212'
port = 80
pixels = 150
sleep = 1

color = sys.argv[1:]

def string_char_array(arr):
    return ''.join(chr(int(i)) for i in arr)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    message = string_char_array(color*pixels)
    s.sendto(message, (ip, port))
except:
    s.close()
    print("LED client Exiting")
s.close()
