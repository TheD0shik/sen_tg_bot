import asyncio
import telebot
from telebot.async_telebot import AsyncTeleBot
from characterai import pycai

sen=telebot.TeleBot('7341040063:AAEQDpm85uxyg6xrGGqCg_8qOWz-xGvcoIA')#токен
char = '2-IwcgqJb4BUzVBv2J3d9Pe3NbiaMFr2dl7oNf6-Iok'#бот
#char ='pW4CWZO96QeyVvR22iBAR7uWRQ1kfhKolfpYKda11eQ'
client =  pycai.Client('74a212327a64233a5997b05795f5596a85543629')#апи
me = client.get_me()
print("запуск бота...")
with client.connect() as chat:

    new, answer = chat.new_chat(
        char, me.id
    )
    print(" бот создан")
        
    @sen.message_handler(func=lambda message: True)
    def handle(message):
        
        user_name = message.from_user.username
        s=message.text
        if 'яэ'.lower() in s.lower():
            s = s.replace('яэ', '', 1)
            text=f"{s} *это был {user_name}*"
            messages = chat.send_message(
                char, new.chat_id, text
            )
            s=f'{messages.text}'
            print(s)
            sen.send_message(message.chat.id,s)
    
    sen.polling(non_stop=True)