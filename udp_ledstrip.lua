dofile("config.lua")

wifi.setmode(wifi.STATION)
wifi.sta.config(ssid, psk)
print("LED server starting!")

srv = net.createServer(net.UDP)

srv:on("receive", function(client, data)
    ws2812.write(pin, data)
end)

-- Clear the strip (write all black pixels to it once)
ws2812.write(pin, string.char(0,  0,  0):rep(pixels))

srv:listen(port)
print("LED server running!")
