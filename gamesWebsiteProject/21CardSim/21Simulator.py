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
playersHand = ["PC1", "PC2", "PC3", "PC4", "PC5"]
dealersHand = ["DC1", "DC2", "DC3", "DC4", "DC5"]
#Could make PC1-5 and DC1-5 their own objects, adding to hand when hitting and replace with real cards when revealing

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
        print("Shuffling the deck")
        print("Rules: ")
        random.shuffle(fullDeck)
        print(" ___________")
        print("||||########|")
        print("||||########|")
        print("||||########|")
        print("||||########|")
        print("||||########|")
        time.sleep(4)
        state=2

    if(state==2): #Game
        #Player gets 1st card, hidden
        clear()
        playersHand[0] = fullDeck[0]
        fullDeck.pop(0)
        print("Game Start, Player dealt one card")
        print(" ___________")
        print("||||########|")
        print("||||########|")
        print("||||########|")
        print("||||########|")
        print("||||########|")
        print("                ________")
        print("               |########|")
        print("               |########|")
        print("               |########|")
        print("               |########|")
        print("               |########|")
        time.sleep(1)

        #Player 1st card revealed
        clear()
        print("Player card revealed")
        print(" ___________")
        print("||||########|")
        print("||||########|")
        print("||||########|")
        print("||||########|")
        print("||||########|")
        print("                ________")
        print("               |        |")
        print("               |" + playersHand[0] + "     |")
        print("               |        |")
        print("               |        |")
        print("               |________|")
        time.sleep(2)

        #Dealer gets 1st card, hidden
        dealersHand[0] = fullDeck[0]
        fullDeck.pop(0)
        clear()
        print("Dealer dealt one card")
        print(" ___________    ________")
        print("||||########|  |########|")
        print("||||########|  |########|")
        print("||||########|  |########|")
        print("||||########|  |########|")
        print("||||########|  |########|")
        print("                ________")
        print("               |        |")
        print("               |" + playersHand[0] + "     |")
        print("               |        |")
        print("               |        |")
        print("               |________|")
        time.sleep(1)

        #Dealer 1st card revealed
        clear()
        print("Dealer card revealed")
        print(" ___________    ________")
        print("||||########|  |        |")
        print("||||########|  |" + dealersHand[0] + "     |")
        print("||||########|  |        |")
        print("||||########|  |        |")
        print("||||########|  |________|")
        print("                ________")
        print("               |        |")
        print("               |" + playersHand[0] + "     |")
        print("               |        |")
        print("               |        |")
        print("               |________|")
        time.sleep(2)

        clear()
        playersHand[1] = fullDeck[0]
        fullDeck.pop(0)
        print("Player 2nd card dealt")
        print(" ___________    ________")
        print("||||########|  |        |")
        print("||||########|  |" + dealersHand[0] + "     |")
        print("||||########|  |        |")
        print("||||########|  |        |")
        print("||||########|  |________|")
        print("                ___ ________")
        print("               |   |########|")
        print("               |" + playersHand[0] + "|########|")
        print("               |   |########|")
        print("               |   |########|")
        print("               |___|########|")
        time.sleep(1)

        clear()
        print("Player 2nd card revealed")
        print(" ___________    ________")
        print("||||########|  |        |")
        print("||||########|  |" + dealersHand[0] + "     |")
        print("||||########|  |        |")
        print("||||########|  |        |")
        print("||||########|  |________|")
        print("                ___ ________")
        print("               |   |        |")
        print("               |" + playersHand[0] + "|" + playersHand[1] + "     |")
        print("               |   |        |")
        print("               |   |        |")
        print("               |___|________|")
        time.sleep(2)

        clear()
        dealersHand[1] = fullDeck[0]
        fullDeck.pop(0)
        print("Dealer 2nd card dealt")
        print(" ___________    ________ ___")
        print("||||########|  |        |###|")
        print("||||########|  |" + dealersHand[0] + "     |###|")
        print("||||########|  |        |###|")
        print("||||########|  |        |###|")
        print("||||########|  |________|###|")
        print("                ___ ________")
        print("               |   |        |")
        print("               |" + playersHand[0] + "|" + playersHand[1] + "     |")
        print("               |   |        |")
        print("               |   |        |")
        print("               |___|________|")
        time.sleep(2)
        choice = input("Hit or Stand? (h/s) > ")



    if(state==9): #Program end
        print("Program end")
        break