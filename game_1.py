__author__ = 'Brandon Liston'
from Tkinter import *
import random
guesses = 15 #Number of guesses for word guess


## -----------------------------------All Tkinter Initializing Objects Below--------------------------------------
class Game_1():
    def __init__(self, frame, root, coins): ##frame for game, and
        global guesses
        self.CV_Height = 480
        self.CV_Width = 640
        self.master = frame

        self.coins = coins #Coins for the class

        word_list = open("./Data/Word_Search_word.txt")
        words = word_list.readlines()
        self.Guess_Word = random.choice(words)   ## Define Guess_Word from random import of word list
        self.Guess_Word = self.Guess_Word.replace("\n", "") ##Strip from next lines in word

        self.letters_to_guess = []   ##All Letter to Guess by user (3 unique)
        self.Stripped_Word = self.Guess_Word      ##New Stripped word.replaced(...,"-")
        for i in range(0,3):
            letter = random.choice(self.Stripped_Word)
            while letter == "-":
                letter = random.choice(self.Stripped_Word)
            self.letters_to_guess.append(letter)
            self.Stripped_Word = self.Stripped_Word.replace(self.letters_to_guess[i], "-")


        ###---------------------START Tkinter Objects-----------------------------------------

        self.gameImage = PhotoImage(file = "Data/smeagol_game.gif")
        self.wonImage = PhotoImage(file = "Data/smeagol_lost.gif")           ##Game Photos for: in game, lost, won
        self.lostImage = PhotoImage(file = "Data/smeagol_won.gif")


        self.TopLabel = Label(self.master, text = " Enter a single letter guess below! ", bg = "green")   ##Top Bar, display Game 1 info
        self.TopLabel.grid(row=0, columnspan=2, sticky="EW")

        self.coverImage = Label(self.master, image = self.gameImage, bg = "black")
        self.coverImage.grid(row=1, column = 0, columnspan = 2)

        self.word = Label(self.master, text = self.Stripped_Word, font = ("Ariel", 50))        ##Word to Guess Label
        self.word.grid(row=2, column=0)


        self.Guess_Button = Button(self.master, text = " Guess: ", command = self.Guess_function)
        self.Guess_Button.grid(row=3, column=0)                  ##Guess Label, w/ Guess Entry
        self.user_guess = Entry(self.master)
        self.user_guess.grid(row=3, column=1)


        self.GUESSES = Label(self.master, text = " Remaining Guesses ")
        self.GUESSES.grid(row=4, column = 0)
        self.remainingGuesses = Label(self.master, text = guesses, bg = "white")
        self.remainingGuesses.grid(row=4, column = 1, sticky = "EW")

        self.done = Button(self.master, text="END GAME", state = DISABLED, command = root.done_playing_game)
        self.done.grid(row = 5)

        #print self.Guess_Word #FOR TESTING



        ###---------------------STOP Tkinter Objects-----------------------------------------



    def Guess_function(self):
        global guesses
        guesses -= 1
        self.remainingGuesses.configure(text = str(guesses))


        temp_Guess = (self.user_guess.get()).upper()
        self.user_guess.delete(0, END)
        temp_indexes = []   ##Used to see where to replace "-" with "<char>"

        if len(temp_Guess) > 1:
            self.TopLabel.configure(text = " Please enter only one letter at a time, a count has been recorded ", bg = "red")
        elif len(temp_Guess) == 0:
            self.TopLabel.configure(text = " Please enter one letter, a count has been recorded ", bg = "red")
        else:
            if temp_Guess in self.letters_to_guess: ##IF GUESSED LETTER IS IN letters to guess array
                self.TopLabel.configure(text=(" Youve entered a found letter, '%s'! " % temp_Guess), bg="green")
                temp_actual_word = list(self.Guess_Word)
                while self.Guess_Word.find(temp_Guess) != (-1):
                    temp_indexes.append(self.Guess_Word.find(temp_Guess))
                    temp_actual_word[temp_indexes[-1]] = " "
                    self.Guess_Word = ''.join(temp_actual_word)
                for n in temp_indexes:          #### FOR RESTORING APEEARING STRIPPED WORD
                    temp_strip = list(self.Stripped_Word)
                    temp_strip[n] = temp_Guess
                    self.Stripped_Word = ''.join(temp_strip)


                self.word.configure(text = self.Stripped_Word) ##Update word with found letter
            else:
                self.TopLabel.configure(text=" You did not enter a found letter. ", bg="red")


        if "-" in self.Stripped_Word:
                if guesses == 0:
                    self.TopLabel.configure(text=" You lost Game 1, Click 'END GAME' to exit ", bg="orange")
                    self.coverImage.configure(image = self.lostImage)
                    self.done.configure(state=NORMAL)
                    self.Guess_Button.configure(state=DISABLED)
        else:
            ##Game Beaten
            print guesses
            self.coins.add(guesses * 10)
            self.TopLabel.configure(text=" You beat Game 1! Click 'END GAME' to exit. ", bg="blue")
            self.coverImage.configure(image=self.wonImage)
            self.done.configure(state = NORMAL)
            self.Guess_Button.configure(state = DISABLED)
