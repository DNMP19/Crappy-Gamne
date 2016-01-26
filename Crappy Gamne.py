#Crappy Gamne v 1.10 USERS, Load and create users WIP
import pygame
import time
import random
import sys

global name

name = "defaultUserName"
open("defaultUserName.txt", 'a')
open(".txt", 'a')

pygame.init()

display_width = 1000
display_height = 700

black = (0, 0, 0)
white = (255, 255, 255)
grey = (195, 195, 195)
dark_grey = (127, 127, 127)

red = (200, 0, 0)
green = (34, 177, 76)
blue = (0, 50, 200)
orange = (255, 128, 0)
pink = (255, 128, 192)
purple = (128, 0, 255)
yellow = (255, 242, 0)
brown = (94, 47, 0)

yel_gre = (181, 230, 29)

light_red = (255, 0, 0)
light_blue = (0, 76, 230)
light_orange = (255, 128, 64)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Crappy Gamne v 1.10')
clock = pygame.time.Clock()

iconImg = pygame.image.load('Crappy Gamne icon stufe.png')
startImg = pygame.image.load('Crappy Gamne start stufe.png')
winImg = pygame.image.load('Crappy Gamne win stufe.png')
lostImg = pygame.image.load('Crappy Gamne lost stufe.png')

pygame.display.set_icon(iconImg)

rcolor = red
bcolor = green
rectailiniumHealth = 0
trialiniumHealth = 0
circailiniumHealth = 0

rectangle = 0
triangle = 1
circle = 2

bshape = rectangle
fshape = rectangle
eshape = rectangle
etp = 0
ecp = 0
ftpay = 0
fcpay = 0
shape = rectangle
tpay = 0
cpay = 0
ypay = 0
wpay = 0
bpay = 0

btp = 0
bcp = 0

craps = 0
w = 0
h = 0

pause = False

def startpic(x,y):
    gameDisplay.blit(startImg, (x,y))
    
def winpic(x,y):
    gameDisplay.blit(winImg, (x,y))

def lostpic(x,y):
    gameDisplay.blit(lostImg, (x,y))
    
def eaten(count):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Eaten i have: "+str(count), True, black)
    gameDisplay.blit(text, (0, 0))

def frenzy(count):
    font = pygame.font.SysFont(None, 50)
    text = font.render("FreNzY Tim: "+str (format(count, "2.0f")), True, black)
    gameDisplay.blit(text, (300, 0))

def health(count):
    font = pygame.font.SysFont(None, 50)
    text = font.render("BoS HEaLth: "+str(count), True, black)
    gameDisplay.blit(text, (0, 0))
    
def rhealth(count):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Rectailinium helth: "+str(count), True, black)
    gameDisplay.blit(text, (600, 0))
def thealth(count):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Trialinium helth: "+str(count), True, black)
    gameDisplay.blit(text, (600, 0))
def chealth(count):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Circailinium helth: "+str(count), True, black)
    gameDisplay.blit(text, (600, 0))
    
def crapa(count):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Craps: "+str(count), True, black)
    gameDisplay.blit(text, (800, 650))

def rectailinium(x,y,w,h):
    pygame.draw.rect(gameDisplay, rcolor,[x,y,w,h])
    smallText = pygame.font.SysFont(None,fonts)
    textSurf, textRect = text_objects("rectailinium", smallText)
    textRect.center = ( (x+(w/2)), y+(h/2) )
    gameDisplay.blit(textSurf, textRect)
def trialinium(x,y,w,h):
    pygame.draw.polygon(gameDisplay, rcolor, [[x+w,y+h],[x,y],[x-w, y+h]],0)
    smallText = pygame.font.SysFont(None,fonts)
    textSurf, textRect = text_objects("triailinium", smallText)
    textRect.center = (( x )), ( y+h-15 ) 
    gameDisplay.blit(textSurf, textRect)
def circailinium(x,y,r):
    pygame.draw.circle(gameDisplay, rcolor,[int(x),int(y)],r)
    smallText = pygame.font.SysFont(None,fonts)
    textSurf, textRect = text_objects("circailinium", smallText)
    textRect.center = ( (x), y )
    gameDisplay.blit(textSurf, textRect)

def foodrec(fx,fy,fw,fh):
    pygame.draw.rect(gameDisplay, grey,[fx,fy, fw, fh])
def foodtri(fx,fy,fw,fh):
    pygame.draw.polygon(gameDisplay, grey, [[fx+fw,fy+fh],[fx,fy],[fx-fw, fy+fh]],0)
def foodcirc(fx,fy,fr):
    pygame.draw.circle(gameDisplay, grey,[int(fx),int(fy)],fr)

def bossrec(bx,by,bw,bh):
    pygame.draw.rect(gameDisplay, grey,[bx,by, bw, bh])
    smallText = pygame.font.SysFont(None,20)
    textSurf, textRect = text_objects("BoS", smallText)
    textRect.center = ( (bx+(bw/2)), by+(bh/2) )
    gameDisplay.blit(textSurf, textRect)
def bosstri(bx,by,bw,bh):
    pygame.draw.polygon(gameDisplay, grey, [[bx+bw,by+bh],[bx,by],[bx-bw, by+bh]],0)
    smallText = pygame.font.SysFont(None,20)
    textSurf, textRect = text_objects("BoS", smallText)
    textRect.center = ( bx, by+bh-15 )
    gameDisplay.blit(textSurf, textRect)
def bosscirc(bx,by,br):
    pygame.draw.circle(gameDisplay, grey,[int(bx),int(by)],br)
    smallText = pygame.font.SysFont(None,20)
    textSurf, textRect = text_objects("BoS", smallText)
    textRect.center = ( (bx), by )
    gameDisplay.blit(textSurf, textRect)

def enemyrec(ex,ey,ew,eh):
    pygame.draw.rect(gameDisplay, dark_grey,[ex,ey, ew, eh])
    smallText = pygame.font.SysFont(None,20)
    textSurf, textRect = text_objects("GArd", smallText)
    textRect.center = ( (ex+(ew/2)), ey+(eh/2) )
    gameDisplay.blit(textSurf, textRect)
def enemytri(ex,ey,ew,eh):
    pygame.draw.polygon(gameDisplay, grey, [[ex+ew,ey+eh],[ex,ey],[ex-ew, ey+eh]],0)
    smallText = pygame.font.SysFont(None,20)
    textSurf, textRect = text_objects("GArd", smallText)
    textRect.center = ( ex, ey+eh-15 )
    gameDisplay.blit(textSurf, textRect)
def enemycirc(ex,ey,er):
    pygame.draw.circle(gameDisplay, grey,[int(ex),int(ey)],er)
    smallText = pygame.font.SysFont(None,20)
    textSurf, textRect = text_objects("GArd", smallText)
    textRect.center = ( (ex), ey )
    gameDisplay.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.SysFont(None, 95)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def message2display(text):
    largeText = pygame.font.SysFont(None, 95)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

def message3display(text):
    largeText = pygame.font.SysFont(None, 95)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height - 55))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(1)

def wine():
    global user
    global craps
    global bshape
    global btp
    global bcp
    global etp
    global ecp
    global eshape
    ctime = 0
    while wine:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        winpic(0,0)
        largeText = pygame.font.SysFont(None, 95)
        TextSurf, TextRect = text_objects("YU W1N!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        if shape == rectangle:
            if bshape == rectangle:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(rectailiniumHealth + 5), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
            if bshape == triangle and btp <= 2:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(rectailiniumHealth + 30), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
            if bshape == circle and bcp <= 3:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(rectailiniumHealth + 55), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
                
        if shape == triangle:
            if bshape == rectangle:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(trialiniumHealth + 5), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
            if bshape == triangle and btp <= 2:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(trialiniumHealth + 30), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
            if bshape == circle and bcp <= 3:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(trialiniumHealth + 55), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
                
        if shape == circle:
            if bshape == rectangle:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(circailiniumHealth + 5), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
            if bshape == triangle and btp <= 2:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(circailiniumHealth + 30), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
            if bshape == circle and bcp <= 3:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(circailiniumHealth + 55), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)

        button("Agin",150,550,100,50,purple,pink,game_loope)
        button("Menu",450,550,100,50,blue,light_blue,game_menu)
        button("Ex It",750,550,100,50,orange,light_orange,quit_game)
        crapa(craps)
    
        if ctime < 1 and shape == rectangle:
            if bshape == rectangle:
                craps += rectailiniumHealth + 5
                ctime += 1
            if bshape == triangle:
                craps += rectailiniumHealth + 5
                ctime += 1
                craps += 25
                btp += 1
                if btp == 2:
                    bshape = rectangle
                    btp = 0
            if bshape == circle:
                craps += rectailiniumHealth + 5
                ctime += 1
                craps += 50
                bcp += 1
                if bcp == 3:
                    bshape = rectangle
                    bcp = 0
        if ctime < 1 and shape == triangle:
            if bshape == rectangle:
                craps += trialiniumHealth + 5
                ctime += 1
            if bshape == triangle:
                craps += trialiniumHealth + 5
                ctime += 1
                craps += 25
                btp += 1
                if btp == 2:
                    bshape = rectangle
                    btp = 0
            if bshape == circle:
                craps += trialiniumHealth + 5
                ctime += 1
                craps += 50
                bcp += 1
                if bcp == 3:
                    bshape = rectangle
                    bcp = 0
        if ctime < 1 and shape == circle:
            if bshape == rectangle:
                craps += circailiniumHealth + 5
                ctime += 1
            if bshape == triangle:
                craps += circailiniumHealth + 5
                ctime += 1
                craps += 25
                btp += 1
                if btp == 2:
                    bshape = rectangle
                    btp = 0
            if bshape == circle:
                craps += circailiniumHealth + 5
                ctime += 1
                craps += 50
                bcp += 1
                if bcp == 3:
                    bshape = rectangle
                    bcp = 0
                    
        user = load
        etp = 0
        ecp = 0
        eshape = rectangle

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()
     
        pygame.display.update()
        clock.tick(15)
def winm():
    global user
    global craps
    global bshape
    global btp
    global bcp
    global etp
    global ecp
    global eshape
    ctime = 0
    while winm:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        winpic(0,0)
        largeText = pygame.font.SysFont(None, 95)
        TextSurf, TextRect = text_objects("YU W1N!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        if shape == rectangle:
            if bshape == rectangle:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(rectailiniumHealth + 25), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
            if bshape == triangle and btp <= 2:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(rectailiniumHealth + 50), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
            if bshape == circle and bcp <= 3:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(rectailiniumHealth + 75), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
                
        if shape == triangle:
            if bshape == rectangle:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(trialiniumHealth + 25), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
            if bshape == triangle and btp <= 2:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(trialiniumHealth + 50), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
            if bshape == circle and bcp <= 3:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(trialiniumHealth + 75), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
                
        if shape == circle:
            if bshape == rectangle:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(circailiniumHealth + 25), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
            if bshape == triangle and btp <= 2:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(circailiniumHealth + 50), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
            if bshape == circle and bcp <= 3:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(circailiniumHealth + 75), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)

        button("Agin",150,550,100,50,purple,pink,game_loopm)
        button("Menu",450,550,100,50,blue,light_blue,game_menu)
        button("Ex It",750,550,100,50,orange,light_orange,quit_game)
        crapa(craps)
    
        if ctime < 1 and shape == rectangle:
            if bshape == rectangle:
                craps += rectailiniumHealth + 25
                ctime += 1
            if bshape == triangle:
                craps += rectailiniumHealth + 25
                ctime += 1
                craps += 25
                btp += 1
                if btp == 2:
                    bshape = rectangle
                    btp = 0
            if bshape == circle:
                craps += rectailiniumHealth + 25
                ctime += 1
                craps += 50
                bcp += 1
                if bcp == 2:
                    bshape = rectangle
                    bcp = 0
        if ctime < 1 and shape == triangle:
            if bshape == rectangle:
                craps += trialiniumHealth + 25
                ctime += 1
            if bshape == triangle:
                craps += trialiniumHealth + 25
                ctime += 1
                craps += 25
                btp = 0
                bshape = rectangle
            if bshape == circle:
                craps += trialiniumHealth + 25
                ctime += 1
                craps += 50
                bcp += 1
                if bcp == 2:
                    bshape = rectangle
                    bcp = 0
        if ctime < 1 and shape == circle:
            if bshape == rectangle:
                craps += circailiniumHealth + 25
                ctime += 1
            if bshape == triangle:
                craps += circailiniumHealth + 25
                ctime += 1
                craps += 25
                btp += 1
                if btp == 2:
                    bshape = rectangle
                    btp = 0
            if bshape == circle:
                craps += circailiniumHealth + 25
                ctime += 1
                craps += 50
                bcp += 1
                if bcp == 2:
                    bshape = rectangle
                    bcp = 0
                    
        user = load
        etp = 0
        ecp = 0
        eshape = rectangle

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()
     
        pygame.display.update()
        clock.tick(15)
