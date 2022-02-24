
from time import sleep
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait
import os
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
import time
from time import sleep
if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
app = Client('dedinside-session', api_id=1016382, api_hash='c27834e5683d50a9bacf835a95ec4763')

app.start()

app.stop()
print('''
      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
      ┃       Made by dayot               Созданно dayot        ┃
      ┃  Instagram: @d.dayot1     ┃
      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


''')
print("После ввода задержки напишите в любой телеграм чат команду \n --Команды-- \n.dd 0 \n.night 0 \n.ghoul")
print("\n МЫ НЕ НЕСЕМ ОТВЕТСВЕННОСТИ ЗА ВАШИ ДЕЙСТВИЯ!")
print()
cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))
if cool == 0:
    print("Слишком быстро!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))
if cool > 10:
    print("Слишком медленно!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость (Норма 8):  "))
if cool < 5:
    print("Слишком быстро!")
    cool = int(input("Введите завис.число - от него будет зависеть скорость(Норма 8):  "))


@app.on_message(filters.command("dd", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = textded.split("\n")
    e = True
    etime = int(msg.text.split('.dd ', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</>')
                sleep(0.5)
                msg.delete()
            except:
               pass
        else:
            try:
                msg.edit(f'❤️{i} ❤️')
                sleep(time/cool)
                msg.edit(f'🧡 {i} 🧡')
                sleep(time/cool)
                msg.edit(f'💛 {i} 💛')
                sleep(time/cool)
                msg.edit(f'💚 {i} 💚')
                sleep(time/cool)
                msg.edit(f'💙 {i} 💙')
                sleep(time/cool)
                msg.edit(f'💜 {i} 💜')
                sleep(time/cool)
                msg.edit(f'🖤 {i} 🖤')
                sleep(time/cool)
                msg.edit(f'🤍 {i} 🤍')
                sleep(time/cool)
            except:
                pass
    msg.edit(f'<b> ⭐ inst: d.dayot1</b>')

textded = '''
<b>доброе утро зайка</b> 
<b>доброе утро солнышко</b> 
<b>доброе утро котёнок</b> 
<b>доброе утро цветочек</b> 
<b>доброе утро ангелочек</b> 
<b>доброе утро принцесса</b> 
<b>доброе утро красотка</b> 
<b>доброе утро милашк</b> 
<b>доброе утро симпатяжка</b> 
<b>доброе утро бусинка</b> 
❤ <b>я</b> ❤
<b>💚 тебя 💚</b>
<b>💙 очень 💙</b>
<b>💛 сильно 💛</b>
<b>💜 люблю 💜</b>
'''

textded1 = '''
<b>спокойной ночи зайка</b> 💚
<b>спокойной ночи солнышко</b> 💛
<b>спокойной ночи котёнок</b> ❤
<b>спокойной ночи цветочек</b> 💙
<b>спокойной ночи ангелочек</b> 💜
<b>спокойной ночи принцесса</b> 💓
<b>спокойной ночи красотка</b> 💕 
<b>спокойной ночи милашк</b>а 💖 
<b>спокойной ночи симпатяжка</b> 💗
<b>спокойной ночи бусинка</b> 💘
❤ <b>я</b> ❤
<b>💚 тебя 💚</b>
<b>💙 очень 💙</b>
<b>💛 сильно 💛</b>
<b>💜 люблю 💜</b>
'''

@app.on_message(filters.command("night", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = textded1.split("\n")
    e = True
    etime = int(msg.text.split('.night ', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    msg.edit(f'<b> ⭐ inst: d.dayot1</b>')

textded2 = '''
<b>ты лучшая</b> 💚
<b>ты солнышко</b> 💛
<b>ты котёнок</b> ❤
<b>ты милашкarrrr</b> 💙
<b>ты ангелочек</b> 💜
<b>ты принцесса</b> 💓
<b>ты красотка</b> 💕 
<b>ты милашк</b>а 💖 
<b>ты симпатяжка</b> 💗
<b>ты бусинка</b> 💘
❤ <b>я</b> ❤
<b>💚 тебя 💚</b>
<b>💙 очень 💙</b>
<b>💛 сильно 💛</b>
<b>💜 люблю 💜</b>
<b>🫀 и уважаю 🫀<

@app.on_message(filters.command("rep", prefixes=".") & filters.me)
def valentine(_, msg):
    txt = textded1.split("\n")
    e = True
    etime = int(msg.text.split('.rep ', maxsplit=1)[1])
    for i in txt:
        time = etime
        if e == True:
            e = False
        elif time > 10:
            try:
                msg.edit('<b>Error: Нельзя ставить больше 10с!</b>')
                sleep(0.5)
                msg.delete()
            except:
                pass
        else:
            try:
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
                msg.edit(f'{i}')
                sleep(time/cool)
            except:
                pass
    msg.edit(f'<b> ⭐ inst: d.dayot1</b>')

@app.on_message(filters.command("creators", prefixes="!") & filters.me)
def valentine(app, message):
    app.send_message(message.chat.id,f'''

 —Создатель—
<b>vk creators<b>
<i>+ @gromyy </i>
<b>instagram creators<b>
<i>+ inst: d.dayot1 </i>
<b>TikTok creators<b>
<i>+ @d.dayot </i>
''')
app.run()

@app.on_message(filters.command("help", prefixes="!") & filters.me)
def valentine(app, message):
    app.send_message(message.chat.id,f'''

 —Команды—
<b>Скрипт спама 1000-7</b>
<i>+ Введите: </i><code>.dd 0</code>
<b>Скрипт анимации « Доброе утро»</b>
<i>+ Введите</i> <code>.dead 0     
</code><code>Скрипт анимации для </code><b>влюблённых: «Спокойной ночи❤️»</b>
<i>+ Введите </i><code>.night 0
Все команды нужно писать в любой чат </code><i>телеграмм после выполнения кода! (Ввода зависим. числа)</i>
''')
app.run()