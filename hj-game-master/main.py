print('''Gnomovision version 69, Copyright (C)  Ray Hu Jr.
Gnomovision comes with ABSOLUTELY NO WARRANTY; for details
choose `license'.  This is free software, and you are welcome
to redistribute it under certain conditions; choose `license'
for details.''')
import pygame
import dumbmenu as dm
import os

def load():
    wait =0
    with open("color", "r") as myfile:
        color = myfile.read().replace('\n', "")
        print(color)
    pygame.init()
    pygame.mixer.music.load("music.wav")
    pygame.mixer.music.play()
    # Just a few static variables
    red   = 255,  0,  0
    green =   0,255,  0
    blue  =   0,  0,255
    pygame.init()
    size = width, height = 340,240
    screen = pygame.display.set_mode(size)
    screen.fill(blue)
    pygame.display.update()
    pygame.key.set_repeat(500,30)

    choose = dm.dumbmenu(screen, [
                            'Start Game',
                            'Options',
                            'License',
                            'How To Play',
                            'Show lastscore',
                            'Donate',
                            'Quit Game'], 64,64,"Times New Roman Italic",32,1.4,green,red)



    if choose == 0:

        import sys, random

        score = 0
        pygame.init()


        def lose():
            print("YOU LOSE!!!")
            print("score:", score)
            sc2 = open("sc2", 'w')
            sc2.write(str(score))
            sc2.close()
            load()




        size = width, height = 1000, 1000
        vector = [2, 0]


        screen = pygame.display.set_mode(size)

        ball = pygame.image.load("m.gif")
        ballrect = ball.get_rect()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                if pygame.key.get_focused():
                    press = pygame.key.get_pressed()
                else:
                    press = False

                if press:
                    for i in range(0, len(press)):
                        if press[i] == 1:
                            speed = random.randint(1, 20)
                            if speed >= 10:
                                ball = pygame.image.load("hhh.gif")
                            elif speed < 10:
                                ball = pygame.image.load("m.gif")
                            else:
                                print ("BUG ACCORED!!! YOUR COMPUTER SUCKS!!!")
                                print(speed)
                                print(vector)
                                exit(233)
                            name = pygame.key.name(i)
                            print(name)
                            if name == "down":
                                vector = [0, speed]
                                score = score + 5
                            elif name == "up":
                                vector = [0, -speed]
                                score = score + 5
                            elif name =="left":
                                vector = [-speed, 0]
                                score = score + 5
                            elif name == "right":
                                vector = [speed, 0]
                                score = score + 5
                            elif name == "space":
                                ball = pygame.image.load("p.gif")
                                vector = [0, 0]

                            else:
                                pass
            if ballrect.left < 0 or ballrect.right > width:
                lose()
            if ballrect.top < 0 or ballrect.bottom > height:
                lose()
            print(vector)
            # 2
            ballrect = ballrect.move(vector)
            screen.fill(eval(color))
            screen.blit(ball, ballrect)
            pygame.display.flip()
    elif choose == 1:
        os.system("python3 op.py")

        # wait until op.py exit and reload main with new color
        with open("color", "r") as myfile:
            color = myfile.read().replace('\n', "")
            print(color)

    elif choose == 2:
        os.system("open L.html")
    elif choose == 3:
        pygame.init()
        window = pygame.display.set_mode(size)
        #title
        TITLEFONT = pygame.font.SysFont("Arial Bold Italic", 30)
        SURFACEFONT2 = TITLEFONT.render("How To Play" , True, red, green)
        SURFACE2 = SURFACEFONT2.get_rect()
        SURFACE2.center=(90,10)
        #main
        FONT = pygame.font.SysFont("Andale Mono",12)
        SURFACEFONT = FONT.render("Use the arrow keys to conrtol the huaji.",True,red,green)
        SURFACE = SURFACEFONT.get_rect()
        SURFACE.center=(140,40)

        FONT4 = pygame.font.SysFont("Andale Mono",12)
        SURFACEFONT4 = FONT4.render("Don't let the huaji go out of the window.",True,red,green)
        SURFACE4 = SURFACEFONT4.get_rect()
        SURFACE4.center=(150,60)

        SUBFONT = pygame.font.SysFont("Myanmar MN",10)
        SURFACEFONT3 = SUBFONT.render("Press enter to return to main menu.",True,red,green)
        SURFACE3 = SURFACEFONT3.get_rect()
        SURFACE3.center=(120,100)

        window.fill(green)
        while (1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if pygame.key.get_focused():
                    press = pygame.key.get_pressed()
                else:
                    press = False

                if press:
                    for i in range(0, len(press)):
                        if press[i] == 1:
                            name = pygame.key.name(i)
                            print(name)
                            if name == "return":
                                load()
            window.blit(SURFACEFONT,SURFACE)
            window.blit(SURFACEFONT2,SURFACE2)
            window.blit(SURFACEFONT3, SURFACE3)
            window.blit(SURFACEFONT4, SURFACE4)
            pygame.display.update()

    elif choose == 4:
        with open("sc2", "r") as myfile:
            d = myfile.read().replace('\n', "")
        pygame.init()
        window = pygame.display.set_mode(size)
        #title
        TITLEFONT = pygame.font.SysFont("Arial Bold Italic", 30)
        SURFACEFONT2 = TITLEFONT.render("Last Time Score" , True, red, green)
        SURFACE2 = SURFACEFONT2.get_rect()
        SURFACE2.center=(90,10)
        #main
        FONT = pygame.font.SysFont("Andale Mono",20)
        SURFACEFONT = FONT.render("YOUR SCORE IS :"+d,True,red,green)
        SURFACE = SURFACEFONT.get_rect()
        SURFACE.center=(100,40)

        SUBFONT = pygame.font.SysFont("Myanmar MN",10)
        SURFACEFONT3 = SUBFONT.render("Press enter to return to main menu.",True,red,green)
        SURFACE3 = SURFACEFONT3.get_rect()
        SURFACE3.center=(100,80)

        window.fill(green)
        while (1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if pygame.key.get_focused():
                    press = pygame.key.get_pressed()
                else:
                    press = False

                if press:
                    for i in range(0, len(press)):
                        if press[i] == 1:
                            name = pygame.key.name(i)
                            print(name)
                            if name == "return":
                                load()
            window.blit(SURFACEFONT,SURFACE)
            window.blit(SURFACEFONT2,SURFACE2)
            window.blit(SURFACEFONT3, SURFACE3)
            pygame.display.update()
    elif choose == 5:
        import webbrowser
        webbrowser.open("https://huyilin.com/ds")
        load()
    elif choose == 6:
        exit()
    pygame.quit()

while 1:
    load()

