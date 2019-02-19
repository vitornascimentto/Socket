from socket import *

serverHost = 'localhost'
serverPort = 30800

sockObj = socket(AF_INET, SOCK_STREAM)
sockObj.connect((serverHost, serverPort))

#link = b'https://www.youtube.com/watch?v=8TqSsx0Y7Gg'

link = str(input('Digite o link do vídeo: ')).encode('utf-8')

sockObj.send(link)

data = sockObj.recv(1024).decode()
print('Download Concluído')
print(data)

sockObj.close()