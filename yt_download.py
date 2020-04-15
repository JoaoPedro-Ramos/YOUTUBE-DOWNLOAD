import pyttsx3
from pytube import YouTube, Playlist

speak = pyttsx3.init('sapi5')

def speaking(s):
    speak.say(s)
    speak.runAndWait()

def menu():
    phrase = '''OLÁ, BEM VINDO AO YOUTUBE DOWNLOAD
    ESCOLHA O QUE VOCÊ DESEJA FAZER:
    [ 1 ] PARA BAIXAR UM VÍDEO
    [ 2 ] PARA BAIXAR UMA PLAYLIST
    [ 3 ] PARA BAIXAR SOMENTE O ÁUDIO DE UM VÍDEO (arquivo MP4)'''
    print(phrase)
    speaking(phrase)
    escolha_()

def escolha_():
    n = int(input('POR FAVOR DIGITE A OPÇÃO DESEJADA: '))
    if n <= 3 and n >= 1:
        caminhos(n)
    else:
        escolha_()


def caminhos(x):
    if x == 1:
        download_video()
    elif x == 2:
        download_playlist()
    elif x == 3:
        download_audio()


def download_video():
    speaking('POR FAVOR, COPIE A URL DO VÍDEO DESEJADO NO CAMPO ABAIXO: ')
    video = input('(para sair digite "exit") | URL: ')
    if video == 'exit':
        end()
    else:
        try:
            YouTube(video).streams.first().download()
            speaking('SEU DOWNLOAD TERMINOU, O VÍDEO ESTÁ EM DOCUMENTOS/PYTHON_... ESPERO TER SIDO ÚTIL, ATÉ A PRÓXIMA')
        except:
            speaking('OCORREU ALGUM IMPREVISTO, POR FAVOR TENTE NOVAMENTE!')
            download_video()

def download_playlist():
    speaking('POR FAVOR, COPIE A URL DA PLAYLIST DESEJADA NO CAMPO ABAIXO: ')
    playlist_url = input('URL DA PLAYLIST: ')
    try:
        pl = Playlist(playlist_url)
        for url in pl:
            v = YouTube(url)
            stream = v.streams.get_highest_resolution()
            stream.download(output_path='playlist')         # EM BREVE COLOCAR PARA O USUÁRIO ESCOLHER O NOME DA PASTA QUE SERÁ ARMAZENADA A PLAYLIST
        speaking('SEU DOWNLOAD TERMINOU, A PLAYLISTA ESTÁ EM DOCUMENTOS/PYTHON_ ... ESPERO TER SIDO ÚTIL, ATÉ A PRÓXIMA')
    except:
        print('ERROR')
        speaking('HOUVE ALGUM IMPREVISTO, CHEQUE SUA CONEXÃO E TENTE NOVAMENTE... DESCULPE PELO TRANSTORNO')

def download_audio():
    speaking('POR FAVOR, COPIE A URL DO VÍDEO DESEJADO NO CAMPO ABAIXO: ')
    audio = input('URL: ')
    yt = YouTube(audio)
    au = yt.streams.filter(only_audio= True)[0]
    au.download()
    speaking('SEU DOWNLOAD TERMINOU, O ÁUDIO ESTÁ EM DOCUMENTOS/PYTHON_... ESPERO TER SIDO ÚTIL, ATÉ A PRÓXIMA')

def end():
    speaking('ATÉ MAIS!')


menu()
