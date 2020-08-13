import socket,time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 8080

s.bind((host,port))
s.listen(5)

print('等待客户端连接中…')

client,client_address = s.accept()
print('新连接')
print('IP:'+str(client_address[0]))
client_IP = str(client_address[0])
print('Port:' + str(client_address[1]))
client_port = str(client_address[1])


for i in range(1,360):
    dirt = 'after/' + str(i) + '.pbm'
    with open(dirt,'rb') as f:
        f.readline()
        f.readline()
        data= f.read()
        client.send(data)
        print(i)
        time.sleep(0.19)


