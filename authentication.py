from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from random import randint, choice, shuffle
import mazeGeneration as mg
from database import *
import menu
from sys import exit

USERNAME = ""

class LoginForm():
    def __init__(self, window):
        self.window = window
        self.window.geometry('1280x720')
        self.window.title('Authentication')
        self.window.resizable(False, False)
        self.current_frame = 'login'
        # =============== Login Frame ================
        self.lg_frame = Frame(self.window, bg='#FFFFFF' , width=1280/8*6, height=600)
        # =============== Signup Frame ================
        self.su_frame = Frame(self.window, bg='#FFFFFF', width=1280/8*6, height=600)
        # =============== ForgetPass Frame ================
        self.fgp_frame = Frame(self.window, bg='#FFFFFF', width=1280/8*6, height=600)
        # =============== Background Image ================
        self.bg_frame = Image.open("Photos\\background1.jpg")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image= photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')  
        self.setup_login_form()
        self.show_lgsu_frame()

    def setup_login_form(self):
        self.lg_frame = Frame(self.window, bg='#FFFFFF', width= 1280/8*6, height= 600)
        self.lg_frame.place(x=1280/8, y= 60)
        # =============== Top Left =================
        self.side_image = Image.open("Photos\\logo hcmus.png")
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lg_frame, image=photo, bg= "#FFFFFF")
        self.side_image_label.image = photo
        self.side_image_label.place(x=240, y= 40) 
        # =============== Right Side Image ================
        #self.side_image = Image.open("rightside.jpg")
        #photo = ImageTk.PhotoImage(self.side_image)
        #self.side_image_label = Label(self.lg_frame, image=photo, bg= "#FFFFFF")
        #self.side_image_label.image = photo
        #self.side_image_label.place(x=500, y= 20)  
        # =============== Login Image ================
        #self.sign_in_image = Image.open("rightside.jpg")
        #photo = ImageTk.PhotoImage(self.sign_in_image)
        #self.sign_in_image_label = Label(self.lg_frame, image=photo, bg= "#FFFFFF")
        #self.sign_in_image_label.image = photo
        #self.sign_in_image_label.place(x=20, y= 130) 
        self.sign_in_label = Label(self.lg_frame, text= "Sign In", bg="#FFFFFF",fg= "black", font=('yu gothic ui', 17, 'bold'))
        self.sign_in_label.place(x=250, y=140)

        # =============== Username ================
        self.username_label = Label(self.lg_frame, text= "Username", bg="#FFFFFF",fg= "black", font=('yu gothic ui', 13, 'bold'))
        self.username_label.place(x=120, y=200)

        self.username_entry = Entry(self.lg_frame, highlightthickness=0, relief= FLAT, bg="#FFFFFF", fg="black", font=('yu gothic ui', 12, 'bold') )
        self.username_entry.focus_set()
        self.username_entry.bind('<Return>', self.check_log)
        self.username_entry.place(x=150, y=240, width=270)
        self.username_line = Canvas(self.lg_frame, width= 350, height= 2.0, bg ="black", highlightthickness= 0)
        self.username_line.place(x=110,y=270)
        
        # =============== Username Icon ================
        self.username_icon = Image.open("Photos\\usernameicon.png")
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lg_frame, image=photo, bg= "#FFFFFF")
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=105, y= 230) 
        

        # =============== Password ================
        self.password_label = Label(self.lg_frame, text= "Password", bg="#FFFFFF",fg= "black", font=('yu gothic ui', 13, 'bold'))
        self.password_label.place(x=120, y=320)

        self.password_entry = Entry(self.lg_frame, highlightthickness=0, relief= FLAT, bg="#FFFFFF", fg="black", font=('yu gothic ui', 13, 'bold'), show='*')
        self.password_entry.bind('<Return>', self.check_log)
        self.password_entry.place(x=150, y=356, width=240)
        self.password_line = Canvas(self.lg_frame, width= 350, height= 2.0, bg ="black", highlightthickness= 0)
        self.password_line.place(x=110, y=386)

        # =============== Password Icon ================
        self.password_icon = Image.open("Photos\\password.png")
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lg_frame, image=photo, bg= "#FFFFFF")
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=105, y=345) 

        # =============== Login Button ================
        self.login = Button(self.lg_frame, text = "LOG IN", font=('yu gothic ui', 13, 'bold'), width=25, bd=2, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg="white", command=self.check_log)
        self.login.place(x=150, y=430)
        
        # =============== Forgot Password ================
        self.forgot_button = Button(self.lg_frame, text= 'Forgot Password?', font=('yu gothic ui', 11, 'underline'), fg = 'black', width= 25, bd=0, bg='#FFFFFF', activebackground='#FFFFFF', cursor= 'hand2', command=self.toggle_fgp_forms)
        self.forgot_button.place(x=320, y=480)

        # =============== Sign up ================
        self.sign_label = Label(self.lg_frame, text='Don\'t have an account yet?', font=('yu gothic ui', 11, 'bold'), fg='black', bg='white')
        self.sign_label.place(x=120, y=534)

        self.signup_button = Image.open('Photos\\show.png')
        photo = ImageTk.PhotoImage(self.signup_button)
        self.signup_button_label = Button(self.lg_frame, text="SIGN ME UP", bg= '#3047ff', activebackground='#3047ff', cursor='hand2', bd=2, fg='white', command= self.toggle_lgsu_forms, font=('yu gothic ui', 13, 'bold'))
        self.signup_button_label.image = photo
        self.signup_button_label.place(x=320, y=530, width=170, height= 35)

        # ============== Show/Hide Password ==============
        self.show_image = ImageTk.PhotoImage(file='Photos\\show.png')
        self.hide_image = ImageTk.PhotoImage(file='Photos\\hide.png')

        self.show_button = Button(self.lg_frame, image=self.show_image, command=self.show, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=440, y=350)

    def setup_signup_form(self):
        self.su_frame = Frame(self.window, bg='#FFFFFF', width= 1280/8*6, height= 600)
        self.su_frame.place(x= 1280/8, y= 60)
        # =============== Top Left =================
        self.side_image = Image.open("Photos\\logo hcmus1.png")
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.su_frame, image=photo, bg= "#FFFFFF")
        self.side_image_label.image = photo
        self.side_image_label.place(x=120, y= 720/4-20)
        self.credit_label = Label(self.su_frame, text= "Powered by Group 4 - 23TNT - FIT.HCMUS", bg="#FFFFFF",fg= "black", font=('yu gothic ui', 13, 'bold'))
        self.credit_label.place(x=80, y=430)
        self.time = Label(self.su_frame, text= "Lastest update: April 2024", bg="#FFFFFF",fg= "black", font=('yu gothic ui', 13, 'bold'))
        self.time.place(x=147, y=470)
        # =============== Back to login page ============
        back_tologin_button = Button(self.su_frame, text = "⭠ Back to login page", font=('yu gothic ui', 13, 'bold'), width=20, bd=0, cursor='hand2', fg="black",bg= 'white', command=self.toggle_lgsu_forms)
        back_tologin_button.place(x=730, y=30)
        # =============== Register ================
        self.sign_up_label = Label(self.su_frame, text= "Register", bg="#FFFFFF",fg= "black", font=('yu gothic ui', 17, 'bold'))
        self.sign_up_label.place(x=690, y=70)

        # =============== Username ================
        self.username_label = Label(self.su_frame, text= "Username", bg="#FFFFFF",fg= "black", font=('yu gothic ui', 13, 'bold'))
        self.username_label.place(x=560, y=120)

        self.username_entry = Entry(self.su_frame, highlightthickness=0, relief= FLAT, bg="#FFFFFF", fg="black", font=('yu gothic ui', 12, 'bold') )
        self.username_entry.bind('<Return>', self.save)
        self.username_entry.focus_set()
        self.username_entry.place(x=560, y=160, width=270)
        self.username_line = Canvas(self.su_frame, width= 350, height= 2.0, bg ="black", highlightthickness= 0)
        self.username_line.place(x=560,y=190)
        
        # =============== Username Icon ================
        self.username_icon = Image.open("Photos\\usernameicon.png")
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.su_frame, image=photo, bg= "#FFFFFF")
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=525, y= 155) 

        # =============== Password ================
        self.password_label = Label(self.su_frame, text= "Password", bg="#FFFFFF",fg= "black", font=('yu gothic ui', 13, 'bold'))
        self.password_label.place(x=560, y=220)

        self.password_entry = Entry(self.su_frame, highlightthickness=0, relief= FLAT, bg="#FFFFFF", fg="black", font=('yu gothic ui', 13, 'bold'), show='*')
        self.password_entry.place(x=560, y=260, width=240)
        self.password_entry.bind('<Return>', self.save)
        self.password_line = Canvas(self.su_frame, width= 350, height= 2.0, bg ="black", highlightthickness= 0)
        self.password_line.place(x=560, y=290)

        # =============== Password Icon ================
        self.password_icon = Image.open("Photos\\password.png")
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.su_frame, image=photo, bg= "#FFFFFF")
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=525, y=255)

        # ============== Show/Hide Password ==============
        self.show_image = ImageTk.PhotoImage(file='Photos\\show.png')
        self.hide_image = ImageTk.PhotoImage(file='Photos\\hide.png')
        self.show_button = Button(self.su_frame, image=self.show_image, command=self.show1, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=880, y=260)

        # =============== Generate password ============
        generate_password_button = Button(self.su_frame, text = "Suggest a strong password!", font=('yu gothic ui', 13, 'bold'), width=25, bd=0, cursor='hand2', fg="black",bg= 'white', command=self.generatepass)
        generate_password_button.place(x = 670, y= 300)

        # =============== Confirm Password ================
        self.password_label = Label(self.su_frame, text= "Confirm Password", bg="#FFFFFF",fg= "black", font=('yu gothic ui', 13, 'bold'))
        self.password_label.place(x=560, y=340)
        self.password_entry1 = Entry(self.su_frame, highlightthickness=0, relief= FLAT, bg="#FFFFFF", fg="black", font=('yu gothic ui', 13, 'bold'), show='*')
        self.password_entry1.place(x=560, y=380, width=240)
        self.password_entry1.bind('<Return>', self.save)
        self.password_line = Canvas(self.su_frame, width= 350, height= 2.0, bg ="black", highlightthickness= 0)
        self.password_line.place(x=560, y=410)

        # =============== Confirm Password Icon ================
        self.password_icon = Image.open("Photos\\password.png")
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.su_frame, image=photo, bg= "#FFFFFF")
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=525, y=375) 


        # =============== Signup Button ================
        self.signup = Button(self.su_frame, text = "SIGN UP", font=('yu gothic ui', 13, 'bold'), width=25, bd=2, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg="white", command=self.save)
        self.signup.place(x=610, y=510)

        
        # =============== PIN ================
        self.PIN_label = Label(self.su_frame, text= "PIN (4 numbers)", bg="#FFFFFF",fg= "black", font=('yu gothic ui', 13, 'bold'))
        self.PIN_label.place(x=620, y=440)
        self.PIN_entry = Entry(self.su_frame, highlightthickness=0, relief= FLAT, bg="#FFFFFF", fg="black", font=('yu gothic ui', 13, 'bold'), validate='key')
        self.PIN_entry['validatecommand'] = (self.PIN_entry.register(self.validate_input), '%P')
        self.PIN_entry.place(x=780, y=440, width=240)
        self.PIN_entry.bind('<Return>', self.save)
        self.PIN_line = Canvas(self.su_frame, width= 40, height= 2.0, bg ="black", highlightthickness= 0)
        self.PIN_line.place(x=780, y=470)
    
    def setup_forgetpass_form(self):
        self.fgp_frame = Frame(self.window, bg='#FFFFFF', width= 1280/8*6, height= 600)
        self.fgp_frame.place(x= 1280/8, y= 60)
        # =============== Top Left =================
        self.side_image = Image.open("Photos\\logo hcmus1.png")
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.fgp_frame, image=photo, bg= "#FFFFFF")
        self.side_image_label.image = photo
        self.side_image_label.place(x=120, y= 720/4-20)
        self.credit_label = Label(self.fgp_frame, text= "Powered by Group 4 - 23TNT - FIT.HCMUS", bg="#FFFFFF",fg= "black", font=('yu gothic ui', 13, 'bold'))
        self.credit_label.place(x=80, y=430)
        # =============== Back to login page ============
        back_tologin_button = Button(self.fgp_frame, text = "⭠ Back to login page", font=('yu gothic ui', 13, 'bold'), width=25, bd=0, cursor='hand2', fg="black",bg= 'white', command=self.toggle_fgp_forms)
        back_tologin_button.place(x=730, y=30)
        # =============== Set new password ================
        self.sign_up_label = Label(self.fgp_frame, text= "Set new password", bg="#FFFFFF",fg= "black", font=('yu gothic ui', 17, 'bold'))
        self.sign_up_label.place(x=650, y=70)

        # =============== Username ================
        self.username_label = Label(self.fgp_frame, text= "Username", bg="#FFFFFF",fg= "black", font=('yu gothic ui', 13, 'bold'))
        self.username_label.place(x=560, y=120)

        self.username_entry = Entry(self.fgp_frame, highlightthickness=0, relief= FLAT, bg="#FFFFFF", fg="black", font=('yu gothic ui', 12, 'bold') )
        self.username_entry.focus_set()
        self.username_entry.place(x=560, y=160, width=270)
        self.username_entry.bind('<Return>', self.update)
        self.username_line = Canvas(self.fgp_frame, width= 350, height= 2.0, bg ="black", highlightthickness= 0)
        self.username_line.place(x=560,y=190)
        
        # =============== Username Icon ================
        self.username_icon = Image.open("Photos\\usernameicon.png")
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.fgp_frame, image=photo, bg= "#FFFFFF")
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=525, y= 155)

        # =============== PIN ================

        self.PIN_label = Label(self.fgp_frame, text= "Enter your registered PIN", bg="#FFFFFF",fg= "black", font=('yu gothic ui', 13, 'bold'))
        self.PIN_label.place(x=560, y=220)
        self.PIN_entry = Entry(self.fgp_frame, highlightthickness=0, relief= FLAT, bg="#FFFFFF", fg="black", font=('yu gothic ui', 13, 'bold'), validate='key')
        self.PIN_entry['validatecommand'] = (self.PIN_entry.register(self.validate_input), '%P')
        self.PIN_entry.bind('<Return>', self.update)
        self.PIN_entry.place(x=820, y=220, width=240)
        self.PIN_line = Canvas(self.fgp_frame, width= 40, height= 2.0, bg ="black", highlightthickness= 0)
        self.PIN_line.place(x=820, y=250)

        # =============== New Password ================
        self.password_label = Label(self.fgp_frame, text= "New password", bg="#FFFFFF",fg= "black", font=('yu gothic ui', 13, 'bold'))
        self.password_label.place(x=560, y=300)

        self.password_entry = Entry(self.fgp_frame, highlightthickness=0, relief= FLAT, bg="#FFFFFF", fg="black", font=('yu gothic ui', 13, 'bold'), show='*')
        self.password_entry.place(x=560, y=340, width=240)
        self.password_entry.bind('<Return>', self.update)
        self.password_line = Canvas(self.fgp_frame, width= 350, height= 2.0, bg ="black", highlightthickness= 0)
        self.password_line.place(x=560, y=370)

        # =============== Password Icon ================
        self.password_icon = Image.open("Photos\\password.png")
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.fgp_frame, image=photo, bg= "#FFFFFF")
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=525, y=335)

        # ============== Show/Hide Password ==============
        self.show_image = ImageTk.PhotoImage(file='Photos\\show.png')
        self.hide_image = ImageTk.PhotoImage(file='Photos\\hide.png')
        self.show_button = Button(self.fgp_frame, image=self.show_image, command=self.show2, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=880, y=340)

        # =============== Generate password ============
        generate_password_button = Button(self.fgp_frame, text = "Suggest a strong password!", font=('yu gothic ui', 13, 'bold'), width=25, bd=0, cursor='hand2', fg="black",bg= 'white', command=self.generatefpass)
        generate_password_button.place(x = 670, y= 390)

        # =============== Confirm New Password ================
        self.password_label = Label(self.fgp_frame, text= "Confirm New Password", bg="#FFFFFF",fg= "black", font=('yu gothic ui', 13, 'bold'))
        self.password_label.place(x=560, y=430)
        self.password_entry1 = Entry(self.fgp_frame, highlightthickness=0, relief= FLAT, bg="#FFFFFF", fg="black", font=('yu gothic ui', 13, 'bold'), show='*')
        self.password_entry1.bind('<Return>', self.update)
        self.password_entry1.place(x=560, y=470, width=240)
        self.password_line = Canvas(self.fgp_frame, width= 350, height= 2.0, bg ="black", highlightthickness= 0)
        self.password_line.place(x=560, y=500)

        # =============== Confirm  New Password Icon ================
        self.password_icon = Image.open("Photos\\password.png")
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.fgp_frame, image=photo, bg= "#FFFFFF")
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=525, y=465) 

        # =============== Update Button ================
        self.updatep = Button(self.fgp_frame, text = "Update", font=('yu gothic ui', 13, 'bold'), width=25, bd=2, bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg="white", command=self.update)
        self.updatep.place(x=610, y=530)

        
    def save(self, even = None):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confpass = self.password_entry1.get()
        PIN = self.PIN_entry.get()
        if check_username_availability(username):
            if len(username) == 0 or len(password) == 0 or len(confpass) == 0 or len(PIN) == 0:
                messagebox.showinfo(title='Oops', message="Please make sure you haven't left any field empty")
            elif len(password) < 6 or len(password) > 15:
                messagebox.showinfo(title='Oops', message="The password must be at least 6 characters and no more than 15 in length")
            elif len(username) < 6 or len(username) > 20:
                messagebox.showinfo(title='Oops', message="The username must be at least 6 characters and no more than 20 in length")
            elif " " in password:
                messagebox.showinfo(title='Oops', message="Please don't include space character in the password")
            elif " " in username:
                messagebox.showinfo(title='Oops', message="Please don't include space character in the username")
            elif confpass != password:
                messagebox.showerror(title='Oops', message="The password does not match")
            else:
                self.password_entry.delete(0, END)
                self.password_entry1.delete(0, END)
                self.username_entry.delete(0, END)
                self.PIN_entry.delete(0, END)
                self.username_entry.focus()
                add_user(username, password, PIN)
                messagebox.showinfo(title= 'Congrats', message="Sign up successfully")
                self.toggle_lgsu_forms()

    def update(self, event = None):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confpass = self.password_entry1.get()
        PIN = self.PIN_entry.get()
        if check_PIN(username, PIN):
            if password != confpass:
                messagebox.showinfo(title='Oops', message="Passwords do not match")
            else:
                self.password_entry.delete(0, END)
                self.password_entry1.delete(0, END)
                self.username_entry.delete(0, END)
                self.PIN_entry.delete(0, END)
                self.username_entry.focus()
                change_password(username, password)
                messagebox.showinfo(title= 'Congrats', message="Password updated successfully")
                self.toggle_fgp_forms()
        else:
            if len(username) == 0 or len(password) == 0 or len(confpass) == 0 or len(PIN) == 0:
                messagebox.showinfo(title='Oops', message="Please make sure you haven't left any field empty")
            elif len(password) < 6 or len(password) > 15:
                messagebox.showinfo(title='Oops', message="The password must be at least 6 characters and no more than 15 in length")
            elif len(username) < 6 or len(username) > 20:
                messagebox.showinfo(title='Oops', message="The username must be at least 6 characters and no more than 20 in length")
            elif " " in password:
                messagebox.showinfo(title='Oops', message="Please don't include space character in the password")
            elif " " in username:
                messagebox.showinfo(title='Oops', message="Please don't include space character in the username")
            else:
                messagebox.showinfo(title='Oops', message="Your credentials don't match an account in our system")
                
    
    def check_log(self, event = None):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if check_user(username, password):
            messagebox.showinfo(title="Message", message="Login Successfully")
            self.window.destroy()
            login_success(username)
        elif len(username) == 0 or len(password) == 0:
            messagebox.showinfo(title="Message",message="Please make sure you haven't left any field empty") 
        else:
            messagebox.showinfo(title="Message",message="Your login credentials don't match an account in our system")    

    def generatepass(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '@', '&', '*', '+', '#', '%']
        self.password_entry.delete(0, END)
        password_letters = [choice(letters) for _ in range(randint(4,6))]
        password_numbers = [choice(numbers) for _ in range(randint(2,4))]
        password_symbols = [choice(symbols) for _ in range(randint(0,3))]
        password_list = password_letters + password_numbers + password_symbols   
        shuffle(password_list)
        password = "".join(password_list)
        self.show1()
        self.password_entry.insert(0, password)

    def show(self):
        self.hide_button = Button(self.lg_frame, image=self.hide_image, command=self.hide, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=440, y=350)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lg_frame, image=self.show_image, command=self.show, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=440, y=350)
        self.password_entry.config(show='*')
    
    def show1(self):
        self.hide_button = Button(self.su_frame, image=self.hide_image, command=self.hide1, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=880, y=260)
        self.password_entry.config(show='')

    def hide1(self):
        self.show_button = Button(self.su_frame, image=self.show_image, command=self.show1, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=880, y=260)
        self.password_entry.config(show='*')

    def show2(self):
        self.hide_button = Button(self.fgp_frame, image=self.hide_image, command=self.hide2, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=880, y=340)
        self.password_entry.config(show='')

    def hide2(self):
        self.show_button = Button(self.fgp_frame, image=self.show_image, command=self.show2, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=880, y=340)
        self.password_entry.config(show='*')
    
    def generatefpass(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '@', '&', '*', '+', '#', '%']
        self.password_entry.delete(0, END)
        password_letters = [choice(letters) for _ in range(randint(4,6))]
        password_numbers = [choice(numbers) for _ in range(randint(2,4))]
        password_symbols = [choice(symbols) for _ in range(randint(0,3))]
        password_list = password_letters + password_numbers + password_symbols   
        shuffle(password_list)
        password = "".join(password_list)
        self.show2()
        self.password_entry.insert(0, password)
    
    def validate_input(self, text):
        if (text.isdigit() and len(text) <= 4) or len(text) == 0:
            return True
        else:
            return False

    def show_lgsu_frame(self):
        self.lg_frame.destroy()
        self.su_frame.destroy()
        if self.current_frame == 'login':
            self.setup_login_form()
        else:
            self.setup_signup_form()
        

    def toggle_lgsu_forms(self):
        if self.current_frame == 'login':
            self.current_frame = 'signup'
        else:
            self.current_frame = 'login'
        self.show_lgsu_frame()

    def show_fgp_frame(self):
        self.lg_frame.destroy()
        self.fgp_frame.destroy()
        if self.current_frame == 'login':
            self.setup_login_form()
        else:
            self.setup_forgetpass_form()
        

    def toggle_fgp_forms(self):
        if self.current_frame == 'login':
            self.current_frame = 'forget'
        else:
            self.current_frame = 'login'
        self.show_fgp_frame()

