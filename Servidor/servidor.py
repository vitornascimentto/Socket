from __future__ import unicode_literals
import os
import youtube 
from socket import *

meuHost = ''
minhaPort = 30801
sockObj = socket(AF_INET, SOCK_STREAM)

sockObj.bind((meuHost, minhaPort))
sockObj.listen(5)

print('Aguardando conexão...')

yt = youtube.Youtube()

conexao, endereco = sockObj.accept()
print('O servidor está conectado por', endereco)

parametros = conexao.recv(1024).decode('utf-8')
parametros = yt.getSplit(parametros)

yt.setParametros(parametros[0], parametros[1], parametros[2])
yt.download(parametros[0])

conexao.send(yt.getTitulo(parametros[0], parametros[1]).encode('utf-8'))

with open('{}.mp3'.format(yt.getTitulo(parametros[0], parametros[1])), 'rb') as f:
    arquivo = f.read(10240)

    while arquivo:
        conexao.send(arquivo)
        arquivo = f.read(10240)

    os.remove('{}.mp3'.format(yt.getTitulo(parametros[0], parametros[1])))
        
conexao.close()

