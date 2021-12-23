# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 12:23:03 2021

@author: xepml
"""

import pygame
import sys
from layout import *
import numpy as np
#import dice

white=[255,255,255]
lightgrey=[220,220,220]
grey=[100,100,100]
red=[255,0,0]

class text:
    def __init__(self, msg, position, clr=[100, 100, 100], font="Segoe Print", font_size=15, mid=False):
        self.position = position
        self.font = pygame.font.SysFont(font, font_size)
        self.txt_surf = self.font.render(msg, 1, clr)

        if len(clr) == 4:
            self.txt_surf.set_alpha(clr[3])

        if mid:
            self.position = self.txt_surf.get_rect(center=position)


    def draw(self, screen):
        screen.blit(self.txt_surf, self.position)

def gameturn(dice,player):
    
    points = 0
    numbers = np.zeros((6))
    
    ### read dice
    for j,face in enumerate(dice):
        numbers[face]+=1
    
    ### points for 1 and 5
    points+=100*numbers[0]
    points+=50*numbers[4]
    
    ### points for multiples
    for j in range(6):
        if numbers[j]==3:
            points+=100*j
    
    return points

if __name__ == '__main__':
    pygame.init()
    width       = 720
    height      = 480
    screen_size = (width, height)
    size        = 10
    clr         = [255, 0, 255]
#    bg          = (255, 255, 0)
    font_size   = 15
    font        = pygame.font.Font(None, font_size)
    clock       = pygame.time.Clock()
    numberofplayers     = 1

    screen    = pygame.display.set_mode(screen_size)
#    screen.fill(bg)
    bg = pygame.image.load("pics/testpic.jpg")
    screen.blit(bg, (0, 0))
    
    crash = True
    game = False
    numberofplayers = 1
    instance = 'menu'
    
    curpage = page(screen_size,instance,numberofplayers)
    
    while crash:
        pos = pygame.mouse.get_pos()
        curpage.draw(screen,instance)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    crash = False
    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
#                    print(curpage.setbuttons)
                    
                    #### check if start button is pressed
                    if instance == 'menu' and curpage.funcbuttons[0].rect.collidepoint(pos):
                        instance = 'main game'
                        screen.blit(bg, (0, 0))
                        for j,b in enumerate(curpage.setbuttons):
                            if b.plnumberset == True:
                                numberofplayers = j+1
                                break
                        curpage = page(screen_size,instance,numberofplayers)
                    
                    #### check if quit button is pressed
                    if instance == 'menu':
                        if curpage.funcbuttons[1].rect.collidepoint(pos):
                            crash = False
                            pygame.quit()
                    if instance == 'main game':
                        if curpage.funcbuttons[0].rect.collidepoint(pos):
#                            print(numberofplayers)
                            crash = False
                            pygame.quit()
                    
                    #### buttons for settings
                    for b in curpage.setbuttons:
                        if b.rect.collidepoint(pos):
                            b.call_back(curpage.setbuttons)
                    
                    #### functional buttons
#                    numberofplayers=curpage.numberofplayers
#                    for b in curpage.funcbuttons:
#                        if b.rect.collidepoint(pos):
#                            b.call_back(crash)
#        print(instance)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()