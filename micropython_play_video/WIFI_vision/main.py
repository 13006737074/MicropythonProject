import socket,framebuf,time,machine
from machine import I2C,Pin
from ssd1306 import SSD1306_I2C

i2c = I2C(scl = Pin(23),sda = Pin(22))
display = SSD1306_I2C(128,64,i2c)
host = '192.168.137.1'
port = 8080

s = socket.socket()
addr = (host,port)
s.connect(addr)

i = 0

while True:
    data = s.recv(1024)
    if data != 0:
        fbuf = framebuf.FrameBuffer(bytearray(data),88,64,framebuf.MONO_HLSB)
        display.fill(0)
        display.blit(fbuf,19,0)
        display.show()
        del data

