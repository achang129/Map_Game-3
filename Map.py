__author__ = 'Brandon Liston'
""""
MAIN CLASS, RUN FROM MAP TO START GAME
"""

from Tkinter import *
from game_1 import Game_1              ##Import All Games
from game_2 import Game_2
from game_3 import Game_3
from game_4 import Game_4
from Coins_Class import coin_tracker        ##Import Coins Clas
import pickle

#s = {"Sally": 10, "Me": 10, "B": 15, "C": 20, "D": 55, "E": 50, "F": 1, "Test": 9, "Carmina": 100, "Last": -1, "Next": 0}
#pickle.dump(s, open("Data/Leaderboard.p", "wb"))

game_spots = [[[150, 250], [70, 170], False], [[315, 415], [5, 100], False], [[450, 550], [10, 110], False], [[280, 380], [215, 315], False], [[460, 560], [300, 400], False]] # Create tuple of all game locations, sequential order based on travel
                                                    # 5 total cords. for 5 games
                                                    # False statements to initialize games haven't been played yet, no multi-playing each game
range = [False,False,False,False,False] ##Used for slecting game on range, works with game_spots var.
coins = coin_tracker()
global Name #set Name for player, if none will not store to leaderboard


## -----------------------------------All Tkinter Initializing Objects Below--------------------------------------(all placed in __init__)
class Master_Class:

    def __init__(self, master):
        self.CV_Height = 480
        self.CV_Width = 640  ##Dimensions of Canvas

        self.master = master ##MASTER FRAME

        self.w = Canvas(self.master, width=self.CV_Width, height=self.CV_Height, bg="lightblue")
        self.w.grid()


        self.Map_Background = PhotoImage(file="Data/middle_Earth.gif")
        self.ring_image = PhotoImage(file="Data/ring.gif")


        print "\nWidth: ", self.Map_Background.width()
        print "\nHeight: ", self.Map_Background.height()
        self.w.create_image(0,0,image=self.Map_Background, anchor = NW)
        self.w.grid(row=1, column=0, columnspan=3)                       #w SETS THE BACKGROUND MAP/CANVAS with "w.create_image"

        self.ring_Id = self.w.create_image(60, 265, image = self.ring_image, anchor = NW) ##Starting Ring Cords. (60, 265)

        self.TopLabel = Label(self.master, text = " Welcome to your Journey Taveler! ", bg = "white")   ##Top Bar, display info to traveler
        self.TopLabel.grid(row=0, column=0, columnspan=3, sticky="EW")

        self.player_score = Label(self.master, text = "Player Coins")
        self.player_score.grid(row=2, column=2, columnspan=2)
        self.score = Label(self.master, justify=CENTER, width=20, text = 0, bg = "white")         ##Player Score Label and Entry
        self.score.grid(row=3, column=2)

        self.start_end_button = Button(self.master, text="START JOURNEY", command=self.start_game)     ##START / END Button for Game
        self.start_end_button.grid(row=2, column=0)


        self.play_game = Button(self.master, text="Play Game")
        self.play_game.grid(row=2, column=1)
        self.play_game.configure(state=DISABLED)

        self.name_entry = Entry(self.master, justify=CENTER)
        self.name_entry.grid(row=3, column=0) ##Name for leaderboard to display
        self.name_entry.insert(0, "NAME")

        self.Leaderboard_Button = Button(self.master, text="Leaderboard", command=self.leaderboard, state = DISABLED)
        self.Leaderboard_Button.grid(row=3, column=1)



