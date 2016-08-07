# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 17:04:09 2016

@author: developer
"""

import random
import os
import sys
from pygame import mixer

projectRoot = os.path.dirname(os.path.realpath(__file__))

def PlayBlocking(fn):
    mixer.Sound(fn).play()
    while mixer.get_busy():
        pass

def PlayStall(stallNum):
    if stallNum == 1:
        PlayBlocking(os.path.join(projectRoot, 'stalling/ahright.wav'))
    elif stallNum == 2:
        PlayBlocking(os.path.join(projectRoot, 'stalling/difficult.wav'))
    elif stallNum == 3:
        PlayBlocking(os.path.join(projectRoot, 'stalling/itsallhere.wav'))
    elif stallNum == 4:
        PlayBlocking(os.path.join(projectRoot, 'stalling/rightok.wav'))
    else:
        PlayBlocking(os.path.join(projectRoot, 'stalling/wheretoputyou.wav'))

def PlayHouse(HouseName, girlsname):
    print 'Welcome %s, to House %s!' %(girlsname, HouseName)

def PlayKnow(KnowNum):
    if KnowNum == 1:
        PlayBlocking(os.path.join(projectRoot, 'know/iknow.wav'))
    elif KnowNum == 2:
        PlayBlocking(os.path.join(projectRoot,'know/iknowjustwhattodo.wav'))

if __name__ == '__main__':
    mixer.init()

    number_of_girls = input("How many girls are in the camp? ")
    #number_of_girls = int(sys.argv[1])
    houses = ['Hopper', 'Lovelace', 'Borg', 'Fried']
    girls = []
    stalls = [1, 2, 3, 4, 5]
    random_stalls = []
    iknows = [0, 1, 2]
    iknows_random = []
    girl_index = 0

    for i in range(number_of_girls):
        girls.append(houses[i%len(houses)])
        random_stalls.append(stalls[i%len(stalls)])
        iknows_random.append(iknows[i%len(iknows)])
    random.shuffle(girls)
    random.shuffle(random_stalls)
    random.shuffle(iknows_random)

    #print girls
    #print random_stalls
    #print iknows_random

    for i in range(number_of_girls):
        name = raw_input("What is your name campee? ")
        PlayStall(random_stalls[i])
        PlayKnow(iknows_random[i])
        PlayHouse(girls[i], name)
    #print 'done'
