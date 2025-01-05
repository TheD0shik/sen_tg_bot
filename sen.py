import telebot
from telebot import types
import time
#import spacy
import random
import os
import sys
import pyodbc

import config

from characterai import pycai
f="nen"
sa=0   
ggg=1
uzinv=0   
char ='TQvxq3ui2Pfr0gM8aU68NiK7SXcFeLmPOypYJRlN02M'
client =  pycai.Client(config.clientt)#апи
me = client.get_me()
server = config.serverr
database = config.databasee
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
sen=telebot.TeleBot(config.senko)
x=1
y=10000
z=True
nums=[1,2,3,4,5,6,7,8,9]


def get_user_info(table_name, id_column, id_value):
    # SQL-запрос для получения строки
    select_query = f"""
    SELECT * FROM {table_name}
    WHERE {id_column} = ?
    """
    # Выполнение запроса
    cursor.execute(select_query, (id_value,))
    row = cursor.fetchone()
    
    if row:
        # Получение названий столбцов
        columns = [column[0] for column in cursor.description]
        # Формирование строки с данными пользователя
        user_info = "\n".join([f"{columns[i]}: {row[i]}" for i in range(len(columns))])
        return user_info
    else:
        return "Пользователь не найден"

def cheksoo(uz,uzsoo,soo):

    cursor.execute('SELECT команда, соо FROM rpchar')


    for row in cursor:
        ids = row.команда
        if ids in soo:  
            value = row.соо
            soo=soo.replace(f'{ids}', '', 1)
            value = value.lower().replace('uz', uz, 1)
            value = value.lower().replace('uzsoo', uzsoo, 1) 
            value = value.lower().replace('soso', soo, 1)
            return value


vn=1   
new_value = 1
new_value1 = 1
def give(uz,usgive,soos):
    global vn ,new_value ,new_value1
    soo=soos
    cursor.execute(f'SELECT айди, имя, количество FROM {usgive}')
    for row in cursor.fetchall():
        ids = row[1] 
        if ids in soos:  
            vn=row[2]
    cursor.execute(f'SELECT айди, имя, количество FROM {uz}')
    for row in cursor.fetchall():
        ids = row[1] 
        if ids in soos:  
            v = row[2] 
            soos = soos.replace(ids, '', 1)
            new_value = int(v) - int(soos)
            new_value1 = int(vn) + int(soos)
            cursor.execute(f'UPDATE {uz} SET количество = ? WHERE имя = ?', (new_value, ids))
            conn.commit()
        
            cursor.execute(f'SELECT айди, имя, количество FROM {usgive}')
            if (get_info(usgive, 'имя', ids)):
                print(1)
                cursor.execute(f'UPDATE {usgive} SET количество = ? WHERE имя = ?', (new_value1, ids))
            else:
                print(2)
                insert_query = f'INSERT INTO {usgive} (айди, имя, количество) VALUES (?,?,?);'
                cursor.execute(insert_query,(0, ids, new_value1))
                
                
    conn.commit()
            
def get_info(table_name, id_column, id_value):
    # SQL-запрос для получения строки
    select_query = f"""
    SELECT * FROM {table_name}
    WHERE {id_column} = ?
    """
    # Выполнение запроса
    cursor.execute(select_query, (id_value,))
    row = cursor.fetchone()
    
    if row:
        return 1
    else:
        return 0
    


def cheksenshop(uzin, so,m):
    global sa,uzinv
    
    uzinv = uzin
    
    sa=so
    
    cursor = conn.cursor()
    conn.commit()
    mark = types.InlineKeyboardMarkup(row_width=2)
    k=types.InlineKeyboardButton('git',callback_data='git')
    n=types.InlineKeyboardButton('мора',callback_data='мора')
    mark.add(k,n)
    b=types.InlineKeyboardButton('гиткоин',callback_data='гиткоин')
    mark.add(b)
    
    sen.send_message(m,'выбери валюту для оплаты',reply_markup = mark)   
    
