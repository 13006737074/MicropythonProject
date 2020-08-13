#boot.py
import network
import ssd1306
from machine import Pin
import time


WIFI_LED=Pin(12, Pin.OUT) #初始化WIFI指示灯
wlan = network.WLAN(network.STA_IF) #STA模式
wlan.active(True)#激活接口
start_time=time.time()#记录时间做超时判断

if not wlan.isconnected():
  print('connecting to network...')
  wlan.connect('iPhone', 'chenjixuan308') #输入WIFI账号密码

  while not wlan.isconnected():
    #未连接到WIFI时LED闪烁提示
    WIFI_LED.value(1)
    time.sleep_ms(300)
    WIFI_LED.value(0)
    time.sleep_ms(300)

    #超时判断,15秒没连接成功判定为超时
    if time.time()-start_time > 15 :
      print('WIFI Connected Timeout!')
      break

if wlan.isconnected():#如果WIFI连接上，就把网络的各种参数输出在OLED屏幕中
  #LED点亮
  WIFI_LED.value(1)

#串口打印信息
  print('network information:', wlan.ifconfig())



