import random #to generate random dice
import os #to help clear the screen
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.moves = {}
        self.bonus_given = False
        self.yahtzee_won = False

    def reset(self):
        self.score = 0
        self.moves = {}
        self.bonus_given = False
        self.yahtzee_won = False

def roll():
    global current_dice
    current_dice = rolldie(5) #for first roll
    replacing = []
    replacing_indexes = []
    rolls = 0
    print("Your first roll was:", current_dice, "\n")
    result = input("Do you want to keep these dice? (y or n) ")
    result = (result.lower()).strip()
    while result not in ("y", "n"):
        result = input("\nYou probably mistyped something. Try again. ")
        result = (result.lower().strip())
    if result == "n":
        while rolls != 2:
            if rolls != 0: #Only show this for the second and third roll
                print("Your current dice are:", current_dice, "\n")
                result = input("Do you want to keep these dice (y or n) (default is n)? ")
                result = (result.lower()).strip()
                if result == "y":
                    break
            indexes = input("Type the ordinal numbers (first would be 1, second would be 2, etc)\nof dice to replace. (no spaces) ")
            try:
                replaced_dice = list(indexes)
                for index in replaced_dice:
                    skip = False
                    #subtracting 1 to convert ordinal numbers to indexes in an array
                    array_index = int(index) - 1
                    if array_index < 0:
                        raise IndexError("That wasn't an ordinal number!")
                    #Error checking to make sure replaced dice are only replaced once
                    while array_index in replacing_indexes:
                        print("Sorry, you are already replacing " + str(current_dice[array_index]) + ".\n")
                        skip = True
                        break
                    if skip:
                        continue
                    replacing.append(current_dice[array_index])
                    replacing_indexes.append(array_index)
            except IndexError:
                print("\nYou only have 5 dice!\n")
                replacing = []
                replacing_indexes = []
                continue
            except:
                print("\nYou probably mistyped something. Try again.\n")
                replacing = []
                replacing_indexes = []
                continue
            if len(replacing) == 0:
                print("Keeping all dice ...")
                break
            print("Replacing", replacing, "")
            keeping = []
            #Keep the ones we are not replacing
            for index in (set([0,1,2,3,4]) - set(replacing_indexes)):
                keeping.append(current_dice[index])
            #Use the number of dice replacing to replace those dice
            new_dice = rolldie(len(replacing))
            #Add the newly rolled dice to the ones we kept originally
            for new_die in new_dice:
                keeping.append(new_die)
            #Update and reset attributes for next roll
            current_dice = keeping
            replacing = []
            replacing_indexes = []
            rolls += 1
    print("\nYour new roll was: %s\n" % current_dice)

#Simulates a dice roll, returning the dice in an array
def rolldie(numToRoll):
    diechoices = ['1', '2', '3', '4', '5', '6']
    result = []
    for x in range(numToRoll):
        result.append(int(random.choice(diechoices)))
    return result

#Counts how many dice are of a certain number
def countDice(number):
    counter = 0
    for n in current_dice:
        if n == number:
            counter += 1
    score = counter * number
    return score

def choosePoints(player):
    key = allOptions[0]
    value = allOptions[1]
    bestOption = max(value)
    counter = 1
    for index in range(0, len(key)):
        if value[index] == bestOption:
            print('\033[1m' + str(counter) + ":\t", end='\033[0m')
            print('\033[1m' + str(key[index]) + ":\t" + str(value[index]) + " points" + '\033[0m')
        else:
            print(str(counter) + ":\t", end="")
            print(str(key[index]) + ":\t" + str(value[index]) + " points.")
        counter += 1
    option = input("\nHere are all of your options. Select an option by entering its sequential number.\n")
    while True:
        try:
            option = key[int(option) - 1]
            option = (option.strip()).lower()
            for index in range(0, len(key)):
                keycopy = (key[index].strip(" ")).lower()
                if keycopy == option:
                    player.score += int(value[index])
                    player.moves[key[index]] = int(value[index])
                    return
        except:
            option = input("You probably mistyped something. Try again.\n")

#Checks for full house
def checkFullHouse():
    for num in current_dice:
        if current_dice.count(num) == 3:
            for second_num in current_dice:
                if current_dice.count(second_num) == 2:
                    return 25
    return 0

#Checks for a dice of a 3 of a kind, 4 of a kind, or 5 of a kind
def ofAKind(player, numOfKind):
    for number in current_dice:
        if current_dice.count(number) == numOfKind:
            if numOfKind == 5: #Yahtzee
                if player.yahtzee_won: #Second Yahtzee
                    return 100
                else: #First Yahtzee
                    player.yahtzee_won = True
                    return 50
            else:
                return numOfKind * number
    return 0

def checkStraight(smallOrLarge):
    sortedArray = list(set(current_dice))
    if smallOrLarge == 1: #large
        if [1,2,3,4,5] == sortedArray or [2,3,4,5,6] == sortedArray:
            return 40
    else: #small
        #Check if 1234,2345,3456 is in sortedArray
        if all(x in sortedArray for x in [1,2,3,4]) or all(x in sortedArray for x in [2,3,4,5]) or all(x in sortedArray for x in [3,4,5,6]):
            return 30
    return 0

