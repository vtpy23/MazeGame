import sqlite3 as sql
from tkinter import messagebox

conn = sql.connect('user.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT NOT NULL,
               password TEXT NOT NULL,
               PIN INTERGER NOT NULL
               )
               '''
)
conn.commit()

def add_user(username, password, PIN):
    try:
        cursor.execute('INSERT INTO users (username, password, PIN) VALUES (?, ?, ?)', (username, password, PIN))
        conn.commit()
        return True
    except sql.IntegrityError:
        messagebox.showerror(title='Oops', message="This username is already taken, please choose another username")
        return False
    
def check_user(username, password):
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()
    if user:
        return True
    return False

def check_PIN(username, PIN):
    cursor.execute('SELECT * FROM users WHERE username=? AND PIN=?', (username, PIN))
    user = cursor.fetchone()
    if user:
        return True
    return False

def check_cpass_PIN(password, PIN):
    cursor.execute('SELECT * FROM users WHERE password=? AND PIN=?', (password, PIN))
    user = cursor.fetchone()
    if user:
        return True
    return False

def change_password(username, new_password):
    cursor.execute('UPDATE users SET password=? WHERE username=?',(new_password, username))
    conn.commit()
    

def delete_account(username):
    cursor.execute('DELETE from users WHERE username=?', username)
    conn.commit()
    
def check_username_availability(username):
        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            messagebox.showerror(title='Oops', message="This username is already taken, please choose another username")
            return False
        return True

def close_connection():
    conn.close()

