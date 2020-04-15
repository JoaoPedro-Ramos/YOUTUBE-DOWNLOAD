import pyttsx3
from pytube import YouTube, Playlist

speak = pyttsx3.init('sapi5')


def menu():
    phrase = '''OLÁ, BEM VINDO AO YOUTUBE DOWNLOAD
    ESCOLHA O QUE VOCÊ DESEJA FAZER:
    [ 1 ] PARA BAIXAR UM VÍDEO
    [ 2 ] PARA BAIXAR UMA PLAYLIST
    [ 3 ] PARA BAIXAR SOMENTE O ÁUDIO DE UM VÍDEO (arquivo MP4)'''
    print(phrase)
    speak.say(phrase)
    speak.runAndWait()
    n = int(input('DIGITE AQUI O NÚMERO: '))
    escolha(n)


def escolha(x):
    if x == 1:
        download_video()
    elif x == 2:
        download_playlist()
    elif x == 3:
        download_audio()


def download_video():
    speak.say('POR FAVOR, COPIE A URL DO VÍDEO DESEJADO NO CAMPO ABAIXO: ')
    speak.runAndWait()
    video = input('URL: ')
    YouTube(video).streams.first().download()
    speak.say('SEU DOWNLOAD TERMINOU, O VÍDEO ESTÁ EM DOCUMENTOS/PYTHON_')
    speak.say('ESPERO TER SIDO ÚTIL, ATÉ A PRÓXIMA')
    speak.runAndWait()

def download_playlist():
    speak.say('POR FAVOR, COPIE A URL DA PLAYLIST DESEJADA NO CAMPO ABAIXO: ')
    speak.runAndWait()
    playlist_url = input('URL DA PLAYLIST: ')
    try:
        pl = Playlist(playlist_url)
        for url in pl:
            v = YouTube(url)
            stream = v.streams.get_highest_resolution()
            stream.download(output_path='playlist')
        speak.say('SEU DOWNLOAD TERMINOU, A PLAYLISTA ESTÁ EM DOCUMENTOS/PYTHON_')
        speak.say('ESPERO TER SIDO ÚTIL, ATÉ A PRÓXIMA')
        speak.runAndWait()
    except:
        print('ERROR')
        speak.say('HOUVE ALGUM IMPREVISTO, CHEQUE SUA CONEXÃO E TENTE NOVAMENTE')
        speak.say('DESCULPE PELO TRANSTORNO')


def download_audio():
    speak.say('POR FAVOR, COPIE A URL DO VÍDEO DESEJADO NO CAMPO ABAIXO: ')
    speak.runAndWait()
    audio = input('URL: ')
    yt = YouTube(audio)
    au = yt.streams.filter(only_audio= True)[0]
    au.download()
    speak.say('SEU DOWNLOAD TERMINOU, O ÁUDIO ESTÁ EM DOCUMENTOS/PYTHON_')
    speak.say('ESPERO TER SIDO ÚTIL, ATÉ A PRÓXIMA')
    speak.runAndWait()

menu()
