def frogger(fensterhoehe):
    import pygame
    import time
    pygame.init()


    #__________________________________Definieren der Variablen

    godmode = False
    nichtWasser = False
    inAnimation = False
    Froschda = True

    level = 1
    

    #Fensterhöhe
    FENSTERHOEHE = fensterhoehe

    bereich = (3 / 8) * FENSTERHOEHE
    abschnitt = bereich / 6

    #Fensterbreite
    FENSTERBREITE = (abschnitt * 0.7) * 20
    
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

    #Autos
    speed1 = 700
    speed2 = -350
    speed3 = 800
    speed4 = -100
    speed5 = 890
    speed6 = 960
    ges = 2

     #holz

    speedh1 = -100
    speedh2 = -375
    speedh3 = -500

    #Schildkröte
    speeds1 = FENSTERBREITE + 50
    speeds2 = FENSTERBREITE + 350
    speeds3 = FENSTERBREITE + 500

    #berechnung der Autoposition auf y-Koordinate

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

    #berechnung der Holzposition auf y-Koordinate

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

    #berechnen der Auto Höhe
    autobreite = FENSTERHOEHE / 10
    autohoehe = 0.75 * abschnitt

    #Frog
    bewegung = abschnitt
    ballbreite = autohoehe
    ballhoehe = autohoehe
    last_direction = 'up'
    spawnx = (FENSTERBREITE // 2) - (ballbreite // 2)
    spawny = FENSTERHOEHE - (FENSTERHOEHE /16)
    ballpos_x = spawnx
    ballpos_y = spawny

    #berechnen der Holz Höhe
    holzbreite = FENSTERHOEHE / 4
    holzhoehe = 0.7 * abschnitt

    # Schildkrötenbreite/ höhe
    schildbreite = 130
    schildhoehe = 0.7 * abschnitt

    #Leben
    leben = 3

    # Farbe
    ORANGE  = ( 255, 140, 0)
    ROT     = ( 255, 0, 0)
    GRUEN   = ( 0, 255, 0)
    SCHWARZ = ( 0, 0, 0)
    WEISS   = ( 255, 255, 255)

    #hintergrundmusik
    pygame.mixer.music.load('Level.mp3')
    pygame.mixer.music.play(-1,0.0)
    pygame.mixer.music.set_volume(.6)

    #Sounds
    springen = pygame.mixer.Sound('springen.mp3')
    springen.set_volume(.7)
    tod = pygame.mixer.Sound('tod.mp3')
    wasser = pygame.mixer.Sound('wasser.mp3')
    death = pygame.mixer.Sound('death.wav')
    gameover = pygame.mixer.Sound('game_over.wav')
    pygame.mixer.Sound.set_volume(springen, 0.3)
    #_______Bilder

    #Hintergrund
    hintergrund1 = pygame.image.load("frogger_background.png")
    hintergrund = pygame.transform.scale(hintergrund1, (FENSTERBREITE, FENSTERHOEHE))

    #Spieler
    frog1 = pygame.image.load("frog.png")
    frog = pygame.transform.scale(frog1, (ballbreite, ballhoehe))
    bildgroessen = frog.get_rect()

    #Autos
    auto1_g = pygame.image.load("auto1.png")
    auto1 = pygame.transform.scale(auto1_g, (autobreite, autohoehe))

    auto2_g = pygame.image.load("auto2.png")
    auto2 = pygame.transform.scale(auto2_g, (autobreite, autohoehe))

    auto3_g = pygame.image.load("auto3.png")
    auto3 = pygame.transform.scale(auto3_g, (autobreite, autohoehe))

    auto4_g = pygame.image.load("auto4.png")
    auto4 = pygame.transform.scale(auto4_g, (autobreite, autohoehe))

    auto5_g = pygame.image.load("auto5.png")
    auto5 = pygame.transform.scale(auto5_g, (100, autohoehe))

    #Holzstämme

    holz1_g = pygame.image.load("holz1.png")
    holz1 = pygame.transform.scale(holz1_g, (holzbreite , holzhoehe))

    holz2_g = pygame.image.load("holz2.png")
    holz2 = pygame.transform.scale(holz2_g, (holzbreite, holzhoehe))

    holz3_g = pygame.image.load("holz3.png")
    holz3 = pygame.transform.scale(holz3_g, (holzbreite, holzhoehe))

    #Schildkröten

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

    frame = 0
    frame1 = 0

    #Leben
    lebenbild_g = pygame.image.load("life-final.png")
    lebenbild = pygame.transform.scale(lebenbild_g, (autohoehe * 0.75 , autohoehe * 0.77))

    # importiere Schriftart
    font = pygame.font.Font('minecraft.ttf', 32)

    #Tod

    tod0_g = pygame.image.load("todn0.png")
    tod0 = pygame.transform.scale(tod0_g, (50 , 50))

    tod1_g = pygame.image.load("todn1.png")
    tod1 = pygame.transform.scale(tod1_g, (50 , 50))

    tod2_g = pygame.image.load("todn2.png")
    tod2 = pygame.transform.scale(tod2_g, (50 , 50))

    tod3_g = pygame.image.load("todn3.png")
    tod3 = pygame.transform.scale(tod3_g, (50 , 50))

    tod4_g = pygame.image.load("todn4.png")
    tod4 = pygame.transform.scale(tod4_g, (50 , 50))

    tod5_g = pygame.image.load("todn5.png")
    tod5 = pygame.transform.scale(tod5_g, (50 , 50))

    tod6_g = pygame.image.load("todn6.png")
    tod6 = pygame.transform.scale(tod6_g, (50 , 50))

    todl = ['','','','','','','']
    todl[0] = tod3
    todl[1] = tod2
    todl[2] = tod1
    todl[3] = tod4
    todl[4] = tod5
    todl[5] = tod6
    todl[6] = tod0

    frame2 = -1
    frametod = 0
    
    #Ziel Animation
    ziel0_g = pygame.image.load("Froschenden_1.png")
    ziel0 = pygame.transform.scale(ziel0_g, (zielbreite , zielhoehe))

    ziel1_g = pygame.image.load("Froschenden_2.png")
    ziel1 = pygame.transform.scale(ziel1_g, (zielbreite , zielhoehe))
    
    ziell = ['','']
    ziell[0] = ziel0
    ziell[1] = ziel1
    
    Ziel1 = False
    Ziel2 = False
    Ziel3 = False
    Ziel4 = False
    Ziel5 = False
    
    framez = -1
    frameziel = 0

    
    

    # Fenster öffnen
    screen = pygame.display.set_mode((FENSTERBREITE, FENSTERHOEHE))

    pygame.display.set_caption("Frogger")

    # solange die Variable True ist, soll das Spiel laufen
    spielaktiv = True

    # Bildschirm Aktualisierungen einstellen
    clock = pygame.time.Clock()

    # ____________________________________________________Schleife Hauptprogramm
    while spielaktiv:
        # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spielaktiv = False
            elif event.type == pygame.KEYDOWN:

                # Taste für Spieler 1
                if event.key == pygame.K_RIGHT and Froschda == True:
                    if not ballpos_x + ballbreite >= FENSTERBREITE - (ballhoehe -1):
                        ballpos_x += bewegung
                        pygame.mixer.Sound.play(springen)
                    last_direction = 'right'
                elif event.key == pygame.K_LEFT and Froschda == True:
                    if not ballpos_x <= 0 + (ballhoehe + 1):
                        ballpos_x -= bewegung
                        pygame.mixer.Sound.play(springen)
                    last_direction = 'left'
                elif event.key == pygame.K_UP and Froschda == True:
                    if not ballpos_y <= 0:
                        ballpos_y -= bewegung
                        pygame.mixer.Sound.play(springen)
                    last_direction = 'up'
                elif event.key == pygame.K_DOWN and Froschda == True:
                    if not ballpos_y + ballhoehe >= FENSTERHOEHE - (ballhoehe- 1):
                        ballpos_y += bewegung
                        pygame.mixer.Sound.play(springen)
                    last_direction = 'down'
    #           elif event.key == pygame.K_SPACE:


    #           elif event.type == pygame.MOUSEBUTTONDOWN:

        # Ziel
        
        if ballpos_y >= 0 and ballpos_y <= FENSTERHOEHE * (1/16):
            if ballpos_x > (rest + (seeblatt * 0) + (zwischen * 0)) and ballpos_x + ballbreite <= (rest + (seeblatt * 1) + (zwischen * 0)):
                Ziel1 = True
                ballpos_x = spawnx
                ballpos_y = spawny
                last_direction = 'up'
            elif ballpos_x > (rest + (seeblatt * 1) + (zwischen * 1)) and ballpos_x + ballbreite <= (rest + (seeblatt * 2) + (zwischen * 1)):
                Ziel2 = True
                ballpos_x = spawnx
                ballpos_y = spawny
                last_direction = 'up'
            elif ballpos_x > (rest + (seeblatt * 2) + (zwischen * 2)) and ballpos_x + ballbreite <= (rest + (seeblatt * 3) + (zwischen * 2)):
                Ziel3 = True
                ballpos_x = spawnx
                ballpos_y = spawny
                last_direction = 'up'
            elif ballpos_x > (rest + (seeblatt * 3) + (zwischen * 3)) and ballpos_x + ballbreite <= (rest + (seeblatt * 4) + (zwischen * 3)):
                Ziel4 = True
                ballpos_x = spawnx
                ballpos_y = spawny
                last_direction = 'up'
            elif ballpos_x > (rest + (seeblatt * 4) + (zwischen * 4)) and ballpos_x + ballbreite <= (rest + (seeblatt * 5) + (zwischen * 4)):
                Ziel5 = True
                ballpos_x = spawnx
                ballpos_y = spawny
                last_direction = 'up'
            elif not Ziel1 == True or Ziel2 == True or Ziel3 == True or Ziel4 == True or Ziel5 == True:
                ballpos_y += bewegung
                



        # Spielfeld löschen
        screen.fill(SCHWARZ)

        # Spielfeld/figuren zeichnen
        if last_direction == 'right':
            frog_r = pygame.transform.rotate(frog, -90)
        if last_direction == 'left':
            frog_r = pygame.transform.rotate(frog, 90)
        if last_direction == 'up':
            frog_r = pygame.transform.rotate(frog, 0)
        if last_direction == 'down':
            frog_r = pygame.transform.rotate(frog, 180)
        screen.blit(hintergrund, (0 ,0))

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


        #Holz einfügen
        screen.blit(holz1, (speedh1 ,holz_pos1))
        screen.blit(holz2, (speedh2 ,holz_pos3))
        screen.blit(holz3, (speedh3 ,holz_pos5))

        #Autos einfügen
        screen.blit(auto1, (speed1 ,auto_pos1))
        screen.blit(auto2, (speed2 ,auto_pos2))
        screen.blit(auto3, (speed3 ,auto_pos3))
        screen.blit(auto4, (speed4 ,auto_pos4))
        screen.blit(auto5, (speed5 ,auto_pos5))
        screen.blit(auto1, (speed6 ,auto_pos6))

        #Schildkröten einfügen
        screen.blit(schildkröte[frame], (speeds3, holz_pos6))
        screen.blit(schildkröte[frame], (speeds1, holz_pos2))
        screen.blit(schildi1, (speeds2, holz_pos4))
        
        #Animation Ziel
        
        if Ziel1 == True:
            frameziel += 1
            if frameziel % 100 == 0:
                framez += 1
                if framez > 1:
                    framez = 0
            screen.blit(ziell[framez], (zielpos_1, zielpos_y))
        if Ziel2 == True:
            frameziel += 1
            if frameziel % 100 == 0:
                framez += 1
                if framez > 1:
                    framez = 0
            screen.blit(ziell[framez], (zielpos_2, zielpos_y))
        if Ziel3 == True:
            frameziel += 1
            if frameziel % 100 == 0:
                framez += 1
                if framez > 1:
                    framez = 0
            screen.blit(ziell[framez], (zielpos_3, zielpos_y))
        if Ziel4 == True:
            frameziel += 1
            if frameziel % 100 == 0:
                framez += 1
                if framez > 1:
                    framez = 0
            screen.blit(ziell[framez], (zielpos_4, zielpos_y))
        if Ziel5 == True:
            frameziel += 1
            if frameziel % 100 == 0:
                framez += 1
                if framez > 1:
                    framez = 0
            screen.blit(ziell[framez], (zielpos_5, zielpos_y))
        
        


        #Spielfigur
        if Froschda == True:
            screen.blit(frog_r, (ballpos_x ,ballpos_y))

        # Fenster aktualisieren
    #    pygame.display.flip()

        # Refresh-Zeiten festlegen
        clock.tick(60)

        # Autos bewegen
        speed1 -= ges + 0.5
        speed2 += ges
        speed3 -= ges + 1
        speed4 += ges
        speed5 -= ges
        speed6 -= ges + 2

        #Holz bewegen
        speedh1 += ges + 0.3
        speedh2 += ges - 0.2
        speedh3 += ges + 0.1

        #Schildkröten bewegen
        speeds1 -= ges - 0.3
        speeds2 -= ges + 0.6
        speeds3 -= ges - 0.3



        # Autos zurücksetzen
        if speed1 <= -1 * autobreite:
            speed1 = FENSTERBREITE + 50
        if speed2 >= FENSTERBREITE:
            speed2 = -50
        if speed3 <= -1 * autobreite:
            speed3 = FENSTERBREITE + 50
        if speed4 >= FENSTERBREITE:
            speed4 = -50
        if speed5 <= -100:
            speed5 = FENSTERBREITE + 50
        if speed6 <= -1 * autobreite:
            speed6 = FENSTERBREITE + 50

        #Holz zurücksetzen
        if speedh1 >= FENSTERBREITE:
            speedh1 = - (50 + holzbreite)
        if speedh2 >= FENSTERBREITE:
            speedh2 = - (50 + holzbreite)
        if speedh3 >= FENSTERBREITE:
            speedh3 = - (50 + holzbreite)

        #Schildkröten zurücksetzen
        if speeds1 <= -1 * schildbreite:
            speeds1 = FENSTERBREITE + 50
        if speeds2 <= -1 * schildbreite:
            speeds2 = FENSTERBREITE + 50
        if speeds3 <= -1 * schildbreite:
            speeds3 = FENSTERBREITE + 50


        if godmode == False:
            #Kollisieon mit Autos
            if ballpos_y == auto_pos1 and ballpos_x + ballbreite >= speed1 and ballpos_x <= speed1 + autobreite:
                pygame.mixer.Sound.play(tod)
                leben -= 1
                ballpos_x = (FENSTERBREITE / 2) - (ballbreite / 2)
                ballpos_y = FENSTERHOEHE - (FENSTERHOEHE /16)
                last_direction = 'up'
            if ballpos_y == auto_pos2 and ballpos_x + ballbreite >= speed2 and ballpos_x <= speed2 + autobreite:
                pygame.mixer.Sound.play(tod)
                leben -= 1
                ballpos_x = (FENSTERBREITE / 2) - (ballbreite / 2)
                ballpos_y = FENSTERHOEHE - (FENSTERHOEHE /16)
                last_direction = 'up'
            if ballpos_y == auto_pos3 and ballpos_x + ballbreite >= speed3 and ballpos_x <= speed3 + autobreite:
                pygame.mixer.Sound.play(tod)
                leben -= 1
                ballpos_x = (FENSTERBREITE / 2) - (ballbreite / 2)
                ballpos_y = FENSTERHOEHE - (FENSTERHOEHE /16)
                last_direction = 'up'
            if ballpos_y == auto_pos4 and ballpos_x + ballbreite >= speed4 and ballpos_x <= speed4 + autobreite:
                pygame.mixer.Sound.play(tod)
                leben -= 1
                ballpos_x = (FENSTERBREITE / 2) - (ballbreite / 2)
                ballpos_y = FENSTERHOEHE - (FENSTERHOEHE /16)
                last_direction = 'up'
            if ballpos_y == auto_pos5 and ballpos_x + ballbreite >= speed5 and ballpos_x <= speed5 + 100:
                pygame.mixer.Sound.play(tod)
                leben -= 1
                ballpos_x = (FENSTERBREITE / 2) - (ballbreite / 2)
                ballpos_y = FENSTERHOEHE - (FENSTERHOEHE /16)
                last_direction = 'up'
            if ballpos_y == auto_pos6 and ballpos_x + ballbreite >= speed6 and ballpos_x <= speed6 + autobreite:
                pygame.mixer.Sound.play(tod)
                leben -= 1
                ballpos_x = (FENSTERBREITE / 2) - (ballbreite / 2)
                ballpos_y = FENSTERHOEHE - (FENSTERHOEHE /16)
                last_direction = 'up'

            #Kollision mit Holz
            if ballpos_y == holz_pos1 and ballpos_x + (ballbreite * 0.5) >= speedh1 and ballpos_x + (ballbreite * 0.8) <= speedh1 + holzbreite:
                nichtWasser = True
                if not ballpos_x + ballbreite >= FENSTERBREITE :
                    ballpos_x += ges + 0.3

            if ballpos_y == holz_pos3 and ballpos_x + (ballbreite * 0.5) >= speedh2 and ballpos_x + (ballbreite * 0.8) <= speedh2 + holzbreite:
                nichtWasser = True
                if not ballpos_x + ballbreite >= FENSTERBREITE :
                    ballpos_x += ges - 0.2

            if ballpos_y == holz_pos5 and ballpos_x + (ballbreite * 0.5) >= speedh3 and ballpos_x + (ballbreite * 0.8) <= speedh3 + holzbreite:
                nichtWasser = True
                if not ballpos_x + ballbreite >= FENSTERBREITE :
                    ballpos_x += ges + 0.1


            #Kollision mit Schildkröte
            if ballpos_y == holz_pos2 and ballpos_x + (ballbreite * 0.2) >= speeds1 and ballpos_x + (ballbreite * 0.7) <= speeds1 + schildbreite:
                if not frame == 5:
                    nichtWasser = True
                if not ballpos_x  <= 0 :
                    if not frame == 5:
                        ballpos_x -= ges - 0.3

            if ballpos_y == holz_pos4 and ballpos_x + (ballbreite * 0.2) >= speeds2 and ballpos_x + (ballbreite * 0.7) <= speeds2 + schildbreite:
                nichtWasser = True
                if not ballpos_x  <= 0 :
                        ballpos_x -= ges + 0.6

            if ballpos_y == holz_pos6 and ballpos_x + (ballbreite * 0.2) >= speeds3 and ballpos_x + (ballbreite * 0.7) <= speeds3 + schildbreite:
                if not frame == 5:
                    nichtWasser = True
                if not ballpos_x  <= 0 :
                    if not frame == 5:
                        ballpos_x -= ges - 0.3

            #Kollision mit Wasser
            if ballpos_y >= FENSTERHOEHE * (1/8) and ballpos_y <= FENSTERHOEHE * (7/16) :
                if nichtWasser == False or inAnimation == True:
                    Froschda = False
                    inAnimation = True
                    if frametod == 0:
                        pygame.mixer.Sound.play(wasser)
                        todpos_x = ballpos_x
                        todpos_y = ballpos_y
                    frametod += 1
                    if frametod % 10 == 0:
                        frame2 += 1
                    screen.blit(todl[frame2], (todpos_x, todpos_y))

                    if frame2 == 6:
                        ballpos_x = spawnx
                        ballpos_y = spawny
                        Froschda = True
                        frame2 = 0
                        frametod = 0
                        last_direction = 'up'
                        nichtWasser = True
                        inAnimation = False
                        leben -= 1



        #Leben anzeigen
        for i in range(0, leben):
            screen.blit(lebenbild, (FENSTERBREITE - (i * 50) - 50, spawny + (FENSTERHOEHE * (1/128))))

        # Levelanzeige
        text = font.render('Level ' + str(level), True, WEISS)
        textRect = text.get_rect()
        textRect.center = (FENSTERBREITE * (1/9), spawny + (FENSTERHOEHE * (1/32)))
        screen.blit(text, textRect)


        frame1 += 1
        if frame1 % 30 == 0:
            frame += 1
            if frame > 9:
                frame = 0

        pygame.display.update()


        nichtWasser = False

    #______________________________________________________
        #Spielende

    pygame.quit()

if __name__ == "__main__":
    frogger(700)