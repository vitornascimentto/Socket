from __future__ import unicode_literals
import youtube_dl
import youtube
from socket import *

meuHost = ''
minhaPort = 30800
sockObj = socket(AF_INET, SOCK_STREAM)

sockObj.bind((meuHost, minhaPort))
sockObj.listen(5)

yt = youtube.Youtube()

for i in range(1):
    conexao, endereco = sockObj.accept()
    print('O servidor está conectado por', endereco)

    data = conexao.recv(1024).decode()
    print('link:', data)
    
    yt.setParametros(data)
    yt.download(data)

    if not data:
        print('No data')
        break
        
    conexao.send(data)

conexao.close()