class UserInterface():
    def __init__(self, window, username):
        self.window = window
        self.username = username
        USERNAME = self.username
        self.window.geometry('1280x720')
        self.window.title(f'Group4 Maze Game UI - 23TNT - FIT - HCMUS')
        self.window.resizable(False, False)
        self.window.config(bg='white')
        self.bg_color = 'white'
        self.btn_bg = 'white'
        self.btn_active_bg = 'white'
        self.text_color = 'black'
        self.setup_ui()
        self.show_image = ImageTk.PhotoImage(file='Photos\\show.png')
        self.hide_image = ImageTk.PhotoImage(file='Photos\\hide1.png')


    
    def setup_ui(self):
        self.window.config(bg= self.bg_color)
        self.greet_label = Label(self.window, text=f'Welcome!', font=('yu gothuic ui', 24, 'bold'), bg=self.bg_color, fg=self.text_color)
        self.greet_label.place(x= 140+410, y=60)
        self.label = Label(self.window, text=f'What do you want to do today?', font=('yu gothuic ui', 13), bg=self.bg_color, fg=self.text_color)
        self.label.place(x=90+420, y=120+60)
        # =============== Play Game ================
        self.Play = Button(self.window, text = "Play", font=('yu gothic ui', 13, 'bold'), width=25, height=3, bd=2, bg=self.bg_color, cursor='hand2', activebackground=self.btn_active_bg, fg=self.text_color, command=self.run)
        self.Play.place(x=75+420, y=180+60)
        # =============== Change Password ================
        self.chpass_but = Button(self.window, text = "Change Password", font=('yu gothic ui', 13, 'bold'), width=25, height=3, bd=2, bg=self.bg_color, cursor='hand2', activebackground=self.btn_active_bg, fg=self.text_color, command=self.setup_passchange)
        self.chpass_but.place(x=75+420, y=260+60)
        # =============== Sign out ================
        self.signout_ = Button(self.window, text = "Sign Out", font=('yu gothic ui', 13, 'bold'), width=25, height=3, bd=2, bg=self.bg_color, cursor='hand2', activebackground=self.btn_active_bg, fg=self.text_color, command=self.signout)
        self.signout_.place(x=75+420, y=340+60)
        # =============== Exit ================
        self.exit_ = Button(self.window, text = "Exit", font=('yu gothic ui', 13, 'bold'), width=25, height=3, bd=2, bg=self.bg_color, cursor='hand2', activebackground=self.btn_active_bg, fg=self.text_color, command=self.exit)
        self.exit_.place(x=75+420, y=420+60)
        # =============== Right Side Image ================
        self.side_image = Image.open("Photos//Tom.png")
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.window, image=photo, bg= self.bg_color)
        self.side_image_label.image = photo
        self.side_image_label.place(x=800, y= 80)  
        # =============== Left Side Image ================
        self.side_image = Image.open("Photos//Jerry.png")
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.window, image=photo, bg= self.bg_color)
        self.side_image_label.image = photo
        self.side_image_label.place(x=150, y= 310) 
        #================ Theme ================
        self.theme = Label(self.window, text="Theme:", font=('yu gothic ui', 13, 'bold'), fg=self.text_color, bg=self.bg_color)
        self.theme.place(x=40+420, y=532+60)
        self.option1 = Button(self.window, text="Yellow", bg=self.bg_color, font=('yu gothic ui', 13, 'bold'), activebackground=self.btn_active_bg, bd=0, fg=self.text_color, command=lambda: self.change_theme('#F2E9C5', '#FFECA1','#F8D755','#9C7E06'))
        self.option1.place(x=110+420, y=530+60)
        self.option2 = Button(self.window, text="Blue", bg=self.bg_color, font=('yu gothic ui', 13, 'bold'), activebackground=self.btn_active_bg, bd=0, fg=self.text_color, command=lambda: self.change_theme('#BCBAFF', '#8884FD', '#453EFD', '#060194'))
        self.option2.place(x=175+420, y=530+60)
        self.option3 = Button(self.window, text="Lavender", bg=self.bg_color, font=('yu gothic ui', 13, 'bold'), activebackground=self.btn_active_bg, bd=0, fg=self.text_color, command=lambda: self.change_theme('#F1EDFC', '#DACCFB', '#BA9FFB', '#9C73FF'))
        self.option3.place(x=220+420, y=530+60)
        self.option4 = Button(self.window, text="Original", bg=self.bg_color, font=('yu gothic ui', 13, 'bold'), activebackground=self.btn_active_bg, bd=0, fg=self.text_color, command=lambda: self.change_theme('white', 'white', 'white', 'black'))
        self.option4.place(x=300+420, y=530+60)
        
        
    def change_theme(self, bg_color, btn_bg, btn_active_bg, text_color):
        self.bg_color = bg_color
        self.btn_bg = btn_bg
        self.btn_active_bg = btn_active_bg
        self.text_color = text_color
        self.setup_ui()
    
    def signout(self):
        if messagebox.askyesnocancel(title='Wanna sign out? =(',message='Sign out?'):
            self.window.destroy()
            window = Tk()
            LoginForm(window)
            window.mainloop()
    
    def pass_change(self, event = None):
        username = self.username
        cpassword = self.cpassword_entry.get()
        password = self.password_entry.get()
        confpass = self.password_entry1.get()
        PIN = self.PIN_entry.get()
        if check_cpass_PIN(cpassword, PIN):
            if password != confpass:
                messagebox.showinfo(title='Oops', message="Passwords do not match")
            else:
                if messagebox.askyesnocancel(title="Confirm", message="Are you sure you want to change your password?"):
                    self.cpassword_entry.delete(0, END)
                    self.password_entry.delete(0, END)
                    self.password_entry1.delete(0, END)
                    self.PIN_entry.delete(0, END)
                    self.cpassword_entry.focus()
                    change_password(username, password)
                    messagebox.showinfo(title= 'Congrats', message="Password updated successfully")
                    self.back()
        else:
            if len(password) == 0 or len(confpass) == 0 or len(PIN) == 0:
                messagebox.showinfo(title='Oops', message="Please make sure you haven't left any field empty")
            elif len(password) < 6 or len(password) > 15:
                messagebox.showinfo(title='Oops', message="The password must be at least 6 characters and no more than 15 in length")
            elif " " in password:
                messagebox.showinfo(title='Oops', message="Please don't include space character in the password")
            else:
                messagebox.showinfo(title='Oops', message="Your credentials don't match an account in our system")
    
    def setup_passchange(self):
        self.chpass_frame = Frame(self.window, width=1280, height=720, bg=self.bg_color)
        self.chpass_frame.place(x=420, y=40)
        # =============== Back to main page ============
        generate_password_button = Button(self.chpass_frame, text = "⭠ Back to main page", font=('yu gothic ui', 13, 'bold'), width=25, bd=0, cursor='hand2', fg=self.text_color, bg= self.bg_color, activebackground=self.bg_color, command=self.back)
        generate_password_button.place(x=170, y=40)
        
        # =============== Change password =============
        self.chpass_label = Label(self.chpass_frame, text='Change password', font=('yu gothuic ui', 20, 'bold'), bg=self.bg_color, fg=self.text_color)
        self.chpass_label.place(x=100, y=80)

        # =============== Current password ============
        
        self.cpassword_label = Label(self.chpass_frame, text= "Current password", bg=self.bg_color,fg= self.text_color, font=('yu gothic ui', 13, 'bold'))
        self.cpassword_label.place(x=60, y= 140)
        self.cpassword_entry = Entry(self.chpass_frame, highlightthickness=0, relief= FLAT, bg=self.bg_color, fg=self.text_color, font=('yu gothic ui', 13, 'bold'), show='*')
        self.cpassword_entry.place(x=60, y=180, width=270)
        self.cpassword_entry.focus_set()
        self.cpassword_entry.bind('<Return>', self.pass_change)
        self.password_line = Canvas(self.chpass_frame, width= 300, height= 2.0, bg = self.text_color, highlightthickness= 0)
        self.password_line.place(x=60, y=210)
    
        # =============== New Password ================
        self.password_label = Label(self.chpass_frame, text= "New password", bg=self.bg_color,fg= self.text_color, font=('yu gothic ui', 13, 'bold'))
        self.password_label.place(x=60, y= 240)
        self.password_entry = Entry(self.chpass_frame, highlightthickness=0, relief= FLAT, bg=self.bg_color, fg=self.text_color, font=('yu gothic ui', 13, 'bold'), show='*')
        self.password_entry.place(x=60, y=280, width=270)
        self.password_entry.bind('<Return>', self.pass_change)
        self.password_line = Canvas(self.chpass_frame, width= 300, height= 2.0, bg = self.text_color, highlightthickness= 0)
        self.password_line.place(x=60, y=310)
        
        # ================= Show/Hide pass image ==============
        self.show_button = Button(self.chpass_frame, image=self.show_image, command=self.show, relief=FLAT, activebackground=self.bg_color, borderwidth=0, background=self.bg_color, cursor="hand2")
        self.show_button.place(x=330, y=280)

        # =============== Generate password ============
        generate_password_button = Button(self.chpass_frame, text = "Suggest a strong password!", font=('yu gothic ui', 13, 'bold'), width=25, bd=0, cursor='hand2', fg=self.text_color, bg= self.bg_color, activebackground=self.bg_color, command=self.generatepass)
        generate_password_button.place(x = 130, y= 320)

        # =============== Confirm New Password ================
        self.password_label = Label(self.chpass_frame, text= "Confirm new password", bg=self.bg_color, fg= self.text_color, font=('yu gothic ui', 13, 'bold'))
        self.password_label.place(x=60, y=360)
        self.password_entry1 = Entry(self.chpass_frame, highlightthickness=0, relief= FLAT, bg=self.bg_color, fg=self.text_color, font=('yu gothic ui', 13, 'bold'), show='*')
        self.password_entry1.place(x=60, y=400, width=270)
        self.password_entry1.bind('<Return>', self.pass_change)
        self.password_line = Canvas(self.chpass_frame, width= 300, height= 2.0, bg=self.text_color, highlightthickness= 0)
        self.password_line.place(x=60, y=430)

        # =============== PIN ================
        self.PIN_label = Label(self.chpass_frame, text= "Enter your registered PIN", bg=self.bg_color,fg= self.text_color, font=('yu gothic ui', 13, 'bold'))
        self.PIN_label.place(x=60, y=460)
        self.PIN_entry = Entry(self.chpass_frame, highlightthickness=0, relief= FLAT, bg=self.bg_color, fg=self.text_color, font=('yu gothic ui', 13, 'bold'), validate='key')
        self.PIN_entry['validatecommand'] = (self.PIN_entry.register(self.validate_input), '%P')
        self.PIN_entry.bind('<Return>', self.pass_change)
        self.PIN_entry.place(x=290, y=460, width=240)
        self.PIN_line = Canvas(self.chpass_frame, width= 40, height= 2.0, bg =self.text_color, highlightthickness= 0)
        self.PIN_line.place(x=290, y=490)

        # =============== Update Button ================
        self.updatep = Button(self.chpass_frame, text = "Update", font=('yu gothic ui', 13, 'bold'), width=25, bd=2, bg=self.btn_bg, cursor='hand2', activebackground=self.btn_active_bg, fg=self.text_color, command=self.pass_change)
        self.updatep.place(x=80, y=520)
        
        # =============== Right Side Image ================
        self.side_image = Image.open("Photos//Tom.png")
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.window, image=photo, bg= self.bg_color)
        self.side_image_label.image = photo
        self.side_image_label.place(x=800, y= 80)  
        # =============== Left Side Image ================
        self.side_image = Image.open("Photos//Jerry.png")
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.window, image=photo, bg= self.bg_color)
        self.side_image_label.image = photo
        self.side_image_label.place(x=150, y= 310) 
    
    def exit(self):
        if messagebox.askyesnocancel(title='Wanna leave? =(',message='Exit this screen?'):
            self.window.destroy()

    def generatepass(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '@', '&', '*', '+', '#', '%']
        self.password_entry.delete(0, END)
        password_letters = [choice(letters) for _ in range(randint(4,6))]
        password_numbers = [choice(numbers) for _ in range(randint(2,4))]
        password_symbols = [choice(symbols) for _ in range(randint(0,3))]
        password_list = password_letters + password_numbers + password_symbols   
        shuffle(password_list)
        password = "".join(password_list)
        self.show()
        self.password_entry.insert(0, password)


    def show(self):
        self.hide_button = Button(self.chpass_frame, image=self.hide_image, command=self.hide, relief=FLAT, activebackground=self.bg_color, borderwidth=0, background=self.bg_color, cursor="hand2")
        self.hide_button.place(x=330, y=280)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.chpass_frame, image=self.show_image, command=self.show, relief=FLAT, activebackground=self.bg_color, borderwidth=0, background=self.bg_color, cursor="hand2")
        self.show_button.place(x=330, y=280)
        self.password_entry.config(show='*')
    
    def validate_input(self, text):
        if (text.isdigit() and len(text) <= 4) or len(text) == 0:
            return True
        else:
            return False
        
    def back(self):
        self.chpass_frame.destroy()
    
    def run(self):
        run_ = menu.Menu()
        self.window.destroy()
        mg.Initialization().draw_floor()
        running = True
        while running: 
            run_.handle_menu_events()
            run_.draw_menu()

def page():
    window = Tk()
    LoginForm(window)
    window.mainloop()


def login_success(username):
    new_window = Tk()
    UserInterface(new_window, username)
    new_window.mainloop()
    
