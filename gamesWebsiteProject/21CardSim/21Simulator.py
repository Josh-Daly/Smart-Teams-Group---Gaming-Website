import os
import time
import random
clear = lambda: os.system('cls') #Creates obj for clearing serial screen

#Variables
state = 0 #Controls what part of game
#0 - Title, 1 - Setup, 2 - Start, MORE TO BE ADDED, 9 - End
win = 21
#Card Array
spadeDeck = [" A♠"," 2♠"," 3♠"," 4♠"," 5♠"," 6♠"," 7♠"," 8♠"," 9♠","10♠"," J♠"," Q♠"," K♠"]
diamsDeck = [" A♦"," 2♦"," 3♦"," 4♦"," 5♦"," 6♦"," 7♦"," 8♦"," 9♦","10♦"," J♦"," Q♦"," K♦"]
clubsDeck = [" A♣"," 2♣"," 3♣"," 4♣"," 5♣"," 6♣"," 7♣"," 8♣"," 9♣","10♣"," J♣"," Q♣"," K♣"]
heartsDeck = [" A♥"," 2♥"," 3♥"," 4♥"," 5♥"," 6♥"," 7♥"," 8♥"," 9♥","10♥"," J♥"," Q♥"," K♥"]
fullDeck = spadeDeck + diamsDeck + clubsDeck + heartsDeck

while True:
    if(state==0): #Title
        clear()
        print("TItle Screen")
        choice = input("Play? (y/n) > ")
        if(choice=="y"):
            state = 1
            
        elif(choice=="n"):
            state = 9

    if(state==1): #Setup
        clear()
        print("Game Setup Here")
        random.shuffle(fullDeck)
        print(" ______ ________")
        print("|" + fullDeck[0] + "   |" + fullDeck[1] + "     |")
        print("|      |        |")
        print("|      |        |")
        print("|      |        |")
        print("|______|________|")
        time.sleep(10)

    if(state==9): #Program end
        print("Program end")
        break
