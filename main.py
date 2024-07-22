import telebot
import datetime
import time
import os
import subprocess
import sqlite3
import hashlib
import sys

bot_token = '7334655367:AAFvbzlRVBACKzqB7aUx35i5U6SitX5H-7s'
bot = telebot.TeleBot(bot_token)

allowed_group_id = -1002221164686

allowed_users = [5651360746, 5893904488, 7434545806, 6693170165]
processes = []
ADMIN_ID = [5651360746]

connection = sqlite3.connect('user_data.db')
cursor = connection.cursor()

# Create the users table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        expiration_time TEXT
    )
''')
connection.commit()

def TimeStamp():
    now = str(datetime.date.today())
    return now

def load_users_from_database():
    cursor.execute('SELECT user_id, expiration_time FROM users')
    rows = cursor.fetchall()
    for row in rows:
        user_id = row[0]
        expiration_time = datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
        if expiration_time > datetime.datetime.now():
            allowed_users.append(user_id)

def save_user_to_database(connection, user_id, expiration_time):
    cursor = connection.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO users (user_id, expiration_time)
        VALUES (?, ?)
    ''', (user_id, expiration_time.strftime('%Y-%m-%d %H:%M:%S')))
    connection.commit()

def add_user(message):
    admin_id = message.from_user.id
    if admin_id != ADMIN_ID:
        bot.reply_to(message, 'Bạn tuổi gì mà dùng lệnh này?')
        return

    if len(message.text.split()) == 1:
        bot.reply_to(message, 'Nhập ID người dùng.')
        return

    user_id = int(message.text.split()[1])
    allowed_users.append(user_id)
    expiration_time = datetime.datetime.now() + datetime.timedelta(days=30)
    connection = sqlite3.connect('user_data.db')
    save_user_to_database(connection, user_id, expiration_time)
    connection.close()

    bot.reply_to(message, f'Người dùng có ID: {user_id} đã được cấp quyền sử dụng lệnh /sms.')

load_users_from_database()

@bot.message_handler(commands=['sms'])
def lqm_sms(message):
    if message.chat.type == 'private':
        bot.reply_to(message, 'Không nhắn riêng nha.')
        return

    user_id = message.from_user.id
    if user_id not in allowed_users:
        bot.reply_to(message, text='Bạn tuổi gì mà dùng lệnh này?')
        return
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'Nhập số điện thoại vô.')
        return

    sdt = message.text.split()[1]
    if not sdt.isnumeric():
        bot.reply_to(message, 'Số không hợp lệ.')
        return

    if sdt in ['113', '911', '114', '115']:
        bot.reply_to(message, "Ai cho chú em spam số này??.")
        return

    file_path = os.path.join(os.getcwd(), "sms.py")
    process = subprocess.Popen(["python", file_path, sdt, "120"])
    processes.append(process)
    bot.reply_to(message, f'✨ Yêu cầu tấn công thành công! ✨\n+ 📞 Số tấn công: [ {sdt} ]\n+ 💼 Gói: PROMAX\n+ 👾 Số luồng : 1 \n+ 🔗 Số API: 64')

@bot.message_handler(commands=['how'])
def how_to(message):
    if message.chat.type == 'private':
        bot.reply_to(message, 'Không nhắn riêng nha.')
        return

    how_to_text = '''
Hướng dẫn sử dụng:

- Sử dụng lệnh /sms {số điện thoại} để gửi tin nhắn SMS.
- Admin cho phép dùng mới dùng được nhaa.
'''
    bot.reply_to(message, how_to_text)

@bot.message_handler(commands=['help'])
def help(message):
    if message.chat.type == 'private':
        bot.reply_to(message, 'Không nhắn riêng nha.')
        return

    help_text = '''
Danh sách lệnh:
- /sms {số điện thoại}: Spam cháy máy
 (phải được admin thêm vào danh sách).
- /how: Hướng dẫn sử dụng.
- /help: Danh sách lệnh.
'''
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['status'])
def status(message):
    if message.chat.type == 'private':
        bot.reply_to(message, 'Không nhắn riêng nha.')
        return

    user_id = message.from_user.id
    if user_id != ADMIN_ID:
        bot.reply_to(message, 'Bạn tuổi gì mà dùng lệnh này?.')
        return
    if user_id not in allowed_users:
        bot.reply_to(message, text='Bạn tuổi gì mà dùng lệnh này?')
        return
    process_count = len(processes)
    bot.reply_to(message, f'Số quy trình đang chạy: {process_count}.')

@bot.message_handler(commands=['restart'])
def restart(message):
    if message.chat.type == 'private':
        bot.reply_to(message, 'Không nhắn riêng nha.')
        return

    user_id = message.from_user.id
    if user_id != ADMIN_ID:
        bot.reply_to(message, 'Bạn tuổi gì mà dùng lệnh này?.')
        return

    bot.reply_to(message, 'Bot đang được restart...')
    time.sleep(2)
    python = sys.executable
    os.execl(python, python, *sys.argv)

@bot.message_handler(commands=['stop'])
def stop(message):
    if message.chat.type == 'private':
        bot.reply_to(message, 'Không nhắn riêng nha.')
        return

    user_id = message.from_user.id
    if user_id != ADMIN_ID:
        bot.reply_to(message, 'Bạn tuổi gì mà dùng lệnh này?.')
        return

    bot.reply_to(message, 'Bot sẽ dừng lại trong giây lát...')
    time.sleep(2)
    bot.stop_polling()

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.chat.id == allowed_group_id:
        return 
    if message.chat.type == 'private':
        bot.reply_to(message, 'Không nhắn riêng nha.')
        return

bot.polling()
