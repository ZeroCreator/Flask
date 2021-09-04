# 1. Database - БД
# 2. send_message - отправка сообщений
# 3. get_messages - получение сообщений

# Списки
db = [
    ['msg', 'who', 'date'],
    ['Hello Patrick', 'Ann', "02.09.2021 21:50"],
    ['Hi. How are you doing Ann', 'Patrick', "02.09.2021 21:52"],
    ["Let's go shopping!", 'Ann', "02.09.2021 21:55"]
]

print(db[1][0])

# Словарь
from datetime import datetime
import time

dct = {
    "msg": "Hello",
    "name": "Patrick",
    "date": "02.09.2021 21:55"
}

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

print(db[0]['msg'])

def send_message(text, name):
    mes = {
        "msg": text,
        "name": name,
        "date": time.time() #datetime.now().strftime("%Y.%m.%d %H:%M:%S")
    }
    db.append(mes)
    return

send_message("Yes. Let's do it", "Patrick")
print(db)

def get_messages(after):
    result = []
    for item in db:
        if item["date"] > after:
            result.append(item)
    return result

get_messages(0)

def print_db(sub_db):
    for item in sub_db:
        print(item['msg'])
        print(item['name'])
        print(datetime.fromtimestamp(item['date']).strftime("%Y.%m.%d %H:%M:%S"))
        print("-------------------------------------------------")

sub_db = get_messages(0)
print_db(sub_db)