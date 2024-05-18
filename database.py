import sqlite3 as sql
from tkinter import messagebox

conn = sql.connect('user.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT NOT NULL,
               password TEXT NOT NULL,
               PIN INTERGER NOT NULL,
               sound INTERGER NOT NULL, 
               song INTERGER NOT NULL
               )
               '''
)
conn.commit()

def add_user(username, password, PIN):
   # try:
    cursor.execute('INSERT INTO users (username, password, PIN, sound, song) VALUES (?, ?, ?, ?, ?)', (username, password, PIN, 1, 0))
    conn.commit()
    return True
    #except sql.IntegrityError:
     #   messagebox.showerror(title='Oops', message="This usernamee is already taken, please choose another username")
      #  return False
    
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
            messagebox.showerror(title='Oops', message="This usernamee is already taken, please choose another username")
            return False
        return True


def change_sound_stage(username, sound):
    try:
        sound_value = 1 if sound else 0
        cursor.execute('UPDATE users SET sound=? WHERE username=?', (sound_value, username))
        conn.commit()
    except Exception as e:
        messagebox.showerror(title='Oops', message=f"Something went wrong: {e}")

def get_sound_value(username):
    try:
        cursor.execute('SELECT sound FROM users WHERE username=?', (username,))
        row = cursor.fetchone()
        if row:
            sound = row[0]  # The sound value is in the first column of the result
            return sound
        else:
            print("User not found")
            return None
    except sql.Error as e:
        print(f"Database error: {e}")
        return None

def get_song(username):
    try:
        cursor.execute('SELECT song FROM users WHERE username=?', (username,))
        row = cursor.fetchone()
        if row:
            song = row[0]  # The sound value is in the first column of the result
            return song
        else:
            print("User not found")
            return None
    except sql.Error as e:
        print(f"Database error: {e}")

def change_song(username, song):
    try:
        cursor.execute('UPDATE users SET song=? WHERE username=?', (song, username))
        conn.commit()
    except Exception as e:
        messagebox.showerror(title='Oops', message=f"Something went wrong: {e}")

def close_connection():
    conn.close()

