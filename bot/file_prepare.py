import speech_recognition as sr
import soundfile as sf



def recognition_sound():
    '''return text from source telegram voice'''

    #transfer to .wav with soundfile help*
    data, samplerate = sf.read('audio/audio.ogg')
    sf.write('audio/new_file.wav', data, samplerate)

    work = sr.Recognizer()

    #throw .way to speech model
    file = sr.AudioFile('audio/new_file.wav')
    with file as source:
        audio = work.record(source)

    #speech model <--- vosk*
    #when you will make a deploy download more quality speech model!!!
    #recognize text and handle need text
    text = work.recognize_vosk(audio_data=audio)
    output = text[14:len(text)-3]
    return output

