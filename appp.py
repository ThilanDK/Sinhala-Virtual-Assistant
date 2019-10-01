from ttkthemes import ThemedStyle
import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
import speech_recognition as sr
from selenium import webdriver
from googletrans import Translator
from googlesearch import search
import re
import subprocess
translator = Translator()
r=sr.Recognizer()
app = tk.Tk()
app.title('App')
#app.
side = tk.Frame(app, width=200, bg='white', height=500, relief='sunken', borderwidth=2)
side.pack(expand=True, fill='both', side='left', anchor='nw')
main = tk.Frame(app, bg='#CCC', width=500, height=500)
main.pack(expand=True, fill='both', side='right')
can=tk.PhotoImage(file="ORANGE+DJ-BOT.png")
background_image = tk.PhotoImage(file="chatbot_0.png")
background_label = tk.Label(main, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.image = background_image
#background_image2 = tk.PhotoImage(file="hello.png")
#background_label2 = tk.Label(main, image=background_image)
#background_label2.place(x=0, y=0, relwidth=1, relheight=1)
#background_label2.image = background_image2
side.configure(bg='darkorange')
style = ThemedStyle(app)
style.set_theme("blue")
sider = tk.Frame(app, width=200, bg='white', height=500, relief='sunken', borderwidth=2)
#app.configure(image="Reasons-to-use-a-virtual-assistant_chapt3 (1).png")
#tktext = tk.Label(side, text=" tk Label")
#tktext.pack(side="top")
#tkbutton = tk.Button(side, text="tk Button", justify=tk.LEFT)
#tkbutton.pack(side="left")

#text = ttk.Label(side, text=" ttk Label")
#text.pack()

class alien(object):
    def __init__(self):
        self.root = app
        button.place_forget()
        part = tk.Frame(side, width=100, bg='white', height=100, relief='sunken', borderwidth=2)
        part.pack(expand=True, fill='both')
        part.configure(bg="darkorange")
        part2= tk.Frame(sider, width=100, bg='white', height=100, relief='sunken', borderwidth=2)
        part2.pack(expand=True, fill='both')
        part2.configure(bg="darkorange")
        self.canvas = Canvas(part)
        self.canvas.pack()
        self.canvas.create_image(150,150,image=can,anchor="center")
       # self.alien1 = self.canvas.create_arc(20, 260, 120, 360, outline='white', fill='blue')
        self.alien2 = self.canvas.create_oval(2, 2, 80, 80, outline='darkorange', fill='darkorange')
        self.canvas.pack()
        self.root.after(0, self.animation)

        self.root.mainloop()
    def labe(app):
        button.place_forget()

    def animation(self):
        track = 0
        while True:
            x = 5
            y = 0
            if track == 0:
                for i in range(0, 51):
                    time.sleep(0.025)
                   # self.canvas.move(self.alien1, x, y)
                    self.canvas.move(self.alien2, x, y)
                    self.canvas.update()
                track = 1
                print("check")

            else:
                for i in range(0, 51):
                    time.sleep(0.025)
                   # self.canvas.move(self.alien1, -x, y)
                    self.canvas.move(self.alien2, -x, y)
                    self.canvas.update()
                track = 0
            print(track)



def start():
    sider.pack(expand=True, fill='both', side='left', anchor='nw')
    button2 = tk.Button(side, text="record started")
    button2.pack(side="top")
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func
button = tk.Button(side, text="recording", command =start())
button.pack(side="top")





app.geometry('1000x523')






app.mainloop()