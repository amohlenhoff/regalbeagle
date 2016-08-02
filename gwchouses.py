# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 17:04:09 2016

@author: developer
"""

import random
import winsound
import time
import os

projectRoot = os.path.dirname(__file__)
def PlayStall(stallNum):
    if stallNum == 1:
        #winsound.PlaySound('C:/Users/Developer/Desktop/SortingHat/stalling/ahright.wav', winsound.SND_FILENAME)
        winsound.PlaySound(projectRoot + '/stalling/ahright.wav', winsound.SND_FILENAME)
    elif stallNum == 2:
        winsound.PlaySound(projectRoot + '/stalling/difficult.wav', winsound.SND_FILENAME)
       # winsound.PlaySound('C:/Users/Developer/Desktop/SortingHat/stalling/difficult.wav', winsound.SND_FILENAME)
    elif stallNum == 3:
        winsound.PlaySound(projectRoot + '/stalling/itsallhere.wav', winsound.SND_FILENAME)
        #winsound.PlaySound('C:/Users/Developer/Desktop/SortingHat/stalling/itsallhere.wav', winsound.SND_FILENAME)
    elif stallNum == 4:
        winsound.PlaySound(projectRoot + '/stalling/rightok.wav', winsound.SND_FILENAME)
        #winsound.PlaySound('C:/Users/Developer/Desktop/SortingHat/stalling/rightok.wav', winsound.SND_FILENAME)
    else:
        winsound.PlaySound(projectRoot + '/stalling/wheretoputyou.wav', winsound.SND_FILENAME)
        #winsound.PlaySound('C:/Users/Developer/Desktop/SortingHat/stalling/wheretoputyou.wav', winsound.SND_FILENAME)
        
def PlayHouse(HouseName):
    if HouseName == 'Hopper':
        print 'Welcome to House Hopper %s!' % (name)
    elif HouseName == 'Lovelace':
        print 'Welcome to House Lovelace %s!' % (name)
    elif HouseName == 'Borg':
        print 'Welcome to House Borg %s!' % (name)
    else:
        print 'Welcome to House Fried %s!' % (name)
        
def PlayKnow(KnowNum):
    if KnowNum == 0:
        time.sleep(0)
    elif KnowNum == 1:
        winsound.PlaySound(projectRoot + '/know/iknow.wav', winsound.SND_FILENAME)
        #winsound.PlaySound('C:/Users/Developer/Desktop/SortingHat/know/iknow.wav', winsound.SND_FILENAME)
    else:
        winsound.PlaySound(projectRoot + '/know/iknowjustwhattodo.wav', winsound.SND_FILENAME)
        #winsound.PlaySound('C:/Users/Developer/Desktop/SortingHat/know/iknowjustwhattodo.wav', winsound.SND_FILENAME)
        
        
number_of_girls = input("How many girls are in the camp? ")
houses = ['Hopper', 'Lovelace', 'Borg', 'Fried']
girls = []
stalls = [1, 2, 3, 4, 5]
random_stalls = []
iknows = [0, 1, 2]
iknows_random = []
names = []

for i in range(number_of_girls):
    girls.append(houses[i%len(houses)])
    random_stalls.append(stalls[i%len(stalls)])
    iknows_random.append(iknows[i%len(iknows)])
random.shuffle(girls)
random.shuffle(random_stalls) 
random.shuffle(iknows_random)

print girls   
print random_stalls
print iknows_random

for i in range(number_of_girls):
    name = raw_input("What is your name campee? ")
    names.append(name[i])
    PlayStall(random_stalls[i])
    time.sleep(1)
    PlayKnow(iknows_random[i])
    time.sleep(0.25)
    PlayHouse(girls[i])
    time.sleep(3) 

from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    def __init__(self):
	QtGui.QWidget.__init__(self)
	self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(584, 384)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.sorts_girls_btn = QtGui.QPushButton(Dialog)
        self.sorts_girls_btn.setObjectName(_fromUtf8("sorts_girls_btn"))
        self.verticalLayout.addWidget(self.sorts_girls_btn)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Sorting Hat", None))
        self.sorts_girls_btn.setText(_translate("Dialog", "Let the Sorting Begin...", None))
        self.sorts_girls_btn.clicked.connect(self.SortGirls)

    def SortGirls(self):
        for i in range(number_of_girls):
            PlayStall(random_stalls[i])
            time.sleep(1)
            PlayKnow(iknows_random[i])
            time.sleep(0.25)
            PlayHouse(girls[i])
            time.sleep(3) 

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())
        

    
    