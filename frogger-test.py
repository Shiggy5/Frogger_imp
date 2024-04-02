# Frogger made with pygame

# Importiere die Pygame Bibliothek
import pygame
import random
import time

# Initialisiere Pygame
pygame.init()

# Definiere die Fenstergröße
FENSTERBREITE = 650
FENSTERHOEHE = 800

# Definiere die Variablen
ballpos_x = 300
ballpos_y = 750
bewegung = 50
ballbreite = 50
ballhoehe = 50
last_direction = 'up'
score = 0
leben = 3
level = 1
level2 = 1
level3 = 1
level4 = 1
level5 = 1

# Definiere die Geschwindigkeit der Autos
speed = 1
speed2 = 1
speed3 = 1
speed4 = 1
speed5 = 1

# Definiere die Geschwindigkeit der Schildkröten
speed6 = 1
speed7 = 1
speed8 = 1
speed9 = 1
speed10 = 1
speed11 = 1
speed12 = 1

# Importiere die Hintergrundmusik
pygame.mixer.music.load('Level.mp3')
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(.6)

# Importiere die Sounds
springen = pygame.mixer.Sound('springen.mp3')
springen.set_volume(.7)
tod = pygame.mixer.Sound('tod.mp3')
tod.set_volume(.7)
levelup = pygame.mixer.Sound('levelup.mp3')
levelup.set_volume(.7)
gameover = pygame.mixer.Sound('gameover.mp3')
gameover.set_volume(.7)

# Importiere die Bilder
hintergrund1 = pygame.image.load("frogger_background.png")
hintergrund = pygame.transform.scale(hintergrund1, (FENSTERBREITE, FENSTERHOEHE))

frog1 = pygame.image.load("frog.png")
frog = pygame.transform.scale(frog1, (ballbreite, ballhoehe))
bildgroessen = frog.get_rect()

auto1 = pygame.image.load("auto1.png")
auto1 = pygame.transform.scale(auto1, (100, 50))
auto1groessen = auto1.get_rect()

auto2 = pygame.image.load("auto2.png")
auto2 = pygame.transform.scale(auto2, (100, 50))
auto2groessen = auto2.get_rect()

auto3 = pygame.image.load("auto3.png")
auto3 = pygame.transform.scale(auto3, (100, 50))
auto3groessen = auto3.get_rect()

auto4 = pygame.image.load("auto4.png")
auto4 = pygame.transform.scale(auto4, (100, 50))
auto4groessen = auto4.get_rect()

auto5 = pygame.image.load("auto5.png")
auto5 = pygame.transform.scale(auto5, (100, 50))
auto5groessen = auto5.get_rect()

# Importiere die Schildkröten
schildkroete1 = pygame.image.load("schildkroete1.png")
schildkroete1 = pygame.transform.scale(schildkroete1, (100, 50))
schildkroete1groessen = schildkroete1.get_rect()

schildkroete2 = pygame.image.load("schildkroete2.png")
schildkroete2 = pygame.transform.scale(schildkroete2, (100, 50))
schildkroete2groessen = schildkroete2.get_rect()

schildkroete3 = pygame.image.load("schildkroete3.png")
schildkroete3 = pygame.transform.scale(schildkroete3, (100, 50))
schildkroete3groessen = schildkroete3.get_rect()

schildkroete4 = pygame.image.load("schildkroete4.png")
schildkroete4 = pygame.transform.scale(schildkroete4, (100, 50))
schildkroete4groessen = schildkroete4.get_rect()

schildkroete5 = pygame.image.load("schildkroete5.png")
schildkroete5 = pygame.transform.scale(schildkroete5, (100, 50))
schildkroete5groessen = schildkroete5.get_rect()

schildkroete6 = pygame.image.load("schildkroete6.png")
schildkroete6 = pygame.transform.scale(schildkroete6, (100, 50))
schildkroete6groessen = schildkroete6.get_rect()

schildkroete7 = pygame.image.load("schildkroete7.png")
schildkroete7 = pygame.transform.scale(schildkroete7, (100, 50))
schildkroete7groessen = schildkroete7.get_rect()

# Fenster öffnen
screen = pygame.display.set_mode((FENSTERBREITE, FENSTERHOEHE))

pygame.display.set_caption("Frogger")

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()


# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == pygame.KEYDOWN:
            print("Spieler hat Taste gedrückt")

            # Taste für Spieler 1
            if event.key == pygame.K_RIGHT:
                if not ballpos_x + ballbreite >= FENSTERBREITE:
                    ballpos_x += bewegung
                    pygame.mixer.Sound.play(springen)
                    last_direction = 'right'
            elif event.key == pygame.K_LEFT:
                if not ballpos_x <= 0:
                    ballpos_x -= bewegung
                    pygame.mixer.Sound.play(springen)
                    last_direction = 'left'
            elif event.key == pygame.K_UP:
                if not ballpos_y <= 0:
                    ballpos_y -= bewegung
                    pygame.mixer.Sound.play(springen)
                    last_direction = 'up'
            elif event.key == pygame.K_DOWN:
                if not ballpos_y + ballhoehe >= FENSTERHOEHE:
                    ballpos_y += bewegung
                    pygame.mixer.Sound.play(springen)
                    last_direction = 'down'
            elif event.key == pygame.K_SPACE:
                print("Spieler hat Leertaste gedrückt")


        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Spieler hast Maus angeklickt")

    # Hintergrundbild anzeigen
    screen.blit(hintergrund, (0, 0))

    # Autos anzeigen
    screen.blit(auto1, (0 + speed, 650))
    screen.blit(auto2, (150 + speed2, 650))
    screen.blit(auto3, (300 + speed3, 650))
    screen.blit(auto4, (450 + speed4, 650))
    screen.blit(auto5, (600 + speed5, 650))

    # Schildkröten anzeigen
    screen.blit(schildkroete1, (0 + speed6, 450))
    screen.blit(schildkroete2, (150 + speed7, 450))
    screen.blit(schildkroete3, (300 + speed8, 450))
    screen.blit(schildkroete4, (450 + speed9, 450))
    screen.blit(schildkroete5, (600 + speed10, 450))
    screen.blit(schildkroete6, (0 + speed11, 250))
    screen.blit(schildkroete7, (150 + speed12, 250))

    # Spielfeld/figuren zeichnen
    if last_direction == 'right':
        frog_r = pygame.transform.rotate(frog, -90)
    if last_direction == 'left':
        frog_r = pygame.transform.rotate(frog, 90)
    if last_direction == 'up':
        frog_r = pygame.transform.rotate(frog, 0)
    if last_direction == 'down':
        frog_r = pygame.transform.rotate(frog, 180)
    screen.blit(frog_r, (ballpos_x ,ballpos_y))

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

    # Autos bewegen
    speed += 1
    speed2 += 1
    speed3 += 1
    speed4 += 1
    speed5 += 1

    # Schildkröten bewegen
    speed6 += 1
    speed7 += 1
    speed8 += 1
    speed9 += 1
    speed10 += 1
    speed11 += 1
    speed12 += 1

    # Autos zurücksetzen
    if speed >= 650:
        speed = -100
    if speed2 >= 650:
        speed2 = -100
    if speed3 >= 650:
        speed3 = -100
    if speed4 >= 650:
        speed4 = -100
    if speed5 >= 650:
        speed5 = -100

    # Schildkröten zurücksetzen
    if speed6 >= 650:
        speed6 = -100
    if speed7 >= 650:
        speed7 = -100
    if speed8 >= 650:
        speed8 = -100
    if speed9 >= 650:
        speed9 = -100
    if speed10 >= 650:
        speed10 = -100
    if speed11 >= 650:
        speed11 = -100
    if speed12 >= 650:
        speed12 = -100

    # Kollision mit Auto
    if ballpos_y == 650 and ballpos_x + ballbreite >= 0 + speed and ballpos_x <= 100 + speed:
        pygame.mixer.Sound.play(tod)
        leben -= 1
        ballpos_x = 300
        ballpos_y = 750
        last_direction = 'up'
    if ballpos_y == 650 and ballpos_x + ballbreite >= 150 + speed2 and ballpos_x <= 250 + speed2:
        pygame.mixer.Sound.play(tod)
        leben -= 1
        ballpos_x = 300
        ballpos_y = 750
        last_direction = 'up'
    if ballpos_y == 650 and ballpos_x + ballbreite >= 300 + speed3 and ballpos_x <= 400 + speed3:
        pygame.mixer.Sound.play(tod)
        leben -= 1
        ballpos_x = 300
        ballpos_y = 750
        last_direction = 'up'
    if ballpos_y == 650 and ballpos_x + ballbreite >= 450 + speed4 and ballpos_x <= 550 + speed4:
        pygame.mixer.Sound.play(tod)
        leben -= 1
        ballpos_x = 300
        ballpos_y = 750
        last_direction = 'up'
    if ballpos_y == 650 and ballpos_x + ballbreite >= 600 + speed5 and ballpos_x <= 700 + speed5:
        pygame.mixer.Sound.play(tod)
        leben -= 1
        ballpos_x = 300
        ballpos_y = 750
        last_direction = 'up'

    # Kollision mit Schildkröte
    if ballpos_y == 450 and ballpos_x + ballbreite >= 0 + speed6 and ballpos_x <= 100 + speed6:
        ballpos_x += speed6
    if ballpos_y == 450 and ballpos_x + ballbreite >= 150 + speed7 and ballpos_x <= 250 + speed7:
        ballpos_x += speed7
    if ballpos_y == 450 and ballpos_x + ballbreite >= 300 + speed8 and ballpos_x <= 400 + speed8:
        ballpos_x += speed8
    if ballpos_y == 450 and ballpos_x + ballbreite >= 450 + speed9 and ballpos_x <= 550 + speed9:
        ballpos_x += speed9
    if ballpos_y == 450 and ballpos_x + ballbreite >= 600 + speed10 and ballpos_x <= 700 + speed10:
        ballpos_x += speed10
    if ballpos_y == 250 and ballpos_x + ballbreite >= 0 + speed11 and ballpos_x <= 100 + speed11:
        ballpos_x += speed11
    if ballpos_y == 250 and ballpos_x + ballbreite >= 150 + speed12 and ballpos_x <= 250 + speed12:
        ballpos_x += speed12

    # Kollision mit Rand
    if ballpos_y == 0:
        pygame.mixer.Sound.play(levelup)
        score += 100
        level += 1
        ballpos_x = 300
        ballpos_y = 750
        last_direction = 'up'
    if ballpos_y == 450 and ballpos_x + ballbreite >= 650:
        ballpos_x = 300
        ballpos_y = 750
        last_direction = 'up'
    if ballpos_y == 250 and ballpos_x + ballbreite >= 650:
        ballpos_x = 300
        ballpos_y = 750
        last_direction = 'up'

    # Leben
    if leben == 0:
        pygame.mixer.Sound.play(gameover)
        print("Game Over")
        time.sleep(3)
        spielaktiv = False

    # Level
    if level == 2 and level2 == 1:
        print("Level 2")
        time.sleep(3)
        level2 += 1
        speed += 1
        speed2 += 1
        speed3 += 1
        speed4 += 1
        speed5 += 1
        speed6 += 1
        speed7 += 1
        speed8 += 1
        speed9 += 1
        speed10 += 1
        speed11 += 1
        speed12 += 1
    if level == 3 and level3 == 1:
        print("Level 3")
        time.sleep(3)
        level3 += 1
        speed += 1
        speed2 += 1
        speed3 += 1
        speed4 += 1
        speed5 += 1
        speed6 += 1
        speed7 += 1
        speed8 += 1
        speed9 += 1
        speed10 += 1
        speed11 += 1
        speed12 += 1
    if level == 4 and level4 == 1:
        print("Level 4")
        time.sleep(3)
        level4 += 1
        speed += 1
        speed2 += 1
        speed3 += 1
        speed4 += 1
        speed5 += 1
        speed6 += 1
        speed7 += 1
        speed8 += 1
        speed9 += 1
        speed10 += 1
        speed11 += 1
        speed12 += 1
    if level == 5 and level5 == 1:
        print("Level 5")
        time.sleep(3)
        level5 += 1
        speed += 1
        speed2 += 1
        speed3 += 1
        speed4 += 1
        speed5 += 1
        speed6 += 1
        speed7 += 1
        speed8 += 1
        speed9 += 1
        speed10 += 1
        speed11 += 1
        speed12 += 1

    # Score
    if level == 2:
        score += 1
    if level == 3:
        score += 2
    if level == 4:
        score += 3
    if level == 5:
        score += 4

    # Score anzeigen
    font = pygame.font.SysFont("arial", 30)
    text = font.render("Score: " + str(score), True, SCHWARZ)
    screen.blit(text, (10, 10))

    # Leben anzeigen
    font = pygame.font.SysFont("arial", 30)
    text = font.render("Leben: " + str(leben), True, SCHWARZ)
    screen.blit(text, (10, 40))

    # Level anzeigen
    font = pygame.font.SysFont("arial", 30)
    text = font.render("Level: " + str(level), True, SCHWARZ)
    screen.blit(text, (10, 70))

# Pygame beenden
pygame.quit()


# Ende
