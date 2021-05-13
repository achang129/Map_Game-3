__author__ = 'Abrar Khandoker'

from Tkinter import *


def a():
    global score
    score += 10

def close_window2():
    print "Score from quiz: ", score
    coins.add(score)
    root.destroy()
    master.done_playing_game()

def main():
    root.title("Lord of the Rings Quiz")
    Label(root, text="Please tick your choice only and click on the submit button to submit your answers", font="Helvetica 15").grid(row=0, column=2, sticky=W + E)

    Label(root, text="Question 1: How many Rings of Power were forged in the second age?", font="Verdana 10 bold").grid(row=1, column=2, sticky=W+E)
    Checkbutton(root, text="1", command=a).grid(row=2, column=2, sticky=W+E)
    Checkbutton(root, text="19").grid(row=3, column=2, sticky=W+E)
    Checkbutton(root, text="20").grid(row=4, column=2, sticky=W+E, pady=(0, 20))

    Label(root, text="Question 2: What gift does Lady Galadriel give Gimli before the fellowship leaves Lothlorien?", font="Verdana 10 bold").grid(row=5, column=2, sticky=W + E)
    Checkbutton(root, text="Elvish rope").grid(row=6, column=2, sticky=W + E)
    Checkbutton(root, text="Three strands of her hair", command=a).grid(row=7, column=2, sticky=W + E)
    Checkbutton(root, text="A dagger").grid(row=8, column=2, sticky=W + E, pady=(0, 20))

    Label(root, text="Question 3: Gollum wasn't always Gollum. He was a hobbit of the River-folk. What was his name?", font="Verdana 10 bold").grid(row=9, column=2, sticky=W + E)
    Checkbutton(root, text="Deagol").grid(row=10, column=2, sticky=W + E)
    Checkbutton(root, text="Bandobras").grid(row=11, column=2, sticky=W + E)
    Checkbutton(root, text="Smeagol", command=a).grid(row=12, column=2, sticky=W + E, pady=(0, 20))

    Label(root, text="Question 4: Who is Shelob? A man? An elf? An ent?", font="Verdana 10 bold").grid(row=13, column=2, sticky=W + E)
    Checkbutton(root, text="A beastly spider that tries to eat Frodo and Sam", command=a).grid(row=14, column=2, sticky=W + E)
    Checkbutton(root, text="An elf queen").grid(row=15, column=2, sticky=W + E)
    Checkbutton(root, text="Uruk-hai leader").grid(row=16, column=2, sticky=W + E, pady=(0, 20))

    Label(root, text="Question 5: Gandalf is imprisoned on top of Orthanc by Saruman. Who helps him escape?", font="Verdana 10 bold").grid(row=17, column=2, sticky=W + E)
    Checkbutton(root, text="Frodo and Sam").grid(row=18, column=2, sticky=W + E)
    Checkbutton(root, text="Gwaihir", command=a).grid(row=19, column=2, sticky=W + E)
    Checkbutton(root, text="Gothmog").grid(row=20, column=2, sticky=W + E, pady=(0, 20))

    Label(root, text="Question 5: Gandalf is imprisoned on top of Orthanc by Saruman. Who helps him escape?", font="Verdana 10 bold").grid(row=17, column=2, sticky=W + E)
    Checkbutton(root, text="Frodo and Sam").grid(row=18, column=2, sticky=W + E)
    Checkbutton(root, text="Gwaihir", command=a).grid(row=19, column=2, sticky=W + E)
    Checkbutton(root, text="Gothmog").grid(row=20, column=2, sticky=W + E, pady=(0, 20))

    Button(root, text="Submit", command=close_window2).grid(row=21, column=2, sticky=W + E, pady=(0, 0), padx=(250, 250))

    root.mainloop()

class Game_3():
    def __init__(self, frame, roots, coin):
        global root
        global coins
        global master
        global score
        root = frame
        score = 0
        master = roots
        coins = coin

        main()



"""
References:
https://stackoverflow.com/questions/39555194/how-to-add-space-between-two-widgets-placed-in-grid-in-tkinter-python
"""