## -----------------------------------All Tkinter Initializing Objects Above--------------------------------------

    def start_game(self): #Start Game, based on location
        global Name
        self.TopLabel.configure(text="YOUR JOURNEY HAS STARTED, TRAVEL TO THE FIRST LOCATION WITH THE MOVE BUTTON", bg="red")
        self.start_end_button.configure(text="END JOURNEY", bg= "red", command=self.end_game)
        self.w.bind("<Button-1>", self.move_ring)
        Name = self.name_entry.get() ## Set name for later Leaderboard upload
        self.name_entry.configure(state = DISABLED)
        self.Leaderboard_Button.configure(state = NORMAL)

    def end_game(self):
        global Name
        global coins
        self.start_end_button.configure(state=DISABLED)
        self.play_game.configure(state=DISABLED)
        self.Leaderboard_Button.configure(state=DISABLED)

        self.TopLabel.configure(text="Thanks for travelling", bg= "white")


        ## ===== Leaderboard Update ====>
        if len(Name) > 0: ##Only store if user has entered name
            leaders = pickle.load( open( "Data/Leaderboard.p", "rb" ) )
            total = coins.return_total()
            leaders.update({Name: total})      ##LOADS, DUMPS, SORTS, AND TRIMS TO 10 OF TOP ON LEADERBOARD
            temp_keys = leaders.keys()
            temp_keys.sort(key = lambda x: leaders[x], reverse = True)
            print "Keys: ", temp_keys

            Leaders_10 = dict()
            counter = 0
            for keys in temp_keys:
                Leaders_10.update({keys:leaders[keys]})
                counter += 1
                if counter > 10:
                    break

            print Leaders_10
            pickle.dump(Leaders_10, open("Data/Leaderboard.p", "wb") ) #Dump data back into file





    def leaderboard(self):
        global game_master

        leaders = pickle.load(open("Data/Leaderboard.p", "rb"))
        self.playing_game()

        game_master = Toplevel(self.master)

        Label(game_master, text = "Players", justify = CENTER).grid(row = 0, column = 0)
        Label(game_master, text = "Coins", justify = CENTER).grid(row = 0, column = 1)
        Label(game_master, text = "============", justify = CENTER).grid(row = 1, column = 0, columnspan = 2)

        leader_keys = leaders.keys()
        leader_keys.sort(key = lambda x: leaders[x], reverse = True)
        counter = 2
        for k in leader_keys:
            Label(game_master, text = k, justify = CENTER).grid(row = counter, column = 0)
            Label(game_master, text = leaders[k], justify = CENTER).grid(row = counter, column = 1)

            counter+=1

        exit_button = Button(game_master, text = "EXIT", justify = CENTER, command = self.done_playing_game)
        exit_button.grid(row = counter, column = 0)


    def move_ring(self, event):
        global game_spots
        global location
        global range
        mouse_x = int(event.x)
        mouse_y = int(event.y)

        self.w.delete(self.ring_Id)
        self.ring_Id = self.w.create_image(mouse_x, mouse_y, image=self.ring_image)


        counter = 0
        for g in game_spots:
            print g, '\n\n'
            if ((mouse_x > g[0][0]) and (mouse_x < g[0][1]) and (mouse_y > g[1][0]) and (mouse_y < g[1][1])):
                print "Mouse X, Mouse Y", mouse_x, mouse_y
                print g[0][0],g[0][1],"---", g[1][0], g[1][1]
                range[counter] = True
            counter += 1

        if range[0] == True:
            range[0] = False
            next_game = self.first_game
            temp_location=0
        elif range[1] == True:
            range[1] = False
            next_game = self.second_game
            temp_location = 1
        elif range[2] == True:
            range[2] = False
            next_game = self.third_game
            temp_location = 2
        elif range[3] == True:
            range[3] = False
            next_game = self.fourth_game
            temp_location = 3
        elif range[4] == True:
            range[4] = False
            next_game = self.fifth_game
            temp_location = 4
        else:
            self.TopLabel.configure(text="You're in no-man's land traveler", bg="red")
            temp_location = -1

        if temp_location == -1:
            self.play_game.configure(state=DISABLED) ##Not in a valid Zone
        elif (game_spots[temp_location][2] == False):
            self.TopLabel.configure(text = ("You're in Game %d Traveler" % (1+temp_location)), bg="green")
            self.play_game.configure(state=NORMAL, command=next_game)   #Valid Zone and un-played
            print next_game
        else:
            self.TopLabel.configure(text = ("You're in Game %d Traveler, but you've already played this game." % (temp_location + 1)), bg="red")
            self.play_game.configure(state=DISABLED)    #Valid Zone and played




    ### GAME METHODS ==============================================================================>
    def first_game(self): #Game 1
        global game_spots
        global coins
        game_spots[0][2] = True  # SETS PLAYED GAME TO TRUE
        ##
        ##PLAY THE GAME, GET SCORE
        global game_master
        game_master = Toplevel(self.master)
        Game1 = Game_1(game_master, self, coins)
        self.playing_game()
        ##
        ##
        print "PLAYED GAME 1!!!"

    def second_game(self): #Game 2
        global game_spots
        global coins
        game_spots[1][2] = True  # SETS PLAYED GAME TO TRUE
        ##
        ##
        global game_master
        game_master = Toplevel(self.master)
        self.playing_game()
        Game2 = Game_2(game_master, self, coins)
        ##
        print "PLAYED GAME 2!!!"

    def third_game(self):#Game 3
        global game_spots
        global coins
        game_spots[2][2] = True  # SETS PLAYED GAME TO TRUE
        ##
        global game_master
        game_master = Toplevel(self.master)
        self.playing_game()
        Game3 = Game_3(game_master, self, coins)
        ##
        print "PLAYED GAME 3!!!"

    def fourth_game(self): #Game 4
        global game_spots
        global coins
        game_spots[3][2] = True  # SETS PLAYED GAME TO TRUE
        ##
        global game_master
        game_master = Toplevel(self.master)
        self.playing_game()
        Game4 = Game_4(game_master, self, coins)
        ##
        print "PLAYED GAME 4!!!"

    def fifth_game(self): #Game 5
        global game_spots
        global coins
        game_spots[4][2] = True  # SETS PLAYED GAME TO TRUE
        ##
        global game_master
        game_master = Toplevel(self.master)
        self.playing_game()

        print "PLAYED GAME 5!!!"
    ### GAME METHODS ==============================================================================>

    ### IN GAME SWITCH METHODS ==============================================================================>
    def playing_game(self):
        self.start_end_button.configure(state=DISABLED)
        self.play_game.configure(state=DISABLED)
        self.TopLabel.configure(text=" In Game, must finish before returning to travelling. ", bg="white")
        self.w.unbind("<Button-1>")

        print "playing Game"

    def done_playing_game(self):
        global game_master
        game_master.destroy()
        self.start_end_button.configure(state=NORMAL)
        self.TopLabel.configure(text=" Finished game, may return to travelling! ", bg="white")
        self.w.bind("<Button-1>", self.move_ring)

        self.score.configure(text = coins.return_total())

        print "Done Playing Game"
    ### IN GAME SWITCH METHODS ==============================================================================>

if __name__ == '__main__':
    root = Tk()
    print "went through main!"
    root.title(" SIMPLE WALK THROUGH MORRODOR ")
    master_page = Master_Class(root)
    root.mainloop()