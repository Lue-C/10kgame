# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 12:23:03 2021

@author: xepml
"""

from maingame import *
from layout import *
from rounded import *

#import dice

white=[255,255,255]
lightgrey=[220,220,220]
grey=[100,100,100]
red=[255,0,0]
black=[0,0,0]
blue=[0,0,100]

def main(curpage,screen):
    pos = pygame.mouse.get_pos()
    screen.fill(black)
    curpage.draw(screen)
    width = 1024
    height = 768
    screen_size = (width, height)

    for event in pygame.event.get():
        print('1')
        if event.type == pygame.QUIT:
            crash = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                crash = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(3)
            if event.button == 1:
                #### check if start button is pressed
                if curpage.stage == 'menu' and curpage.funcbuttons[0].rect.collidepoint(pos):
                    screen.fill(black)
                    for j, b in enumerate(curpage.setbuttons):
                        if b.plnumberset == True:
                            numberofplayers = j + 1
                            curpage.numberofplayers=numberofplayers
                            break
                    curpage.stage = 'main game'
                    curpage.initobjects(screen_size)
                    curpage.draw(screen)
                    activeplayerindex = randint(1, len(curpage.playerpanels)) - 1
                    curpage.playerpanels[activeplayerindex].active = True

                #### check if quit button is pressed
                if curpage.stage == 'menu':
                    if curpage.funcbuttons[1].rect.collidepoint(pos):
                        crash = False
                        pygame.quit()
                if curpage.stage == 'main game':
                    print('crash2',curpage.funcbuttons)
                    if curpage.funcbuttons[0].rect.collidepoint(pos):
                        crash = False
                        pygame.quit()

                #### buttons for settings
                for b in curpage.setbuttons:
                    if b.rect.collidepoint(pos):
                        b.call_back(curpage.setbuttons)

                #### dicebuttons
                for db in curpage.dicebuttons:
                    if db.rect.collidepoint(pos):
                        db.call_back(screen)

                for jpp, pp in enumerate(curpage.playerpanels):
                    if pp.active:
                        if pp.rollbutton.rect.collidepoint(pos):
                            pp.rolldice(curpage.dicebuttons, curpage.curdiceset, screen)
#                            if pp.active == False:
#                                curpage.nextturn()
#                                curpage.renewdice(screen)
                        if pp.stopbutton.rect.collidepoint(pos):
                            pp.pointupdate(curpage.dicebuttons)
                            #for j in range(6):
                            curpage.renewdice(screen)
                            curpage.nextturn()
    pygame.display.update()
    clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    width       = 1024
    height      = 768
    screen_size = (width, height)
    size        = 10
    clr         = [255, 0, 255]
#    bg          = (255, 255, 0)
    font_size   = 15
    font        = pygame.font.Font(None, font_size)
    clock       = pygame.time.Clock()
    numberofplayers     = 1

    screen    = pygame.display.set_mode(screen_size)
    screen.fill(black)
#    bg = pygame.image.load("pics/testpic.jpg")
#    screen.blit(bg, (0, 0))
    
    crash = True
    game = False
    #numberofplayers = 1
    #instance = 'menu'
    
    curpage = gameboard(screen_size)
    
    while True:
        main(curpage,screen)
    pygame.quit()