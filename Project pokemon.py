# -*- coding: utf-8 -*-
"""
Created on Sun May 15 11:40:08 2022

@author: Cupcake@250
note:There are mny of these cards but I will add them slowly cause i think for now these are enough
"""

from tkinter import*
from PIL import ImageTk,Image
import random
root=Tk()
root.title("Pokemon")
root.geometry("700x700")
root.configure(bg="#f5b505")

Button_img=ImageTk.PhotoImage(Image.open("button.jpg"))
Abra=ImageTk.PhotoImage(Image.open("abra.jpg"))
Bulbasor=ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
Charmender=ImageTk.PhotoImage(Image.open("charmender.jpg"))
Iyvasour=ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
Jigglypuff=ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
Kadabra=ImageTk.PhotoImage(Image.open("Kadabra.jpg"))
Meowth=ImageTk.PhotoImage(Image.open("meowth.jpg"))
Nidoking=ImageTk.PhotoImage(Image.open("nidoking.jpg"))
Paras=ImageTk.PhotoImage(Image.open("paras.jpg"))
Persion=ImageTk.PhotoImage(Image.open("persion.jpg"))
Pikachu=ImageTk.PhotoImage(Image.open("pikachu.jpg"))
Ratata=ImageTk.PhotoImage(Image.open("ratata.jpg"))
Sguirtle=ImageTk.PhotoImage(Image.open("squirtle.jpg"))
Mewtwo=ImageTk.PhotoImage(Image.open("mewtwo.png"))




label_player1=Label(root,text="Player1",bg="#f50525",fg="white")
label_player1.place(relx=0.1,rely=0.3,anchor=CENTER)

label_player2=Label(root,text="Player2",bg="#8505f5",fg="white")
label_player2.place(relx=0.9,rely=0.3,anchor=CENTER)

label_score1=Label(root,text="",bg="#f50525",fg="white")
label_score1.place(relx=0.1,rely=0.4,anchor=CENTER)

label_score2=Label(root,text="",bg="#8505f5",fg="white")
label_score2.place(relx=0.9,rely=0.4,anchor=CENTER)

label_img=Label(root,bg="#f50525",fg="white")
label_img.place(relx=0.5,rely=0.5,anchor=CENTER)

pokemon_list=[Abra, Bulbasor, Charmender, Iyvasour, Jigglypuff, Kadabra, Meowth, Nidoking, Paras, Persion, Pikachu, Ratata, Sguirtle, Mewtwo]
pokemon_power=[30, 60, 50, 100, 70, 70, 60, 90, 40, 70, 200, 40, 50, 170]
player1_score=0
def player1():
    global player1_score
    random_no1=random.randint(0, 15)
    random_pokemon1=pokemon_list[random_no1]
    random_power_level1=pokemon_power[random_no1]
    label_img['image']=random_pokemon1
    player1_score=player1_score + random_power_level1
    label_score1["text"]=str(player1_score)


player1_button=Button(root, image=Button_img,command=player1)
player1_button.place(relx=0.1,rely=0.6,anchor=CENTER)

player2_score=0
def player2():
    global player2_score
    random_no2=random.randint(0, 15)
    random_pokemon2=pokemon_list[random_no2]
    random_power_level2=pokemon_power[random_no2]
    label_img['image']=random_pokemon2
    player2_score=player2_score + random_power_level2
    label_score2["text"]=str(player2_score)

player2_button=Button(root, image=Button_img,command=player2)
player2_button.place(relx=0.9,rely=0.6,anchor=CENTER)


root.mainloop()