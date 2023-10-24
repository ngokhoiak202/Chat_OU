import os
from gtts import gTTS

import requests
import pyttsx3
import speech_recognition as sr

vi = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An'
bot_message = ""
message = ""
# r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "hi"})
# print("OU Chatbot:", end=' ')
# for i in r.json():
#     bot_message = i['text']
#     print(f"{bot_message}")
# engine = pyttsx3.init()
# engine.setProperty('voice', vi)
# # Định nghĩa văn bản cần chuyển đổi
# engine.say(bot_message)
# print("Chatbot đang trả lời....")
# engine.runAndWait()
while bot_message != "Rất vui được gặp bạn. Tạm biệt":

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print("Bạn hãy hỏi :")
        audio = r.listen(source)
        print("Ngừng ghi âm Nhận dạng giọng nói")
        try:
            message = r.recognize_google(audio, language='vi-VN')
            print("Bạn hỏi: {}".format(message))
        except:
            print("Xin lỗi tôi không hiểu bạn đang nói gì?")
            message = ""

    if len(message) == 0:
        continue

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})
    print("OU Chatbot:", end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    engine = pyttsx3.init()
    engine.setProperty('voice', vi)
    # Định nghĩa văn bản cần chuyển đổi
    engine.say(bot_message)
    print("Chatbot đang trả lời....")
    engine.runAndWait()

    # rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
    # rasa run actions
