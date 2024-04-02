import tkinter as tk
import Frogger_PP
from PIL import Image, ImageTk
from supabase import create_client, Client
from tkinter import simpledialog
from tkinter import ttk

# Supabase-URL und API-Schlüssel aus Umgebungsvariablen laden
url = "https://fobkwrwilrrkrfpxntiz.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZvYmt3cndpbHJya3JmcHhudGl6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDgxODg2ODUsImV4cCI6MjAyMzc2NDY4NX0.xZKRGJPLqrWmky8h-fO-BsZQrD8R_G16tv96286Li8s"
supabase = create_client(url, key)


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
frogskin = 0
anzeigescore = 0
anzeigehighscore = 0
player_name = "want to stay anonym :P "

#____________Master______________

master = tk.Tk()
master.title("Frogger")
master.geometry(size)
master.resizable(width=0, height=0)
master.config(bg = "#000047")
minifrog = tk.PhotoImage(file="minifrog.png",)
master.iconphoto(False, minifrog)

#Befehl zum Starten des Frogger Programms
def skinwechsel(kostüm):
        root2.destroy
        global frogskin
        frogskin = kostüm
        print(kostüm)

def skin():
    global root2    
    root2 = tk.Toplevel()
    root2.geometry(size)
    root2.title("Frogger")
    root2.resizable(width=0, height=0)
    root2.config(bg = "#500027")
    skinButton1 = tk.Button(root2 ,image = exit_ , command = root2.destroy, width = 200, height = 66, bg = "#500027", border= 0)
    skinButton1.place(relx = 0.33, rely = 0.85)
    skin0 = tk.Button(root2 ,image = buy , command = lambda: skinwechsel(3), width = 150, height = 43, bg = "#500027", border= 0)
    if not frogskin == 3:
        skin0.place(relx = 0.085, rely = 0.65)
    skin1 = tk.Button(root2 ,image = buy , command = lambda: skinwechsel(4), width = 150, height = 43, bg = "#500027", border= 0)
    if not frogskin == 4:
        skin1.place(relx = 0.385, rely = 0.65)
    skin2 = tk.Button(root2 ,image = buy , command = lambda: skinwechsel(5), width = 150, height = 43, bg = "#500027", border= 0)
    if not frogskin == 5:
        skin2.place(relx = 0.685, rely = 0.65)
    skin3 = tk.Button(root2 ,image = buy , command = lambda: skinwechsel(0), width = 150, height = 43, bg = "#500027", border= 0)
    if not frogskin == 0:
        skin3.place(relx = 0.085, rely = 0.3)
    skin4 = tk.Button(root2 ,image = buy , command = lambda: skinwechsel(1), width = 150, height = 43, bg = "#500027", border= 0)
    if not frogskin == 1:
        skin4.place(relx = 0.385, rely = 0.3)
    skin5 = tk.Button(root2 ,image = buy , command = lambda: skinwechsel(2), width = 150, height = 43, bg = "#500027", border= 0)
    if not frogskin == 2:
        skin5.place(relx = 0.685, rely = 0.3)
    #Skin Bilder
    s0kin = tk.Label(root2, image = skin0_, bg = "#500027")
    s0kin.place(relx = 0.16, rely = 0.2)
    s1kin = tk.Label(root2, image = skin1_, bg = "#500027")
    s1kin.place(relx = 0.46, rely = 0.2)
    s2kin = tk.Label(root2, image = skin2_, bg = "#500027")
    s2kin.place(relx = 0.76, rely = 0.2)
    s3kin = tk.Label(root2, image = skin3_, bg = "#500027")
    s3kin.place(relx = 0.16, rely = 0.55)
    s4kin = tk.Label(root2, image = skin4_, bg = "#500027")
    s4kin.place(relx = 0.46, rely = 0.55)
    s5kin = tk.Label(root2, image = skin5_, bg = "#500027")
    s5kin.place(relx = 0.76, rely = 0.55)


    
def control():
    root3 = tk.Toplevel()
    root3.geometry(size)
    root3.title("Frogger")
    root3.resizable(width=0, height=0)
    root3.config(bg = "#004017")
    controlButton1 = tk.Button(root3 ,image = exit_ , command = root3.destroy, width = 200, height = 66, bg = "#004017", border= 0)
    controlButton1.place(relx = 0.33, rely = 0.85)
    anleitung = tk.Label(root3, image = Anleitung)
    anleitung.place(relx = -0.004, rely = 0.00)
    
def get_highscores():
    global my_listbox
    worldrank = []
    my_listbox.delete(0, 'end')
    response = supabase.table("Highscore").select("*").order("score", desc=True).execute()
    highscores = response.data
    for rank, score in enumerate(highscores, start=1,):
        worldrank += [f"{rank}. Player:  {score['name']} - Score: {score['score']}"]
    for in_listbox in range(10):
        my_listbox.insert(tk.END, worldrank[in_listbox])
    print(anzeigescore)
    print(anzeigehighscore)


def start():
    global anzeigescore, anzeigehighscore   
    anzeigescore, reset = Frogger_PP.frogger(Hoehe, frogskin)
    if anzeigescore > anzeigehighscore:
        anzeigehighscore = anzeigescore
        data, count = supabase.table("Highscore").insert({"name": player_name, "score": anzeigehighscore}).execute()
    score.config(text = anzeigehighscore)
    if reset:
        start()

username = simpledialog.askstring("Nutzername", "Bitte gib deinen Namen ein:")
if username:
    player_name = str(username)
    
#_________________Bilder__________________

#Skins
skinb = 60
skinh = 50  
    
