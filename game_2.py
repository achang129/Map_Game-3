__author__ = 'Arjun Pillai'

import time
import random # Used to generate random system failures and number of enemies
from Tkinter import *



class Game_2():
    def __init__(self, frame, roots, coin):
        global root
        global master
        global coins
        root = frame
        root.title("DEFEND THE CASTLE")
        master = roots
        coins = coin
        main()

def fireCommand():
    global enemyCount, firedStatus, readyStatus, point
    if firedStatus == False and readyStatus == True:
        topLabel.configure(text="FIRING!")
        point += 1
        test.delete(0, END)
        test.insert(0, str(point))
        enemyCount -= 3
        if enemyCount < 0:
            enemyCount = 0
        enemyCounter.delete(0, END)
        enemyCounter.insert(0, enemyCount)
        firedStatus = True
        readyStatus = False
        fireButton.config(state=DISABLED)
        reloadButton.config(state=NORMAL)
        #enemyCount+=4
        print enemyCount
        enemyCounter.delete(0,END)
        enemyCounter.insert(0, str(enemyCount))
        enemyIncrease()


def reloadCommand():
    global firedStatus, readyStatus
    print "clicked"
    if firedStatus == True and readyStatus == False:
        topLabel.config(text="RELOADING!")
        countdown(3)
        firedStatus = False
        readyStatus = True
        topLabel.config(text="READY TO FIRE AGAIN!")
        enemyIncrease()
        reloadButton.config(state=DISABLED)
        fireButton.config(state=NORMAL)


def damageTaken():
    global enemyCount, healthBar
    if enemyCount % 5 >= 0 and enemyCount % 5 <=3 and enemyCount != 0:
        healthBar -= 5
        if healthBar <= 0:
            healthBar=0
            fireButton.config(state=DISABLED)
            reloadButton.config(state=DISABLED)
            coins.add(int(test.get()) * 10)
            topLabel.config(text='The Orcs have won....')
            enemyCountLabel.config(text='DONE')
    healthSummary.delete(0, END)
    healthSummary.insert(0, str(healthBar))

def randError():
    global healthBar
    probability= random.randint(1,100)
    if probability<=15:
        healthBar-=8
        healthSummary.delete(0,END)
        healthSummary.insert(0, str(healthBar))
    return



def countdown(n):
    if n == 0:
        timerCount.delete(0, END)
        timerCount.insert(0, 'READY TO FIRE!')
        return
    else:
        print n
        timerCount.delete(0, END)
        timerCount.insert(0, n)
        randError()
        time.sleep(1)
        countdown(n-1)
        #root.after(1000, countdown(n-1))



def enemyIncrease():
    global enemyCount
    num = random.randint(2,5)
    enemyCount+=num
    enemyCountLabel.delete(0, END)
    enemyCountLabel.insert(0, str(enemyCount))
    damageTaken()

def reset():
    global enemyCount
    global firedStatus
    global readyStatus
    firedStatus = False
    readyStatus = True
    if healthBar <= 0:
        fireButton.config(state=DISABLED)
        reloadButton.config(state=DISABLED)
        coins.add(int(test.get()) * 10)
        topLabel.config(text='The Orcs have won....')
        enemyCountLabel.config(text='DONE')
        return



def main():
    global canvas1
    canvas1 = Canvas(root, width=640, height=480, bg = "blue")
    canvas1.grid(row=1, columnspan=4)

    catapult = PhotoImage(file = 'data/catapult.gif')
    canvas1.create_image(250, 2+500-226, image=catapult, anchor=CENTER)

    global firedStatus
    global readyStatus
    global healthBar
    global enemyCount
    global point
    firedStatus = False  # hasn't fired yet
    readyStatus = True  # ready to fire
    healthBar = 100
    enemyCount = 1
    point = 0

    global enemyCountLabel
    enemyCountLabel = Entry(root, justify=CENTER)
    enemyCountLabel.grid(row=3, column=0)
    enemyCountLabel.delete(0, END)
    enemyCountLabel.insert(0, str(enemyCount))
    Label(root, text="Enemy Count").grid(row=2, column=0)

    global fireButton
    fireButton = Button(root, text='FIRE!', command=fireCommand)
    fireButton.grid(row=2, column=3)

    global reloadButton
    reloadButton = Button(root, text='RELOAD!', command=reloadCommand)
    reloadButton.grid(row=3, column=3)

    global countDownLabel
    countDownLabel = Entry(root, justify=CENTER)
    countDownLabel.grid(row=3, column=1)

    global timerCount
    timerCount = Entry(root, justify=CENTER)
    timerCount.grid(row=3, column=2)
    timerCount.delete(0, END)
    timerCount.insert(0, 'test')
    Label(root, text="Timer").grid(row=2, column=1)

    global healthSummary
    Label(root, text="Health").grid(row=2, column=2)
    healthSummary = Entry(root, justify=CENTER)
    healthSummary.grid(row=3, column=2)
    healthSummary.delete(0, END)
    healthSummary.insert(0, str(healthBar))

    global enemyCounter
    enemyCounter = Entry(root, justify=CENTER)
    enemyCounter.grid(row=3, column=0)

    global topLabel
    topLabel = Label(root, text="HELP DEFEND THE CASTLE, AN ORC ARMY IS APPROACHING!!", bg='red')
    topLabel.grid(row=0, columnspan=4)

    global test
    test = Entry(root, justify= CENTER)
    test.grid(row=4, column=2)
    Label(root, text = "Points:").grid(row=4, column=1)

    done = Button(root, text="END GAME", command = master.done_playing_game)
    done.grid(row=5)


    root.mainloop()