def winh():
    global user
    global craps
    global bshape
    global btp
    global bcp
    global etp
    global ecp
    global eshape
    ctime = 0
    while winh:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        winpic(0,0)
        largeText = pygame.font.SysFont(None, 95)
        TextSurf, TextRect = text_objects("YU W1N!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        if shape == rectangle:
            if bshape == rectangle:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(rectailiniumHealth + 50), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
            if bshape == triangle and btp <= 2:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(rectailiniumHealth + 75), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
            if bshape == circle and bcp <= 3:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(rectailiniumHealth + 100), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
                
        if shape == triangle:
            if bshape == rectangle:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(trialiniumHealth + 50), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
            if bshape == triangle and btp <= 2:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(trialiniumHealth + 75), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
            if bshape == circle and bcp <= 3:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(trialiniumHealth + 100), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
                
        if shape == circle:
            if bshape == rectangle:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(circailiniumHealth + 50), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
            if bshape == triangle and btp <= 2:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(circailiniumHealth + 75), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)
            if bshape == circle and bcp <= 3:
                largeText = pygame.font.SysFont(None, 20)
                TextSurf, TextRect = text_objects("Craps Ernd: "+str(circailiniumHealth + 100), largeText)
                TextRect.center = ((display_width/2),(display_height/1 - 55))
                gameDisplay.blit(TextSurf, TextRect)

        button("Agin",150,550,100,50,purple,pink,game_looph)
        button("Menu",450,550,100,50,blue,light_blue,game_menu)
        button("Ex It",750,550,100,50,orange,light_orange,quit_game)
        crapa(craps)
    
        if ctime < 1 and shape == rectangle:
            if bshape == rectangle:
                craps += rectailiniumHealth + 50
                ctime += 1
            if bshape == triangle:
                craps += rectailiniumHealth + 50
                ctime += 1
                craps += 25
                btp += 1
                if btp == 2:
                    bshape = rectangle
                    btp = 0
            if bshape == circle:
                craps += rectailiniumHealth + 50
                ctime += 1
                craps += 50
                bcp += 1
                if bcp == 2:
                    bshape = rectangle
                    bcp = 0
        if ctime < 1 and shape == triangle:
            if bshape == rectangle:
                craps += trialiniumHealth + 50
                ctime += 1
            if bshape == triangle:
                craps += trialiniumHealth + 50
                ctime += 1
                craps += 25
                btp += 1
                if btp == 2:
                    bshape = rectangle
                    btp = 0
            if bshape == circle:
                craps += trialiniumHealth + 50
                ctime += 1
                craps += 50
                bcp += 1
                if bcp == 2:
                    bshape = rectangle
                    bcp = 0
        if ctime < 1 and shape == circle:
            if bshape == rectangle:
                craps += circailiniumHealth + 50
                ctime += 1
            if bshape == triangle:
                craps += circailiniumHealth + 50
                ctime += 1
                craps += 25
                btp += 1
                if btp == 2:
                    bshape = rectangle
                    btp = 0
            if bshape == circle:
                craps += circailiniumHealth + 50
                ctime += 1
                craps += 50
                bcp += 1
                if bcp == 2:
                    bshape = rectangle
                    bcp = 0
                    
        user = load
        etp = 0
        ecp = 0
        eshape = rectangle

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()
     
        pygame.display.update()
        clock.tick(15)

def guarde():
    global user
    global craps
    global etp
    global ecp
    global eshape
    ctime = 0
    while guarde:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        lostpic(0,0)
        largeText = pygame.font.SysFont(None, 90)
        TextSurf, TextRect = text_objects("R3KT M8!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        if bossHealth < 100:
            largeText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("BoS Health: "+str(bossHealth), largeText)
            TextRect.center = ((display_width/2),(display_height/1 - 55))
            gameDisplay.blit(TextSurf, TextRect)

        if bossHealth == 100:
            largeText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("BoS Health: "+str(bossHealth), largeText)
            TextRect.center = ((display_width/2),(display_height/1 - 55))
            gameDisplay.blit(TextSurf, TextRect)
            
        crapa(craps)
        button("Agin",150,550,100,50,purple,pink,game_loope)
        button("Menu",450,550,100,50,blue,light_blue,game_menu)
        button("Ex It",750,550,100,50,orange,light_orange,quit_game)

        user = load
        etp = 0
        ecp = 0
        eshape = rectangle
        if ctime < 1:
            craps += 1
            ctime += 1

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()
     
        pygame.display.update()
        clock.tick(15)
def guardm():
    global craps
    global user
    global etp
    global ecp
    global eshape
    ctime = 0
    while guardm:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        lostpic(0,0)
        largeText = pygame.font.SysFont(None, 90)
        TextSurf, TextRect = text_objects("R3KT M8!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        if bossHealth < 100:
            largeText = pygame.font.SysFont(None, 65)
            TextSurf, TextRect = text_objects("BoS Health: "+str(bossHealth), largeText)
            TextRect.center = ((display_width/2),(display_height/1 - 55))
            gameDisplay.blit(TextSurf, TextRect)

        if bossHealth == 100:
            largeText = pygame.font.SysFont(None, 65)
            TextSurf, TextRect = text_objects("BoS Health: "+str(bossHealth), largeText)
            TextRect.center = ((display_width/2),(display_height/1 - 55))
            gameDisplay.blit(TextSurf, TextRect)

        crapa(craps)
        button("Agin",150,550,100,50,purple,pink,game_loopm)
        button("Menu",450,550,100,50,blue,light_blue,game_menu)
        button("Ex It",750,550,100,50,orange,light_orange,quit_game)

        if ctime < 1:
            craps += 2
            ctime += 1

        user = load
        etp = 0
        ecp = 0
        eshape = rectangle

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()
     
        pygame.display.update()
        clock.tick(15)
def guardh():
    global craps
    global user
    global etp
    global ecp
    global eshape
    ctime = 0
    while guardh:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        lostpic(0,0)
        largeText = pygame.font.SysFont(None, 90)
        TextSurf, TextRect = text_objects("R3KT M8!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        if bossHealth < 100:
            largeText = pygame.font.SysFont(None, 65)
            TextSurf, TextRect = text_objects("BoS Health: "+str(bossHealth), largeText)
            TextRect.center = ((display_width/2),(display_height/1 - 55))
            gameDisplay.blit(TextSurf, TextRect)

        if bossHealth == 100:
            largeText = pygame.font.SysFont(None, 55)
            TextSurf, TextRect = text_objects("BoS Health: "+str(bossHealth), largeText)
            TextRect.center = ((display_width/2),(display_height/1 - 55))
            gameDisplay.blit(TextSurf, TextRect)
            
        crapa(craps)
        button("Agin",150,550,100,50,purple,pink,game_looph)
        button("Menu",450,550,100,50,blue,light_blue,game_menu)
        button("Ex It",750,550,100,50,orange,light_orange,quit_game)

        if ctime < 1:
            craps += 3
            ctime += 1

        user = load
        etp = 0
        ecp = 0
        eshape = rectangle

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()
     
        pygame.display.update()
        clock.tick(15)
    
def quit_game():
    pygame.quit()
    quit()

def textBox(msg,x,y,w,h,ic):
    pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont(None, 25)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/4)), y+(h/2) )
    gameDisplay.blit(textSurf, textRect)

def button(msg,x,y,w,h,ic,ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
         
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.SysFont(None, 20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), y+(h/2) )
        gameDisplay.blit(textSurf, textRect)

def recta(x,y,w,h,ic,msg):
    pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont(None, 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), y+(h/2) )
    gameDisplay.blit(textSurf, textRect)

def unpause():
    global pause
    pause = False

def paused():

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startpic(0,0)
        largeText = pygame.font.SysFont(None, 115)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("ReSme",150,550,100,50,purple,pink,unpause)
        button("Ex It",750, 550, 100, 50,orange,light_orange,quit_game)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()
     
        pygame.display.update()
        clock.tick(15)
def greenU():
    global rcolor
    rcolor = green
    colorBpick()
def blueU():
    global rcolor
    rcolor = blue
    colorBpick()
def redU():
    global rcolor
    rcolor = red
    colorBpick()
def yellowU():
    global rcolor
    if ypay > 0:
        rcolor = yellow
        colorBpick()
    else:
        message3display("U dont ohn")
        colorUpick()
def whiteU():
    global rcolor
    if wpay > 0:
        rcolor = white
        colorBpick()
    else:
        message3display("U dont ohn")
        colorUpick()
def brownU():
    global rcolor
    if bpay > 0:
        rcolor = brown
        colorBpick()
    else:
        message3display("U dont ohn")
        colorUpick()
     