@sen.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    global sa,uzinv,ggg
    saa=sa
    if callback.data =='git':
        sen.send_message(callback.message.chat.id,callback.data)
    if callback.data =='мора':
        sen.send_message(callback.message.chat.id,callback.data)
    if callback.data =='гиткоин':
        sen.send_message(callback.message.chat.id,callback.data)
        
        
    sql_query = f"SELECT курс FROM rpmoney WHERE имя = ?"
    cursor.execute(sql_query, callback.data)
    result = cursor.fetchone()
    sell = result[0]
    sell= float(sell)
    cursor.execute('SELECT айди, название, цена FROM item') 
    for item_row in cursor:
        ids = item_row.название
        sa=str(saa)
        if ids in sa:  
            
            item_id = item_row.айди
            sel = item_row.цена
            
            soo = sa.replace(f'{ids}', '', 1)
            
            sell=  (int(sel) / sell)*int(soo)
            sen.send_message(callback.message.chat.id, f"цена за{soo} {ids}:{sell} {callback.data}")
                
            
            select_query = f'SELECT имя FROM {uzinv} WHERE имя =  ?;'
            
            cursor.execute(select_query, (ids,))
            
            row = cursor.fetchone()
            if row is None:
                
                insert_query = f'INSERT INTO {uzinv} (айди, имя, количество) VALUES (?,?,?);'
                cursor.execute(insert_query,(item_id, ids, soo))
                conn.commit()
                return 0
            else:
                
                conn.commit()
                new_cursor = conn.cursor()
                
                new_cursor.execute(f'SELECT айди, имя, количество FROM {uzinv}')
               
                
                for uzinv_row in new_cursor:
                    
                    iid = uzinv_row.айди
                    if str(iid) in str(item_id):  
                        koll = uzinv_row.количество
                        newkoll = int(koll) + int(soo)
                        update_query = f"UPDATE {uzinv} SET количество = ? WHERE айди = ?"
                        new_value = newkoll 
                        new_cursor.execute(update_query, (new_value, iid))
                        conn.commit()
                        moni(callback.data,uzinv,sell,callback.message.chat.id)
                        sen.send_message(callback.message.chat.id, "выдано")
                        sen.send_message(callback.message.chat.id, f"ваш текущий баланс:{ggg} {callback.data}")
                        return 0


#@sen.message_handler(commands=['money'])
#def main(message):
    

def moni(dta, uz, kol,m):
    global ggg
    cursor = conn.cursor()
    cursor.execute(f"SELECT количество FROM {uz} WHERE имя = ?", (dta,))
    row = cursor.fetchone()
    
    if row:
        new_kol = int(row[0]) - kol
        update_query = f"UPDATE {uz} SET количество = ? WHERE имя = ?"
        cursor.execute(update_query, (new_kol, dta))
        ggg=new_kol
        conn.commit()



def mani(uzin, soo):
    cursor = conn.cursor()
    conn.commit()
    sell = 0
    cursor.execute('SELECT айди, имя, курс FROM rpmoney')
    
    for item_row in cursor:
        ids = item_row.имя
        if ids in soo:  
            uzinv = uzin
            item_id = item_row.айди
            sell = item_row.курс
            soo = soo.replace(f'{ids}', '', 1)
            
            select_query = f'SELECT имя FROM {uzinv} WHERE имя =  ?;'
            
            cursor.execute(select_query, (ids,))
            
            row = cursor.fetchone()
            if row is None:
                
                insert_query = f'INSERT INTO {uzinv} (айди, имя, количество) VALUES (?,?,?);'
                cursor.execute(insert_query,(item_id, ids, soo))
                conn.commit()
                return 0
            else:
                
                conn.commit()
                new_cursor = conn.cursor()
                
                new_cursor.execute(f'SELECT айди, имя, количество FROM {uzinv}')
               
                
                for uzinv_row in new_cursor:
                    
                    iid = uzinv_row.айди
                    if str(iid) in str(item_id):  
                        select_query = f'SELECT имя FROM {uzinv} WHERE имя = ?;'
                        koll = uzinv_row.количество
                        newkoll = int(koll) + int(soo)
                        update_query = f"UPDATE {uzinv} SET количество = ? WHERE айди = ?"
                        new_value = newkoll 
                        new_cursor.execute(update_query, (new_value, iid))
                        conn.commit()
                        return 0
                            
                        
                        
            
        



def upde(table_name,column_name,id_column,new_value,id_value):
    
    update_query = f"""
    UPDATE {table_name}
    SET {column_name} = ?
    WHERE {id_column} = ?
    """
    # Выполнение запроса
    cursor.execute(update_query, (new_value, id_value))
    conn.commit()




