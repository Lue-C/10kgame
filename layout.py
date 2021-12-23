# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 23:13:27 2021

@author: xepml
"""

import pygame
import sys
from random import randint

white=[255,255,255]
lightgrey=[220,220,220]
grey=[100,100,100]
red=[255,0,0]

#### button functions
def quitfunc(run):
    run=False
    pygame.quit()

def plnumber(run,num,var):
    run=False
    pygame.quit()

def gamestart():
    return True

class button:
    def __init__(self, position, size, clr=[100, 100, 100], cngclr=None, func=None, text='', font="Segoe Print", font_size=16, font_clr=[0, 0, 0]):
        self.clr    = clr
        self.size   = size
        self.func   = func
        self.surf   = pygame.Surface(size)
        self.rect   = self.surf.get_rect(center=position)

        if cngclr:
            self.cngclr = cngclr
        else:
            self.cngclr = clr
        
        #### for additional transparency parameter
        if len(clr) == 4:
            self.surf.set_alpha(clr[3])


        self.font = pygame.font.SysFont(font, font_size)
        self.txt = text
        self.font_clr = font_clr
        self.txt_surf = self.font.render(self.txt, 1, self.font_clr)
        self.txt_rect = self.txt_surf.get_rect(center=[wh//2 for wh in self.size])

    def draw(self, screen):
        self.mouseover()

        self.surf.fill(self.curclr)
        self.surf.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surf, self.rect)

    def mouseover(self):
        self.curclr = self.clr
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.curclr = self.cngclr

    def call_back(self, *args):
#        print(self.clr)
        if self.func:
            return self.func(*args)

class permanentbutton:
    def __init__(self, position, size, clr=[100, 100, 100], cngclr=None, func=None, text='', font="Segoe Print", font_size=16, font_clr=[0, 0, 0]):
        self.clr    = clr
        self.size   = size
        self.func   = func
        self.surf   = pygame.Surface(size)
        self.rect   = self.surf.get_rect(center=position)
        self.plnumberset = False

        if cngclr:
            self.cngclr = cngclr
        else:
            self.cngclr = clr
        
        #### for additional transparency parameter
        if len(clr) == 4:
            self.surf.set_alpha(clr[3])


        self.font = pygame.font.SysFont(font, font_size)
        self.txt = text
        self.font_clr = font_clr
        self.txt_surf = self.font.render(self.txt, 1, self.font_clr)
        self.txt_rect = self.txt_surf.get_rect(center=[wh//2 for wh in self.size])

    def draw(self, screen):
        self.surf.fill(self.clr)
        self.surf.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surf, self.rect)

    def call_back(self, permbuttons):
        buttons = []
        for b in permbuttons:
            buttons.append(b)
            b.plnumberset = False
        buttons.remove(self)
        self.plnumberset = True
        self.clr = (255,0,0)
        for b in buttons:
            b.clr = white



class player():
    def __init__(self):
        self.name = ''
        self.points = 0
        self.temppoints = 0
        self.color = [255,255,255]
    def addpoints(self):
        self.points += self.temppoints

class dice:
    def __init__(self):
        self.face = randint(1, 6)

    def roll(self):
        self.dice = randint(1, 6)



class page():
    def __init__(self,winsize,instance,numberofplayers):
        self.funcbuttons = []
        self.setbuttons = []
        self.numberofplayers = numberofplayers
        
        width = winsize[0]
        height = winsize[1]
        
        ### initiate dice
        dice1=dice()
        dice2=dice()
        dice3=dice()
        dice4=dice()
        dice5=dice()
        diceset=[dice1,dice2,dice3,dice4,dice5]
        
        self.curdiceset = diceset
        self.fixeddiceset = []
        
        if instance == 'menu':
            startbutton = button((width/2, 100), (100, 50), (220, 220, 220), (255, 0, 0), gamestart, 'Start game')
            quitbutton = button((width/2, height-100), (100, 50), (220, 220, 220), (255, 0, 0), quitfunc, 'Quit')
        
            button1pl = permanentbutton((width/2, 150), (100, 50), (220, 220, 220), (255, 0, 0), plnumber, '1 player')
            button2pl = permanentbutton((width/2, 250), (100, 50), (220, 220, 220), (255, 0, 0), plnumber, '2 player')
            button3pl = permanentbutton((width/2, 350), (100, 50), (220, 220, 220), (255, 0, 0), plnumber, '3 player')
            button4pl = permanentbutton((width/2, 450), (100, 50), (220, 220, 220), (255, 0, 0), plnumber, '4 player')
        
            self.funcbuttons = [startbutton,quitbutton]
            self.setbuttons = [button1pl,button2pl,button3pl,button4pl]
        
        if instance == 'main game':
            quitbutton = button((width/2, height-100), (100, 50), (220, 220, 220), (255, 0, 0), quitfunc, 'Quit')
            rollbutton = button((width/2, height-100), (100, 50), (220, 220, 220), (255, 0, 0), self.rolldice, 'roll the dice')
            
            self.funcbuttons = [quitbutton]
            self.gamebuttons = [rollbutton]
    
    def rolldice(self):
        for d in self.curdiceset:
            d.roll()
    
    def get_playernumber(self):
        numberofplayers = 1
        setbuttons = self.setbuttons
        for j in range(len(setbuttons)):
            if setbuttons[j].plnumberset == True:
                numberofplayers = j
                break
        self.numberofplayers = numberofplayers
    
    def draw(self,screen,instance):
        for b1 in self.funcbuttons:
            b1.draw(screen)
        for b2 in self.setbuttons:
            b2.draw(screen)
    
#    def gamestart(self):
#        self.instance = 'main game'