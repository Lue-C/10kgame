# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:10:39 2021

@author: xepml
"""

from breezypythongui import EasyFrame
import time
from tkinter import *

class player(object):
    def __init__(self):
        self.points = 0
        self.temppoints = 0
        self.name = None
        
    def nameplayer(self,name):
        self.name = name
    def addpoints(self,points):
        self.points += points
    def addtemppoints(self,temppoints):
        self.temppoints += temppoints

class DiceGenerator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, "Dice Generator")
        self.setResizable(True)
        self.setBackground('#6D8DB9')
        self.addLabel(text = 'Dice Generator', row = 0,
                      column = 0, columnspan = 2, background = '#6D8DB9')
        self.generate = self.addButton(text = 'Go!', row = 2,
                                       column = 0, columnspan = 2)
        self.generate = self.addButton(text = 'Quit', row = 3,
                                       column = 0, columnspan = 2,
                                       command = self.quitprog)
        self.generate.configure(width = 10)
    
    def quitprog(self):
#        self.quit()
        self.master.destroy()
    
    def generate(self):
        'This is where I am attempting the animation'

#        for i in range(20):
#
#            time.sleep(.1)
#            self.image1.configure(file = 'd' + str(x1) + '.png')
#            self.image2.configure(file = 'd' + str(y1) + '.png')
#            self.image1.configure(dice.dice1())
#            self.image2.configure(dice.dice1())
#            self.update()


def main():
    DiceGenerator().mainloop()

if __name__ == '__main__':
    main()