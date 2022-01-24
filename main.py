from tkinter import *
import requests as req
import schedule
from time import sleep, time
from datetime import datetime

import tk
from websocket import create_connection
i = 0



def btn_clicked():
    print("AutoPosting started, don't close program!")
    token = "TOKEN"
    channelid = 'ID KANAL'
    message = ['Здарова парни',
               'Че есть будущие у проекта как считаете?',
               'Как я понимаю работать часа 4 на лвл',
               "Ну че, парни, работаем!",
               'Хотя на самом деле чат ламповый, время быстро летит',
               'Кто откуда?',
               'ахахаха',
               'Удачи, парни!',
               'Не подскажете, когда минт?',
               'Кто дела у кого?',
               'Есть те кому меньше 18?',
               'Парни, не скажемся, время окупится!',
               'Кто как вообще о этой теме узнал?',
               'Я короче че то'
               ]
    n = len(message)
    delay = entry0.get()

    def sendMessage(token, channelid, message):
        s = req.session()
        s.headers.update({'authorization': token, 'Content-Type': 'application/json'})
        global i
        payload = {"content": message[i], "tts": False}
        i += 1
        if i > n:
            i = 0



        ws = create_connection("wss://gateway.discord.gg/")
        data = '''
        {
            "op": 2,
            "d":{
                "token": "%s",
                "properties": {
                    "$os": "linux",
                    "$browser": "ubuntu",
                    "$device": "ubuntu"
                },
            }
        }
        ''' % token
        ws.send(data)
        b = s.post("https://discordapp.com/api/v9/channels/%s/messages" % channelid, json=payload)
        try:
            ws.close()
        except:
            pass
        current_datetime = datetime.now()
        print("[X] " + str(current_datetime) + " | Сообщение удачно отправлено")

    def timee():
        sendMessage(token, channelid, message)


    schedule.every(float(delay)).seconds.do(timee)

    while True:
        schedule.run_pending()

        sleep(1)


window = Tk()
window.title("XXXXXXXXXXXX")
window.geometry("1000x600")
window.configure(bg="#36393e")


def two_win():
    window2 = Tk()
    window2.geometry("1000x600")
    window2.title("XXXXXXXXX")


canvas = Canvas(
    window,
    bg="#36393e",
    height=600,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(
    513.5, 300.0,
    image=background_img)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    661.0, 429.0,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#c4c4c4",
    highlightthickness=0)

entry0.place(
    x=644.0, y=418,
    width=34.0,
    height=20)

entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(
    754.0, 293.0,
    image=entry1_img)

entry1 = Text(
    bd=0,
    bg="#c4c4c4",
    highlightthickness=0)

entry1.place(
    x=536.0, y=182,
    width=436.0,
    height=220)

entry2_img = PhotoImage(file=f"img_textBox2.png")
entry2_bg = canvas.create_image(
    755.0, 132.0,
    image=entry2_img)

entry2 = Entry(
    bd=0,
    bg="#c4c4c4",
    highlightthickness=0)

entry2.place(
    x=537.0, y=121,
    width=436.0,
    height=20)

entry3_img = PhotoImage(file=f"img_textBox3.png")
entry3_bg = canvas.create_image(
    756.0, 71.0,
    image=entry3_img)

entry3 = Entry(
    bd=0,
    bg="#c4c4c4",
    highlightthickness=0)

entry3.place(
    x=538.0, y=60,
    width=436.0,
    height=20)

img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b1 = Button(
    image=img0,
    borderwidth=1,
    highlightthickness=1,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=661, y=482,
    width=194,
    height=69)


window.resizable(False, False)
window.mainloop()
