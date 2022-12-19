from flask import Flask
from flask import request
from flask import Response
import requests 

from botMessaging import*


app = Flask(__name__)



@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        msg = request.get_json()
        chat_id,txt = parse_message(msg)
        if txt == "hi":
            tel_send_message(chat_id,"Hello!!")
        else:
            tel_send_message(chat_id,txt)
        return Response('ok',status=200)
    else:
        return "<h1>Здрасьте.</h1>\n<p>Вы попали на кривой костыль, который я использую для веб хука для телеграм бота, который превращает слова в хуенитивы. Поздравляю?</p>"

        
if __name__ == '__main__':
   app.run(debug=True)