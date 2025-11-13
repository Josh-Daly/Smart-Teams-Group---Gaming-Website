import os
import time
import random
clear = lambda: os.system('cls') #Creates obj for clearing serial screen

#Variables
state = 0 #Controls what part of game is active, 0 - Title, 1 - Setup, 2 - Start, MORE TO BE ADDED, 9 - End
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
        #Card Array
        spadeDeck = [" A♠"," 2♠"," 3♠"," 4♠"," 5♠"," 6♠"," 7♠"," 8♠"," 9♠","10♠"," J♠"," Q♠"," K♠"]
        diamsDeck = [" A♦"," 2♦"," 3♦"," 4♦"," 5♦"," 6♦"," 7♦"," 8♦"," 9♦","10♦"," J♦"," Q♦"," K♦"]
        clubsDeck = [" A♣"," 2♣"," 3♣"," 4♣"," 5♣"," 6♣"," 7♣"," 8♣"," 9♣","10♣"," J♣"," Q♣"," K♣"]
        heartsDeck = [" A♥"," 2♥"," 3♥"," 4♥"," 5♥"," 6♥"," 7♥"," 8♥"," 9♥","10♥"," J♥"," Q♥"," K♥"]
        fullDeck = spadeDeck + diamsDeck + clubsDeck + heartsDeck
        playersHand = ["PC1", "PC2", "PC3", "PC4", "PC5"]
        dealersHand = ["DC1", "DC2", "DC3", "DC4", "DC5"]
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
        # /// PLAYER 1ST CARD ///
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

        # /// DEALER 1ST CARD ///
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

        # /// PLAYER 2ND CARD ///
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

        # /// DEALER 2ND CARD ///
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

        #TODO: If loop for player holding Ace and ten/jack/queen/king, dealer reveals, if both 21, tie, if not, players wins


        # //// Actual game starts, ask player if they want to hit or stand ///
        choice = input("Hit or Stand? (h/s) > ")
        if(choice == 'h'):
            # /// PLAYER 3RD CARD ///
            clear()
            playersHand[2] = fullDeck[0]
            fullDeck.pop(0)
            print("Player Stands: 3rd card dealt")
            print(" ___________    ________ ___")
            print("||||########|  |        |###|")
            print("||||########|  |" + dealersHand[0] + "     |###|")
            print("||||########|  |        |###|")
            print("||||########|  |        |###|")
            print("||||########|  |________|###|")
            print("                ___ ___ ________")
            print("               |   |   |########|")
            print("               |" + playersHand[0] + "|" + playersHand[1] + "|########|")
            print("               |   |   |########|")
            print("               |   |   |########|")
            print("               |___|___|########|")
            time.sleep(2)

            clear()
            print("Player 3rd card revealed")
            print(" ___________    ________ ___")
            print("||||########|  |        |###|")
            print("||||########|  |" + dealersHand[0] + "     |###|")
            print("||||########|  |        |###|")
            print("||||########|  |        |###|")
            print("||||########|  |________|###|")
            print("                ___ ___ ________")
            print("               |   |   |        |")
            print("               |" + playersHand[0] + "|" + playersHand[1] + "|" + playersHand[2] + "     |")
            print("               |   |   |        |")
            print("               |   |   |        |")
            print("               |___|___|________|")
            time.sleep(2)

            #TODO: Loop to check if player busted

            # /// DEALER 2ND CARD REVEAL ///
            clear()
            print("Dealer 2nd card revealed")
            print(" ___________    ___ ________")
            print("||||########|  |   |        |")
            print("||||########|  |" + dealersHand[0] + "|" + dealersHand[1] + "     |")
            print("||||########|  |   |        |")
            print("||||########|  |   |        |")
            print("||||########|  |___|________|")
            print("                ___ ___ ________")
            print("               |   |   |        |")
            print("               |" + playersHand[0] + "|" + playersHand[1] + "|" + playersHand[2] + "     |")
            print("               |   |   |        |")
            print("               |   |   |        |")
            print("               |___|___|________|")
            time.sleep(2)

            #If dealer hits
            # /// DEALER 3RD CARD ///
            dealerHits = 1
            if (dealerHits == 1):
                clear()
                print("Dealer hits: 3rd card dealt")
                time.sleep(2)

                clear()
                print("Dealer 3rd card revealed")
                time.sleep(2)

                #TODO: Check if Dealer busts
            else:
                pass
            

        else:
            # /// PLAYER STANDS: 2 CARDS DEALT
            #TODO: Dealer hits til 17 or more, check who wins
            pass









        #End
        choice = input("Play again? (y/n)")
        if(choice == 'y'):
            state=1
        else:
            state=9


    if(state==9): #Program end
        print("Program end")
        break