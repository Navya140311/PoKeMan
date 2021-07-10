from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.geometry("500x500")
root.title("PoKeMaN")
root.configure(background="#f5bd1f")


bulbasour_image=ImageTk.PhotoImage(Image.open("bulbasour.jpg"))

jigglypuff_image=ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))

ratata_image=ImageTk.PhotoImage(Image.open("ratata.jpg"))

kadabra_image=ImageTk.PhotoImage(Image.open("kadabra.jpg"))

squirtle_image=ImageTk.PhotoImage(Image.open("squirtle.jpg"))

charmender_image=ImageTk.PhotoImage(Image.open("charmender.jpg"))

meowth_image=ImageTk.PhotoImage(Image.open("meowth.jpg"))

nideoking_image=ImageTk.PhotoImage(Image.open("nidoking.jpg"))

paras_image=ImageTk.PhotoImage(Image.open("paras.jpg"))

abra_image=ImageTk.PhotoImage(Image.open("abra.jpg"))

persion_image=ImageTk.PhotoImage(Image.open("persion.jpg"))

ivyasour_image=ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))

pikachu_image=ImageTk.PhotoImage(Image.open("pikachu.jpg"))


player1 = Label(root, text = "Player 1", bg="#800000",fg = "#f5bd1f")
player1.place(relx=0.1, rely=0.3, anchor=CENTER)

player2 = Label(root, text = "Player 2", bg="#800000",fg = "#f5bd1f")
player2.place(relx=0.9, rely=0.3, anchor=CENTER)

player_1_score_label = Label(root,bg="#800000" ,fg = "#f5bd1f")
player_1_score_label.place(relx=0.1, rely=0.4, anchor=CENTER)

player_2_score_label = Label(root,bg="#800000", fg = "#f5bd1f")
player_2_score_label.place(relx=0.9, rely=0.4, anchor=CENTER)

random_pokeman_label = Label(root, bg="#800000",fg = "#f5bd1f")
random_pokeman_label.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
