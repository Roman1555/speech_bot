import os
from pytubefix import YouTube



def download(link):
    # link = 'https://youtu.be/B1KqXea442k?si=J7vpLoQeUOhjhzJG'
    '''return mp3 file from youtube link'''
    wrong = ['.', '"', '/', '\\', '[', ']', ':', ';', '*', '|', '=', ',', '?']
    SAVE_PATH = './videos'

    #drop into off docs
    #add an exceptions for pytube.exceptions.AgeRestrictedError and other

    yt = YouTube(link)
    name = yt.title
    for item in name:
        if item in wrong:
                name = name.replace(item, '')


    check = f'/mnt/c/speech_bot/videos/{name}.mp4'
    if os.path.isfile(check):
        return check
    else:   
    # only mp3 streams
        video = yt.streams.get_audio_only()
        #videos/ПОЧЕМУ ОБ ЭТОМ ВСЕ МОЛЧАТ!  Полгода с iPhone 15 Pro.mp4
        #download mp3 video at once
        output = video.download(output_path=SAVE_PATH)
        return output


        

    
    #rename <sourc title>mp3 to base.mp3 for bot can read
    #split /mnt/c/speech_bot >> base and <name>mp3 >> ext
    # base, ext = os.path.split(output)
    # del ext
    # #make a new way and filename
    # new_name = base + f'/{name}.mp3'
    # #change name
    # os.rename(output, new_name)
    # print(new_name)

        








