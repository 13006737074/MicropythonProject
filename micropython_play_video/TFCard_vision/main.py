from time import sleep_ms
import os, machine, gc
from ssd1306 import SSD1306_I2C
from machine import I2C,Pin
import framebuf,time

SD_SW = Pin(5, Pin.IN)
os.mount(machine.SDCard(), '/sd')

i2c = I2C(sda = Pin(23),scl = Pin(22))
display = SSD1306_I2C(128,64,i2c)

for i in range(1,41):
    dirt = 'sd/BAD_APPLE/' + str(i) + '.pbm'
    print(i)
    with open(dirt,'rb') as f :
        f.readline()
        f.readline()
        data = bytearray(f.read())
        fbuf = framebuf.FrameBuffer(data,88,64,framebuf.MONO_HLSB)
        display.fill(0)
        display.blit(fbuf,19,0)
        display.show()
        del fbuf
        time.sleep(0.2)

