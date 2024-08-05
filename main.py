# import os
import telebot
# import threading
# import time
from bot.config import TOKEN
from bot.file_prepare import recognition_sound
from bot.youtube_down import download






# logger =logging.getLogger(__name__)
# # add a normal logging and deploy
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO,
#     filename="bot.log"
# )


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    #logger.info('start')
    bot.reply_to(message, "Hello")



@bot.message_handler(content_types=['voice'])
def handle_audio(message):
    #information about location of file:
    #{'file_id': 'AwACAgIAAxkBAAM1ZnQcg7Y492_1F2wlFP-WTHC3OQYAAh9GAAI4d6BL89mJpAZ91lo1BA',
    #'file_unique_id': 'Agh3oEs', 'file_size': 25592, 'file_path': 'voice/file_6.oga'}
    file_info = bot.get_file(message.voice.file_id)
    #download_file return a raw bytes of voice
    file_bytes = bot.download_file(file_info.file_path)
    #we write bytes in audio.ogg
    with open('audio/audio.ogg', 'wb') as f:
         f.write(file_bytes)
         
    bot.reply_to(message, text="Start recogntion>>3")
    output_text = recognition_sound()
    bot.send_message(message.chat.id, text=output_text)
        

# def handle_video(message, link):
    

# files = []
# threads = []
@bot.message_handler(content_types=['text'])
def ex(message):
    # files.append(message.text)
    source_link = message.text
    path = download(source_link)
    audio = open(path, 'rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()
    # files.append(message.text)
    # t1 = time.time()
    # for item in range(len(files)):
    #     t = threading.Thread(target=handle_video, args=[message, files[item]])
    #     t.start()
    #     threads.append(t)

    # print(threads)
    # for t in threads:
    #     t.join()

    # t2 = time.time()
    
    # print(t2-t1)

#5.995939254760742
#12.103719234466553
#11.538761854171753


# def load(message):



if __name__ == '__main__':	
    bot.infinity_polling()