def removeTakenOptions(player):
    key = allOptions[0]
    value = allOptions[1]
    index = len(key) - 1
    #Remove all zero options first
    while index >= 0:
        if "Pass          " not in key[index]: #Don't remove pass
            if value[index] == 0:
                del key[index]
                del value[index]
        index -= 1
    #Gather already taken choices
    for takenKey in player.moves.keys():
        index = len(key) - 1
        while index >= 0:
            if "Pass          " not in takenKey: #Don't remove pass
                if takenKey == key[index]:
                    del key[index]
                    del value[index]
            index -= 1

def over63(player):
    if player.bonus_given:
        return False
    sumOfFirstSix = 0
    arrayToCheck = ['Ones          ', 'Twos          ', 'Threes        ',
                     'Fours         ', 'Fives         ', 'Sixes         ']
    if all(x in list(player.moves.keys()) for x in arrayToCheck):
        for index in arrayToCheck:
            sumOfFirstSix += int(player.moves[index])
    if sumOfFirstSix >= 63:
        player.bonus_given = True
        return True
    else:
        return False

def printScoreCard(player, allOptions):
    printedBonus = True
    print("Yahtzee Score Card")
    for key in allOptions:
        if key == "Over 63 = +35 ":
            print(key + "|\t", end="")
        elif key != "Pass          ":
            print(key + "|\t", end="")
        for k, v in player.moves.items():
            if k == key and k != "Pass          ": #already taken
                print(str(v), end="")
            if key == "Over 63 = +35 ":
                if over63(player):
                    player.score += 35
                if player.bonus_given and printedBonus:
                    print("35", end="")
                    printedBonus = False
        print()
    print("Current Score: " + str(player.score))


#to clear screen after number of players have been entered
def clear():
    i = 64
    mpt = ""
    while i>0:
        print(mpt,end="\n")
        i -= 1


# Welcome text
text1 = '''

██╗░░░██╗░█████╗░██╗░░██╗████████╗███████╗███████╗███████╗
╚██╗░██╔╝██╔══██╗██║░░██║╚══██╔══╝╚════██║██╔════╝██╔════╝
░╚████╔╝░███████║███████║░░░██║░░░░░███╔═╝█████╗░░█████╗░░
░░╚██╔╝░░██╔══██║██╔══██║░░░██║░░░██╔══╝░░██╔══╝░░██╔══╝░░
░░░██║░░░██║░░██║██║░░██║░░░██║░░░███████╗███████╗███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚══════╝╚══════╝


 _________   _________  
|         | |         | 
|  o   o  | |  o   o  | 
|  o   o  | |    o    | 
|  o   o  | |  o   o  |
|_________| |_________|

                         _________   _________
                        |         | |         |
                        |  o   o  | |  o      |
                        |         | |    o    |
                        |  o   o  | |      o  |
                        |_________| |_________|

                                                  _________   _________
                                                 |         | |         |
                                                 |  o      | |         |
                                                 |         | |    o    |
                                                 |      o  | |         |
                                                 |_________| |_________|


░██████╗░░█████╗░███╗░░░███╗███████╗
██╔════╝░██╔══██╗████╗░████║██╔════╝
██║░░██╗░███████║██╔████╔██║█████╗░░
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝
'''

print(text1)
print("Welcome to Yahtzee!")

#Where the program starts
num_players = int(input("Enter the number of players: "))
players = [Player(input(f"Enter name for player {i + 1}: ")) for i in range(num_players)]

for turnNumber in range(13):
    for player in players:
        print(f"{player.name}'s Turn {turnNumber + 1} started.\n")
        roll()

        allOptions = [   ["Ones          ", "Twos          ", "Threes        ",
                         "Fours         ", "Fives         ", "Sixes         ",
                         "Over 63 = +35 ",
                         "3 of a kind   ", "4 of a kind   ", "Full House    ",
                         "Small Straight", "Large Straight", "Yahtzee       ",
                         "Chance        ", "Pass          "],
                        [countDice(1), countDice(2), countDice(3),
                         countDice(4), countDice(5), countDice(6), 0,
                         ofAKind(player, 3), ofAKind(player, 4), checkFullHouse(),
                         checkStraight(0), checkStraight(1), ofAKind(player, 5),
                         sum(current_dice), 0]]
        allKeys = allOptions[0].copy()
        removeTakenOptions(player)
        choosePoints(player)
        time.sleep(0.5) #Sleep for half a second
        os.system('cls' if os.name=='nt' else 'clear') #Will work on both Unix and Windows
        print(f"\nTurn {turnNumber + 1} completed for {player.name}.")
        print("Here is your current Score Card:\n\n")
        printScoreCard(player, allKeys)

#End of game
for player in players:
    print(f"Game Over! {player.name}'s score was: {player.score}")

# Display high score
high_score = max(players, key=lambda p: p.score)
print(f"The highest score was {high_score.score} by {high_score.name}.")

