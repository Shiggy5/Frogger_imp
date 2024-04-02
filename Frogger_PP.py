def frogger(fensterhoehe, skin):
    
    import pygame
    import time
    import random
    pygame.init()

    #__________________________________Definieren der Variablen
    
    score = 0
    godmode = False
    nichtWasser = False
    inAnimation = False
    Froschda = True
    pause = False
    überfahren = False

    reset = False

    level = 1
    #Levelmultiplikator (Erhöhung der Geschwindigkeit/Animationsgeschwindigkeit)
    levelm = (1 + (level * 0.2)) - 0.2
    animultiplikator = (2/level)
    
    #Um Pause aufzuheben
    pausezähler = 0

    #Fensterhöhe
    FENSTERHOEHE = fensterhoehe

    bereich = (3 / 8) * FENSTERHOEHE
    abschnitt = bereich / 6

    #Fensterbreite
    FENSTERBREITE = (abschnitt * 0.7) * 20

    #Aurechnung der Zielbereiche
    rest = FENSTERBREITE * 0.0174
    zwischen = FENSTERBREITE * 0.1085
    seeblatt = FENSTERBREITE * 0.1066
    zielhoehe = FENSTERHOEHE * 0.0595
    zielbreite = FENSTERBREITE * 0.05814
    zielrest = FENSTERBREITE * 0.042636
    zielzwischen = FENSTERBREITE * 0.157
    zielpos_1 = zielrest + (zielzwischen * 0) + (zielbreite * 0)
    zielpos_2 = zielrest + (zielzwischen * 1) + (zielbreite * 1)
    zielpos_3 = zielrest + (zielzwischen * 2) + (zielbreite * 2)
    zielpos_4 = zielrest + (zielzwischen * 3) + (zielbreite * 3)
    zielpos_5 = zielrest + (zielzwischen * 4) + (zielbreite * 4)
    zielpos_y = FENSTERHOEHE * 0.045635
    
    #Ausrechnung der Krokodiel Position
    krokopos_y = FENSTERHOEHE * 0.06
    krokopos_1 = (zielrest * 0.7) + (zielzwischen * 0) + (zielbreite * 0)
    krokopos_2 = (zielrest * 0.7) + (zielzwischen * 1) + (zielbreite * 1)
    krokopos_3 = (zielrest * 0.7) + (zielzwischen * 2) + (zielbreite * 2)
    krokopos_4 = (zielrest * 0.7) + (zielzwischen * 3) + (zielbreite * 3)
    krokopos_5 = (zielrest * 0.7) + (zielzwischen * 4) + (zielbreite * 4)
    krokopos = [krokopos_1, krokopos_2, krokopos_3, krokopos_4, krokopos_5, -100, -140, -130]
    krokopos_x = random.choice(krokopos)            

    #Geschwindigkeit
    ges = 1

    #Leben
    leben = 3

    # Farbe
    SCHWARZ = ( 0, 0, 0)
    WEISS   = ( 255, 255, 255)

    #_________________Hintergrund_____________
       
    #Bild
    hintergrund1 = pygame.image.load("frogger_background.png")
    hintergrund = pygame.transform.scale(hintergrund1, (FENSTERBREITE, FENSTERHOEHE))
    
    #Musik
    pygame.mixer.music.load('Level.mp3')
    pygame.mixer.music.play(-1,0.0)
    pygame.mixer.music.set_volume(.6)

    #___________________Sounds_____________________
    
    springen = pygame.mixer.Sound('springen.mp3')
    springen.set_volume(.7)
    tod = pygame.mixer.Sound('tod.mp3')
    wasser = pygame.mixer.Sound('wasser.mp3')
    death = pygame.mixer.Sound('death.wav')
    gameover = pygame.mixer.Sound('game_over.wav')
    pygame.mixer.Sound.set_volume(springen, 0.3)
    #Krokodiel = pygame.mixer.Sound('krokodiel.mp3')
    die = pygame.mixer.Sound('die.mp3')
    ende = pygame.mixer.Sound('ende.mp3')

    #_______________Frosch_________________
    
    #Frog Allgemeines
    bewegung = abschnitt
    ballbreite = 0.75 * abschnitt
    ballhoehe = 0.75 * abschnitt
    last_direction = 'up'
    spawnx = (FENSTERBREITE // 2) - (ballbreite // 2)
    spawny = FENSTERHOEHE - (FENSTERHOEHE /16)
    ballpos_x = spawnx
    ballpos_y = spawny

    #Bilder
    frog1 = pygame.image.load("frog.png")
    frog = pygame.transform.scale(frog1, (ballbreite, ballhoehe))
    sprung_g = pygame.image.load("frog_jump.png")
    sprung = pygame.transform.scale(sprung_g, (ballbreite, ballhoehe + (ballhoehe * (1/2))))
    frogs2 = pygame.image.load("skin1.png")
    frog2 = pygame.transform.scale(frogs2, (ballbreite, ballhoehe))
    frogs3 = pygame.image.load("skin2.png")
    frog3 = pygame.transform.scale(frogs3, (ballbreite, ballhoehe))
    frogs4 = pygame.image.load("skin3.png")
    frog4 = pygame.transform.scale(frogs4, (ballbreite, ballhoehe))
    frogs5 = pygame.image.load("skin4.png")
    frog5 = pygame.transform.scale(frogs5, (ballbreite, ballhoehe))
    frogs6 = pygame.image.load("skin5.png")
    frog6 = pygame.transform.scale(frogs6, (ballbreite, ballhoehe))

    
    #Liste für Animation
    frogl = ['','']
    frogl[0] = frog
    frogl[1] = sprung
    
    #Variablen für Animation
    framefrog = 0
    framef = 0

    #______________Autos_______________
    
    #Startposition der Autos
    speed1 = FENSTERBREITE + 100
    speed2 = -350
    speed3 = FENSTERBREITE + 250
    speed4 = -100
    speed5 = FENSTERBREITE + 150
    speed6 = FENSTERBREITE + 300
    speed1_ = FENSTERBREITE + 450
    speed2_ = -500
    speed3_ = FENSTERBREITE + 600
    speed4_ = -550
    speed5_ = FENSTERBREITE + 725
    
    #Berechnung der Autoposition auf y-Koordinate
    for i in range(1, 7):
        auto_pos = FENSTERHOEHE - ((FENSTERHOEHE /16) + (abschnitt * i ))
        if i == 1:
            auto_pos1 = auto_pos
        if i == 2:
            auto_pos2 = auto_pos
        if i == 3:
            auto_pos3 = auto_pos
        if i == 4:
            auto_pos4 = auto_pos
        if i == 5:
            auto_pos5 = auto_pos
        if i == 6:
            auto_pos6 = auto_pos
            
    #Berechnen der Auto Höhe
    autobreite = FENSTERHOEHE / 10
    autohoehe = ballhoehe
    lkw = autobreite * 1.5

    #Bilder
    auto1_g = pygame.image.load("auto1.png")
    auto1 = pygame.transform.scale(auto1_g, (autobreite, autohoehe))

    auto2_g = pygame.image.load("auto2.png")
    auto2 = pygame.transform.scale(auto2_g, (autobreite, autohoehe))

    auto3_g = pygame.image.load("auto3.png")
    auto3 = pygame.transform.scale(auto3_g, (autobreite, autohoehe))

    auto4_g = pygame.image.load("auto4.png")
    auto4 = pygame.transform.scale(auto4_g, (autobreite, autohoehe))

    auto5_g = pygame.image.load("auto5.png")
    auto5 = pygame.transform.scale(auto5_g, (lkw, autohoehe))
    
    #Autotod (Blutfleck)
    autotod_g = pygame.image.load("blut.png")
    autotod = pygame.transform.scale(autotod_g, (ballbreite , ballhoehe))

    #Variablen für Animation
    framea2 = 0
    frameatod = 0

    #_________________Holzstämme__________________
    
    #Startposition der Holzstämme
    speedh1 = -100
    speedh2 = -375
    speedh3 = -500
    speedh1_ = -1000
    speedh2_ = -575
    speedh3_ = -100

    #Berechnung der Holzposition auf y-Koordinate
    for i in range(1, 7):
        holz_pos = FENSTERHOEHE - ((2 * (FENSTERHOEHE /16)) + (abschnitt * 6) + (abschnitt * i ))
        if i == 1:
            holz_pos1 = holz_pos
        if i == 2:
            holz_pos2 = holz_pos
        if i == 3:
            holz_pos3 = holz_pos
        if i == 4:
            holz_pos4 = holz_pos
        if i == 5:
            holz_pos5 = holz_pos
        if i == 6:
            holz_pos6 = holz_pos
            
    #Berechnen der Holz Höhe
    holzbreite = FENSTERHOEHE / 4
    holzhoehe = 0.7 * abschnitt

    #Bilder
    holz1_g = pygame.image.load("holz1.png")
    holz1 = pygame.transform.scale(holz1_g, (holzbreite , holzhoehe))

    holz2_g = pygame.image.load("holz2.png")
    holz2 = pygame.transform.scale(holz2_g, (holzbreite, holzhoehe))

    holz3_g = pygame.image.load("holz3.png")
    holz3 = pygame.transform.scale(holz3_g, (holzbreite, holzhoehe))

    #__________________Schildkröten___________________
    
    #Startposition der Schildkröten
    speeds1 = FENSTERBREITE + 50
    speeds2 = FENSTERBREITE + 350
    speeds3 = FENSTERBREITE + 500
    speeds1_ = FENSTERBREITE + 750
    speeds2_ = FENSTERBREITE + 100
    speeds3_ = FENSTERBREITE + 300

    # Schildkrötenbreite/ Höhe
    schildbreite = FENSTERBREITE/ 5
    schildhoehe = 0.7 * abschnitt

    #Bilder
    schildi1_g = pygame.image.load("turtle_r_1.png")
    schildi1 = pygame.transform.scale(schildi1_g, (schildbreite , schildhoehe))

    schildi2_g = pygame.image.load("turtle_r_2.png")
    schildi2 = pygame.transform.scale(schildi2_g, (schildbreite , schildhoehe))

    schildi3_g = pygame.image.load("turtle_r_3.png")
    schildi3 = pygame.transform.scale(schildi3_g, (schildbreite , schildhoehe))

    schildi4_g = pygame.image.load("turtle_r_4.png")
    schildi4 = pygame.transform.scale(schildi4_g, (schildbreite , schildhoehe))

    schildi5_g = pygame.image.load("turtle_r_5.png")
    schildi5 = pygame.transform.scale(schildi5_g, (schildbreite , schildhoehe))

    schildi0_g = pygame.image.load("turtle_r_0.png")
    schildi0 = pygame.transform.scale(schildi0_g, (schildbreite , schildhoehe))

    #Liste für Animation
    schildkröte = ['','','','','','','','','','']
    schildkröte[0] = schildi1
    schildkröte[1] = schildi2
    schildkröte[2] = schildi3
    schildkröte[3] = schildi4
    schildkröte[4] = schildi5
    schildkröte[5] = schildi0
    schildkröte[6] = schildi4
    schildkröte[7] = schildi3
    schildkröte[8] = schildi2
    schildkröte[9] = schildi1

    #Variablen für Animation
    frame = 0
    frame1 = 0

    #_______________Leben______________
    lebenbild_g = pygame.image.load("life-final.png")
    lebenbild = pygame.transform.scale(lebenbild_g, (autohoehe * 0.75 , autohoehe * 0.77))

    #Importieren der Schriftart
    font = pygame.font.Font('minecraft.ttf', 32)

    #_______________Tod___________________

    todbreite = FENSTERHOEHE / 13
    
    #Bilder
    tod0_g = pygame.image.load("todn0.png")
    tod0 = pygame.transform.scale(tod0_g, (todbreite, todbreite))

    tod1_g = pygame.image.load("todn1.png")
    tod1 = pygame.transform.scale(tod1_g, (todbreite, todbreite))

    tod2_g = pygame.image.load("todn2.png")
    tod2 = pygame.transform.scale(tod2_g, (todbreite, todbreite))

    tod3_g = pygame.image.load("todn3.png")
    tod3 = pygame.transform.scale(tod3_g, (todbreite, todbreite))

    tod4_g = pygame.image.load("todn4.png")
    tod4 = pygame.transform.scale(tod4_g, (todbreite, todbreite))

    tod5_g = pygame.image.load("todn5.png")
    tod5 = pygame.transform.scale(tod5_g, (todbreite, todbreite))

    tod6_g = pygame.image.load("todn6.png")
    tod6 = pygame.transform.scale(tod6_g, (todbreite, todbreite))

    #Liste für Animation
    todl = ['','','','','','','','']
    todl[0] = tod3
    todl[1] = tod2
    todl[2] = tod1
    todl[3] = tod4
    todl[4] = tod5
    todl[5] = tod6
    todl[6] = tod0
    todl[7] = tod0
    
    #Variablen für Animation
    frame2 = -1
    frametod = 0

        
    #_________________Ziel_______________
    
    #Bilder
    ziel0_g = pygame.image.load("Froschenden_1.png")
    ziel0 = pygame.transform.scale(ziel0_g, (zielbreite , zielhoehe))

    ziel1_g = pygame.image.load("Froschenden_2.png")
    ziel1 = pygame.transform.scale(ziel1_g, (zielbreite , zielhoehe))

    #Liste für Animation
    ziell = ['','']
    ziell[0] = ziel0
    ziell[1] = ziel1

    #Variablen zur Überprüfung, ob das Level abgeschlossen wurde
    Ziel1 = False
    Ziel2 = False
    Ziel3 = False
    Ziel4 = False
    Ziel5 = False

    #wilde Variable
    Zielk = False

    #Variablen für Animation
    framez = -1
    frameziel = 0
    anzahlziel = 0
    zielcontrol = False

    #_______________________Krokodile______________________
    
    #Bilder
    kroko0_g = pygame.image.load("Krokodiel_Kopf0.png")
    kroko0 = pygame.transform.scale(kroko0_g, (zielbreite , zielhoehe))

    kroko1_g = pygame.image.load("Krokodiel_Kopf.png")
    kroko1 = pygame.transform.scale(kroko1_g, (zielbreite , zielhoehe))

    #Liste für Animation
    krokol = ['','']
    krokol[0] = kroko0
    krokol[1] = kroko1

    #Variablen für Animation
    framek = 0
    framekroko = 0
    framek2 = 0
    framektod = 0
    inAnimation2 = False
    
    #_______________Schlangen_______________________
    
    #Größen
    schlangenbreite = ballbreite * 3
    
    #Position auf Y-Koordinate / Bewegung auf X-Koordinate
    schlangepos_y = FENSTERHOEHE * (4/8)
    schlangepos_x = -1 * (FENSTERBREITE * (2/8))
    
    #Bilder
    schlange0_g = pygame.image.load("Schlange.png")
    schlange0 = pygame.transform.scale(schlange0_g, (schlangenbreite , ballhoehe))

    schlange1_g = pygame.image.load("Schlange_Mund.png")
    schlange1 = pygame.transform.scale(schlange1_g, (schlangenbreite , ballhoehe))

    schlange2_g = pygame.image.load("Schlange_Zunge.png")
    schlange2 = pygame.transform.scale(schlange2_g, (schlangenbreite , ballhoehe))
    
    #Liste für Animation
    schlangel = ['','','','']
    schlangel[0] = schlange0
    schlangel[1] = schlange1
    schlangel[2] = schlange2
    schlangel[3] = schlange1
    
    #Variablen für Animation
    frames = 0
    frameschlange = 0
    links = False
    rechts = True
    inAnimation3 = False
    frames2 = 0
    framestod = 0

    #Bilder rechts
    schlanger0_g = pygame.image.load("Schlange.png")
    schlange0r = pygame.transform.scale(schlanger0_g, (schlangenbreite , ballhoehe))
    schlanger0 =pygame.transform.flip(schlange0r, True, False)

    schlanger1_g = pygame.image.load("Schlange_Mund.png")
    schlange1r = pygame.transform.scale(schlanger1_g, (schlangenbreite , ballhoehe))
    schlanger1 =pygame.transform.flip(schlange1r, True, False)

    schlanger2_g = pygame.image.load("Schlange_Zunge.png")
    schlange2r = pygame.transform.scale(schlanger2_g, (schlangenbreite , ballhoehe))
    schlanger2 =pygame.transform.flip(schlange2r, True, False)
    
    #Liste für Animation rechts
    schlangerl = ['','','','']
    schlangerl[0] = schlanger0
    schlangerl[1] = schlanger1
    schlangerl[2] = schlanger2
    schlangerl[3] = schlanger1
    
    #___________Pause__________
    
    pausebreite = FENSTERHOEHE * (1/3)
    pausehoehe = FENSTERHOEHE * (1/3)
    pausepos_x =  (FENSTERBREITE / 2) - (pausebreite / 2)
    pausepos_y = (FENSTERHOEHE / 3.3) - (pausebreite / 2)
    
    #Bild
    pausek_g = pygame.image.load("pause.png")
    pausek = pygame.transform.scale(pausek_g, (pausebreite , pausehoehe))
    

    # Fenster öffnen
    screen = pygame.display.set_mode((FENSTERBREITE, FENSTERHOEHE))

    pygame.display.set_caption("Frogger")

    # solange die Variable True ist, soll das Spiel laufen
    spielaktiv = True

    # Bildschirm Aktualisierungen einstellen
    clock = pygame.time.Clock()

    # _______________________Schleife Hauptprogramm__________________________
    while spielaktiv:
        
        # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spielaktiv = False
            elif event.type == pygame.KEYDOWN:

                # Tasten für Spieler
                if event.key == pygame.K_RIGHT and Froschda == True and pause == False:
                    if not ballpos_x + ballbreite >= FENSTERBREITE - (ballhoehe -1):
                        ballpos_x += bewegung
                        pygame.mixer.Sound.play(springen)
                    last_direction = 'right'                    
                elif event.key == pygame.K_LEFT and Froschda == True and pause == False:
                    if not ballpos_x <= 0 + (ballhoehe + 1):
                        ballpos_x -= bewegung
                        pygame.mixer.Sound.play(springen)
                    last_direction = 'left'
                elif event.key == pygame.K_UP and Froschda == True and pause == False:
                    if not ballpos_y <= 0:
                        ballpos_y -= bewegung
                        pygame.mixer.Sound.play(springen)
                    last_direction = 'up'
                elif event.key == pygame.K_DOWN and Froschda == True and pause == False:
                    if not ballpos_y + ballhoehe >= FENSTERHOEHE - (ballhoehe- 1):
                        ballpos_y += bewegung
                        pygame.mixer.Sound.play(springen)
                    last_direction = 'down'
                #Pause
                elif event.key == pygame.K_SPACE:
                    pausezähler += 1
                    if pausezähler % 2 == 0:
                        pause = False
                        pygame.mixer.music.unpause()
                    else:
                        pause = True
                        pygame.mixer.music.pause()
                #Home
                elif event.key == pygame.K_ESCAPE:
                    spielaktiv = False
                #Reset
                elif event.key == pygame.K_r:
                    reset = True
                    spielaktiv = False
                    
                        
        #Levelmultiplikator        
        levelm = (1 + (level * 0.25)) - 0.25
        
        # Leben
        if leben == 0:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.set_volume(death, 1)
            pygame.mixer.Sound.play(death)
            time.sleep(2)
            pygame.mixer.Sound.set_volume(gameover, 1)
            pygame.mixer.Sound.play(gameover)
            time.sleep(1.3)
            spielaktiv = False
            
        # Spielfeld löschen
        screen.fill(SCHWARZ)

        # Spielfeld/figuren zeichnen
        if last_direction == 'right':
            frog_r = pygame.transform.rotate(frog, -90)
            frog2_r = pygame.transform.rotate(frog2, -90)
            frog3_r = pygame.transform.rotate(frog3, -90)
            frog4_r = pygame.transform.rotate(frog4, -90)
            frog5_r = pygame.transform.rotate(frog5, -90)
            frog6_r = pygame.transform.rotate(frog6, -90)           
        if last_direction == 'left':
            frog_r = pygame.transform.rotate(frog, 90)
            frog2_r = pygame.transform.rotate(frog2, 90)
            frog3_r = pygame.transform.rotate(frog3, 90)
            frog4_r = pygame.transform.rotate(frog4, 90)
            frog5_r = pygame.transform.rotate(frog5, 90)
            frog6_r = pygame.transform.rotate(frog6, 90)
        if last_direction == 'up':
            frog_r = pygame.transform.rotate(frog, 0)
            frog2_r = pygame.transform.rotate(frog2, 0)
            frog3_r = pygame.transform.rotate(frog3, 0)
            frog4_r = pygame.transform.rotate(frog4, 0)
            frog5_r = pygame.transform.rotate(frog5, 0)
            frog6_r = pygame.transform.rotate(frog6, 0)
        if last_direction == 'down':
            frog_r = pygame.transform.rotate(frog, 180)
            frog2_r = pygame.transform.rotate(frog2, 180)
            frog3_r = pygame.transform.rotate(frog3, 180)
            frog4_r = pygame.transform.rotate(frog4, 180)
            frog5_r = pygame.transform.rotate(frog5, 180)
            frog6_r = pygame.transform.rotate(frog6, 180)
        
        #Hintergrund
        screen.blit(hintergrund, (0 ,0))

                        
        # Blut anzeigen
        if überfahren == True:
            Froschda = False                
            if frameatod == 0:
                pygame.mixer.Sound.play(tod)
                leben -= 1
                score -= 10
            if pause == False:
                frameatod += 1
            if frameatod % 10 == 0:
                framea2 += 1
            screen.blit(autotod, (ballpos_x ,ballpos_y))

            if framea2 == 6:
                last_direction = 'up'
                ballpos_x = spawnx
                ballpos_y = spawny
                if not leben == 0:
                            Froschda = True
                überfahren = False
                framea2 = 0
                frameatod = 0

        #Holz anzeigen
        screen.blit(holz1, (speedh1 ,holz_pos1))
        screen.blit(holz1, (speedh1_ ,holz_pos5))
        screen.blit(holz2, (speedh2 ,holz_pos3))
        screen.blit(holz2, (speedh2_ ,holz_pos1))
        screen.blit(holz3, (speedh3 ,holz_pos5))
        screen.blit(holz3, (speedh3_ ,holz_pos3))

        #Schildkröten anzeigen
        screen.blit(schildkröte[frame], (speeds3, holz_pos6))
        screen.blit(schildkröte[frame], (speeds1, holz_pos2))
        screen.blit(schildi1, (speeds2, holz_pos4))
        screen.blit(schildi1, (speeds3_, holz_pos2))
        screen.blit(schildkröte[frame], (speeds2_, holz_pos6))
        screen.blit(schildkröte[frame], (speeds1_, holz_pos4))
        
        #Animation Ziel       
        if Ziel1 == True:
            if pause == False:
                frameziel += 1
            if frameziel % 100 == 0:
                framez += 1
                if framez > 1:
                    framez = 0
            screen.blit(ziell[framez], (zielpos_1, zielpos_y))
        if Ziel2 == True:
            if pause == False:
                frameziel += 1
            if frameziel % 100 == 0:
                framez += 1
                if framez > 1:
                    framez = 0
            screen.blit(ziell[framez], (zielpos_2, zielpos_y))
        if Ziel3 == True:
            if pause == False:
                frameziel += 1
            if frameziel % 100 == 0:
                framez += 1
                if framez > 1:
                    framez = 0
            screen.blit(ziell[framez], (zielpos_3, zielpos_y))
        if Ziel4 == True:
            if pause == False:
                frameziel += 1
            if frameziel % 100 == 0:
                framez += 1
                if framez > 1:
                    framez = 0
            screen.blit(ziell[framez], (zielpos_4, zielpos_y))
        if Ziel5 == True:
            if pause == False:
                frameziel += 1
            if frameziel % 100 == 0:
                framez += 1
                if framez > 1:
                    framez = 0
            screen.blit(ziell[framez], (zielpos_5, zielpos_y))
            
        if Ziel1 == True and Ziel2 == True and Ziel3 == True and Ziel4 == True and Ziel5 == True:
            anzahlziel += 1
            if anzahlziel % 2 == 0:
                zielcontrol = True
            
        #Animation Krokodiel       
        if level >= 2:
            if pause == False:
                if framekroko % 650 == 0 or not krokopos_x in krokopos:
                    framek = 0
                    krokopos_x = random.choice(krokopos)
                                    
                framekroko += 1            
            if framekroko % 150 == 0:
                framek += 1
                if framek > 1:
                    framek = 0
            screen.blit(krokol[framek], (krokopos_x, krokopos_y))
            
        #Animation Schlange
        if level >= 3:
            if pause == False:
                frameschlange += 1
                if schlangepos_x < -1 * (FENSTERBREITE * (2/8)):
                    rechts = True
                    links = False
                if schlangepos_x > FENSTERBREITE + (FENSTERBREITE * (1/8)):
                    links = True
                    rechts = False
                if links == True:
                    schlangepos_x -= 1 * levelm
                if rechts == True:
                    schlangepos_x += 1 * levelm
                    
            if frameschlange % 50 == 0:
                frames += 1
                if frames > 3:
                    frames = 0
            
            if rechts == True:
                screen.blit(schlangerl[frames], (schlangepos_x, schlangepos_y))
            if links == True:
             screen.blit(schlangel[frames], (schlangepos_x, schlangepos_y))
            

        #Spielfigur
        if Froschda == True:
            if skin == 0:
                screen.blit(frog_r, (ballpos_x ,ballpos_y))
            if skin == 1:
                screen.blit(frog2_r, (ballpos_x ,ballpos_y))
            if skin == 2:
                screen.blit(frog3_r, (ballpos_x ,ballpos_y))
            if skin == 3:
                screen.blit(frog4_r, (ballpos_x ,ballpos_y))
            if skin == 4:
                screen.blit(frog5_r, (ballpos_x ,ballpos_y))
            if skin == 5:
                screen.blit(frog6_r, (ballpos_x ,ballpos_y))
                
        
        #Autos anzeigen
        screen.blit(auto1, (speed1 ,auto_pos1))
        screen.blit(auto1, (speed1_ ,auto_pos5))
        screen.blit(auto2, (speed2 ,auto_pos2))
        screen.blit(auto2, (speed2_ ,auto_pos4))
        screen.blit(auto3, (speed3 ,auto_pos3))
        screen.blit(auto3, (speed3_ ,auto_pos1))
        screen.blit(auto4, (speed4 ,auto_pos4))
        screen.blit(auto4, (speed4_ ,auto_pos2))
        screen.blit(auto5, (speed5 ,auto_pos5))
        screen.blit(auto5, (speed5_ ,auto_pos3))
        screen.blit(auto1, (speed6 ,auto_pos6))
        
        # Fenster aktualisieren
    #    pygame.display.flip()

        # Refresh-Zeiten festlegen        
        clock.tick(60)

        if pause == False:
            
            # Autos bewegen
            speed1 -= (ges + 0.5) * levelm
            speed2 += ges * levelm
            speed3 -= (ges + 1) * levelm
            speed4 += ges * levelm
            speed5 -= ges * levelm
            speed6 -= (ges + 3) * levelm
            speed1_ -= ges * levelm
            speed2_ += ges * levelm
            speed3_ -= (ges + 0.5) * levelm
            speed4_ += ges * levelm
            speed5_ -= (ges + 1) * levelm
            

            #Holz bewegen
            speedh1 += (ges + 0.3) * levelm
            speedh2 += (ges - 0.2) * levelm
            speedh3 += (ges + 0.1) * levelm
            speedh1_ += (ges + 0.1) * levelm
            speedh2_ += (ges + 0.3) * levelm
            speedh3_ += (ges - 0.2) * levelm

            #Schildkröten bewegen
            speeds1 -= (ges - 0.2) * levelm
            speeds2 -= (ges + 0.6) * levelm
            speeds3 -= (ges - 0.3) * levelm
            speeds1_ -= (ges + 0.6) * levelm
            speeds2_ -= (ges - 0.3) * levelm
            speeds3_ -= (ges - 0.2) * levelm

        # Autos zurücksetzen
        if speed1 <= -1 * autobreite:
            speed1 = FENSTERBREITE + 50
        if speed2 >= FENSTERBREITE:
            speed2 = -50
        if speed3 <= -1 * 100:
            speed3 = FENSTERBREITE + 50
        if speed4 >= FENSTERBREITE:
            speed4 = -50
        if speed5 <= -100:
            speed5 = FENSTERBREITE + 50
        if speed6 <= -1 * autobreite:
            speed6 = FENSTERBREITE + 50
        if speed1_ <= -100:
            speed1_ = FENSTERBREITE + 50
        if speed2_ >= FENSTERBREITE:
            speed2_ = -50
        if speed3_<= -1 * autobreite:
            speed3_ = FENSTERBREITE + 50
        if speed4_ >= FENSTERBREITE:
            speed4_ = -50
        if speed5_ <= -1 * 100:
            speed5_ = FENSTERBREITE + 50

        #Holz zurücksetzen
        if speedh1 >= FENSTERBREITE:
            speedh1 = - (50 + holzbreite)
        if speedh2 >= FENSTERBREITE:
            speedh2 = - (50 + holzbreite)
        if speedh3 >= FENSTERBREITE:
            speedh3 = - (50 + holzbreite)
        if speedh1_ >= FENSTERBREITE:
            speedh1_ = - (50 + holzbreite)
        if speedh2_ >= FENSTERBREITE:
            speedh2_ = - (50 + holzbreite)
        if speedh3_ >= FENSTERBREITE:
            speedh3_ = - (50 + holzbreite)

        #Schildkröten zurücksetzen
        if speeds1 <= -1 * schildbreite:
            speeds1 = FENSTERBREITE + 50
        if speeds2 <= -1 * schildbreite:
            speeds2 = FENSTERBREITE + 50
        if speeds3 <= -1 * schildbreite:
            speeds3 = FENSTERBREITE + 50
        if speeds1_ <= -1 * schildbreite:
            speeds1_ = FENSTERBREITE + 50
        if speeds2_ <= -1 * schildbreite:
            speeds2_ = FENSTERBREITE + 50
        if speeds3_ <= -1 * schildbreite:
            speeds3_ = FENSTERBREITE + 50


        if godmode == False:
                                   
            #Kollision mit Autos
            if ballpos_y == auto_pos1 and ballpos_x + ballbreite >= speed1 and ballpos_x <= speed1 + autobreite:
                überfahren = True
            if ballpos_y == auto_pos2 and ballpos_x + ballbreite >= speed2 and ballpos_x <= speed2 + autobreite:
                überfahren = True
            if ballpos_y == auto_pos3 and ballpos_x + ballbreite >= speed3 and ballpos_x <= speed3 + autobreite:
                überfahren = True
            if ballpos_y == auto_pos4 and ballpos_x + ballbreite >= speed4 and ballpos_x <= speed4 + autobreite:
                überfahren = True
            if ballpos_y == auto_pos5 and ballpos_x + ballbreite >= speed5 and ballpos_x <= speed5 + 100:
                überfahren = True
            if ballpos_y == auto_pos6 and ballpos_x + ballbreite >= speed6 and ballpos_x <= speed6 + autobreite:
                überfahren = True
            if ballpos_y == auto_pos5 and ballpos_x + ballbreite >= speed1_ and ballpos_x <= speed1_ + autobreite:
                überfahren = True
            if ballpos_y == auto_pos4 and ballpos_x + ballbreite >= speed2_ and ballpos_x <= speed2_ + autobreite:
                überfahren = True
            if ballpos_y == auto_pos1 and ballpos_x + ballbreite >= speed3_ and ballpos_x <= speed3_ + autobreite:
                überfahren = True
            if ballpos_y == auto_pos2 and ballpos_x + ballbreite >= speed4_ and ballpos_x <= speed4_ + autobreite:
                überfahren = True
            if ballpos_y == auto_pos3 and ballpos_x + ballbreite >= speed5_ and ballpos_x <= speed5_ + autobreite:
                überfahren = True


            #Kollision mit Holz
            if ballpos_y == holz_pos1 and ballpos_x + (ballbreite * 0.5) >= speedh1 and ballpos_x + (ballbreite * 0.8) <= speedh1 + holzbreite:
                nichtWasser = True
                if not ballpos_x + ballbreite >= FENSTERBREITE and pause == False:
                    ballpos_x += (ges + 0.3) * levelm

            if ballpos_y == holz_pos3 and ballpos_x + (ballbreite * 0.5) >= speedh2 and ballpos_x + (ballbreite * 0.8) <= speedh2 + holzbreite:
                nichtWasser = True
                if not ballpos_x + ballbreite >= FENSTERBREITE and pause == False:
                    ballpos_x += (ges - 0.2) * levelm

            if ballpos_y == holz_pos5 and ballpos_x + (ballbreite * 0.5) >= speedh3 and ballpos_x + (ballbreite * 0.8) <= speedh3 + holzbreite:
                nichtWasser = True
                if not ballpos_x + ballbreite >= FENSTERBREITE and pause == False:
                    ballpos_x += (ges + 0.1) * levelm

            if ballpos_y == holz_pos5 and ballpos_x + (ballbreite * 0.5) >= speedh1_ and ballpos_x + (ballbreite * 0.8) <= speedh1_ + holzbreite:
                nichtWasser = True
                if not ballpos_x + ballbreite >= FENSTERBREITE and pause == False:
                    ballpos_x += (ges + 0.1) * levelm

            if ballpos_y == holz_pos1 and ballpos_x + (ballbreite * 0.5) >= speedh2_ and ballpos_x + (ballbreite * 0.8) <= speedh2_ + holzbreite:
                nichtWasser = True
                if not ballpos_x + ballbreite >= FENSTERBREITE and pause == False:
                    ballpos_x += (ges + 0.3) * levelm

            if ballpos_y == holz_pos3 and ballpos_x + (ballbreite * 0.5) >= speedh3_ and ballpos_x + (ballbreite * 0.8) <= speedh3_ + holzbreite:
                nichtWasser = True
                if not ballpos_x + ballbreite >= FENSTERBREITE and pause == False:
                    ballpos_x += (ges - 0.2) * levelm


            #Kollision mit Schildkröte
            if ballpos_y == holz_pos2 and ballpos_x + (ballbreite * 0.2) >= speeds1 and ballpos_x + (ballbreite * 0.7) <= speeds1 + schildbreite:
                if not frame == 5:
                    nichtWasser = True
                if not ballpos_x  <= 0 :
                    if not frame == 5 and pause == False:
                        ballpos_x -= (ges - 0.3) * levelm

            if ballpos_y == holz_pos4 and ballpos_x + (ballbreite * 0.2) >= speeds2 and ballpos_x + (ballbreite * 0.7) <= speeds2 + schildbreite:
                nichtWasser = True
                if not ballpos_x  <= 0 and pause == False:
                        ballpos_x -= (ges + 0.6) * levelm

            if ballpos_y == holz_pos6 and ballpos_x + (ballbreite * 0.2) >= speeds3 and ballpos_x + (ballbreite * 0.7) <= speeds3 + schildbreite:
                if not frame == 5:
                    nichtWasser = True
                if not ballpos_x  <= 0 :
                    if not frame == 5 and pause == False:
                        ballpos_x -= (ges - 0.3) * levelm

            if ballpos_y == holz_pos4 and ballpos_x + (ballbreite * 0.2) >= speeds1_ and ballpos_x + (ballbreite * 0.7) <= speeds1_ + schildbreite:
                if not frame == 5:
                    nichtWasser = True
                if not ballpos_x  <= 0 :
                    if not frame == 5 and pause == False:
                        ballpos_x -= (ges + 0.6) * levelm

            if ballpos_y == holz_pos6 and ballpos_x + (ballbreite * 0.2) >= speeds2_ and ballpos_x + (ballbreite * 0.7) <= speeds2_ + schildbreite:
                if not frame == 5:
                    nichtWasser = True
                if not ballpos_x  <= 0 :
                    if not frame == 5 and pause == False:
                        ballpos_x -= (ges - 0.3) * levelm

            if ballpos_y == holz_pos2 and ballpos_x + (ballbreite * 0.2) >= speeds3_ and ballpos_x + (ballbreite * 0.7) <= speeds3_ + schildbreite:
                nichtWasser = True
                if not ballpos_x  <= 0 and pause == False:
                        ballpos_x -= (ges - 0.3) * levelm

            #Kollision mit Wasser
            if ballpos_y >= FENSTERHOEHE * (1/8) and ballpos_y <= FENSTERHOEHE * (7/16) :
                if nichtWasser == False or inAnimation == True:
                    Froschda = False
                    inAnimation = True
                    if frametod == 0:
                        pygame.mixer.Sound.play(wasser)
                        todpos_x = ballpos_x
                        todpos_y = ballpos_y
                    if pause == False :
                        frametod += 1
                    if frametod % 10 == 0:
                        frame2 += 1
                    screen.blit(todl[frame2], (todpos_x, todpos_y))
                    if frame2 == 7:
                        ballpos_x = spawnx
                        ballpos_y = spawny
                        frame2 = 0
                        frametod = 0
                        last_direction = 'up'
                        nichtWasser = True
                        inAnimation = False
                        leben -= 1
                        score -= 10
                        if not leben == 0:
                            Froschda = True
                                           
        #kollision mit Krokodiel
        if ballpos_y <= FENSTERHOEHE * (1/16) or inAnimation2 == True:
            if ballpos_x + ballbreite >= krokopos_x and ballpos_x <= krokopos_x + zielbreite or inAnimation2 == True:
                if framek == 1:
                    inAnimation2 = True
                    if framektod == 0:
                        pygame.mixer.Sound.play(die)
                    Froschda = False
                    Zielk = True
                    if pause == False :
                        framektod += 1
                    if framektod % 10 == 0:
                        framek2 += 1
                    screen.blit(todl[framek2], (ballpos_x, krokopos_y))
                    if framek2 == 7:
                        ballpos_x = spawnx
                        ballpos_y = spawny
                        framek2 = 0
                        framektod = 0
                        last_direction = 'up'
                        inAnimation2 = False
                        Zielk = False
                        leben -= 1
                        score -= 10
                        if not leben == 0:
                            Froschda = True
                        
        #Kollision mit Schlange
        if ballpos_y == schlangepos_y:
            if ballpos_x + ballbreite >= schlangepos_x and ballpos_x <= schlangepos_x + schlangenbreite or inAnimation3 == True:
                inAnimation3 = True
                if framestod == 0:
                    pygame.mixer.Sound.play(die)
                Froschda = False
                if pause == False :
                    framestod += 1
                if framestod % 10 == 0:
                    frames2 += 1
                screen.blit(todl[frames2], (ballpos_x, ballpos_y))
                if frames2 == 7:
                    ballpos_x = spawnx
                    ballpos_y = spawny
                    frames2 = 0
                    framestod = 0
                    last_direction = 'up'
                    inAnimation3 = False
                    leben -= 1
                    score -= 10
                    if not leben == 0:
                        Froschda = True

        # Ziel            
        if ballpos_y >= 0 and ballpos_y <= FENSTERHOEHE * (1/16):
            if ballpos_x > (rest + (seeblatt * 0) + (zwischen * 0)) and ballpos_x + ballbreite <= (rest + (seeblatt * 1) + (zwischen * 0)) and Zielk == False and Ziel1 == False:
                krokopos.remove(krokopos_1)
                Ziel1 = True
                ballpos_x = spawnx
                ballpos_y = spawny
                last_direction = 'up'
                score += 100
            elif ballpos_x > (rest + (seeblatt * 1) + (zwischen * 1)) and ballpos_x + ballbreite <= (rest + (seeblatt * 2) + (zwischen * 1)) and Zielk == False and Ziel2 == False:
                krokopos.remove(krokopos_2)
                Ziel2 = True
                ballpos_x = spawnx
                ballpos_y = spawny
                last_direction = 'up'
                score += 100
            elif ballpos_x > (rest + (seeblatt * 2) + (zwischen * 2)) and ballpos_x + ballbreite <= (rest + (seeblatt * 3) + (zwischen * 2)) and Zielk == False and Ziel3 == False:
                krokopos.remove(krokopos_3)
                Ziel3 = True
                ballpos_x = spawnx
                ballpos_y = spawny
                last_direction = 'up'
                score += 100
            elif ballpos_x > (rest + (seeblatt * 3) + (zwischen * 3)) and ballpos_x + ballbreite <= (rest + (seeblatt * 4) + (zwischen * 3)) and Zielk == False and Ziel4 == False:
                krokopos.remove(krokopos_4)
                Ziel4 = True
                ballpos_x = spawnx
                ballpos_y = spawny
                last_direction = 'up'
                score += 100
            elif ballpos_x > (rest + (seeblatt * 4) + (zwischen * 4)) and ballpos_x + ballbreite <= (rest + (seeblatt * 5) + (zwischen * 4)) and Zielk == False and Ziel5 == False:
                krokopos.remove(krokopos_5)
                Ziel5 = True
                ballpos_x = spawnx
                ballpos_y = spawny
                last_direction = 'up'
                score += 100
            else:                
                ballpos_y += bewegung
                
        if Ziel1 == True and Ziel2 == True and Ziel3 == True and Ziel4 == True and Ziel5 == True:
            Froschda = False
            if zielcontrol == True:
                score += 400
                pygame.mixer.music.pause()
                pygame.mixer.Sound.play(ende)
                time.sleep(6.3)
                pygame.mixer.music.unpause()
                Froschda = True
                Ziel1 = False
                Ziel2 = False
                Ziel3 = False
                Ziel4 = False
                Ziel5 = False
                krokopos = [krokopos_1, krokopos_2, krokopos_3, krokopos_4, krokopos_5, -150, -140, -130, -120]
                zielcontrol = False

                level += 1
                if leben < 9:
                    leben += 1

        #Leben anzeigen
        for i in range(0, leben):
            screen.blit(lebenbild, (FENSTERBREITE - (i * 50) - 50, spawny + (FENSTERHOEHE * (1/128))))

        # Levelanzeige
        text = font.render('Level ' + str(level), True, WEISS)
        textRect = text.get_rect()
        textRect.center = (FENSTERBREITE * (1/9), spawny + (FENSTERHOEHE * (1/32)))
        screen.blit(text, textRect)
        
        # Scoreanzeige
        text2 = font.render('Score : ' + str(score), True, WEISS)
        text2Rect = text2.get_rect()
        text2Rect.center = (FENSTERBREITE * (3/18), (FENSTERHOEHE * (4/8)) + (FENSTERHOEHE * (1/32)))
        screen.blit(text2, text2Rect)

        # Variablen für die Animation der Schildkröten
        if pause == False:
            frame1 += 1
            if frame1 % (30 * animultiplikator) == 0:
                frame += 1
                if frame > 9:
                    frame = 0
                    
        #Pausesymbol anzeigen
        if pause == True:
            if not leben == 0:
                screen.blit(pausek, (pausepos_x ,pausepos_y))


        pygame.display.update()

        # Variable um festzustellen, ob man im Wasser ist
        nichtWasser = False

#______________________________________________________
        #Spielende

    pygame.quit()
    
    return score, reset

if __name__ == "__main__":
    frogger(700, 1)