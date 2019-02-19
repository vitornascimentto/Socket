import menu
from socket import *

serverHost = 'localhost'
serverPort = 30805

sockObj = socket(AF_INET, SOCK_STREAM)
sockObj.connect((serverHost, serverPort))

        
sockObj.send(menu.menu().encode('utf-8'))

titulo = sockObj.recv(1024).decode('utf-8')
#status = sockObj.recv(1024).decode('utf-8')

#print(status)

with open('{}.mp3'.format(titulo),'wb') as f:
    l = sockObj.recv(10240)
    while l:
        f.write(l)
        l = sockObj.recv(10240)

sockObj.close()