qq=[]
def creat(qq,nami):
    columns_str = ', '.join([f'{col} VARCHAR(255)' for col in qq])
    # SQL запрос для создания таблицы
    create_table_query = f'CREATE TABLE {nami} ({columns_str})'
    # Выполнение запроса
    cursor.execute(create_table_query)
    conn.commit()
    

def chek(nm):
    table_name = nm

    # Проверка наличия таблицы
    cursor.execute(f"""
        IF OBJECT_ID(N'{table_name}', N'U') IS NOT NULL
            SELECT 1 AS TableExists
        ELSE
            SELECT 0 AS TableExists
    """)
    
    table_exists = cursor.fetchone()[0]

    if table_exists:
        return 0
    else:
        return 1



print("запуск бота...")
logt=f"запуск бота,время запуска:{time.ctime(now)}"
with open("log.txt", "a+",encoding='utf-8') as log:
    log.write(f"{str(logt)}\n") 
    log.close  
paimon = 'https://polinka.top/pics1/uploads/posts/2023-11/1699889666_polinka-top-p-chibi-genshin-impakt-9.png'
qiqi = 'https://i.pinimg.com/736x/d4/37/f5/d4307f5814e718b9e42e953bfb9b0976c.jpg'
@sen.message_handler(content_types=['new_chat_members'])
def welcome(message):
    for member in message.new_chat_members:
        sen.send_message(message.chat.id, f'приветики {member.full_name}!')
@sen.message_handler(content_types=['left_chat_member'])
def farewell(message):
    member = message.left_chat_member
    sen.send_message(message.chat.id, f'Покеда {member.full_name}!')
