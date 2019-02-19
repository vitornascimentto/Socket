def menu():
    while True:
        url = str(input('URL do vídeo no YouTube: '))
        if url != '':
            break
        else:
            print('URL inválida.')
            continue
    
    titulo = str(input('Título para o arquivo MP3: '))
    if titulo == '':
        titulo = None
    
    qualidade = str(input('Qualidade desejada (48, 96, 192): '))
    if qualidade == '':
        qualidade = None
    
    return '{}|{}|{}'.format(url, titulo, qualidade)



    

