from hmc5883l import HMC5883L

sencer = HMC5883L()
while True:
    x,y,z = sencer.read()
    print(x,y,z)
    a,b = sencer.heading(x,y)
    print(a,'°',b,"'")
    pyb.delay(500)


