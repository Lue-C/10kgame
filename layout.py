# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 14:16:43 2021

@author: xepml
"""

from random import randint
import pygame
import numpy as np

white = [255, 255, 255]


class button:
    def __init__(self, position, size, clr=[100, 100, 100], cngclr=None, func=None, text='', font="Segoe Print",
                 font_size=16, font_clr=[0, 0, 0]):
        self.clr = clr
        self.size = size
        self.func = func
        self.surf = pygame.Surface(size)
        self.rect = self.surf.get_rect(center=position)

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
        self.mouseover()

        self.surf.fill(self.curclr)
        self.surf.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surf, self.rect)

    def mouseover(self):
        #print('mouseover')
        self.curclr = self.clr
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.curclr = self.cngclr

    def call_back(self, *args):
        #        print(self.clr)
        if self.func:
            return self.func(*args)


class gamebutton:
    def __init__(self, position, size, clr=[80, 80, 20], cngclr=None, func=None, text='', font="Segoe Print",
                 font_size=16, font_clr=[0, 0, 0]):
        self.clr = clr
        self.size = size
        self.func = func
        self.surf = pygame.Surface(size)
        self.rect = self.surf.get_rect(center=position)
        self.curclr = clr

        self.activeclr = [180, 180, 100]
        self.passiveclr = clr

        #### for additional transparency parameter
        if len(clr) == 4:
            self.surf.set_alpha(clr[3])

        self.font = pygame.font.SysFont(font, font_size)
        self.txt = text
        self.font_clr = font_clr
        self.txt_surf = self.font.render(self.txt, 1, self.font_clr)
        self.txt_rect = self.txt_surf.get_rect(center=[wh // 2 for wh in self.size])

    def draw(self, screen):
        self.mouseover()

        self.surf.fill(self.curclr)
        self.surf.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surf, self.rect)

    def mouseover(self):
        self.curclr = self.clr

    #        pos = pygame.mouse.get_pos()
    #        if self.rect.collidepoint(pos):
    #            self.curclr = self.cngclr

    def call_back(self, *args):
        #        print(self.clr)
        if self.func:
            return self.func(*args)


class text:
    def __init__(self, text, position, size, clr=[100, 100, 100], cngclr=None, func=None, font="Segoe Print",
                 font_size=16, font_clr=[0, 0, 0]):
        self.clr = clr
        self.curclr = (200, 0, 0)
        self.size = size
        self.func = func
        self.surf = pygame.Surface(size)
        self.rect = self.surf.get_rect(center=position)

        self.activeclr = [180, 180, 100]
        self.passiveclr = clr

        if len(clr) == 4:
            self.surf.set_alpha(clr[3])

        self.font = pygame.font.SysFont(font, font_size)
        self.txt = text
        self.font_clr = font_clr
        self.txt_surf = self.font.render(self.txt, 1, self.font_clr)
        self.txt_rect = self.txt_surf.get_rect(center=[wh // 2 for wh in self.size])

    def draw(self, screen):
        #        self.mouseover()

        self.surf.fill(self.curclr)
        self.surf.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surf, self.rect)

    def updatetext(self, newtext):
        self.txt = newtext
        self.txt_surf = self.font.render(self.txt, 1, self.font_clr)


def all_zero(liste):
    length = len(liste)
    counter = 0
    for j in range(length):
        if liste[j] == 0:
            counter += 1
    if counter == length:
        return True
    else:
        return False

def all_one(liste):
    length = len(liste)
    counter = 0
    for j in range(length):
        if liste[j] == 1:
            counter += 1
    if counter == length:
        return True
    else:
        return False


def validfixedsetv2(diceset):
    msg = ''

    points = 0
    numbers = np.zeros((6), dtype=int)
    for dice in diceset:
        numbers[dice.face - 1] += 1
    ### check for streets
    if len(diceset) > 4:
        if len(diceset) == 6 and all_one(numbers) == 1:
            msg = 'longstreet'
            return True, 1000, msg

        if len(diceset) == 5:
            if numbers[0] == 0:
                if all_one(numbers[1:]) == 1:
                    points += 500
                    msg = 'smallstreet1'
                    numbers[1:6] = 0

            elif numbers[5] == 0:
                if all_one(numbers[0:5]) == 1:
                    points += 500
                    msg = 'smallstreet2'
                    numbers[0:5] = 0

    if len(numbers) != 0:
        if numbers[0] == 6:
            msg = 'pasch1'
            return True, 8000
        if numbers[0] == 5:
            points += 4000
            msg = 'pasch2'
            numbers[0] = 0
        if numbers[0] == 4:
            points += 2000
            msg = 'pasch3'
            numbers[0] = 0
        if numbers[0] == 3:
            points += 1000
            msg = 'pasch4'
            numbers[0] = 0

        for j in range(1, 6):
            if numbers[j] == 6:
                msg = 'pasch5'
                return 8 * 100 * (j + 1)
            if numbers[j] == 5:
                msg = 'pasch6'
                points += 4 * 100 * (j + 1)
                numbers[j] = 0
            if numbers[j] == 4:
                msg = 'pasch7'
                points += 2 * 100 * (j + 1)
                numbers[j] = 0
            if numbers[j] == 3:
                msg = 'pasch8'
                points += 100 * (j + 1)
                numbers[j] = 0

        if numbers[0] != 0:
            points += 100 * numbers[0]
            numbers[0] = 0

        if numbers[4] != 0:
            points += 50 * numbers[4]
            numbers[4] = 0

    print(numbers)
    if all_zero(numbers):
        return True, points, msg
    if not all_zero(numbers):
        return False, points, msg


class dice:
    def __init__(self, face):
        self.face = face

    def roll(self):
        self.dice = randint(1, 6)


class playerpanel:
    def __init__(self, name, position, angle, bgcolor=white, textcolor=(100, 100, 100)):

        self.name = name
        self.position = position
        self.active = False
        self.points = 0
        self.temppoints = 0
        self.info = ''

        self.angle = angle
        self.bgcolor = bgcolor
        self.buttonsize = (100, 60)
        self.txt_clr = textcolor
        self.activetxtclr = textcolor
        self.activeclr = (150, 150, 100)

        activecol = [180, 180, 100]
        passivecol = [80, 80, 20]
        #        self.active     = False

        xpos = self.position[0]
        ypos = self.position[1]

        panelwidth = 200
        panelheight = 250

        ### player info on top
        self.uppertext = text(self.name, (xpos, ypos - 120), (panelwidth, 40), self.txt_clr)
        self.lowertext = text(str(self.points) + '   +   ' + str(self.temppoints), (xpos, ypos - 60), (panelwidth, 40))

        ### infotext in center
        self.infotext = text(self.info, (xpos, ypos), (panelwidth, 40), self.txt_clr)

        ### buttons below info
        self.rollbutton = gamebutton((xpos - 60, ypos + 60), self.buttonsize, func=self.rolldice, text='roll dice')
        self.stopbutton = gamebutton((xpos + 60, ypos + 60), self.buttonsize, func=self.pointupdate, text='stop move')

        self.objects = [self.uppertext, self.lowertext, self.infotext, self.rollbutton, self.stopbutton]

        if self.active == True:
            self.info = 'It is your turn!'

        if self.active == False:
            self.info = 'It is not your turn!'

    def changename(self, newname):
        self.name = newname

    def changeclr(self):

        for obj in self.objects:
            if self.active:
                obj.curclr = obj.passiveclr
            if not self.active:
                obj.curclr = obj.activeclr

    def pointupdate(self, dicebuttons):
        #        print (self.player.points,self.player.temppoints)
        print('pppoints')

        curdice = []
        fixeddice = []
        permdice = []
        for db in dicebuttons:
            if db.fixed == 'active':
                curdice.append(db)
            if db.fixed == 'fixed':
                fixeddice.append(db)
            if db.fixed == 'permanent':
                permdice.append(db)

        settest = validfixedsetv2(fixeddice)

        addpoints2 = 0
        if settest[0]:
            addpoints2 = settest[1]
        # print(addpoints2)
        self.addpoints(addpoints2)
        self.temppoints = 0
        self.lowertext.updatetext(str(self.points) + '   +   ' + str(self.temppoints))
        self.changeclr()
        # self.active = False

    def rolldice(self, dicebuttons, diceset, screen):

        self.info = ''  # clear infopanel

        ### get current dice configuration
        curdice = []
        fixeddice = []
        permdice = []
        for db in dicebuttons:
            if db.fixed == 'active':
                curdice.append(db)
            if db.fixed == 'fixed':
                fixeddice.append(db)
            if db.fixed == 'permanent':
                permdice.append(db)

        settest = validfixedsetv2(fixeddice)
        if len(curdice) == 6:
            self.info = 'choose dice'
        if settest[1] == 0:
            self.info = 'no valid set'
        if settest[0] == True and settest[1] != 0:
            self.addtemppoints(settest[1])
            self.lowertext.updatetext(str(self.points) + '   +   ' + str(self.temppoints))

            for db in fixeddice:
                db.fixed = 'permanent'

            if len(fixeddice + permdice) == 6:

                for d in fixeddice + permdice:
                    d.fixed = 'active'
                    d.face = randint(1, 6)
                    d.draw(screen)
            else:
                for db in curdice:
                    db.face = randint(1, 6)
                settest2 = validfixedsetv2(curdice)

                if settest2[1] == 0:
                    numbers = np.zeros((6))
                    for cd in curdice:
                        numbers[cd.face - 1] += 1
                    print(numbers, 'you are fucked')
                    self.temppoints = 0
                    # self.active = False

        self.lowertext.updatetext(str(self.points) + '   +   ' + str(self.temppoints))
        self.infotext.updatetext(self.info)

    def draw(self, screen):
        #        screen.fill(self.bgcolor,self.uppertext.txt_surf.get_rect())
        self.uppertext.draw(screen)
        self.lowertext.draw(screen)
        self.infotext.draw(screen)
        self.rollbutton.draw(screen)
        self.stopbutton.draw(screen)

    def addpoints(self, addedpoints):
        self.points += self.temppoints + addedpoints

    def addtemppoints(self, points):
        self.temppoints += points