@sen.message_handler(content_types=['audio'])
def get_audio(message):
    print("Загрузка аудиофайла...")
    # Получаем информацию о файле
    file_info = sen.get_file(message.audio.file_id)
    # Скачиваем файл
    downloaded_file = sen.download_file(file_info.file_path)
    # Создаем путь для сохранения файла
    file_path = os.path.join('files', 'audio', f"{message.audio.file_id}.mp3")
    # Сохраняем файл локально
    with open(file_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    print("Аудиофайл скачен!")
    user_name = message.from_user.username
    user_id = message.from_user.id
    tet=f"{tconv(message.date)}|пользователь {user_id} под ником:{user_name} загрузил аудио:{message.audio.file_id}"
    with open("log.txt", "a+",encoding='utf-8') as log:
            log.write(f"{str(tet)}\n")
            log.close
@sen.message_handler(content_types=['video'])
def get_video(message):
    print("Загрузка видеофайла...")
    # Получаем информацию о файле
    file_info = sen.get_file(message.video.file_id)
    # Скачиваем файл
    downloaded_file = sen.download_file(file_info.file_path)
    # Создаем путь для сохранения файла
    file_path = os.path.join('files', 'video', f"{message.video.file_id}.mp4")
    # Сохраняем файл локально
    with open(file_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    print("Видеофайл скачен!")
    user_name = message.from_user.username
    user_id = message.from_user.id
    tet=f"{tconv(message.date)}|пользователь {user_id} под ником:{user_name} загрузил видео:{message.video.file_id}"
    with open("log.txt", "a+",encoding='utf-8') as log:
            log.write(f"{str(tet)}\n")
            log.close
@sen.message_handler(content_types=['photo'])
def get_photo(message):
    print("Загрузка фотографии...")
    # Получаем информацию о файле
    file_info = sen.get_file(message.photo[-1].file_id)
    # Скачиваем файл
    downloaded_file = sen.download_file(file_info.file_path)
    # Создаем путь для сохранения файла
    file_path = os.path.join('files', 'photo', f"{message.photo[-1].file_id}.jpg")
    # Сохраняем файл локально
    with open(file_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    print("Фотография скачена!")
    user_name = message.from_user.username
    user_id = message.from_user.id
    tet=f"{tconv(message.date)}|пользователь {user_id} под ником:{user_name} загрузил фото:{message.photo[-1].file_id}"
    with open("log.txt", "a+",encoding='utf-8') as log:
            log.write(f"{str(tet)}\n")
            log.close      
r=[]
@sen.message_handler(commands=['game1'])
def main(message):
    mark = types.ReplyKeyboardMarkup()
    k=types.KeyboardButton('камень')
    n=types.KeyboardButton('ножницы')
    mark.row(k,n)
    b=types.KeyboardButton('бумага')
    mark.row(b)
    sen.send_message(message.chat.id,'приветик,давай сыграем в камень ножницы бумагу!',reply_markup=mark)
@sen.message_handler(commands=['test'])
def main(message):
    user_name = message.from_user.username
    user_id = message.from_user.id
    sen.send_photo(message.chat.id, photo=paimon)

@sen.message_handler(commands=['qwerty'])
def main(message):
    user_name = message.from_user.username
    user_id = message.from_user.id
    logt=f"{tconv(message.date)}|пользователь {user_id} под ником:{user_name} остановил бота"
    sen.send_message(message.chat.id,'закрытие бота...')
    with open("log.txt", "a+",encoding='utf-8') as log:
        log.write(f"{str(logt)}\n")
        log.close()
        cursor.close()
        conn.close()
        print("перезапуск бота...")
        nnn=0
        sen.stop_polling()  
        sys.exit(0)
        


@sen.message_handler()
def handle(message):
    user_name = message.from_user.username
    user_id = message.from_user.id 
    m=message.chat.id
    #1-камень
    #2-ножницы
    #3-бумага
    if (chek('log')):
        pp=['время','айди','имя','соо']
        creat(pp,'log')
    
    insert_query = 'INSERT INTO log (время,айди,имя,соо) VALUES (?,?,?,?);'
    cursor.execute(insert_query,(tconv(message.date) ,user_id, user_name, message.text))
    conn.commit()
    if (chek('userss')):
        pp=['айди','имя']
        creat(pp,'userss')
    select_query = 'SELECT айди FROM userss WHERE айди = ?;'
    cursor.execute(select_query, (user_id,))
    row = cursor.fetchone()
    if row is None:
        insert_query = 'INSERT INTO userss (айди, имя) VALUES (?, ?);'
        cursor.execute(insert_query, (user_id, user_name))
        conn.commit()
        tet=f"{tconv(message.date)}|пользователь {user_id} под ником:{user_name} добавлен в базу данных"
        with open("log.txt", "a+",encoding='utf-8') as log:
            log.write(f"{str(tet)}\n")
            log.close
        print(user_name,' добавлен в базу')  
    
    print(message.text)
    if (message.text.lower() =='камень'.lower()):
        ran=random.randrange(1, 4)
        if (ran==1):
            sen.send_message(message.chat.id,'камень')
            sen.send_message(message.chat.id,'ничья')
        if (ran==2):
            sen.send_message(message.chat.id,'ножницы')
            sen.send_message(message.chat.id,'ты выйграл!')
        if (ran==3):
            sen.send_message(message.chat.id,'бумага')
            sen.send_message(message.chat.id,'ты проиграл')
    if (message.text.lower() =='ножницы'.lower()):
        ran=random.randrange(1, 4)
        if (ran==1):
            sen.send_message(message.chat.id,'камень')
            sen.send_message(message.chat.id,'ты проиграл')
        if (ran==2):
            sen.send_message(message.chat.id,'ножницы')
            sen.send_message(message.chat.id,'ничья')
        if (ran==3):
            sen.send_message(message.chat.id,'бумага')
            sen.send_message(message.chat.id,'ты выйграл!')
    if (message.text.lower() =='бумага'.lower()):
        ran=random.randrange(1, 4)
        if (ran==1):
            sen.send_message(message.chat.id,'камень')
            sen.send_message(message.chat.id,'ты выйграл!')
        if (ran==2):
            sen.send_message(message.chat.id,'ножницы')
            sen.send_message(message.chat.id,'ты проиграл')
        if (ran==3):
            sen.send_message(message.chat.id,'бумага')
            sen.send_message(message.chat.id,'ничья')
       #s = s.replace('сенко', '', 1)
    s=message.text 
    s=s.lower()      
    if 'инвентарь'.lower() in s.lower():
        sen.send_message(message.chat.id,f'инвентарь {user_name}')
        inv = f'unventori_{user_id}_{user_name}'
        if (chek(f'{inv}')):
            pp=['айди','имя','количество']
            creat(pp,f'{inv}')
            
        cursor.execute(f'SELECT * FROM  {inv}')
        columns = [column[0] for column in cursor.description]
        soo=f'{'|'.join(columns)}\n'
        for row in cursor.fetchall():
            soo=f'{soo}{'|'.join(str(item) for item in row)}\n'
        sen.send_message(message.chat.id, f"{soo}") 
        
        
        
    if 'хапр'.lower() in s.lower():
            sen.send_photo(message.chat.id, photo=qiqi)
    
    if 'сенрп'.lower() in s.lower():
        
        
        if message.reply_to_message and message.reply_to_message.from_user:
            username = message.reply_to_message.from_user.username 
            userid = message.reply_to_message.from_user.id
            inv1 = f'unventori_{user_id}_{user_name}'
            inv2 = f'unventori_{userid}_{username}'
            
            s = s.replace('сенрп', '', 1)
            if 'инвентарь'.lower() in s.lower():
                sen.send_message(message.chat.id,f'инвентарь {username}')
                cursor.execute(f'SELECT * FROM  {inv2}')
                columns = [column[0] for column in cursor.description]
                soo=f'{'|'.join(columns)}\n'
                for row in cursor.fetchall():
                    soo=f'{soo}{'|'.join(str(item) for item in row)}\n'
                sen.send_message(message.chat.id, f"{soo}") 
                
            if 'дать'.lower() in s.lower():
                s = s.replace('дать', '', 1)
                
                if (chek(f'{inv2}')):
                    pp=['айди','имя','количество']
                    creat(pp,f'{inv2}') 
                give(inv1,inv2 ,s)
                sen.send_message(message.chat.id, "выдано")
            
        if 'пойти'.lower() in s.lower():
            s = s.replace('сенрп', '', 1)
            s = s.replace('пойти', '', 1)
            upde('rpan','местонахождение','айди',s,user_id)
            sen.send_message(message.chat.id, f'местонахождение обновлено')
        
            
            
            
        if 'переведи в двоичный'.lower() in s.lower():
            #spacy
            s = s.replace('сенко переведи в двоичный', '', 1)
            sb = bin(int(s))
            sen.send_message(message.chat.id, f'{s}-->{sb[2:]}')
        if 'рп'.lower() in s.lower():
            if 'добавь'.lower() in s.lower():
                select_query = 'SELECT id FROM userrp WHERE id = ?;'
                cursor.execute(select_query, (user_id,))
                row = cursor.fetchone()
                if row is None:
                    insert_query = 'INSERT INTO userrp (id,names,descriptions,unventori,charter,location) VALUES (?, ?, ?, ?, ?,?);'
                    inv = f'unventori_{user_id}_{user_name}'
                    cursor.execute(insert_query, (user_id, user_name, 'данных пока нет', inv, 'данных пока нет','мондштат'))
                    conn.commit()
                    create_table_query = f'''
                    CREATE TABLE {inv} (
                        id VARCHAR(50),
                        quantity VARCHAR(50)
                    );
                    '''
                    cursor.execute(create_table_query)
                    conn.commit()
                    sen.send_message(message.chat.id, "поздравляю, вы теперь в рп процессе")
                else:
                    sen.send_message(message.chat.id, "вы уже в рп")    
        if 'магазинчик'.lower() in s.lower():
            soo=f"выбирай:\n"
            cursor.execute('SELECT * FROM item')
            columns = [column[0] for column in cursor.description]
            soo=f'{soo}{'|'.join(columns)}\n'
            for row in cursor.fetchall():
                soo=f'{soo}{'|'.join(str(item) for item in row)}\n'
            sen.send_message(message.chat.id, f"{soo}")  
            if 'купить'.lower() in s.lower():
                s = s.lower().replace('сенрп', '', 1)
                s = s.lower().replace('магазинчик', '', 1)
                s = s.lower().replace('купить', '', 1) 
                inv = f'unventori_{user_id}_{user_name}'
                if 'денег'.lower() in s.lower():
                    s = s.lower().replace('денег', '', 1)
                    mani(inv,s)
                    sen.send_message(message.chat.id, "выдано")
                m=message.chat.id
                if (chek(f'{inv}')):
                    pp=['айди','имя','количество']
                    creat(pp,f'{inv}')  
                cheksenshop(inv,s,m)
                
                
    if 'сенко'.lower() in s.lower():
        
        s = s.replace('сенко', '', 1)
        text=f"{user_name}:{s}"
        messages = chat.send_message(
        char, new.chat_id, text
        )
        s=f'{messages.text}'
        sen.send_message(message.chat.id,s)            
                      
                
    else:        
        
        if message.reply_to_message and message.reply_to_message.from_user:
            username = message.reply_to_message.from_user.username 
            if (chek('rpchar')):
                pp=['команда','соо']
                creat(pp,'rpchar') 
            sss=cheksoo(user_name,username,s)
            if sss:
                sen.send_message(message.chat.id, f"{sss}") 
            
            
            
        

    if 'анкета'.lower() in s.lower():
        if'заполнить'.lower() in s.lower():
            if (chek('rpan')):
                pp=['айди','имя','номер_анкеты','имя_персонажа','кличка','возраст','расса','местонахождение','фракция','автобиография']
                creat(pp,'rpan')
            if (chek('lokation')):
                pp=['айди','имя','пренадлежность']
                creat(pp,'lokation')
            select_query = 'SELECT айди FROM rpan WHERE айди = ?;'
            cursor.execute(select_query, (user_id))
            row = cursor.fetchone()
            if row is None:
                insert_query = 'INSERT INTO rpan (айди) VALUES (?);'
                cursor.execute(insert_query, (user_id))
                conn.commit()
                sen.send_message(message.chat.id, "анкета создана")
            upde('rpan','имя','айди',user_name,user_id)
            s = s.lower().replace('анкета', '', 1)
            s = s.lower().replace('заполнить', '', 1)
            
            if '3'.lower() in s.lower():
                s = s.lower().replace(' 3 ', '', 1)
                upde('rpan','возраст','айди',s,user_id)
                sen.send_message(message.chat.id, f'возраст обновлен')
            elif '1'.lower() in s.lower():
                s = s.lower().replace(' 1 ', '', 1) 
                upde('rpan','имя_персонажа','айди',s,user_id)
                sen.send_message(message.chat.id, f'имя обновлено')
            elif '2'.lower() in s.lower():
                s = s.lower().replace(' 2 ', '', 1)
                upde('rpan','кличка','айди',s,user_id)
                sen.send_message(message.chat.id, f'кличка обновлена') 
            elif '4'.lower() in s.lower():
                s = s.lower().replace(' 4 ', '', 1)
                upde('rpan','расса','айди',s,user_id)
                sen.send_message(message.chat.id, f'раса обновлена')
            elif '5'.lower() in s.lower():
                s = s.lower().replace(' 5 ', '', 1)
                upde('rpan','местонахождение','айди',s,user_id)
                sen.send_message(message.chat.id, f'местонахождение обновлено')
            elif '6'.lower() in s.lower():
                s = s.lower().replace(' 6 ', '', 1)
                upde('rpan','фракция','айди',s,user_id)
                sen.send_message(message.chat.id, f'фракция обновлена')
            elif '7'.lower() in s.lower():
                s = s.lower().replace(' 7 ', '', 1)
                upde('rpan','автобиография','айди',s,user_id)
                sen.send_message(message.chat.id, f'автобиография обновлена')
        elif'покажи'.lower() in s.lower():
            if message.reply_to_message and message.reply_to_message.from_user:
                username = message.reply_to_message.from_user.username
            else:
                username = user_name
            cursor.execute(f'SELECT * FROM  rpan')
            user_info  =get_user_info('rpan', 'имя', username)
            sen.send_message(message.chat.id, user_info)

                
       
        else:
            sen.send_message(message.chat.id, "Добро пожаловать в Лимбо, место где жизнь и смерть работают воедино. Вы должны показать своë отражение в виде создания анкеты-роли:\n 1) Имя и фамилия (при желании) персонажа\n2) позывной/кличка (необязательно)\n3) возраст (любой)\n4) раса (все виды рас указаны в новостном)\n5) место проживания (все места проживания указаны в новостном)\n6) фракция (при желании, все фракции указаны в новостном)\n7) краткая биография персонажа\nпиши анкета заполнить *номер анкеты* *и то что надо вписать* \nесли этого нет в базе данных то оно там появится, всем удачки")
          
                
                
    
                
nnn=1
while nnn==1:
    try:
        sen.infinity_polling()
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(15)