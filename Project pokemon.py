# -*- coding: utf-8 -*-
"""
Created on Sun May 15 11:40:08 2022

@author: Cupcake@250
"""

from tkinter import*
from PIL import ImageTk,Image
root=Tk()
root.title("Pokemon")
root.geometry("400x500")
root.configure(bg="#f5b505")

Pikachu=ImageTk.PhotoImage(Image.open("pikachu.jpg"))


label_player1=Label(root,text="Player1",bg="#f50525",fg="white")
label_player1.place(relx=0.1,rely=0.3,anchor=CENTER)

Button=ImageTk.PhotoImage(Image.open("button.jpg"))



label_player2=Label(root,text="Player2",bg="#8505f5",fg="white")
label_player2.place(relx=0.9,rely=0.3,anchor=CENTER)

label_score1=Label(root,text="",bg="#f50525",fg="white")
label_score1.place(relx=0.1,rely=0.4,anchor=CENTER)

label_score2=Label(root,text="",bg="#8505f5",fg="white")
label_score2.place(relx=0.9,rely=0.4,anchor=CENTER)

Button=ImageTk.PhotoImage(Image.open("button.jpg"))



root.mainloop()