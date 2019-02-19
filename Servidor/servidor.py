from __future__ import unicode_literals
import youtube_dl
import youtube
from socket import *
import os

meuHost = ''
minhaPort = 30808
sockObj = socket(AF_INET, SOCK_STREAM)

sockObj.bind((meuHost, minhaPort))
sockObj.listen(5)

yt = youtube.Youtube()

for i in range(1):
    conexao, endereco = sockObj.accept()
    print('O servidor está conectado por', endereco)

    url = conexao.recv(1024).decode('utf-8')

    yt.setParametros(url)
    yt.download(url)
    
    conexao.send(yt.getTitulo(url).encode('utf-8'))

    with open('{}.mp3'.format(yt.getTitulo(url)), 'rb') as f: 
        arquivo = f.read(10240)
    
        while arquivo:    
            conexao.send(arquivo)
            arquivo = f.read(10240)

        os.remove('{}.mp3'.format(yt.getTitulo(url)))
        
conexao.close()

