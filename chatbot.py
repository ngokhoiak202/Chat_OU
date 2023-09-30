import requests

bot_message = ""
while bot_message != "Rất vui được gặp bạn. Tạm biệt":
    message = input("Câu hỏi của bạn là gì?\n")

    print("Đang trả lời...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})
    print("...")
    for i in r.json():
        bot_message = i['text']
        print("\n:", end=' ')
        print (f"{bot_message}")

# rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
# rasa run actions
# run chatbot.py