def colorUpick():
    time.sleep(.2)
    picker = True

    while picker:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
             
        gameDisplay.fill(orange)
        smallText = pygame.font.SysFont(None, 55)
        TextSurf, TextRect = text_objects("Whut culler do yu want b?", smallText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        recta(150,450,100,50,yellow,"Yellow")
        recta(450,450,100,50,white,"White")
        recta(750,450,100,50,brown,"Brown")
        button("Green",150,150,100,50,green,green,greenU)
        button("Blue",450,150,100,50,blue,blue,blueU)
        button("Red",750,150,100,50,red,red,redU)
        button("Yellow",150,450,100,50,yellow,yellow,yellowU)
        button("White",450,450,100,50,white,white,whiteU)
        button("Brown",750,450,100,50,brown,brown,brownU)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()
     
        pygame.display.update()

def greenB():
    global bcolor
    bcolor = green
    game_mode()
def blueB():
    global bcolor
    bcolor = blue
    game_mode()
def redB():
    global bcolor
    bcolor = red
    game_mode()
def yellowB():
    global bcolor
    if ypay > 0:
        bcolor = yellow
        game_mode()
    else:
        message3display("U dont ohn")
        colorBpick()
def whiteB():
    global bcolor
    if wpay > 0:
        bcolor = white
        game_mode()
    else:
        message3display("U dont ohn")
        colorBpick()
def brownB():
    global bcolor
    if bpay > 0:
        bcolor = brown
        game_mode()
    else:
        message3display("U dont ohn")
        colorBpick()
     
def colorBpick():
    bpicker = True
    time.sleep(.2)

    while bpicker:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
             
        gameDisplay.fill(orange)
        smallText = pygame.font.SysFont(None, 45)
        TextSurf, TextRect = text_objects("Wut culler do yu want bakground too b? ", smallText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        recta(150,450,100,50,yellow,"Yellow")
        recta(450,450,100,50,white,"White")
        recta(750,450,100,50,brown,"Brown")
        button("Green",150,150,100,50,green,green,greenB)
        button("Blue",450,150,100,50,blue,blue,blueB)
        button("Red",750,150,100,50,red,red,redB)
        button("Yellow",150,450,100,50,yellow,yellow,yellowB)
        button("White",450,450,100,50,white,white,whiteB)
        button("Brown",750,450,100,50,brown,brown,brownB)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()
     
        pygame.display.update()

def easy():
    game_loope()
def medium():
    game_loopm()
def hard():
    game_looph()
    
def game_mode():
    mode = True
    time.sleep(.2)
    while mode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
             
        gameDisplay.fill(orange)
        smallText = pygame.font.SysFont(None, 45)
        TextSurf, TextRect = text_objects("Pck a Gme mOod", smallText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        button("Easy",150,450,100,50,green,green,easy)
        button("Medium",450,450,100,50,blue,blue,medium)
        button("Hard",750,450,100,50,red,red,hard)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()
     
        pygame.display.update()
def new():
    global shape
    global fshape
    global user
    global wpay
    global bpay
    global tpay
    global cpay
    global ypay
    global craps
    global ftpay
    global fcpay
    global btp
    global bcp
    global etp
    global ecp
    craps = 0
    ypay = 0
    bpay = 0
    wpay = 0
    cpay = 0
    tpay = 0
    fcpay = 0
    ftpay = 0
    btp = 0
    cpt = 0
    etp = 0
    ecp = 0
    user = new
    shape = rectangle
    fshape = rectangle
    eshape = rectangle
    userName()
def load():
    global user
    user = load
    userLoad()

def userLoad():
    global space
    global name
    name = ""
    gameDisplay.fill(yel_gre)
    pygame.draw.rect(gameDisplay, grey, (0, 280, 3250, 125))
    smallText = pygame.font.SysFont(None, 200)
    TextSurf, TextRect = text_objects("Mst B 6 LTr nAm", smallText)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)
    space = 3.5
    while userName:
        button("Ex It",250,440,100,50,red,light_red,quit_game)
        button("pLay",650,440,100,50,blue,light_blue,colorUpick)
        if space == 6.5:
            spacing = 650
        if space == 6.0:
            spacing = 600
        if space == 5.5:
            spacing = 550
        if space == 5.0:
            spacing = 500
        if space == 4.5:
            spacing = 450
        if space == 4.0:
            spacing = 400
        if space == 3.5:
            spacing = 350
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    let = "A"
                    name += str("A")
                    userScreen(let, spacing)
                if event.key == pygame.K_b:
                    let = "B"
                    name += str("B")
                    userScreen(let, spacing)
                if event.key == pygame.K_c:
                    let = "C"
                    name += str("C")
                    userScreen(let, spacing)
                if event.key == pygame.K_d:
                    let = "D"
                    name += str("D")
                    userScreen(let, spacing)
                if event.key == pygame.K_e:
                    let = "E"
                    name += str("E")
                    userScreen(let, spacing)
                if event.key == pygame.K_f:
                    let = "F"
                    name += str("F")
                    userScreen(let, spacing)
                if event.key == pygame.K_g:
                    let = "G"
                    name += str("G")
                    userScreen(let, spacing)
                if event.key == pygame.K_h: 
                    let = "H"
                    name += str("H")
                    userScreen(let, spacing)
                if event.key == pygame.K_i:
                    let = "I"
                    name += str("I")
                    userScreen(let, spacing)
                if event.key == pygame.K_j:
                    let = "J"
                    name += str("J")
                    userScreen(let, spacing)
                if event.key == pygame.K_k:
                    let = "K"
                    name += str("K")
                    userScreen(let, spacing)
                if event.key == pygame.K_l:
                    let = "L"
                    name += str("L")
                    userScreen(let, spacing)
                if event.key == pygame.K_m:
                    let = "M"
                    name += str("M")
                    userScreen(let, spacing)
                if event.key == pygame.K_n:
                    let = "N"
                    name += str("N")
                    userScreen(let, spacing)
                if event.key == pygame.K_o:
                    let = "O"
                    name += str("O")
                    userScreen(let, spacing)
                if event.key == pygame.K_p:
                    let = "P"
                    name += str("P")
                    userScreen(let, spacing)
                if event.key == pygame.K_q:
                    let = "Q"
                    name += str("Q")
                    userScreen(let, spacing)
                if event.key == pygame.K_r:
                    let = "R"
                    name += str("R")
                    userScreen(let, spacing)
                if event.key == pygame.K_s:
                    let = "S"
                    name += str("S")
                    userScreen(let, spacing)
                if event.key == pygame.K_t:
                    let = "T"
                    name += str("T")
                    userScreen(let, spacing)
                if event.key == pygame.K_u:
                    let = "U"
                    name += str("U")
                    userScreen(let, spacing)
                if event.key == pygame.K_v:
                    let = "V"
                    name += str("V")
                    userScreen(let, spacing)
                if event.key == pygame.K_w:
                    let = "W"
                    name += str("W")
                    userScreen(let, spacing)
                if event.key == pygame.K_x:
                    let = "X"
                    name += str("X")
                    userScreen(let, spacing)
                if event.key == pygame.K_y:
                    let = "Y"
                    name += str("Y")
                    userScreen(let, spacing)
                if event.key == pygame.K_z:
                    let = "Z"
                    name += str("Z")
                    userScreen(let, spacing)

                if event.key == pygame.K_1:
                    let = "1"
                    name += str("1")
                    userScreen(let, spacing)
                if event.key == pygame.K_2:
                    let = "2"
                    name += str("2")
                    userScreen(let, spacing)
                if event.key == pygame.K_3:
                    let = "3"
                    name += str("3")
                    userScreen(let, spacing)
                if event.key == pygame.K_4:
                    let = "4"
                    name += str("4")
                    userScreen(let, spacing)
                if event.key == pygame.K_5:
                    let = "5"
                    name += str("5")
                    userScreen(let, spacing)
                if event.key == pygame.K_6:
                    let = "6"
                    name += str("6")
                    userScreen(let, spacing)
                if event.key == pygame.K_7:
                    let = "7"
                    name += str("7")
                    userScreen(let, spacing)
                if event.key == pygame.K_8:
                    let = "8"
                    name += str("8")
                    userScreen(let, spacing)
                if event.key == pygame.K_9:
                    let = "9"
                    name += str("9")
                    userScreen(let, spacing)
                if event.key == pygame.K_0:
                    let = "0"
                    name += str("0")
                    userScreen(let, spacing)
        
        pygame.display.update()
        openFile(name + ".txt")


def userPick():
    user = True
    global name

    while user:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
             
        gameDisplay.fill(yel_gre)
        smallText = pygame.font.SysFont(None, 45)
        TextSurf, TextRect = text_objects("PiK Usr", smallText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        button("New",150,450,100,50,orange,light_orange,new)
        button("Ex It",450, 550, 100, 50,red,light_red,quit_game)
        button("SVe pRgrss", 450, 450, 100, 50, green, green, saveProgress(name + ".txt"))
        button("Load",750,450,100,50,blue,light_blue,load)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()
     
        pygame.display.update()
def saveName(fileName):
    if len(fileName) == 10:
        open(fileName, 'a')
def openFile(fileName):
    global craps
    if len(fileName) == 10:
        saveFile = open(fileName, 'r+')
        craps = saveFile.read()
        saveFile.close()
def saveProgress(fileName):
    global craps
    saveFile = open(fileName, 'r+')
    saveFile.write(str(craps))
    saveFile.close()
def userName():
    global space
    global name
    name = ""
    gameDisplay.fill(yel_gre)
    pygame.draw.rect(gameDisplay, grey, (0, 280, 3250, 125))
    smallText = pygame.font.SysFont(None, 200)
    TextSurf, TextRect = text_objects("Mst B 6 LTr nAm", smallText)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)
    space = 3.5
    while userName:
        button("Ex It",250,440,100,50,red,light_red,quit_game)
        button("pLay",650,440,100,50,blue,light_blue,colorUpick)
        if space == 6.5:
            spacing = 650
        if space == 6.0:
            spacing = 600
        if space == 5.5:
            spacing = 550
        if space == 5.0:
            spacing = 500
        if space == 4.5:
            spacing = 450
        if space == 4.0:
            spacing = 400
        if space == 3.5:
            spacing = 350
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    let = "A"
                    name += str("A")
                    userScreen(let, spacing)
                if event.key == pygame.K_b:
                    let = "B"
                    name += str("B")
                    userScreen(let, spacing)
                if event.key == pygame.K_c:
                    let = "C"
                    name += str("C")
                    userScreen(let, spacing)
                if event.key == pygame.K_d:
                    let = "D"
                    name += str("D")
                    userScreen(let, spacing)
                if event.key == pygame.K_e:
                    let = "E"
                    name += str("E")
                    userScreen(let, spacing)
                if event.key == pygame.K_f:
                    let = "F"
                    name += str("F")
                    userScreen(let, spacing)
                if event.key == pygame.K_g:
                    let = "G"
                    name += str("G")
                    userScreen(let, spacing)
                if event.key == pygame.K_h: 
                    let = "H"
                    name += str("H")
                    userScreen(let, spacing)
                if event.key == pygame.K_i:
                    let = "I"
                    name += str("I")
                    userScreen(let, spacing)
                if event.key == pygame.K_j:
                    let = "J"
                    name += str("J")
                    userScreen(let, spacing)
                if event.key == pygame.K_k:
                    let = "K"
                    name += str("K")
                    userScreen(let, spacing)
                if event.key == pygame.K_l:
                    let = "L"
                    name += str("L")
                    userScreen(let, spacing)
                if event.key == pygame.K_m:
                    let = "M"
                    name += str("M")
                    userScreen(let, spacing)
                if event.key == pygame.K_n:
                    let = "N"
                    name += str("N")
                    userScreen(let, spacing)
                if event.key == pygame.K_o:
                    let = "O"
                    name += str("O")
                    userScreen(let, spacing)
                if event.key == pygame.K_p:
                    let = "P"
                    name += str("P")
                    userScreen(let, spacing)
                if event.key == pygame.K_q:
                    let = "Q"
                    name += str("Q")
                    userScreen(let, spacing)
                if event.key == pygame.K_r:
                    let = "R"
                    name += str("R")
                    userScreen(let, spacing)
                if event.key == pygame.K_s:
                    let = "S"
                    name += str("S")
                    userScreen(let, spacing)
                if event.key == pygame.K_t:
                    let = "T"
                    name += str("T")
                    userScreen(let, spacing)
                if event.key == pygame.K_u:
                    let = "U"
                    name += str("U")
                    userScreen(let, spacing)
                if event.key == pygame.K_v:
                    let = "V"
                    name += str("V")
                    userScreen(let, spacing)
                if event.key == pygame.K_w:
                    let = "W"
                    name += str("W")
                    userScreen(let, spacing)
                if event.key == pygame.K_x:
                    let = "X"
                    name += str("X")
                    userScreen(let, spacing)
                if event.key == pygame.K_y:
                    let = "Y"
                    name += str("Y")
                    userScreen(let, spacing)
                if event.key == pygame.K_z:
                    let = "Z"
                    name += str("Z")
                    userScreen(let, spacing)

                if event.key == pygame.K_1:
                    let = "1"
                    name += str("1")
                    userScreen(let, spacing)
                if event.key == pygame.K_2:
                    let = "2"
                    name += str("2")
                    userScreen(let, spacing)
                if event.key == pygame.K_3:
                    let = "3"
                    name += str("3")
                    userScreen(let, spacing)
                if event.key == pygame.K_4:
                    let = "4"
                    name += str("4")
                    userScreen(let, spacing)
                if event.key == pygame.K_5:
                    let = "5"
                    name += str("5")
                    userScreen(let, spacing)
                if event.key == pygame.K_6:
                    let = "6"
                    name += str("6")
                    userScreen(let, spacing)
                if event.key == pygame.K_7:
                    let = "7"
                    name += str("7")
                    userScreen(let, spacing)
                if event.key == pygame.K_8:
                    let = "8"
                    name += str("8")
                    userScreen(let, spacing)
                if event.key == pygame.K_9:
                    let = "9"
                    name += str("9")
                    userScreen(let, spacing)
                if event.key == pygame.K_0:
                    let = "0"
                    name += str("0")
                    userScreen(let, spacing)
        
        pygame.display.update()
        saveName(name + ".txt")   

def userScreen(let, spacing):
    global space
    
    space = spacing / 100

    if space < 6.01:
        smallText = pygame.font.SysFont(None, 100)
        TextSurf, TextRect = text_objects(let, smallText)
        TextRect.center = ((spacing),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
    space += .5
    
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
             
        startpic(0,0)
        largeText = pygame.font.SysFont(None, 115)
        TextSurf, TextRect = text_objects("Crappy Gamne", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        textBox("Hit 'b' to get back here at any time.",700,0,600,50,yel_gre)

        button("Play",150,550,100,50,blue,light_blue,userPick)
        button("Ex It",750, 550, 100, 50,orange,light_orange,quit_game)
     
        pygame.display.update()
        clock.tick(15)
        
def rect():
    global shape
    global craps
    shape = rectangle
    store()
def tria():
    global shape
    global craps
    global tpay
    if craps - 250 >= 0 and tpay < 1:
        craps -= 250
        shape = triangle
        tpay += 1
    elif tpay > 0:
        shape = triangle
    else:
        message3display("NEd Mor craps!")
    store()
def circ():
    global shape
    global craps
    global cpay
    if craps - 500 >= 0 and cpay < 1:
        craps -= 500
        shape = circle
        cpay += 1
    elif cpay > 0:
        shape = circle
    else:
        message3display("NEd Mor craps!")
    store()
def yel():
    global craps
    global ypay
    if craps - 100 >= 0 and ypay < 1:
        craps -= 100
        ypay += 1
    elif ypay > 1:
        ypay = 1
    else:
        message3display("NEd Mor craps!")
    store()
def whi():
    global craps
    global wpay
    if craps - 100 >= 0 and wpay < 1:
        craps -= 100
        wpay += 1
    elif wpay > 1:
        wpay = 1
    else:
        message3display("NEd Mor craps!")
    store()
def bro():
    global craps
    global bpay
    if craps - 100 >= 0 and bpay < 1:
        craps -= 100
        bpay += 1
    elif bpay > 1:
        bpay = 1
    else:
        message3display("NEd Mor craps!")
    store()
def store():
    global craps
    global ypay
    global wpay
    global bpay
    time.sleep(.2)
    store = True

    while store:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
             
        gameDisplay.fill(orange)

        smallText = pygame.font.SysFont(None, 75)
        TextSurf, TextRect = text_objects("ShApEz", smallText)
        TextRect.center = ((display_width/2),(display_height/6))
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.SysFont(None, 75)
        TextSurf, TextRect = text_objects("CulLerz", smallText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        if shape != rectangle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("U hAv", smallText)
            TextRect.center = ((160),(210))
            gameDisplay.blit(TextSurf, TextRect)
        if shape == rectangle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("EqiPt", smallText)
            TextRect.center = ((160),(210))
            gameDisplay.blit(TextSurf, TextRect)
            
        if tpay < 1 and shape != triangle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("250 Craps", smallText)
            TextRect.center = ((460),(210))
            gameDisplay.blit(TextSurf, TextRect)
        if tpay > 0 and shape != triangle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("U hAv", smallText)
            TextRect.center = ((460),(210))
            gameDisplay.blit(TextSurf, TextRect)
        if shape == triangle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("EqiPt", smallText)
            TextRect.center = ((460),(210))
            gameDisplay.blit(TextSurf, TextRect)

        if cpay < 1 and shape != circle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("500 Craps", smallText)
            TextRect.center = ((760),(210))
            gameDisplay.blit(TextSurf, TextRect)
        if cpay > 0 and shape != circle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("U hAv", smallText)
            TextRect.center = ((760),(210))
            gameDisplay.blit(TextSurf, TextRect)
        if shape == circle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("EqiPt", smallText)
            TextRect.center = ((760),(210))
            gameDisplay.blit(TextSurf, TextRect)

        if ypay < 1:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("100 Craps", smallText)
            TextRect.center = ((160),(470))
            gameDisplay.blit(TextSurf, TextRect)
        if ypay > 0:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("U hAv", smallText)
            TextRect.center = ((160),(470))
            gameDisplay.blit(TextSurf, TextRect)

        if wpay < 1:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("100 Craps", smallText)
            TextRect.center = ((460),(470))
            gameDisplay.blit(TextSurf, TextRect)
        if wpay > 0:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("U hAv", smallText)
            TextRect.center = ((460),(470))
            gameDisplay.blit(TextSurf, TextRect)

        if bpay < 1:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("100 Craps", smallText)
            TextRect.center = ((760),(470))
            gameDisplay.blit(TextSurf, TextRect)
        if bpay > 0:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("U hAv", smallText)
            TextRect.center = ((760),(470))
            gameDisplay.blit(TextSurf, TextRect)
            
        crapa(craps)
        recta(750,150,100,50,red,"Circailinium")
        recta(150,410,100,50,yellow,"Yellow")
        recta(450,410,100,50,white,"White")
        recta(750,410,100,50,brown,"Brown")
        button("MEnU",110,640,100,50,red,light_red,game_menu)
        button("nXt",650,640,100,50,red,light_red,store2)
        button("Rectailinium",150,150,100,50,green,green,rect)
        button("Trialinium",450,150,100,50,blue,blue,tria)
        button("Circailinium",750,150,100,50,red,red,circ)
        button("Yellow",150,410,100,50,yellow,yellow,yel)
        button("White",450,410,100,50,white,white,whi)
        button("Brown",750,410,100,50,brown,brown,bro)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()
     
        pygame.display.update()
def frect():
    global fshape
    global craps
    fshape = rectangle
    store2()
def ftria():
    global fshape
    global craps
    global ftpay
    if craps - 750 >= 0 and ftpay < 1:
        craps -= 750
        fshape = triangle
        ftpay += 1
    elif ftpay > 0:
        fshape = triangle
    else:
        message3display("NEd Mor craps!")
    store2()
def fcirc():
    global fshape
    global craps
    global fcpay
    if craps - 1000 >= 0 and fcpay < 1:
        craps -= 1000
        fshape = circle
        fcpay += 1
    elif fcpay > 0:
        fshape = circle
    else:
        message3display("NEd Mor craps!")
    store2()
def btri():
    global bshape
    global craps
    global btp
    if craps - 300 >= 0 and btp < 1:
        craps -= 300
        bshape = triangle
        btp += 1
    elif btp > 0:
        bshape = triangle
    else:
        message3display("NEd Mor craps!")
    store2()
def etri():
    global eshape
    global craps
    global etp
    if craps - 150 >= 0 and etp < 1:
        craps -= 150
        eshape = triangle
        etp += 1
    elif etp > 0:
        eshape = triangle
    else:
        message3display("NEd Mor craps!")
    store2()
def bcirc():
    global bshape
    global craps
    global bcp
    if craps - 500 >= 0 and bcp < 1:
        craps -= 500
        bshape = circle
        bcp += 1
    elif bcp > 0:
        bshape = circle
    else:
        message3display("NEd Mor craps!")
    store2()
def ecirc():
    global eshape
    global craps
    global ecp
    if craps - 300 >= 0 and ecp < 1:
        craps -= 300
        eshape = circle
        ecp += 1
    elif etp > 0:
        eshape = circle
    else:
        message3display("NEd Mor craps!")
    store2()
def store2():
    global craps
    time.sleep(.2)
    store2 = True

    while store2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
             
        gameDisplay.fill(orange)

        smallText = pygame.font.SysFont(None, 75)
        TextSurf, TextRect = text_objects("Fowd ShApEz", smallText)
        TextRect.center = ((display_width/2),(display_height/6))
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.SysFont(None, 75)
        TextSurf, TextRect = text_objects("BoS ShApEz", smallText)
        TextRect.center = ((display_width/2),(display_height/2 - 55))
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.SysFont(None, 75)
        TextSurf, TextRect = text_objects("GArd ShApEz", smallText)
        TextRect.center = ((display_width/2),(display_height - 200))
        gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.SysFont(None, 25)
        TextSurf, TextRect = text_objects("+5 Health", smallText)
        TextRect.center = ((160),(170))
        gameDisplay.blit(TextSurf, TextRect)

        if fshape != rectangle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("U hAv", smallText)
            TextRect.center = ((160),(240))
            gameDisplay.blit(TextSurf, TextRect)
        if fshape == rectangle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("EqiPt", smallText)
            TextRect.center = ((160),(240))
            gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.SysFont(None, 25)
        TextSurf, TextRect = text_objects("+10 Health", smallText)
        TextRect.center = ((460),(170))
        gameDisplay.blit(TextSurf, TextRect)
            
        if ftpay < 1 and fshape != triangle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("750 Craps", smallText)
            TextRect.center = ((460),(240))
            gameDisplay.blit(TextSurf, TextRect)
        if ftpay > 0 and fshape != triangle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("U hAv", smallText)
            TextRect.center = ((460),(240))
            gameDisplay.blit(TextSurf, TextRect)
        if fshape == triangle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("EqiPt", smallText)
            TextRect.center = ((460),(240))
            gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.SysFont(None, 25)
        TextSurf, TextRect = text_objects("+15 Health", smallText)
        TextRect.center = ((760),(170))
        gameDisplay.blit(TextSurf, TextRect)

        if fcpay < 1 and fshape != circle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("1000 Craps", smallText)
            TextRect.center = ((760),(240))
            gameDisplay.blit(TextSurf, TextRect)
        if fcpay > 0 and fshape != circle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("U hAv", smallText)
            TextRect.center = ((760),(240))
            gameDisplay.blit(TextSurf, TextRect)
        if fshape == circle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("EqiPt", smallText)
            TextRect.center = ((760),(240))
            gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.SysFont(None, 25)
        TextSurf, TextRect = text_objects("+25 Craps for 1 round", smallText)
        TextRect.center = ((260),(360))
        gameDisplay.blit(TextSurf, TextRect)

        if btp < 1 and bshape != triangle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("300 Craps", smallText)
            TextRect.center = ((250),(430))
            gameDisplay.blit(TextSurf, TextRect)
        if btp > 0 and bshape != triangle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("U hAv", smallText)
            TextRect.center = ((250),(430))
            gameDisplay.blit(TextSurf, TextRect)
        if bshape == triangle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("EqiPt", smallText)
            TextRect.center = ((250),(430))
            gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.SysFont(None, 25)
        TextSurf, TextRect = text_objects("+50 Craps for 2 rounds", smallText)
        TextRect.center = ((660),(360))
        gameDisplay.blit(TextSurf, TextRect)

        if bcp < 1 and bshape != circle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("500 Craps", smallText)
            TextRect.center = ((650),(430))
            gameDisplay.blit(TextSurf, TextRect)
        if bcp > 0 and bshape != circle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("U hAv", smallText)
            TextRect.center = ((650),(430))
            gameDisplay.blit(TextSurf, TextRect)
        if bshape == circle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("EqiPt", smallText)
            TextRect.center = ((650),(430))
            gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.SysFont(None, 25)
        TextSurf, TextRect = text_objects("-2 Health for 1 round", smallText)
        TextRect.center = ((260),(560))
        gameDisplay.blit(TextSurf, TextRect)

        if etp < 1 and eshape != triangle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("150 Craps", smallText)
            TextRect.center = ((250),(630))
            gameDisplay.blit(TextSurf, TextRect)
        if etp > 0 and eshape != triangle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("U hAv", smallText)
            TextRect.center = ((250),(630))
            gameDisplay.blit(TextSurf, TextRect)
        if eshape == triangle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("EqiPt", smallText)
            TextRect.center = ((250),(630))
            gameDisplay.blit(TextSurf, TextRect)

        smallText = pygame.font.SysFont(None, 25)
        TextSurf, TextRect = text_objects("-0 Health for 1 round", smallText)
        TextRect.center = ((660),(560))
        gameDisplay.blit(TextSurf, TextRect)

        if ecp < 1 and eshape != circle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("300 Craps", smallText)
            TextRect.center = ((650),(630))
            gameDisplay.blit(TextSurf, TextRect)
        if ecp > 0 and eshape != circle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("U hAv", smallText)
            TextRect.center = ((650),(630))
            gameDisplay.blit(TextSurf, TextRect)
        if eshape == circle:
            smallText = pygame.font.SysFont(None, 25)
            TextSurf, TextRect = text_objects("EqiPt", smallText)
            TextRect.center = ((650),(630))
            gameDisplay.blit(TextSurf, TextRect)
            
        crapa(craps)
        recta(750,180,100,50,red,"Circle")
        recta(235,370,100,50,green,"Triangle")
        recta(635,370,100,50,blue,"Circle")
        recta(235,570,100,50,green,"Triangle")
        recta(635,570,100,50,blue,"Circle")
        button("MEnU",110,640,100,50,red,light_red,game_menu)
        button("PrVius",650,640,100,50,red,light_red,store)
        button("Rectangle",150,180,100,50,green,green,frect)
        button("Triangle",450,180,100,50,blue,blue,ftria)
        button("Circle",750,180,100,50,red,red,fcirc)
        
        button("Triangle",235,370,100,50,green,green,btri)
        button("Circle",635,370,100,50,blue,blue,bcirc)

        button("Triangle",235,570,100,50,green,green,etri)
        button("Circle",635,570,100,50,blue,blue,ecirc)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()
     
        pygame.display.update()

def game_menu():
    global craps
    global user
    time.sleep(.2)
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
             
        startpic(0,0)
        largeText = pygame.font.SysFont(None, 115)
        TextSurf, TextRect = text_objects("Crappy Gamne", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        textBox("Hit 'm' to get back here at any time.",700,0,600,50,yel_gre)
        textBox(name,25,0,100,50,yel_gre)
        button("lOg Owt",12,60,100,50,blue,light_blue,userPick)

        button("Play",150,550,100,50,blue,light_blue,colorUpick)
        button("Store",450,550,100,50,red,light_red,store)
        button("Ex It",750, 550, 100, 50,orange,light_orange,quit_game)
        crapa(craps)

        user = load

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()
     
        pygame.display.update()
        clock.tick(15)
     
def game_loope():
    global w
    global h
    global y
    global x
    global r
    global pause
    global rectailiniumHealth
    global trialiniumHealth
    global circailiniumHealth
    global fonts
    global craps

    w= 75
    h = 50
    
    x = (display_width/2)
    y = 400

    r = 50
    fr = 45

    fy = random.randint(10, 650)
    fx = random.randint(10, 950)
    fw = 65
    fh = 40

    if user == load:
        craps = craps
    if user == new:
        craps = 0

    x_change = 0
    y_change = 0

    fonts = 20

    ftime = 45
    i_have_eaten = 0
    rectailiniumHealth = 0
    trialiniumHealth = 0
    circailiniumHealth = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -5
                elif event.key == pygame.K_d:
                    x_change = 5
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y_change = -5
                elif event.key == pygame.K_s:
                    y_change = 5
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0
        gameDisplay.fill(bcolor)
        if fshape == rectangle:
            foodrec(fx,fy,fw,fh)
        if fshape == triangle:
            foodtri(fx,fy,fw,fh)
        if fshape == circle:
            foodcirc(fx,fy,fr)
        if shape == rectangle:
            rectailinium(x,y,w,h)
        if shape == triangle:
            trialinium(x,y,w,h)
        if shape == circle:
            circailinium(x,y,r)
        if shape == rectangle:
            if x > fx and x < fx + fw or x + w > fx and x + w < fx + w:
                if y > fy and y < fy + fh or y + h > fy and y + h < fy + h:
                    if fshape == rectangle:
                        w += 5
                        h += 5
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodrec(fx,fy,fw,fh)
                        rectailinium(x,y,w,h)
                        i_have_eaten += 1
                        rectailiniumHealth += 5
                        fonts += 1
                    if fshape == triangle:
                        w += 5
                        h += 5
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodtri(fx,fy,fw,fh)
                        rectailinium(x,y,w,h)
                        i_have_eaten += 1
                        rectailiniumHealth += 10
                        fonts += 1
                    if fshape == circle:
                        w += 5
                        h += 5
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodcirc(fx,fy,fr)
                        rectailinium(x,y,w,h)
                        i_have_eaten += 1
                        rectailiniumHealth += 15
                        fonts += 1
        if shape == triangle:
            if x > fx and x < fx + fw or x + h > fx and x + h < fx + h or \
               x < fx and x > fx - fw or x - w < fx and x - w > fx - w:
                if y > fy and y < fy + fh or y + h > fy and y + h < fy + h:
                    if fshape == rectangle:
                        w += 2
                        h += 2
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodrec(fx,fy,fw,fh)
                        trialinium(x,y,w,h)
                        i_have_eaten += 1
                        trialiniumHealth += 5
                        fonts += 1
                    if fshape == triangle:
                        w += 2
                        h += 2
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodtri(fx,fy,fw,fh)
                        trialinium(x,y,w,h)
                        i_have_eaten += 1
                        trialiniumHealth += 10
                        fonts += 1
                    if fshape == circle:
                        w += 2
                        h += 2
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodcirc(fx,fy,fr)
                        trialinium(x,y,w,h)
                        i_have_eaten += 1
                        trialiniumHealth += 15
                        fonts += 1
        if shape == circle:
            if x > fx and x < fx + fw or x + r > fx and x + r < fx + r \
              or x < fx and x > fx - fw or x - r < fx and x - r > fx - r:
                if y > fy and y < fy + fh or y + h > fy and y + h < fy + h:
                    if fshape == rectangle:
                        w += 5
                        r += 5
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodrec(fx,fy,fw,fh)
                        circailinium(x,y,r)
                        i_have_eaten += 1
                        circailiniumHealth += 5
                        fonts += 1
                    if fshape == triangle:
                        w += 5
                        r += 5
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodtri(fx,fy,fw,fh)
                        circailinium(x,y,r)
                        i_have_eaten += 1
                        circailiniumHealth += 10
                        fonts += 1
                    if fshape == circle:
                        w += 5
                        r += 5
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodcirc(fx,fy,fr)
                        circailinium(x,y,r)
                        i_have_eaten += 1
                        circailiniumHealth += 15
                        fonts += 1

        if ftime == 0 or ftime < 0 and ftime > -1:
            boss_fighte()
         
        x += x_change
        y += y_change
        
        if shape == rectangle:
            rhealth(rectailiniumHealth)
        if shape == triangle:
            thealth(trialiniumHealth)
        if shape == circle:
            chealth(circailiniumHealth)
        eaten(i_have_eaten)
        frenzy(ftime)
        crapa(craps)

        ftime -= .01
     
        pygame.display.update()
        clock.tick(100)
     
def boss_fighte():
    global w
    global h
    global y
    global x
    global r
    global rectailiniumHealth
    global trialiniumHealth
    global circailiniumHealth
    global bossHealth
    global pause
    global fonts
    global craps

    message2display("Y U b EETen My PePle")
    
    w = w
    h = h
    
    x = x
    y = y

    r = r
    br = 85
    er = 62

    by = random.randint(10, 650)
    bx = random.randint(10, 950)
    bw = 170
    bh = 145

    if user == load:
        craps = craps
    if user == new:
        craps = 0

    ex = random.randrange(0, display_width)
    ey = -100
    e_speed = 1
    ew = 125
    eh = 70

    fonts = fonts

    x_change = 0
    y_change = 0

    foodCount = 0
    bossHealth= 100
    rectailiniumHealth = rectailiniumHealth

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -5
                elif event.key == pygame.K_d:
                    x_change = 5
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y_change = -5
                elif event.key == pygame.K_s:
                    y_change = 5
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                     y_change = 0
        gameDisplay.fill(bcolor)
        
        if bshape == rectangle:
            bossrec(bx,by,bw,bh)
        if bshape == triangle:
            bosstri(bx,by,bw,bh)
        if bshape == circle:
            bosscirc(bx,by,br)
        
        if shape == rectangle:
            rectailinium(x,y,w,h)
        if shape == triangle:
            trialinium(x,y,w,h)
        if shape == circle:
            circailinium(x,y,r)
                
        if shape == rectangle:
            if bshape == rectangle:
                if x > bx and x < bx + bw or x + w > bx and x + w < bx + w:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        w += 5
                        h += 5
                        gameDisplay.fill(bcolor)
                        by = random.randint(10, 690)
                        bx = random.randint(10, 790)
                        bw -= 3
                        bh -= 3
                        bosstri(bx,by,bw,bh)
                        rectailinium(x,y,w,h)
                        foodCount += 1
                        bossHealth -= 5
                        e_speed += .5
                        fonts += 1
            if bshape == triangle:
                if x > bx and x < bx + bw or x + w > bx and x + w < bx + w or \
                   x < bx and x > bx - bw or x - w < bx and x - w > bx - w:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        w += 5
                        h += 5
                        gameDisplay.fill(bcolor)
                        by = random.randint(10, 690)
                        bx = random.randint(10, 790)
                        bw -= 3
                        bh -= 3
                        bosstri(bx,by,bw,bh)
                        rectailinium(x,y,w,h)
                        foodCount += 1
                        bossHealth -= 5
                        e_speed += .5
                        fonts += 1
            if bshape == circle:
                if x > bx and x < bx + br or x + w > bx and x + w < bx + w or \
                   x < bx and x > bx - br or x - w < bx and x - w > bx - w:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        w += 5
                        h += 5
                        gameDisplay.fill(bcolor)
                        by = random.randint(10, 690)
                        bx = random.randint(10, 790)
                        bw -= 3
                        br -= 3
                        bosscirc(bx,by,br)
                        rectailinium(x,y,w,h)
                        foodCount += 1
                        bossHealth -= 5
                        e_speed += .5
                        fonts += 1
            if eshape == rectangle:
                if x > ex and x < ex + ew or x + w > ex and x + w < ex + w:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        rectailiniumHealth -= 5
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            if eshape == triangle:
                if x > ex and x < ex + ew or x + w > ex and x + w < ex + w or \
                   x < bx and x > bx - bw or x - w < bx and x - w > bx - w:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        rectailiniumHealth -= 2
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            if eshape == circle:
                if x > bx and x < bx + br or x + w > bx and x + w < bx + w or \
                   x < bx and x > bx - br or x - w < bx and x - w > bx - w:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        rectailiniumHealth -= 0
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            
        if shape == triangle:
            if bshape == rectangle:
                if x > bx and x < bx + bw or x + w > bx and x + w < bx + w or \
                    x < bx and x > bx - bw or x - w < bx and x - w > bx - w:
                        if y > by and y < by + bh or y + h > by and y + h < by + h:
                            w += 5
                            h += 5
                            gameDisplay.fill(bcolor)
                            by = random.randint(10, 690)
                            bx = random.randint(10, 790)
                            bw -= 3
                            bh -= 3
                            bosstri(bx,by,bw,bh)
                            trialinium(x,y,w,h)
                            foodCount += 1
                            bossHealth -= 5
                            e_speed += .5
                            fonts += 1
                if bshape == triangle:
                    if x > bx and x < bx + bw or x + w > bx and x + w < bx + w or \
                       x < bx and x > bx - bw or x - w < bx and x - w > bx - w:
                        if y > by and y < by + bh or y + h > by and y + h < by + h:
                            w += 5
                            h += 5
                            gameDisplay.fill(bcolor)
                            by = random.randint(10, 690)
                            bx = random.randint(10, 790)
                            bw -= 3
                            bh -= 3
                            bosstri(bx,by,bw,bh)
                            trialinium(x,y,w,h)
                            foodCount += 1
                            bossHealth -= 5
                            e_speed += .5
                            fonts += 1
                if bshape == circle:
                    if x > bx and x < bx + br or x + w > bx and x + w < bx + w or \
                       x < bx and x > bx - br or x - w < bx and x - w > bx - w:
                        if y > by and y < by + bh or y + h > by and y + h < by + h:
                            w += 5
                            h += 5
                            gameDisplay.fill(bcolor)
                            by = random.randint(10, 690)
                            bx = random.randint(10, 790)
                            bw -= 3
                            br -= 3
                            bosscirc(bx,by,br)
                            trialinium(x,y,w,h)
                            foodCount += 1
                            bossHealth -= 5
                            e_speed += .5
                            fonts += 1
            if eshape == rectangle:
                if x > ex and x < ex + ew or x + w > ex and x + w < ex + w:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        trialiniumHealth -= 5
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            if eshape == triangle:
                if x > ex and x < ex + ew or x + w > ex and x + w < ex + w or \
                   x < bx and x > bx - bw or x - w < bx and x - w > bx - w:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        trialiniumHealth -= 2
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            if eshape == circle:
                if x > bx and x < bx + br or x + w > bx and x + w < bx + w or \
                   x < bx and x > bx - br or x - w < bx and x - w > bx - w:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        trialiniumHealth -= 0
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
                
        if shape == circle:
            if bshape == rectangle:
                if x > bx and x < bx + bw or x + r > bx and x + r < bx + r \
                  or x < bx and x > bx - bw or x - r < bx and x - r > bx - r:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        w += 5
                        r += 5
                        gameDisplay.fill(bcolor)
                        by = random.randint(10, 690)
                        bx = random.randint(10, 790)
                        bw -= 3
                        bh -= 3
                        bossrec(bx,by,bw,bh)
                        circailinium(x,y,r)
                        foodCount += 1
                        bossHealth -= 5
                        e_speed += .5
                        fonts += 1
            if bshape == triangle:
                if x > bx and x < bx + bw or x + r > bx and x + r < bx + r \
                  or x < bx and x > bx - bw or x - r < bx and x - r > bx - r:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        w += 5
                        r += 5
                        gameDisplay.fill(bcolor)
                        by = random.randint(10, 690)
                        bx = random.randint(10, 790)
                        bw -= 3
                        bh -= 3
                        bosstri(bx,by,bw,bh)
                        circailinium(x,y,r)
                        foodCount += 1
                        bossHealth -= 5
                        e_speed += .5
                        fonts += 1
            if bshape == circle:
                if x > bx and x < bx + br or x + r > bx and x + r < bx + r \
                  or x < bx and x > bx - br or x - r < bx and x - r > bx - r:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        w += 5
                        r += 5
                        gameDisplay.fill(bcolor)
                        by = random.randint(10, 690)
                        bx = random.randint(10, 790)
                        bw -= 3
                        bh -= 3
                        bosscirc(bx,by,br)
                        circailinium(x,y,r)
                        foodCount += 1
                        bossHealth -= 5
                        e_speed += .5
                        fonts += 1
                        
            if eshape == rectangle:
                if x > ex and x < ex + ew or x + r > ex and x + r < ex + r:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        circailiniumHealth -= 5
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            if eshape == triangle:
                if x > ex and x < ex + ew or x + r > ex and x + r < ex + r or \
                   x < ex and x > ex - ew or x - r < ex and x - r > ex - r:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        circailiniumHealth -= 2
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            if eshape == circle:
                if x > ex and x < ex + er or x + r > ex and x + r < ex + r or \
                   x < ex and x > ex - er or x - r < ex and x - r > ex - r:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        circailiniumHealth -= 0
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
                    
        if eshape == rectangle:
            enemyrec(ex,ey,ew,eh)
            ey += e_speed
        if eshape == triangle:
            enemytri(ex,ey,ew,eh)
            ey += e_speed
        if eshape == circle:
            enemycirc(ex,ey,er)
            ey += e_speed

        if ey > 700:
            ey = 0 - eh
            ex = random.randrange(0, display_width)

        if bossHealth == 0:
            wine()

        if shape == rectangle:
            if rectailiniumHealth == 0:
                guarde()
        if shape == triangle:
            if trialiniumHealth == 0:
                guarde()
        if shape == circle:
            if circailiniumHealth == 0:
                guarde()
                
        x += x_change
        y += y_change

        health(bossHealth)
        if shape == rectangle:
            rhealth(rectailiniumHealth)
        if shape == triangle:
            thealth(trialiniumHealth)
        if shape == circle:
            chealth(circailiniumHealth)

        crapa(craps)
        
        pygame.display.update()
        clock.tick(100)


def game_loopm():
    global w
    global h
    global y
    global x
    global r
    global pause
    global rectailiniumHealth
    global trialiniumHealth
    global circailiniumHealth
    global fonts
    global craps

    w= 75
    h = 50
    
    x = (display_width/2)
    y = 400

    r = 50
    fr = 45

    fy = random.randint(10, 650)
    fx = random.randint(10, 950)
    fw = 65
    fh = 40

    if user == load:
        craps = craps
    if user == new:
        craps = 0

    x_change = 0
    y_change = 0

    fonts = 20

    ftime = 30
    i_have_eaten = 0
    rectailiniumHealth = 0
    trialiniumHealth = 0
    circailiniumHealth = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -5
                elif event.key == pygame.K_d:
                    x_change = 5
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y_change = -5
                elif event.key == pygame.K_s:
                    y_change = 5
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0
        gameDisplay.fill(bcolor)
        if fshape == rectangle:
            foodrec(fx,fy,fw,fh)
        if fshape == triangle:
            foodtri(fx,fy,fw,fh)
        if fshape == circle:
            foodcirc(fx,fy,fr)
        if shape == rectangle:
            rectailinium(x,y,w,h)
        if shape == triangle:
            trialinium(x,y,w,h)
        if shape == circle:
            circailinium(x,y,r)
        if shape == rectangle:
            if x > fx and x < fx + fw or x + w > fx and x + w < fx + w:
                if y > fy and y < fy + fh or y + h > fy and y + h < fy + h:
                    if fshape == rectangle:
                        w += 5
                        h += 5
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodrec(fx,fy,fw,fh)
                        rectailinium(x,y,w,h)
                        i_have_eaten += 1
                        rectailiniumHealth += 5
                        fonts += 1
                    if fshape == triangle:
                        w += 5
                        h += 5
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodtri(fx,fy,fw,fh)
                        rectailinium(x,y,w,h)
                        i_have_eaten += 1
                        rectailiniumHealth += 10
                        fonts += 1
                    if fshape == circle:
                        w += 5
                        h += 5
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodcirc(fx,fy,fr)
                        rectailinium(x,y,w,h)
                        i_have_eaten += 1
                        rectailiniumHealth += 15
                        fonts += 1
        if shape == triangle:
            if x > fx and x < fx + fw or x + h > fx and x + h < fx + h or \
               x < fx and x > fx - fw or x - w < fx and x - w > fx - w:
                if y > fy and y < fy + fh or y + h > fy and y + h < fy + h:
                    if fshape == rectangle:
                        w += 2
                        h += 2
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodrec(fx,fy,fw,fh)
                        trialinium(x,y,w,h)
                        i_have_eaten += 1
                        trialiniumHealth += 5
                        fonts += 1
                    if fshape == triangle:
                        w += 2
                        h += 2
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodtri(fx,fy,fw,fh)
                        trialinium(x,y,w,h)
                        i_have_eaten += 1
                        trialiniumHealth += 10
                        fonts += 1
                    if fshape == circle:
                        w += 2
                        h += 2
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodcirc(fx,fy,fr)
                        trialinium(x,y,w,h)
                        i_have_eaten += 1
                        trialiniumHealth += 15
                        fonts += 1
        if shape == circle:
            if x > fx and x < fx + fw or x + r > fx and x + r < fx + r \
              or x < fx and x > fx - fw or x - r < fx and x - r > fx - r:
                if y > fy and y < fy + fh or y + h > fy and y + h < fy + h:
                    if fshape == rectangle:
                        w += 5
                        r += 5
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodrec(fx,fy,fw,fh)
                        circailinium(x,y,r)
                        i_have_eaten += 1
                        circailiniumHealth += 5
                        fonts += 1
                    if fshape == triangle:
                        w += 5
                        r += 5
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodtri(fx,fy,fw,fh)
                        circailinium(x,y,r)
                        i_have_eaten += 1
                        circailiniumHealth += 10
                        fonts += 1
                    if fshape == circle:
                        w += 5
                        r += 5
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodcirc(fx,fy,fr)
                        circailinium(x,y,r)
                        i_have_eaten += 1
                        circailiniumHealth += 15
                        fonts += 1
        if ftime == 0 or ftime < 0 and ftime > -1:
            boss_fightm()
         
        x += x_change
        y += y_change
        
        if shape == rectangle:
            rhealth(rectailiniumHealth)
        if shape == triangle:
            thealth(trialiniumHealth)
        if shape == circle:
            chealth(circailiniumHealth)
        eaten(i_have_eaten)
        frenzy(ftime)
        crapa(craps)

        ftime -= .01
     
        pygame.display.update()
        clock.tick(100)
     
def boss_fightm():
    global w
    global h
    global y
    global x
    global r
    global rectailiniumHealth
    global trialiniumHealth
    global circailiniumHealth
    global bossHealth
    global pause
    global fonts
    global craps

    message2display("Y U b EETen My PePle")
    
    w = w
    h = h
    
    x = x
    y = y

    r = r
    br = 85
    er = 62

    by = random.randint(10, 650)
    bx = random.randint(10, 950)
    bw = 170
    bh = 145

    if user == load:
        craps = craps
    if user == new:
        craps = 0

    ex = random.randrange(0, display_width)
    ey = -100
    e_speed = 2
    ew = 125
    eh = 70

    fonts = fonts

    x_change = 0
    y_change = 0

    foodCount = 0
    bossHealth= 100
    rectailiniumHealth = rectailiniumHealth

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -5
                elif event.key == pygame.K_d:
                    x_change = 5
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y_change = -5
                elif event.key == pygame.K_s:
                    y_change = 5
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                     y_change = 0
                     
        gameDisplay.fill(bcolor)
        
        if bshape == rectangle:
            bossrec(bx,by,bw,bh)
        if bshape == triangle:
            bosstri(bx,by,bw,bh)
        if bshape == circle:
            bosscirc(bx,by,br)
        
        if shape == rectangle:
            rectailinium(x,y,w,h)
        if shape == triangle:
            trialinium(x,y,w,h)
        if shape == circle:
            circailinium(x,y,r)
                
        if shape == rectangle:
            if bshape == rectangle:
                if x > bx and x < bx + bw or x + w > bx and x + w < bx + w:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        w += 5
                        h += 5
                        gameDisplay.fill(bcolor)
                        by = random.randint(10, 690)
                        bx = random.randint(10, 790)
                        bw -= 3
                        bh -= 3
                        bosstri(bx,by,bw,bh)
                        rectailinium(x,y,w,h)
                        foodCount += 1
                        bossHealth -= 5
                        e_speed += .5
                        fonts += 1
            if bshape == triangle:
                if x > bx and x < bx + bw or x + w > bx and x + w < bx + w or \
                   x < bx and x > bx - bw or x - w < bx and x - w > bx - w:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        w += 5
                        h += 5
                        gameDisplay.fill(bcolor)
                        by = random.randint(10, 690)
                        bx = random.randint(10, 790)
                        bw -= 3
                        bh -= 3
                        bosstri(bx,by,bw,bh)
                        rectailinium(x,y,w,h)
                        foodCount += 1
                        bossHealth -= 5
                        e_speed += .5
                        fonts += 1
            if bshape == circle:
                if x > bx and x < bx + br or x + w > bx and x + w < bx + w or \
                   x < bx and x > bx - br or x - w < bx and x - w > bx - w:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        w += 5
                        h += 5
                        gameDisplay.fill(bcolor)
                        by = random.randint(10, 690)
                        bx = random.randint(10, 790)
                        bw -= 3
                        br -= 3
                        bosscirc(bx,by,br)
                        rectailinium(x,y,w,h)
                        foodCount += 1
                        bossHealth -= 5
                        e_speed += .5
                        fonts += 1
            if eshape == rectangle:
                if x > ex and x < ex + ew or x + w > ex and x + w < ex + w:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        rectailiniumHealth -= 5
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            if eshape == triangle:
                if x > ex and x < ex + ew or x + w > ex and x + w < ex + w or \
                   x < bx and x > bx - bw or x - w < bx and x - w > bx - w:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        rectailiniumHealth -= 2
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            if eshape == circle:
                if x > bx and x < bx + br or x + w > bx and x + w < bx + w or \
                   x < bx and x > bx - br or x - w < bx and x - w > bx - w:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        rectailiniumHealth -= 0
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            
        if shape == triangle:
            if bshape == rectangle:
                if x > bx and x < bx + bw or x + w > bx and x + w < bx + w or \
                    x < bx and x > bx - bw or x - w < bx and x - w > bx - w:
                        if y > by and y < by + bh or y + h > by and y + h < by + h:
                            w += 5
                            h += 5
                            gameDisplay.fill(bcolor)
                            by = random.randint(10, 690)
                            bx = random.randint(10, 790)
                            bw -= 3
                            bh -= 3
                            bosstri(bx,by,bw,bh)
                            trialinium(x,y,w,h)
                            foodCount += 1
                            bossHealth -= 5
                            e_speed += .5
                            fonts += 1
                if bshape == triangle:
                    if x > bx and x < bx + bw or x + w > bx and x + w < bx + w or \
                       x < bx and x > bx - bw or x - w < bx and x - w > bx - w:
                        if y > by and y < by + bh or y + h > by and y + h < by + h:
                            w += 5
                            h += 5
                            gameDisplay.fill(bcolor)
                            by = random.randint(10, 690)
                            bx = random.randint(10, 790)
                            bw -= 3
                            bh -= 3
                            bosstri(bx,by,bw,bh)
                            trialinium(x,y,w,h)
                            foodCount += 1
                            bossHealth -= 5
                            e_speed += .5
                            fonts += 1
                if bshape == circle:
                    if x > bx and x < bx + br or x + w > bx and x + w < bx + w or \
                       x < bx and x > bx - br or x - w < bx and x - w > bx - w:
                        if y > by and y < by + bh or y + h > by and y + h < by + h:
                            w += 5
                            h += 5
                            gameDisplay.fill(bcolor)
                            by = random.randint(10, 690)
                            bx = random.randint(10, 790)
                            bw -= 3
                            br -= 3
                            bosscirc(bx,by,br)
                            trialinium(x,y,w,h)
                            foodCount += 1
                            bossHealth -= 5
                            e_speed += .5
                            fonts += 1
            if eshape == rectangle:
                if x > ex and x < ex + ew or x + w > ex and x + w < ex + w:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        trialiniumHealth -= 5
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            if eshape == triangle:
                if x > ex and x < ex + ew or x + w > ex and x + w < ex + w or \
                   x < bx and x > bx - bw or x - w < bx and x - w > bx - w:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        trialiniumHealth -= 2
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            if eshape == circle:
                if x > bx and x < bx + br or x + w > bx and x + w < bx + w or \
                   x < bx and x > bx - br or x - w < bx and x - w > bx - w:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        trialiniumHealth -= 0
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
                
        if shape == circle:
            if bshape == rectangle:
                if x > bx and x < bx + bw or x + r > bx and x + r < bx + r \
                  or x < bx and x > bx - bw or x - r < bx and x - r > bx - r:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        w += 5
                        r += 5
                        gameDisplay.fill(bcolor)
                        by = random.randint(10, 690)
                        bx = random.randint(10, 790)
                        bw -= 3
                        bh -= 3
                        bossrec(bx,by,bw,bh)
                        circailinium(x,y,r)
                        foodCount += 1
                        bossHealth -= 5
                        e_speed += .5
                        fonts += 1
            if bshape == triangle:
                if x > bx and x < bx + bw or x + r > bx and x + r < bx + r \
                  or x < bx and x > bx - bw or x - r < bx and x - r > bx - r:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        w += 5
                        r += 5
                        gameDisplay.fill(bcolor)
                        by = random.randint(10, 690)
                        bx = random.randint(10, 790)
                        bw -= 3
                        bh -= 3
                        bosstri(bx,by,bw,bh)
                        circailinium(x,y,r)
                        foodCount += 1
                        bossHealth -= 5
                        e_speed += .5
                        fonts += 1
            if bshape == circle:
                if x > bx and x < bx + br or x + r > bx and x + r < bx + r \
                  or x < bx and x > bx - br or x - r < bx and x - r > bx - r:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        w += 5
                        r += 5
                        gameDisplay.fill(bcolor)
                        by = random.randint(10, 690)
                        bx = random.randint(10, 790)
                        bw -= 3
                        bh -= 3
                        bosscirc(bx,by,br)
                        circailinium(x,y,r)
                        foodCount += 1
                        bossHealth -= 5
                        e_speed += .5
                        fonts += 1
                        
            if eshape == rectangle:
                if x > ex and x < ex + ew or x + r > ex and x + r < ex + r:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        circailiniumHealth -= 5
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            if eshape == triangle:
                if x > ex and x < ex + ew or x + r > ex and x + r < ex + r or \
                   x < ex and x > ex - ew or x - r < ex and x - r > ex - r:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        circailiniumHealth -= 2
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            if eshape == circle:
                if x > ex and x < ex + er or x + r > ex and x + r < ex + r or \
                   x < ex and x > ex - er or x - r < ex and x - r > ex - r:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        circailiniumHealth -= 0
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
                
        if eshape == rectangle:
            enemyrec(ex,ey,ew,eh)
            ey += e_speed
        if eshape == triangle:
            enemyrec(ex,ey,ew,eh)
            ey += e_speed
        if eshape == circle:
            enemyrec(ex,ey,er)
            ey += e_speed

        if ey > 700:
            ey = 0 - eh
            ex = random.randrange(0, display_width)

        if bossHealth == 0:
            winm()

        if shape == rectangle:
            if rectailiniumHealth == 0:
                guardm()
        if shape == triangle:
            if trialiniumHealth == 0:
                guardm()
        if shape == circle:
            if circailiniumHealth == 0:
                guardm()
             
        x += x_change
        y += y_change

        health(bossHealth)
        if shape == rectangle:
            rhealth(rectailiniumHealth)
        if shape == triangle:
            thealth(trialiniumHealth)
        if shape == circle:
            chealth(circailiniumHealth)

        crapa(craps)
        
        pygame.display.update()
        clock.tick(100)

def game_looph():
    global w
    global h
    global y
    global x
    global r
    global pause
    global rectailiniumHealth
    global trialiniumHealth
    global circailiniumHealth
    global fonts
    global craps

    w= 75
    h = 50
    
    x = (display_width/2)
    y = 400

    r = 50
    fr = 45

    fy = random.randint(10, 650)
    fx = random.randint(10, 950)
    fw = 65
    fh = 40

    if user == load:
        craps = craps
    if user == new:
        craps = 0

    x_change = 0
    y_change = 0

    fonts = 20

    ftime = 15
    i_have_eaten = 0
    rectailiniumHealth = 0
    trialiniumHealth = 0
    circailiniumHealth = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -5
                elif event.key == pygame.K_d:
                    x_change = 5
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y_change = -5
                elif event.key == pygame.K_s:
                    y_change = 5
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0
        gameDisplay.fill(bcolor)
        if fshape == rectangle:
            foodrec(fx,fy,fw,fh)
        if fshape == triangle:
            foodtri(fx,fy,fw,fh)
        if fshape == circle:
            foodcirc(fx,fy,fr)
        if shape == rectangle:
            rectailinium(x,y,w,h)
        if shape == triangle:
            trialinium(x,y,w,h)
        if shape == circle:
            circailinium(x,y,r)
        if shape == rectangle:
            if x > fx and x < fx + fw or x + w > fx and x + w < fx + w:
                if y > fy and y < fy + fh or y + h > fy and y + h < fy + h:
                    if fshape == rectangle:
                        w += 5
                        h += 5
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodrec(fx,fy,fw,fh)
                        rectailinium(x,y,w,h)
                        i_have_eaten += 1
                        rectailiniumHealth += 5
                        fonts += 1
                    if fshape == triangle:
                        w += 5
                        h += 5
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodtri(fx,fy,fw,fh)
                        rectailinium(x,y,w,h)
                        i_have_eaten += 1
                        rectailiniumHealth += 10
                        fonts += 1
                    if fshape == circle:
                        w += 5
                        h += 5
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodcirc(fx,fy,fr)
                        rectailinium(x,y,w,h)
                        i_have_eaten += 1
                        rectailiniumHealth += 15
                        fonts += 1
        if shape == triangle:
            if x > fx and x < fx + fw or x + h > fx and x + h < fx + h or \
               x < fx and x > fx - fw or x - w < fx and x - w > fx - w:
                if y > fy and y < fy + fh or y + h > fy and y + h < fy + h:
                    if fshape == rectangle:
                        w += 2
                        h += 2
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodrec(fx,fy,fw,fh)
                        trialinium(x,y,w,h)
                        i_have_eaten += 1
                        trialiniumHealth += 5
                        fonts += 1
                    if fshape == triangle:
                        w += 2
                        h += 2
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodtri(fx,fy,fw,fh)
                        trialinium(x,y,w,h)
                        i_have_eaten += 1
                        trialiniumHealth += 10
                        fonts += 1
                    if fshape == circle:
                        w += 2
                        h += 2
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodcirc(fx,fy,fr)
                        trialinium(x,y,w,h)
                        i_have_eaten += 1
                        trialiniumHealth += 15
                        fonts += 1
        if shape == circle:
            if x > fx and x < fx + fw or x + r > fx and x + r < fx + r \
              or x < fx and x > fx - fw or x - r < fx and x - r > fx - r:
                if y > fy and y < fy + fh or y + h > fy and y + h < fy + h:
                    if fshape == rectangle:
                        w += 5
                        r += 5
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodrec(fx,fy,fw,fh)
                        circailinium(x,y,r)
                        i_have_eaten += 1
                        circailiniumHealth += 5
                        fonts += 1
                    if fshape == triangle:
                        w += 5
                        r += 5
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodtri(fx,fy,fw,fh)
                        circailinium(x,y,r)
                        i_have_eaten += 1
                        circailiniumHealth += 10
                        fonts += 1
                    if fshape == circle:
                        w += 5
                        r += 5
                        gameDisplay.fill(bcolor)
                        fy = random.randint(10, 690)
                        fx = random.randint(10, 790)
                        foodcirc(fx,fy,fr)
                        circailinium(x,y,r)
                        i_have_eaten += 1
                        circailiniumHealth += 15
                        fonts += 1

        if ftime == 0 or ftime < 0 and ftime > -1:
            boss_fighth()
         
        x += x_change
        y += y_change
        
        if shape == rectangle:
            rhealth(rectailiniumHealth)
        if shape == triangle:
            thealth(trialiniumHealth)
        if shape == circle:
            chealth(circailiniumHealth)
        eaten(i_have_eaten)
        frenzy(ftime)
        crapa(craps)

        ftime -= .01
     
        pygame.display.update()
        clock.tick(100)
     
def boss_fighth():
    global w
    global h
    global y
    global x
    global r
    global rectailiniumHealth
    global trialiniumHealth
    global circailiniumHealth
    global bossHealth
    global pause
    global fonts
    global craps

    message2display("Y U b EETen My PePle")
    
    w = w
    h = h
    
    x = x
    y = y

    r = r
    br = 85
    er = 62

    by = random.randint(10, 650)
    bx = random.randint(10, 950)
    bw = 170
    bh = 145

    if user == load:
        craps = craps
    if user == new:
        craps = 0

    ex = random.randrange(0, display_width)
    ey = -100
    e_speed = 3
    ew = 125
    eh = 70

    fonts = fonts

    x_change = 0
    y_change = 0

    foodCount = 0
    bossHealth= 100
    rectailiniumHealth = rectailiniumHealth

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -5
                elif event.key == pygame.K_d:
                    x_change = 5
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y_change = -5
                elif event.key == pygame.K_s:
                    y_change = 5
                if event.key == pygame.K_b:
                    game_intro()
                if event.key == pygame.K_m:
                    game_menu()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                     y_change = 0
                     
        gameDisplay.fill(bcolor)
        
        if bshape == rectangle:
            bossrec(bx,by,bw,bh)
        if bshape == triangle:
            bosstri(bx,by,bw,bh)
        if bshape == circle:
            bosscirc(bx,by,br)
            
        if shape == rectangle:
            rectailinium(x,y,w,h)
        if shape == triangle:
            trialinium(x,y,w,h)
        if shape == circle:
            circailinium(x,y,r)
                
        if shape == rectangle:
            if bshape == rectangle:
                if x > bx and x < bx + bw or x + w > bx and x + w < bx + w:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        w += 5
                        h += 5
                        gameDisplay.fill(bcolor)
                        by = random.randint(10, 690)
                        bx = random.randint(10, 790)
                        bw -= 3
                        bh -= 3
                        bosstri(bx,by,bw,bh)
                        rectailinium(x,y,w,h)
                        foodCount += 1
                        bossHealth -= 5
                        e_speed += .5
                        fonts += 1
            if bshape == triangle:
                if x > bx and x < bx + bw or x + w > bx and x + w < bx + w or \
                   x < bx and x > bx - bw or x - w < bx and x - w > bx - w:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        w += 5
                        h += 5
                        gameDisplay.fill(bcolor)
                        by = random.randint(10, 690)
                        bx = random.randint(10, 790)
                        bw -= 3
                        bh -= 3
                        bosstri(bx,by,bw,bh)
                        rectailinium(x,y,w,h)
                        foodCount += 1
                        bossHealth -= 5
                        e_speed += .5
                        fonts += 1
            if bshape == circle:
                if x > bx and x < bx + br or x + w > bx and x + w < bx + w or \
                   x < bx and x > bx - br or x - w < bx and x - w > bx - w:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        w += 5
                        h += 5
                        gameDisplay.fill(bcolor)
                        by = random.randint(10, 690)
                        bx = random.randint(10, 790)
                        bw -= 3
                        br -= 3
                        bosscirc(bx,by,br)
                        rectailinium(x,y,w,h)
                        foodCount += 1
                        bossHealth -= 5
                        e_speed += .5
                        fonts += 1
            if eshape == rectangle:
                if x > ex and x < ex + ew or x + w > ex and x + w < ex + w:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        rectailiniumHealth -= 5
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            if eshape == triangle:
                if x > ex and x < ex + ew or x + w > ex and x + w < ex + w or \
                   x < bx and x > bx - bw or x - w < bx and x - w > bx - w:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        rectailiniumHealth -= 2
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            if eshape == circle:
                if x > bx and x < bx + br or x + w > bx and x + w < bx + w or \
                   x < bx and x > bx - br or x - w < bx and x - w > bx - w:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        rectailiniumHealth -= 0
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            
        if shape == triangle:
            if bshape == rectangle:
                if x > bx and x < bx + bw or x + w > bx and x + w < bx + w or \
                    x < bx and x > bx - bw or x - w < bx and x - w > bx - w:
                        if y > by and y < by + bh or y + h > by and y + h < by + h:
                            w += 5
                            h += 5
                            gameDisplay.fill(bcolor)
                            by = random.randint(10, 690)
                            bx = random.randint(10, 790)
                            bw -= 3
                            bh -= 3
                            bosstri(bx,by,bw,bh)
                            trialinium(x,y,w,h)
                            foodCount += 1
                            bossHealth -= 5
                            e_speed += .5
                            fonts += 1
                if bshape == triangle:
                    if x > bx and x < bx + bw or x + w > bx and x + w < bx + w or \
                       x < bx and x > bx - bw or x - w < bx and x - w > bx - w:
                        if y > by and y < by + bh or y + h > by and y + h < by + h:
                            w += 5
                            h += 5
                            gameDisplay.fill(bcolor)
                            by = random.randint(10, 690)
                            bx = random.randint(10, 790)
                            bw -= 3
                            bh -= 3
                            bosstri(bx,by,bw,bh)
                            trialinium(x,y,w,h)
                            foodCount += 1
                            bossHealth -= 5
                            e_speed += .5
                            fonts += 1
                if bshape == circle:
                    if x > bx and x < bx + br or x + w > bx and x + w < bx + w or \
                       x < bx and x > bx - br or x - w < bx and x - w > bx - w:
                        if y > by and y < by + bh or y + h > by and y + h < by + h:
                            w += 5
                            h += 5
                            gameDisplay.fill(bcolor)
                            by = random.randint(10, 690)
                            bx = random.randint(10, 790)
                            bw -= 3
                            br -= 3
                            bosscirc(bx,by,br)
                            trialinium(x,y,w,h)
                            foodCount += 1
                            bossHealth -= 5
                            e_speed += .5
                            fonts += 1
            if eshape == rectangle:
                if x > ex and x < ex + ew or x + w > ex and x + w < ex + w:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        trialiniumHealth -= 5
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            if eshape == triangle:
                if x > ex and x < ex + ew or x + w > ex and x + w < ex + w or \
                   x < bx and x > bx - bw or x - w < bx and x - w > bx - w:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        trialiniumHealth -= 2
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            if eshape == circle:
                if x > bx and x < bx + br or x + w > bx and x + w < bx + w or \
                   x < bx and x > bx - br or x - w < bx and x - w > bx - w:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        trialiniumHealth -= 0
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
                
        if shape == circle:
            if bshape == rectangle:
                if x > bx and x < bx + bw or x + r > bx and x + r < bx + r \
                  or x < bx and x > bx - bw or x - r < bx and x - r > bx - r:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        w += 5
                        r += 5
                        gameDisplay.fill(bcolor)
                        by = random.randint(10, 690)
                        bx = random.randint(10, 790)
                        bw -= 3
                        bh -= 3
                        bossrec(bx,by,bw,bh)
                        circailinium(x,y,r)
                        foodCount += 1
                        bossHealth -= 5
                        e_speed += .5
                        fonts += 1
            if bshape == triangle:
                if x > bx and x < bx + bw or x + r > bx and x + r < bx + r \
                  or x < bx and x > bx - bw or x - r < bx and x - r > bx - r:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        w += 5
                        r += 5
                        gameDisplay.fill(bcolor)
                        by = random.randint(10, 690)
                        bx = random.randint(10, 790)
                        bw -= 3
                        bh -= 3
                        bosstri(bx,by,bw,bh)
                        circailinium(x,y,r)
                        foodCount += 1
                        bossHealth -= 5
                        e_speed += .5
                        fonts += 1
            if bshape == circle:
                if x > bx and x < bx + br or x + r > bx and x + r < bx + r \
                  or x < bx and x > bx - br or x - r < bx and x - r > bx - r:
                    if y > by and y < by + bh or y + h > by and y + h < by + h:
                        w += 5
                        r += 5
                        gameDisplay.fill(bcolor)
                        by = random.randint(10, 690)
                        bx = random.randint(10, 790)
                        bw -= 3
                        bh -= 3
                        bosscirc(bx,by,br)
                        circailinium(x,y,r)
                        foodCount += 1
                        bossHealth -= 5
                        e_speed += .5
                        fonts += 1
                        
            if eshape == rectangle:
                if x > ex and x < ex + ew or x + r > ex and x + r < ex + r:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        circailiniumHealth -= 5
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            if eshape == triangle:
                if x > ex and x < ex + ew or x + r > ex and x + r < ex + r or \
                   x < ex and x > ex - ew or x - r < ex and x - r > ex - r:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        circailiniumHealth -= 2
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
            if eshape == circle:
                if x > ex and x < ex + er or x + r > ex and x + r < ex + r or \
                   x < ex and x > ex - er or x - r < ex and x - r > ex - r:
                    if y > ey and y < ey + eh or y + h > ey and y + h < ey + h:
                        circailiniumHealth -= 0
                        ey += 700
                        w -= 5
                        h -= 5
                        fonts -= 1
                
        if eshape == rectangle:
            enemyrec(ex,ey,ew,eh)
            ey += e_speed
        if eshape == triangle:
            enemytri(ex,ey,ew,eh)
            ey += e_speed
        if eshape == circle:
            enemycirc(ex,ey,er)
            ey += e_speed

        if ey > 700:
            ey = 0 - eh
            ex = random.randrange(0, display_width)

        if bossHealth == 0:
            winh()

        if shape == rectangle:
            if rectailiniumHealth == 0:
                guardh()
        if shape == triangle:
            if trialiniumHealth == 0:
                guardh()
        if shape == circle:
            if circailiniumHealth == 0:
                guardh()
             
        x += x_change
        y += y_change

        health(bossHealth)
        if shape == rectangle:
            rhealth(rectailiniumHealth)
        if shape == triangle:
            thealth(trialiniumHealth)
        if shape == circle:
            chealth(circailiniumHealth)

        crapa(craps)
        
        pygame.display.update()
        clock.tick(100)

     
game_intro()
userPick()
colorUpick()
colorBpick()
game_mode()
game_loope()
boss_fighte()
game_loopm()
boss_fightm()
pygame_looph()
boss_fighth()
game_menu()
store()
store2()
game.quit()
quit()


