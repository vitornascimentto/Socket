from socket import *

serverHost = 'localhost'
serverPort = 30808

sockObj = socket(AF_INET, SOCK_STREAM)
sockObj.connect((serverHost, serverPort))

#https://www.youtube.com/watch?v=8TqSsx0Y7Gg

link = str(input('Digite o link do vídeo: ')).encode('utf-8')

sockObj.send(link)

titulo = sockObj.recv(1024).decode('utf-8')

with open('{}.mp3'.format(titulo),'wb') as f:
    l = sockObj.recv(10240)
    while l:
        f.write(l)
        l = sockObj.recv(10240)

sockObj.close()