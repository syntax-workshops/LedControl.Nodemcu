# LedControl.Nodemcu

Control a RGB LED strip over the network using an esp8266 and UDP!

## Technical

This program lets you control the colors on a ws2812b LED strip in an extremely
simple way. It runs a UDP server listening on port 80 (configurable in `config.lua`).
A UDP packet sent to it must contain red, green and blue values ranging from 0
to 255, repeated in sequence for every LED you want to color.
For example: if your strip has 50 LED's, you want to send 50 * 3 = 150 bytes
to color all of them.

## Installation

Grab Nodemcu firmware release 0.9.6-dev or later [from GitHub](https://github.com/nodemcu/nodemcu-firmware/releases). Flash it to your microcontroller using [esptool](https://github.com/themadinventor/esptool) or a similar program:

```
esptool --port /dev/tty.SLAB_USBtoUART write_flash 0x00 ~/Downloads/nodemcu_float_0.9.6-dev_20150704.bin
```

Grab a copy of this repository. Configure the settings for wifi and you data pin in `config.lua`. Upload all `.lua` files to your microcontroller using [luatool](https://github.com/4refr0nt/luatool) or a similar program:

```
luatool -p /dev/tty.SLAB_USBtoUART -b 9600 -f ~/Downloads/LedControl.Nodemcu/udp_ledstrip.lua
luatool -p /dev/tty.SLAB_USBtoUART -b 9600 -f ~/Downloads/LedControl.Nodemcu/config.lua
luatool -p /dev/tty.SLAB_USBtoUART -b 9600 -f ~/Downloads/LedControl.Nodemcu/init.lua
```

Connect the data pin of the LED strip to the configured data pin on your esp8266. Also ensure they are both connected to the same ground.

That should be it! You can control the strip using the [iOS app](https://github.com/syntax-workshops/LedControl.iOS) or the [Android app](https://github.com/syntax-workshops/LedControl.Android).

## License

MIT, see `LICENSE.txt`
