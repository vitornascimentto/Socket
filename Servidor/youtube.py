from __future__ import unicode_literals
import youtube_dl

class Youtube:

    parametros = {
        'outtmpl': '{}.%(ext)s'.format(None),
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': None,
        }],
    }

    def setParametros(self, url, titulo=None, qualidade=None):
        self.parametros['outtmpl'] = '{}.%(ext)s'.format(self.getTitulo(url, titulo))
        self.parametros['postprocessors'][0]['preferredquality'] = self.getQualidade(qualidade)

    def getTitulo(self, url, titulo=None):
        if titulo != None:
            return titulo
        else:
            with youtube_dl.YoutubeDL(self.parametros) as ydl:
                return ydl.extract_info(url, download=False)['title']

    def getQualidade(self, qualidade):
        if qualidade in ['48', '96', '192']:
            return qualidade
        else:
            return '192'
    
    def getInformacoes(self, url):
        with youtube_dl.YoutubeDL(self.parametros) as ydl:
            informacoes = ydl.extract_info(url, download=False)
        return('Título: {}, duração: {}s, qualidade: {}k.'.format(informacoes['title'], informacoes['duration'], self.parametros['postprocessors'][0]['preferredquality']))

    def download(self, url):
        with youtube_dl.YoutubeDL(self.parametros) as ydl:
            ydl.download([url])
