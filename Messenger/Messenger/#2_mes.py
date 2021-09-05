# Сервер и клиенты
# Запрос состояит из:
# 1.Строки запроса - GET /search?q=killbox HTTP/1.1
# 2. Из заголовков - Host: google.com, Accept: */*
# 3. Из тела запроса - Content-Type: application/json, Content-Length: 69, {"username': "Jack", "text": "Hi"
# Если надо создавать динамическое вычисление - не надо присваивать ее глобальной переменной.
# O JSON
# 1. Ключи - всегда строкиЖ dct = {1: "asd"}
# 2. True/False, in JSON true/false
# 3. a = None, in JSON null
# 4. JSON may contain [], {}, "bool", "int/float" and "strings"
from flask import Flask, request
from datetime import datetime
import time
import requests

app = Flask(__name__)

db = [
    {
        "msg": "Hello Patrick",
        "name": "Ann",
        "date": time.time() - 100
    },{
        "msg": "Hi. How are you doing Ann",
        "name": "Patrick",
        "date": time.time() - 50
    },{
        "msg": "Let's go shopping!",
        "name": "Ann",
        "date": time.time() - 10
},

]
'''
@app.route("/")
def start():
    return 'Главная страница'

@app.route("/status")
def status():
    return {
        "status": True,
        "name": "MyTestMessenger",
        "time": datetime.now().strftime("%Y.%m.%d %H:%M:%S")
    }
'''

@app.route("/send", methods=["POST"])
def send_message():
    data = request.json
    text = data['text']
    name = data['name']
    mes = {
        "msg": text,
        "name": name,
        "date": time.time() #datetime.now().strftime("%Y.%m.%d %H:%M:%S")
    }
    db.append(mes)
    return {"status": "OK"}

@app.route("/show", methods=["GET"])
def print_db(sub_db):
    return {"database": db}


@app.route("/recive", methods=["GET"])
def get_messages(after):
    after = request.args["after"]
    result = []
    for item in db:
        if item["date"] > after:
            result.append(item)
    return {"messages": result}

if __name__ == "__main__":
    app.run(debug=True)











