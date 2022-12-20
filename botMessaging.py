import requests 

from transformer import *

TOKEN = open('config.txt',mode='r').read()

def parse_message(message):
    print("message-->",message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id,txt

def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    print(transform(text))
    payload = {
                'chat_id': chat_id,
                'text': transform(text)
                }
   
    r = requests.post(url,json=payload)
    return r