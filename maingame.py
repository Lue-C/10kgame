# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 23:13:27 2021

@author: xepml
"""

import pygame
import sys
from random import randint
import os
import numpy as np
from layout import *

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

class dicebutton:
    def __init__(self, position, face, clr=[100, 100, 100], cngclr=None, func=None, text='', font="Segoe Print", font_size=16, font_clr=[0, 0, 0]):

        dicepicname = 'picmaker/' + 'd' + str(str(face)) + 'white.png'
        dicepic = pygame.image.load(dicepicname)
        size = (dicepic.get_width(),dicepic.get_height())

        self.face = face
        self.clr = clr
        self.func = func
        self.surf = pygame.Surface(size)
        self.rect = self.surf.get_rect(center=position)
        self.plnumberset = False
        self.fixed = 'active'

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
        self.txt_rect = self.txt_surf.get_rect(center=[wh//2 for wh in size])

    def draw(self, screen):
        value = self.fixed
        if value == 'active':
                #            print('a1')
                #            dicepic=os.path.abspath('picmaker/'+'d'+str(face)+'white.png')
            dicepic = 'picmaker/' + 'd' + str(self.face) + 'white.png'
        elif value == 'fixed':
                #            print('a2')
                #            dicepic=os.path.abspath('picmaker/'+'d'+str(face)+'green.png')
            dicepic = 'picmaker/' + 'd' + str(self.face) + 'green.png'
        elif value == 'permanent':
                #            print('a3')
                #            dicepic=os.path.abspath('picmaker/'+'d'+str(face)+'green.png')
            dicepic = 'picmaker/' + 'd' + str(self.face) + 'dark.png'
        else:
            print('activity error')
        dice = pygame.image.load(dicepic)
        screen.blit(dice, self.rect)

    def call_back(self, screen):
            #        print('dice pressed')
        value = self.fixed
            #        print('pressed diceb')
        if value != 'permanent':
            if value == 'active':
                self.fixed = 'fixed'
                #            self.cr     = grey
            if value == 'fixed':
                self.fixed = 'active'
                #            self.cr     = white
        self.draw(screen)

class permanentbutton:
    def __init__(self, position, size, clr=[100, 100, 100], cngclr=None, func=None, text='', font="Segoe Print",
                 font_size=16, font_clr=[0, 0, 0]):
        self.clr = clr
        self.size = size
        self.func = func
        self.surf = pygame.Surface(size)
        self.rect = self.surf.get_rect(center=position)
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
        self.txt_rect = self.txt_surf.get_rect(center=[wh // 2 for wh in self.size])

    def draw(self, screen):
        self.surf.fill(self.clr)
        self.surf.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surf, self.rect)

    def call_back(self, permbuttons):
        print('pressed')
        otherbuttons = []
        for b in permbuttons:
            otherbuttons.append(b)
            b.plnumberset = False
        otherbuttons.remove(self)
        self.plnumberset = True
        self.clr = (255, 0, 0)
        for b in otherbuttons:
            b.clr = white

class gameboard():
    def __init__(self,winsize):

        self.funcbuttons        = []
        self.setbuttons         = []
        self.dicebuttons        = []
        self.gamebuttons        = []
        self.numberofplayers    = 1
        self.playerpanels       = []
        self.curdiceset         = []
        self.textwindows        = []
        self.pointwindows       = []
        self.stage              ='menu'
        
        width = winsize[0]
        height = winsize[1]

        ### initiate dice
        for j in range(6):
            self.curdiceset.append(dice(j+1))

        startbutton = button((width/2, 100), (100, 50), (220, 220, 220), (255, 0, 0), gamestart, 'Start game')
        quitbutton = button((width/2, height-100), (100, 50), (220, 220, 220), (255, 0, 0), quitfunc, 'Quit')
        
        button1pl = permanentbutton((width/2, 150), (100, 50), (220, 220, 220), (255, 0, 0), plnumber, '1 player')
        button2pl = permanentbutton((width/2, 250), (100, 50), (220, 220, 220), (255, 0, 0), plnumber, '2 player')
        button3pl = permanentbutton((width/2, 350), (100, 50), (220, 220, 220), (255, 0, 0), plnumber, '3 player')
        button4pl = permanentbutton((width/2, 450), (100, 50), (220, 220, 220), (255, 0, 0), plnumber, '4 player')
        
        self.funcbuttons = [startbutton,quitbutton]
        self.setbuttons = [button1pl,button2pl,button3pl,button4pl]

    def initobjects(self,winsize):
        width = winsize[0]
        height = winsize[1]
        xoffset = 200
        yoffset = 100
        quitbutton = button((width / 2, height - 100), (100, 50), (220, 220, 220), (255, 0, 0), quitfunc, 'Quit')
        dicebutton1 = dicebutton((width / 2 - xoffset, height / 2 + yoffset), 1)
        dicebutton2 = dicebutton((width / 2 - xoffset, height / 2 - yoffset), 4)
        dicebutton3 = dicebutton((width / 2, height / 2 + yoffset), 2)
        dicebutton4 = dicebutton((width / 2, height / 2 - yoffset), 5)
        dicebutton5 = dicebutton((width / 2 + xoffset, height / 2 + yoffset), 3)
        dicebutton6 = dicebutton((width / 2 + xoffset, height / 2 - yoffset), 6)

        self.funcbuttons = [quitbutton]
        self.setbuttons = []
        self.dicebuttons = [dicebutton1, dicebutton2, dicebutton3, dicebutton4, dicebutton5, dicebutton6]

        if self.numberofplayers == 1:
            playerpanel1 = playerpanel('player1', (100, height / 2), 0)
            self.playerpanels = [playerpanel1]

        if self.numberofplayers == 2:
            playerpanel1 = playerpanel('player1', (100, height / 2 + 100), 0)
            playerpanel2 = playerpanel('player2', (100, height / 2 - 200), 0)
            self.playerpanels = [playerpanel1, playerpanel2]

    def renewdice(self,screen):
        for db in self.dicebuttons:
            db.fixed    = 'active'
            db.face     = randint(1,6)
            
            db.draw(screen)
    
    def get_playernumber(self):
        numberofplayers = 1
        setbuttons = self.setbuttons
        for j in range(len(setbuttons)):
            if setbuttons[j].plnumberset == True:
                numberofplayers = j
                break
        self.numberofplayers = numberofplayers
    
    def draw(self,screen):
        for b1 in self.funcbuttons:
            b1.draw(screen)
        for b2 in self.setbuttons:
            b2.draw(screen)
        for j3,b3 in enumerate(self.dicebuttons):
            b3.draw(screen)
        for pp in self.playerpanels:
            pp.draw(screen)

    def nextturn(self):

        for j,pp in enumerate(self.playerpanels):
            if pp.active == True:
                activeindex=j
                break
        self.playerpanels[activeindex].changeclr()
        self.playerpanels[activeindex].active=False
        if activeindex == self.numberofplayers-1:
            activeindex = 0
        else:
            activeindex+=1

        self.playerpanels[activeindex].changeclr()
        self.playerpanels[activeindex].active = True