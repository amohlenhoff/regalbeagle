# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 17:04:09 2016

@author: developer
"""

import random
import winsound
import time
import os
from PyQt4 import QtCore, QtGui, uic
import sys
import Queue

class SoundPlayer(QtCore.QObject):
    
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.soundQueue = Queue.Queue()
        self.playing = True
        self.currentSound = None
        self.workerThread = QtCore.QThread()
        self.moveToThread(self.workerThread)
        self.workerThread.start()
        
    @QtCore.pyqtSlot()
    def startWork(self):
        while self.playing:
            if self.currentSound == None:
                if not self.soundQueue.empty():
                    self.currentSound = QtGui.QSound(self.soundQueue.get())
                    self.currentSound.setLoops(1)
                    self.currentSound.play()
            else:
                if self.currentSound.isFinished():
                    self.currentSound = None
            time.sleep(0.25)
            
    def playSound(self, fileName):
        self.soundQueue.put(fileName)

projectRoot = os.path.dirname(__file__)
sp = SoundPlayer()
def PlayStall(stallNum):
    if stallNum == 1:
        sp.playSound(projectRoot + '/stalling/ahright.wav')
        #QtGui.QSound.play(projectRoot + '/stalling/ahright.wav')
    elif stallNum == 2:
        sp.playSound(projectRoot + '/stalling/difficult.wav')
        #QtGui.QSound.play(projectRoot + '/stalling/difficult.wav')  
    elif stallNum == 3:
        sp.playSound(projectRoot + '/stalling/itsallhere.wav')
        #QtGui.QSound.play(projectRoot + '/stalling/itsallhere.wav') 
    elif stallNum == 4:
        sp.playSound(projectRoot + '/stalling/rightok.wav')
        #QtGui.QSound.play(projectRoot + '/stalling/rightok.wav')  
    else:
        sp.playSound(projectRoot + '/stalling/wheretoputyou.wav')
        #QtGui.QSound.play(projectRoot + '/stalling/wheretoputyou.wav')          
        
def PlayHouse(HouseName):
    '''if HouseName == 'Gryffindor':
        winsound.PlaySound(projectRoot + '/houses/gryffindor.wav', winsound.SND_FILENAME)
        #winsound.PlaySound('C:/Users/Developer/Desktop/SortingHat/houses/gryffindor.wav', winsound.SND_FILENAME)
    elif HouseName == 'Ravenclaw':
        winsound.PlaySound(projectRoot + '/houses/ravenclaw.wav', winsound.SND_FILENAME)        
        #winsound.PlaySound('C:/Users/Developer/Desktop/SortingHat/houses/ravenclaw.wav', winsound.SND_FILENAME)
    elif HouseName == 'Hufflepuff':
        winsound.PlaySound(projectRoot + '/houses/hufflepuff.wav', winsound.SND_FILENAME)
        #winsound.PlaySound('C:/Users/Developer/Desktop/SortingHat/houses/hufflepuff.wav', winsound.SND_FILENAME)
    else:
        winsound.PlaySound(projectRoot + '/houses/slytherin.wav', winsound.SND_FILENAME)
        #winsound.PlaySound('C:/Users/Developer/Desktop/SortingHat/houses/slytherin.wav', winsound.SND_FILENAME)'''
        
def PlayKnow(KnowNum):
    if KnowNum == 0:
        time.sleep(0)
    elif KnowNum == 1:
        sp.playSound(projectRoot + '/know/iknow.wav')
        #QtGui.QSound.play(projectRoot + '/know/iknow.wav')
    else:
        sp.playSound(projectRoot + '/know/iknowjustwhattodo.wav')
        #QtGui.QSound.play(projectRoot + '/know/iknowjustwhattodo.wav')

'''   
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Sorting Hat", None))
        self.sorts_girls_btn.setText(_translate("Dialog", "Let the Sorting Begin...", None))
        self.sorts_girls_btn.clicked.connect(self.SortGirls)

    def SortGirls(self):
        for i in range(number_of_girls):
            
'''

def SortButton():
    global girl_index
    print 'sort button'
    PlayStall(random_stalls[girl_index])
    time.sleep(1)
    PlayKnow(iknows_random[girl_index])
    time.sleep(0.25)
    PlayHouse(girls[girl_index])
    time.sleep(3) 
    girl_index += 1

if __name__ == '__main__':
    number_of_girls = input("How many girls are in the camp? ")
    houses = ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']
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
    
    print girls   
    print random_stalls
    print iknows_random
    
    app = QtGui.QApplication(sys.argv)
    timer = QtCore.QTimer()
    timer.timeout.connect(sp.startWork)
    timer.start(0)
    win = uic.loadUi('UI/GUI.ui')
    win.sorts_girls_btn.clicked.connect(SortButton)    
    
    win.show()    
    sys.exit(app.exec_())