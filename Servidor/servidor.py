from __future__ import unicode_literals
from source import youtube 
from socket import *
import os

meuHost = ''
minhaPort = 30805
sockObj = socket(AF_INET, SOCK_STREAM)

sockObj.bind((meuHost, minhaPort))
sockObj.listen(5)

yt = youtube.Youtube()

for i in range(1):
    conexao, endereco = sockObj.accept()
    print('O servidor está conectado por', endereco)

    parametros = conexao.recv(1024).decode('utf-8')
    parametros = yt.getSplit(parametros)

    yt.setParametros(parametros[0], parametros[1], parametros[2])
    yt.download(parametros[0])
    
    conexao.send(yt.getTitulo(parametros[0], parametros[1]).encode('utf-8'))
    #conexao.send('Download concluído.'.encode('utf-8'))

    with open('{}.mp3'.format(yt.getTitulo(parametros[0], parametros[1])), 'rb') as f: 
        arquivo = f.read(10240)
    
        while arquivo:    
            conexao.send(arquivo)
            arquivo = f.read(10240)

        os.remove('{}.mp3'.format(yt.getTitulo(parametros[0], parametros[1])))
        
conexao.close()

