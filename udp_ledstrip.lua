-- The control pin for your LED strip
pin = 2

-- Amount of LED pixels on the strip
pixels = 5 * 30

-- WiFi config
ssid = "Your wifi network"
psk = "Your wifi password"

-- UDP port to receive data on
port = 80

-- That's all, you don't have to edit anything else!

wifi.setmode(wifi.STATION)
wifi.sta.config(ssid, psk)
print("LED server starting!")

srv=net.createServer(net.UDP)

srv:on("receive", function(client, data)
    ws2812.write(pin, data)
end)

-- Clear the strip (write all black pixels to it once)
ws2812.write(pin, string.char( 0,  0,  0):rep(pixels))

srv:listen(80)
print("LED server running!")
