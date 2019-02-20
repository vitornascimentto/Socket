import os
from menu import menu
from socket import *

serverHost = 'localhost'
serverPort = 30801

sockObj = socket(AF_INET, SOCK_STREAM)
sockObj.connect((serverHost, serverPort))

        
sockObj.send(menu().encode('utf-8'))

titulo = sockObj.recv(1024).decode('utf-8')

with open('{}.mp3'.format(titulo),'wb') as f:
    l = sockObj.recv(10240)
    while l:
        f.write(l)
        l = sockObj.recv(10240)

path = os.path.dirname(os.path.realpath(__file__))
print('Salvo em: {}'.format(path))

sockObj.close()