skin0_g = Image.open("frog.png")
resize_skin0 = skin0_g.resize((skinb, skinh))
skin0_ = ImageTk.PhotoImage(resize_skin0)
skin1_g = Image.open("skin1.png")
resize_skin1 = skin1_g.resize((skinb, skinh))
skin1_ = ImageTk.PhotoImage(resize_skin1)
skin2_g = Image.open("skin2.png")
resize_skin2 = skin2_g.resize((skinb, skinh))
skin2_ = ImageTk.PhotoImage(resize_skin2)
skin3_g = Image.open("skin3.png")
resize_skin3 = skin3_g.resize((skinb, skinh))
skin3_ = ImageTk.PhotoImage(resize_skin3)
skin4_g = Image.open("skin4.png")
resize_skin4 = skin4_g.resize((skinb, skinh))
skin4_ = ImageTk.PhotoImage(resize_skin4)
skin5_g = Image.open("skin5.png")
resize_skin5 = skin5_g.resize((skinb, skinh))
skin5_ = ImageTk.PhotoImage(resize_skin5)

#refreshbutton
re_g = Image.open("refresh.png")
resize_re = re_g.resize((100, 100))
refresh = ImageTk.PhotoImage(resize_re)

#Playbutton
play_g = Image.open("play.png")
resize_play = play_g.resize((100, 100))
play = ImageTk.PhotoImage(resize_play)

#Controlbutton
steuern_g = Image.open("control.png")
resize_steuern = steuern_g.resize((100, 100))
steuern = ImageTk.PhotoImage(resize_steuern)

#Shopbuttom
shop_g = Image.open("shop.png")
resize_shop = shop_g.resize((100, 100))
shop = ImageTk.PhotoImage(resize_shop)

#Zurückbutton
exit_g = Image.open("exit.png")
resize_exit = exit_g.resize((200, 66))
exit_ = ImageTk.PhotoImage(resize_exit)

#Kaufen
buy_g = Image.open("select.png")
resize_buy = buy_g.resize((150, 44))
buy = ImageTk.PhotoImage(resize_buy)

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

hier = tk.Label(master, width = 66, height = 5, bg = "#000047", border= 0)
hier.place(relx = 0.16, rely = 0.57)

# Erstelle einen Scrollbar-Widget
scrollbar = ttk.Scrollbar(hier, orient='vertical')

# Erstelle ein Listbox-Widget und verknüpfe es mit dem Scrollbar
my_listbox = tk.Listbox(hier, width = 66, height = 5, yscrollcommand=scrollbar.set, bg = "#000047", fg = "yellow", border= 0)

# Konfiguriere die Scrollbar, um mit der Listbox zu interagieren
scrollbar.config(command=my_listbox.yview)

# Packe die Widgets auf das Hauptfenster
scrollbar.pack(side="right", fill="y")                                       # .place(relx = 0.135, rely = 0.57,)
my_listbox.pack(side="left", fill="y")

#Froggertitel Label
Frogger = tk.Label(master, image = frogger, bg = "#000047")
Frogger.place(relx = 0.07, rely = 0.05)

#Frosch deko
Deko1 = tk.Label(master, image = deko1, bg = "#000047")
Deko1.place(relx = 0.68, rely = 0.7)

Deko2 = tk.Label(master, image = deko2, bg = "#000047")
Deko2.place(relx = 0.00, rely = 0.7)

#Aktualisieren
aktualisierenButton = tk.Button(master ,image = refresh , command = lambda: get_highscores(), width = 100, height = 100,fg = "white", font = (7), bg = "#000047", border= 0)
aktualisierenButton.place(relx = 0.42, rely = 0.7)

#Playbutton
playButton = tk.Button(master ,image = play , command = start, width = 100, height = 100, bg = "#000047", border= 0)
playButton.place(relx = 0.42, rely = 0.4)

#Steuerungbutton
controlButton = tk.Button(master ,image = steuern , command = control, width = 100, height = 100, bg = "#000047", border= 0)
controlButton.place(relx = 0.67, rely = 0.4)

#Skinbutton
skinButton = tk.Button(master ,image = shop , command = skin, width = 100, height = 100, bg = "#000047", border= 0)
skinButton.place(relx = 0.17, rely = 0.4)

#Exitbutton
exitButton1 = tk.Button(master ,image = exit_ , command = master.destroy, width = 200, height = 66, bg = "#000047", border= 0)
exitButton1.place(relx = 0.34, rely = 0.87)

#Name
Playname = "Name : " + str(username)
anzeigename = tk.Label(master, anchor= 'w', width = 40, height = 1, text = Playname  , font = ("roman", 20), fg = "yellow", bg = "#000047")
anzeigename.place(relx = 0.05, rely = 0.02)

#Highscore
highscore = tk.Label(master, anchor= 'w', width =15, height = 1, text = "Highscore :  " , font = ("Minecraft", 20), fg = "red", bg = "#000047")
highscore.place(relx = 0.6, rely = 0.02)
score = tk.Label(highscore, width =4, height = 1, text = str(anzeigehighscore) , font = ("Minecraft", 20), fg = "red", bg = "#000047")
score.place(relx = 0.65, rely = 0)

# #Lastscore
# lastscore = tk.Label(master, anchor= 'w', width =15, height = 1, text = "Last-score :  " , font = ("Minecraft", 20), fg = "red", bg = "#000047")
# lastscore.place(relx = 0.33, rely = 0.33)
# score2 = tk.Label(lastscore, width =4, height = 1, text = str(anzeigescore) , font = ("Minecraft", 20), fg = "red", bg = "#000047")
# score2.place(relx = 0.65, rely = 0)

master.mainloop()
#Frogger_PP.frogger(Hoehe)

#____________________Quellen____________________

#https://www.python-lernen.de/tkinter-gui.htm
