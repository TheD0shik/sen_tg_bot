from telebot import types
import time
#import spacy
import random
import os
import sys
import pyodbc
import telebot
from characterai import pycai
f="nen"
sa=0   
ggg=1
uzinv=0 
#PvF9dWz_Z8PhqeLXVJYSCLH_6i5eBGKA7ThmtjGAGVw
char ='Dn4-IzMfbl8fi8txGuVYPT6Rxv7t4nDgwx-tohFAXoQ'
client =  pycai.Client('74a212327a64233a5997b05795f5596a85543629')#апи
me = client.get_me()
server = 'DESKTOP-VMD5Q4G\\SQLEXPRESS'  
database = 'rusisz'  
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
chat=client.connect()
new, answer = chat.new_chat(char, me.id)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
from telebot import types
#DESKTOP-VMD5Q4G\SQLEXPRESS
#.env\Scripts\activate
tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x))
now = time.time()
sen=telebot.TeleBot('7374291955:AAGsACqmNzHVZiDze1JpKk-RlpCFMYDZOLQ')
x=1
y=10000

nums=[1,2,3,4,5,6,7,8,9]

print('бот активен')
z = False
@sen.message_handler(commands=['start'])
def main(message):
    global z
    user_name = message.from_user.username
    user_id = message.from_user.id
    z=bool(not(z))
    sen.send_message(message.chat.id,str(z))
    
@sen.message_handler()
def handle(message):
    global z
    user_name = message.from_user.username
    user_id = message.from_user.id 
    s=message.text 
    m=message.chat.id
    text=f"{s}"
    messages = chat.send_message(
    char, new.chat_id, text
    )
    ss=f'{messages.text}'
    sen.send_message(message.chat.id,ss) 
    if (z):
        insert_query = 'INSERT INTO word (слово,пояснение) VALUES (?, ?);'      
        cursor.execute(insert_query, (s ,ss))
        conn.commit()
    

nnn=1
while nnn==1:
    try:
        sen.infinity_polling()
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(15)
        