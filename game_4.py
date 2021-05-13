__author__ = 'Andy Chang'

import random
from Tkinter import *



def attack():
    global player_health
    global enemy_health
    global player_defense
    global enemy_defense
    global point_value
    global starting_health

    list_player_attacks = player_attacks.keys()
    list_enemy_attacks = enemy_attacks.keys()
    next_player_attack = random.choice(list_player_attacks)
    next_enemy_attack = random.choice(list_enemy_attacks)
    print '\tPlayer Attack: %-10s' % next_player_attack
    print '\tEnemy Attack: %-10s' % next_enemy_attack
    player_evasion = random.randint(1, 50)  # Randomizes player evasion
    enemy_evasion = random.randint(1, 50)  # Randomizes enemy evasion

    if player_evasion <= 10:
        enemy_health = max(enemy_health-(player_attacks[next_player_attack]-enemy_defense),0)

        random_enemy_attack.config(text=next_enemy_attack + '\tYou dodged the attack')
        random_player_attack.config(text=next_player_attack + '\tDamage: ' + str((player_attacks[next_player_attack]-enemy_defense)))
        print '\tYou dodged the attack'
    elif enemy_evasion <= 10:
        player_health = max(player_health - (enemy_attacks[next_enemy_attack] - player_defense), 0)

        random_enemy_attack.config(text=next_enemy_attack + '\tDamage: ' + str((enemy_attacks[next_enemy_attack]-player_defense)))
        random_player_attack.config(text=next_player_attack + '\tThe enemy dodged the attack')
        print '\tThe enemy dodged the attack'
    else:
        enemy_health = max(enemy_health - (player_attacks[next_player_attack] - enemy_defense), 0)
        player_health = max(player_health - (enemy_attacks[next_enemy_attack] - player_defense), 0)

        random_enemy_attack.config(text=next_enemy_attack + '\tDamage: ' + str((enemy_attacks[next_enemy_attack] - player_defense)))
        random_player_attack.config(text=next_player_attack + '\tDamage: ' + str((player_attacks[next_player_attack] - enemy_defense)))

    e_health.config(text=enemy_health)
    p_health.config(text=player_health)
    print 'Player Health remaining: ', player_health
    print 'Enemy Health remaining: ', enemy_health

    if enemy_health == 0 or player_health == 0:
        boss_button.config(state=NORMAL)

        if enemy_health == 0 and player_health > 0 and leader == 1:
            print 'Congratulations! You Won!'
            attack_button.config(state=DISABLED)
            boss_button.config(state=DISABLED)
            forage_button.config(state=DISABLED)
            random_enemy_attack.config(text='Congratulations')
            random_player_attack.config(text='You Win')
            e_health.config(bg='red')
            point_value = point_value + starting_health
            points.config(text=point_value)

            coins.add(point_value)
            master.done_playing_game()
        elif enemy_health == 0 and player_health > 0:
            print 'You defeated the enemy'
            attack_button.config(state=DISABLED)
            forage_button.config(state=DISABLED)
            random_player_attack.config(text='Enemy defeated')
            random_enemy_attack.config(text='Enemy defeated')
            e_health.config(bg='red')
            point_value = point_value + starting_health
            points.config(text=point_value)
        else:
            print 'You were defeated'
            attack_button.config(state=DISABLED)
            boss_button.config(state=DISABLED)
            forage_button.config(state=DISABLED)
            random_player_attack.config(text='You were defeated')
            random_enemy_attack.config(text='You were defeated')
            p_health.config(bg='red')
            point_value = point_value + (150 - enemy_health)
            points.config(text=point_value)

            coins.add(point_value)
            master.done_playing_game()
        return

def leader_appears():
    global enemy_health
    global enemy_defense
    global leader
    global leader_health
    global leader_values
    global starting_health

    enemy_health = random.choice(leader_health)
    starting_health = enemy_health
    e_health.config(text=enemy_health,bg='green')
    random_enemy_attack.config(text='The chief has appeared')
    enemy_defense = random.choice(leader_values)
    attack_button.config(state=NORMAL)
    boss_button.config(state=DISABLED)
    forage_button.config(state=NORMAL)
    image_location.config(image=chief_image)
    leader = 1 # Leader has appeared
    print 'The chief has appeared'
    print "The chief's total health and defense are %.3d and %2d, respectively " %(enemy_health,enemy_defense)

