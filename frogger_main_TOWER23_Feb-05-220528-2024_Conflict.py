import tkinter as tk
import Frogger_PP
from PIL import Image, ImageTk

#______________Fenstergrößen______________

#Fensterhöhe
Hoehe = 704

Bereich = (3 / 8) * Hoehe
Abschnitt = Bereich / 6

#Fensterbreite
Breite = int((Abschnitt * 0.7) * 20)
size = str(Breite) + "x" + str(Hoehe) + "+600+150"

choehe = 570
cbreite = Breite


#____________Master______________

master = tk.Tk()
master.title("Frogger")
master.geometry(size)
master.resizable(width=0, height=0)
master.config(bg = "#000047")
minifrog = tk.PhotoImage(file="minifrog.png",)
master.iconphoto(False, minifrog)

#Befehl zum Starten des Frogger Programms
def start():
    root1 = tk.Toplevel()
    root1.geometry(size)
    root1.title("Frogger")
    root1.resizable(width=0, height=0)
    root1.config(bg = "#000047")
    #Frogger_PP.frogger(Hoehe)

def skin():
    root2 = tk.Toplevel()
    root2.geometry(size)
    root2.title("Frogger")
    root2.resizable(width=0, height=0)
    root2.config(bg = "#000047")
    skinButton1 = tk.Button(root2 ,image = exit_ , command = root2.destroy, width = 200, height = 66, bg = "#000047")
    skinButton1.place(relx = 0.33, rely = 0.85)
    
def control():
    root3 = tk.Toplevel()
    root3.geometry(size)
    root3.title("Frogger")
    root3.resizable(width=0, height=0)
    root3.config(bg = "#000047")
    controlButton1 = tk.Button(root3 ,image = exit_ , command = root3.destroy, width = 200, height = 66, bg = "#000047")
    controlButton1.place(relx = 0.33, rely = 0.85)
    anleitung = tk.Label(root3, image = Anleitung)
    anleitung.place(relx = -0.004, rely = 0.00)
    
#_________________Bilder__________________

#Playbutton
play_g = Image.open("play.png")
resize_play = play_g.resize((100, 100))
play = ImageTk.PhotoImage(resize_play)
#play = tk.PhotoImage(file="play.png",)

#Zurückbutton
exit_g = Image.open("exit.png")
resize_exit = exit_g.resize((200, 66))
exit_ = ImageTk.PhotoImage(resize_exit)

#Froggertitel
frogger_g = Image.open("TitelFrogger.png")
resize_frogger = frogger_g.resize((550, 200))
frogger = ImageTk.PhotoImage(resize_frogger)

#Frosch deko
deko2_g = Image.open("deko2_.png")
resize_deko2 = deko2_g.resize((200, 200))
deko2 = ImageTk.PhotoImage(resize_deko2)

deko1_g = Image.open("deko1_.png")
resize_deko1 = deko1_g.resize((200, 200))
deko1 = ImageTk.PhotoImage(resize_deko1)

#Hintergrund
back_g = Image.open("FroggerBack.jpg")
resize_back = back_g.resize((Breite, Hoehe))
back = ImageTk.PhotoImage(resize_back)

#Anleitung
Anleitung_g = Image.open("Anleitung.png")
resize_Anleitung = Anleitung_g.resize((cbreite, choehe))
Anleitung = ImageTk.PhotoImage(resize_Anleitung)

#____________________Elemente_______________

#Froggertitel Label
Frogger = tk.Label(master, image = frogger, bg = "#000047")
Frogger.place(relx = 0.05, rely = 0.05)

#Frosch deko
Deko2 = tk.Label(master, image = deko2, bg = "#000047")
Deko2.place(relx = 0.04, rely = 0.60)

Deko1 = tk.Label(master, image = deko1, bg = "#000047")
Deko1.place(relx = 0.65, rely = 0.55)

#Playbutton
playButton = tk.Button(master ,image = play , command = start, width = 100, height = 100, bg = "#000047")
playButton.place(relx = 0.4, rely = 0.4)

#Steuerungbutton
controlButton = tk.Button(master ,image = play , command = control, width = 100, height = 100, bg = "#000047")
controlButton.place(relx = 0.6, rely = 0.4)

#Skinbutton
skinButton = tk.Button(master ,image = play , command = skin, width = 100, height = 100, bg = "#000047")
skinButton.place(relx = 0.2, rely = 0.4)

#Exitbutton
exitButton1 = tk.Button(master ,image = exit_ , command = master.destroy, width = 200, height = 66, bg = "#000047")
exitButton1.place(relx = 0.33, rely = 0.85)


master.mainloop()
#Frogger_PP.frogger(Hoehe)

#____________________Quellen____________________

#https://www.python-lernen.de/tkinter-gui.htm




