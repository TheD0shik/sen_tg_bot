import asyncio
import telebot
from telebot.async_telebot import AsyncTeleBot
from characterai import pycai


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