def forage():
    global player_health
    global player_defense
    global plants
    global foraging

    list_of_plants = plants.keys()
    found_plant = random.choice(list_of_plants)
    player_health = min(player_health + plants[found_plant], 100)
    random_player_attack.config(text="Foraged")
    foraging.config(text=found_plant + '\tHealing: ' + str(plants[found_plant]))
    player_evasion = random.randint(1, 50)  # Randomizes player evasion

    list_enemy_attacks = enemy_attacks.keys()
    next_enemy_attack = random.choice(list_enemy_attacks)

    if player_evasion <= 5:
        random_enemy_attack.config(text=next_enemy_attack + 'You dodged the attack')
    else:
        player_health = max(player_health - (enemy_attacks[next_enemy_attack] - player_defense), 0)

        random_enemy_attack.config(text=next_enemy_attack + '\tDamage: ' + str((enemy_attacks[next_enemy_attack] - player_defense - plants[found_plant])))
    p_health.config(text=player_health)
    print '\tPlayer foraged for plants'
    print '\tEnemy Attack: %-10s' % next_enemy_attack
    print 'Player Health: ', player_health
    print 'Enemy Health: ', enemy_health

class Game_4():
    def __init__(self, frame, roots, coin):
        global game
        global master
        global coins
        game = frame
        master = roots
        coins = coin

        main()

def main():
    global random_enemy_attack
    global random_player_attack

    game.title('Battle')

    global point_value
    point_value = 0 # Starting point value

    global player_health
    global plants
    player_health = 100 # Starting health for player
    # Dictionary with all possible healing options
    plants = {'Alfrin found': 20,'Athelas found': 20,'Elgaran found': 20,'Mallos found': 20,'Blue Milk found': 10,'Lothrond found': 10,'Naugrimbas found': 10,'Orchamarth found': 10,'Azuradan found': 30,'Earthbread found': 30,'Hithlas found': 30,'Remmenthond found': 30,'Nothing found': 0}

    global common_health
    global leader_health
    global enemy_health
    global starting_health
    common_health = range(75,101,5) # Health for first enemy
    leader_health = range(100,151,5) # Health for second enemy
    enemy_health = random.choice(common_health) # Randomizes enemy health value
    starting_health = enemy_health

    global defense_values
    global leader_values
    global player_defense
    global enemy_defense
    defense_values = range(1,10) # Range for defense value
    leader_values = range(5,11) # Range of defense value for the second enemy and player
    player_defense = random.choice(leader_values) # Randomizes player defense
    enemy_defense = random.choice(defense_values) # Randomizes enemy defense

    global player_attacks
    global enemy_attacks
    player_attacks = {'Stab': 15,'Slash': 20,'Cut': 10,'Strike': 25,'Pierce': 30,'Jab': 15,'Slice': 20,'Poke': 10}
    enemy_attacks = {'Smack': 15,'Smash': 25,'Crush': 30,'Stomp': 10,'Charge': 20,'Whack': 15,'Wallop': 20,'Kick': 10}

    random_player_attack = Label(game,text='Attack to injure the enemy', width=30, bg='blue')
    random_enemy_attack = Label(game,text='An enemy has appeared', width=30, bg='orange')

    global leader
    leader = 0 # Leader has not appeared








    # Enemy Hit Points
    global e_health
    Label(game,text='Enemy Health').grid(row=1, column=0)
    e_health = Label(game,text=enemy_health, bg='green', width=30)
    e_health.grid(row=1, column=1)

    # Player Hit Points
    global p_health
    Label(game,text='Player Health').grid(row=1, column=3)
    p_health = Label(game,text=player_health, bg='green', width=30)
    p_health.grid(row=1, column=4)

    global foraging
    foraging = Label(game,text="Forage for a chance to heal", bg='cyan', width=30)
    foraging.grid(row=3, column=4)

    global points
    Label(game,text='Points').grid(row=2, column=2)
    points = Label(game,text=point_value, bg='yellow', width=5)
    points.grid(row=3, column=2)

    global attack_button
    attack_button = Button(game, text='Attack', command=lambda: attack())
    attack_button.grid(row=2, column=3)

    global forage_button
    forage_button = Button(game, text='Forage', command=lambda: forage())
    forage_button.grid(row=3, column=3)

    random_player_attack.grid(row=2, column=4)
    random_enemy_attack.grid(row=2, column=1)


    global boss_button
    boss_button = Button(game, text='Chief Appears', command=leader_appears, state=DISABLED)
    boss_button.grid(row=3, column=1)

    global images
    global chief_image
    global list_of_images
    global enemy_image
    global image_location
    images = {PhotoImage(file='Data/Uruk.gif'): 0,PhotoImage(file='Data/Uruk1.gif'): 0,PhotoImage(file='Data/Uruk2.gif'): 0}
    chief_image = PhotoImage(file='Data/Uruk_Chief.gif')
    list_of_images = images.keys()
    enemy_image = random.choice(list_of_images)
    image_location = Label(game, image=enemy_image)
    image_location.grid(row=0, column=2)

    print 'You have encountered an enemy'
    print 'Your total health and defense are %.3d and %2d, respectively' %(player_health,player_defense)
    print "The enemy's total health and defense are %3d and %.1d, respectively" %(enemy_health,enemy_defense)

    game.mainloop()