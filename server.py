from __future__ import unicode_literals
import youtube_dl

from socket import *

meuHost = ''
minhaPort = 30801
sockObj = socket(AF_INET, SOCK_STREAM)

sockObj.bind((meuHost, minhaPort))
sockObj.listen(5)

def youtube(link):
    link[1::]
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

for i in range(1):
    conexao, endereco = sockObj.accept()
    print('O servidor está conectado por', endereco)

    data = conexao.recv(1024).decode()
    print('link:', data)
    varTemporaria = youtube(data)
    
    if not data:
        print('No data')
        break
        
    conexao.send(data)

conexao.close()

