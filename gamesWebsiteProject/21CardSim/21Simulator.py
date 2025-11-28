import os
import time
import random
clear = lambda: os.system('cls') #Creates obj for clearing serial screen

#Variables
game = True
state = 0 #Controls what part of game is active, 0 - Title, 1 - Setup, 2 - Start, MORE TO BE ADDED, 9 - End
aceState = 0 #If more than 1, score can be plus 1 or plus 11, whichever benefits player more, each i in this var is how many aces
victoryState = 0 #Victory variable for player, calculated and used to control outcome of game, 0 = Game in progress, 1 = Victory, 2 = Tie, 3 = Game Over
#Could make PC1-5 and DC1-5 their own objects, adding to hand when hitting and replace with real cards when revealing

#Functions
def cardScoreChecker(array, indexVar): #Adds up card values, sets up state for ace cards #Finished (for now)
    sum = 0
    aceState = 0
    for i in range(indexVar):
        if(array[i][0] == " A"):
            aceState += 1
        elif(array[i][0] == " J"):
            sum += 10
        elif(array[i][0] == " Q"):
            sum += 10
        elif(array[i][0] == " K"):
            sum += 10
        else:
            sum += int(array[i][0])
    if(aceState > 0):
        if(aceState == 1):
            if((sum+11) > 21): #If adding 11 would push the player past 21
                sum += 1
            else:
                sum += 11
        elif(aceState == 2):
            sum += 1
            if((sum+11) > 21):
                sum += 1
            else:
                sum += 11
        elif(aceState == 3):
            sum = 13
    return sum

def playerBustChecker(playerScoreVar):
    if(playerScoreVar > 21):
        print("Player has busted!")
        print("Player Card Value: " + playerScoreVar)
        print("ADD CHOICE STATEMENT AND IFS")

def dealerBustChecker(dealerScoreVar):
    if(dealerScoreVar > 21):
        print("Dealer has busted!")
        print("Player wins!")
        print("ADD CHOICE STATEMENT AND IFS")
        

def victoryStateSetter(playerScoreVar, dealerScoreVar): #Sets victory state variable according to 
    victoryVar = 0
    if (playerScoreVar > dealerScoreVar and playerScore <= 21):
        victoryVar = 1 #Win
    elif (playerScoreVar == dealerScoreVar):
        victoryVar = 2 #Tie
    elif (playerScoreVar < dealerScoreVar):
        victoryVar = 3 #Loss

    if (victoryVar == 1):
        print("Player has won!")
        print("Player Card Value: " + str(playerScoreVar) + " Dealer Card Value: " + str(dealerScoreVar))
    elif (victoryVar == 2):
        print("Player has tied.")
        print("Player Card Value: " + str(playerScoreVar) + " Dealer Card Value: " + str(dealerScoreVar))
    elif (victoryVar == 3):
        print("Player has lost.")
        print("Player Card Value: " + str(playerScoreVar) + " Dealer Card Value: " + str(dealerScoreVar))
    
    if(victoryVar == 1 or victoryVar == 2 or victoryVar == 3):
        time.sleep(3)
        choice = input("Play again? (y/n)")
        time.sleep(1)
        if(choice=="y" or choice=="Y"):
            pass   
        elif(choice=="n" or choice=="N"):
            print("Game ended.")
            print("Thanks for playing!")
            quit()
    

#Main Game Code
while (game == True):
    while(state==0): #Title
        
        clear()
        print("TItle Screen")
        choice = input("Play? (y/n) > ")
        if(choice=="y" or choice=="Y"):
            state = 1
            
        elif(choice=="n" or choice=="N"):
            clear()
            print("Game ended.")
            print("Thanks for playing!")
            quit()

    while(state==1): #Setup
        #Card Array
        spadeDeck = [[" A","♠"],[" 2","♠"],[" 3","♠"],[" 4","♠"],[" 5","♠"],[" 6","♠"],[" 7","♠"],[" 8","♠"],[" 9","♠"],["10","♠"],[" J","♠"],[" Q","♠"],[" K","♠"]]
        diamsDeck = [[" A","♦"],[" 2","♦"],[" 3","♦"],[" 4","♦"],[" 5","♦"],[" 6","♦"],[" 7","♦"],[" 8","♦"],[" 9","♦"],["10","♦"],[" J","♦"],[" Q","♦"],[" K","♦"]]
        clubsDeck = [[" A","♣"],[" 2","♣"],[" 3","♣"],[" 4","♣"],[" 5","♣"],[" 6","♣"],[" 7","♣"],[" 8","♣"],[" 9","♣"],["10","♣"],[" J","♣"],[" Q","♣"],[" K","♣"]]
        heartDeck = [[" A","♥"],[" 2","♥"],[" 3","♥"],[" 4","♥"],[" 5","♥"],[" 6","♥"],[" 7","♥"],[" 8","♥"],[" 9","♥"],["10","♥"],[" J","♥"],[" Q","♥"],[" K","♥"]]
        fullDeck = spadeDeck + diamsDeck + clubsDeck + heartDeck
        playersHand = [["PC1Num","PC1Suit"], ["PC2Num","PC2Suit"], ["PC3Num","PC3Suit"]]
        playerScore = 0
        dealersHand = [["DC1Num","DC1Suit"], ["DC2Num","DC2Suit"], ["DC3Num","DC3Suit"]]
        dealerScore = 0
        dealerHits = 0
        clear()
        print("Shuffling the deck...")
        random.shuffle(fullDeck)
        print(" ___________")
        print("||||########|")
        print("||||########|")
        print("||||########|")
        print("||||########|")
        print("||||########|")
        print("")
        print("Rules: Goal is to get 21 or more than the dealer, player will be given") 
        print("two cards, then can 'hit' for another card, or 'stand' to stay at two.")
        print("Player loses if they go over 21 or if dealer gets more.")
        print("Dealer and player can have a max of 3 cards.")
        time.sleep(4)
        #print(fullDeck)
        #print(" //// TEST PRINTS FOR ARRAYS //// ")
        #time.sleep(1)
        choice = input("Ready? (Press enter to continue) > ")
        state=2

    while(state==2): #Game
        # /// PLAYER 1ST CARD ///
        #Player gets 1st card, hidden
        clear()
        playersHand[0][0] = fullDeck[0][0]
        playersHand[0][1] = fullDeck[0][1]
        del fullDeck[0]
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
        print("               |" + playersHand[0][0] + playersHand[0][1] + "     |")
        print("               |        |")
        print("               |        |")
        print("               |________|")
        time.sleep(2)
        # TEST PASSAGE
        #playerScore = cardScoreChecker(playersHand,1)
        #print("TEST PRINT: Player Score is " + str(playerScore))
        #print("END TEST PRINT")
        #time.sleep(5)

        # /// DEALER 1ST CARD ///
        #Dealer gets 1st card, hidden
        dealersHand[0][0] = fullDeck[0][0]
        dealersHand[0][1] = fullDeck[0][1]
        del fullDeck[0]
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
        print("               |" + playersHand[0][0] + playersHand[0][1] + "     |")
        print("               |        |")
        print("               |        |")
        print("               |________|")
        time.sleep(1)

        #Dealer 1st card revealed
        clear()
        print("Dealer card revealed")
        print(" ___________    ________")
        print("||||########|  |        |")
        print("||||########|  |" + dealersHand[0][0] + dealersHand[0][1] + "     |")
        print("||||########|  |        |")
        print("||||########|  |        |")
        print("||||########|  |________|")
        print("                ________")
        print("               |        |")
        print("               |" + playersHand[0][0] + playersHand[0][1] + "     |")
        print("               |        |")
        print("               |        |")
        print("               |________|")
        time.sleep(2)
        # TEST PASSAGE
        #playerScore = cardScoreChecker(playersHand,1)
        #print("TEST PRINT: Player Score is " + str(playerScore))
        #dealerScore = cardScoreChecker(dealersHand,1)
        #print("TEST PRINT: Dealer Score is " + str(dealerScore))
        #print("END TEST PRINT")
        #time.sleep(5)

        # /// PLAYER 2ND CARD ///
        clear()
        playersHand[1][0] = fullDeck[0][0]
        playersHand[1][1] = fullDeck[0][1]
        del fullDeck[0]
        print("Player 2nd card dealt")
        print(" ___________    ________")
        print("||||########|  |        |")
        print("||||########|  |" + dealersHand[0][0] + dealersHand[0][1] + "     |")
        print("||||########|  |        |")
        print("||||########|  |        |")
        print("||||########|  |________|")
        print("                ___ ________")
        print("               |   |########|")
        print("               |" + playersHand[0][0] + playersHand[0][1] + "|########|")
        print("               |   |########|")
        print("               |   |########|")
        print("               |___|########|")
        time.sleep(1)

        clear()
        print("Player 2nd card revealed")
        print(" ___________    ________")
        print("||||########|  |        |")
        print("||||########|  |" + dealersHand[0][0] + dealersHand[0][1] + "     |")
        print("||||########|  |        |")
        print("||||########|  |        |")
        print("||||########|  |________|")
        print("                ___ ________")
        print("               |   |        |")
        print("               |" + playersHand[0][0] + playersHand[0][1] + "|" + playersHand[1][0] + playersHand[1][1] + "     |")
        print("               |   |        |")
        print("               |   |        |")
        print("               |___|________|")
        time.sleep(2)

        # /// DEALER 2ND CARD ///
        clear()
        dealersHand[1][0] = fullDeck[0][0]
        dealersHand[1][1] = fullDeck[0][1]
        del fullDeck[0]
        print("Dealer 2nd card dealt")
        print(" ___________    ________ ___")
        print("||||########|  |        |###|")
        print("||||########|  |" + dealersHand[0][0] + dealersHand[0][1] + "     |###|")
        print("||||########|  |        |###|")
        print("||||########|  |        |###|")
        print("||||########|  |________|###|")
        print("                ___ ________")
        print("               |   |        |")
        print("               |" + playersHand[0][0] + playersHand[0][1] + "|" + playersHand[1][0] + playersHand[1][1] + "     |")
        print("               |   |        |")
        print("               |   |        |")
        print("               |___|________|")
        time.sleep(2)

        #TODO: If loop for player holding Ace and ten/jack/queen/king, dealer reveals, if both 21, tie, if not, players wins

        #TEST TO SET PLAYER AS 21 TO TEST VICTORY STUFF
        playersHand[0][0]=" A"
        playersHand[1][0]=" K"
        dealersHand[0][0]=" 7"
        dealersHand[1][0]=" 7" 


        playerScore = cardScoreChecker(playersHand,2)
        if(playerScore == 21):
            clear()
            print("Player hit 21")
            print(" ___________    ________ ___")
            print("||||########|  |        |###|")
            print("||||########|  |" + dealersHand[0][0] + dealersHand[0][1] + "     |###|")
            print("||||########|  |        |###|")
            print("||||########|  |        |###|")
            print("||||########|  |________|###|")
            print("                ___ ________")
            print("               |   |        |")
            print("               |" + playersHand[0][0] + playersHand[0][1] + "|" + playersHand[1][0] + playersHand[1][1] + "     |")
            print("               |   |        |")
            print("               |   |        |")
            print("               |___|________|")
            time.sleep(5)

            clear()
            print("Dealer 2nd card revealed")
            print(" ___________    ___ ________")
            print("||||########|  |   |        |")
            print("||||########|  |" + dealersHand[0][0] + dealersHand[0][1] + "|" + dealersHand[1][0] + dealersHand[1][1] + "     |")
            print("||||########|  |   |        |")
            print("||||########|  |   |        |")
            print("||||########|  |___|________|")
            print("                ___ ________")
            print("               |   |        |")
            print("               |" + playersHand[0][0] + playersHand[0][1] + "|" + playersHand[1][0] + playersHand[1][1] + "     |")
            print("               |   |        |")
            print("               |   |        |")
            print("               |___|________|")
            time.sleep(5)
            dealerScore = cardScoreChecker(dealersHand,2)
            
            #TODO: IF loop for dealer hitting under 17


            victoryStateSetter(playerScore,dealerScore)
            state=1
            break


        # //// Actual game starts, ask player if they want to hit or stand ///
        choice = input("Hit or Stand? (h/s) > ")
        if(choice == 'h'):
            # /// PLAYER 3RD CARD ///
            clear()
            playersHand[2][0] = fullDeck[0][0]
            playersHand[2][1] = fullDeck[0][1]
            del fullDeck[0]
            print("Player Stands: 3rd card dealt")
            print(" ___________    ________ ___")
            print("||||########|  |        |###|")
            print("||||########|  |" + dealersHand[0][0] + dealersHand[0][1] + "     |###|")
            print("||||########|  |        |###|")
            print("||||########|  |        |###|")
            print("||||########|  |________|###|")
            print("                ___ ___ ________")
            print("               |   |   |########|")
            print("               |" + playersHand[0][0] + playersHand[0][1] + "|" + playersHand[1][0] + playersHand[1][1] + "|########|")
            print("               |   |   |########|")
            print("               |   |   |########|")
            print("               |___|___|########|")
            time.sleep(2)

            clear()
            print("Player 3rd card revealed")
            print(" ___________    ________ ___")
            print("||||########|  |        |###|")
            print("||||########|  |" + dealersHand[0][0] + dealersHand[0][1] + "     |###|")
            print("||||########|  |        |###|")
            print("||||########|  |        |###|")
            print("||||########|  |________|###|")
            print("                ___ ___ ________")
            print("               |   |   |        |")
            print("               |" + playersHand[0][0] + playersHand[0][1] + "|" + playersHand[1][0] + playersHand[1][1] + "|" + playersHand[2][0] + playersHand[2][1] + "     |")
            print("               |   |   |        |")
            print("               |   |   |        |") 
            print("               |___|___|________|")
            time.sleep(2)
            playerScore = cardScoreChecker(playersHand,3)
            print("TEST PRINT: Player Score is " + str(playerScore))
            print("END TEST PRINT")
            time.sleep(5)

            #TODO: Loop to check if player busted

            # /// DEALER 2ND CARD REVEAL ///
            clear()
            print("Dealer 2nd card revealed")
            print(" ___________    ___ ________")
            print("||||########|  |   |        |")
            print("||||########|  |" + dealersHand[0][0] + dealersHand[0][1] + "|" + dealersHand[1][0] + dealersHand[1][1] + "     |")
            print("||||########|  |   |        |")
            print("||||########|  |   |        |")
            print("||||########|  |___|________|")
            print("                ___ ___ ________")
            print("               |   |   |        |")
            print("               |" + playersHand[0][0] + playersHand[0][1] + "|" + playersHand[1][0] + playersHand[1][1] + "|" + playersHand[2][0] + playersHand[2][1] + "     |")
            print("               |   |   |        |")
            print("               |   |   |        |")
            print("               |___|___|________|")
            time.sleep(2)

            # /// DEALER 3RD CARD ///
            #TODO: Loop to decide whether dealer hits
            if (dealerHits == 0):
                clear()
                dealersHand[2][0] = fullDeck[0][0]
                dealersHand[2][1] = fullDeck[0][1]
                del fullDeck[0]
                print("Dealer hits: 3rd card dealt")
                print(" ___________    ___ ___ ________")
                print("||||########|  |   |   |########|")
                print("||||########|  |" + dealersHand[0][0] + dealersHand[0][1] + "|" + dealersHand[1][0] + dealersHand[1][1] + "|########|")
                print("||||########|  |   |   |########|")
                print("||||########|  |   |   |########|")
                print("||||########|  |___|___|########|")
                print("                ___ ___ ________")
                print("               |   |   |        |")
                print("               |" + playersHand[0][0] + playersHand[0][1] + "|" + playersHand[1][0] + playersHand[1][1] + "|" + playersHand[2][0] + playersHand[2][1] + "     |")
                print("               |   |   |        |")
                print("               |   |   |        |")
                print("               |___|___|________|")
                time.sleep(2)

                clear()
                print("Dealer 3rd card revealed")
                print(" ___________    ___ ___ ________")
                print("||||########|  |   |   |        |")
                print("||||########|  |" + dealersHand[0][0] + dealersHand[0][1] + "|" + dealersHand[1][0] + dealersHand[1][1] + "|" + dealersHand[2][0] + dealersHand[2][1] + "     |")
                print("||||########|  |   |   |        |")
                print("||||########|  |   |   |        |")
                print("||||########|  |___|___|________|")
                print("                ___ ___ ________")
                print("               |   |   |        |")
                print("               |" + playersHand[0][0] + playersHand[0][1] + "|" + playersHand[1][0] + playersHand[1][1] + "|" + playersHand[2][0] + playersHand[2][1] + "     |")
                print("               |   |   |        |")
                print("               |   |   |        |")
                print("               |___|___|________|")
                time.sleep(5)

                #TODO: Check if Dealer busts

                #TODO: Victory Checks
            else:
                #TODO: Dealer stands, victory checks
                print("PLAYER STANDS @3: DEALER STANDS @2")
                time.sleep(10)
                pass
            
        else:
            # /// PLAYER STANDS: 2 CARDS DEALT
            #TODO: Dealer hit if loop, bust check then victory check
            print("PLAYER STANDS @2: TODO: ADD DEALER IF LOOP")
            time.sleep(5)
            clear()
            print("Players stands at 2 cards")
            print(" ___________    ________ ___")
            print("||||########|  |        |###|")
            print("||||########|  |" + dealersHand[0][0] + dealersHand[0][1] + "     |###|")
            print("||||########|  |        |###|")
            print("||||########|  |        |###|")
            print("||||########|  |________|###|")
            print("                ___ ________")
            print("               |   |        |")
            print("               |" + playersHand[0][0] + playersHand[0][1] + "|" + playersHand[1][0] + playersHand[1][1] + "     |")
            print("               |   |        |")
            print("               |   |        |")
            print("               |___|________|")
            time.sleep(5)

            clear()
            print("Dealer 2nd card revealed")
            print(" ___________    ___ ________")
            print("||||########|  |   |        |")
            print("||||########|  |" + dealersHand[0][0] + dealersHand[0][1] + "|" + dealersHand[1][0] + dealersHand[1][1] + "     |")
            print("||||########|  |   |        |")
            print("||||########|  |   |        |")
            print("||||########|  |___|________|")
            print("                ___ ________")
            print("               |   |        |")
            print("               |" + playersHand[0][0] + playersHand[0][1] + "|" + playersHand[1][0] + playersHand[1][1] + "     |")
            print("               |   |        |")
            print("               |   |        |")
            print("               |___|________|")
            time.sleep(5)

            #TODO: Loop to decide whether dealer hits
            if(dealerHits == 0):
                clear()
                dealersHand[2][0] = fullDeck[0][0]
                dealersHand[2][1] = fullDeck[0][1]
                del fullDeck[0]
                print("Dealer hits: 3rd card dealt")
                print(" ___________    ___ ___ ________")
                print("||||########|  |   |   |########|")
                print("||||########|  |" + dealersHand[0][0] + dealersHand[0][1] + "|" + dealersHand[1][0] + dealersHand[1][1] + "|########|")
                print("||||########|  |   |   |########|")
                print("||||########|  |   |   |########|")
                print("||||########|  |___|___|########|")
                print("                ___ ________")
                print("               |   |        |")
                print("               |" + playersHand[0][0] + playersHand[0][1] + "|" + playersHand[1][0] + playersHand[1][1] + "     |")
                print("               |   |        |")
                print("               |   |        |")
                print("               |___|________|")
                time.sleep(2)

                clear()
                print("Dealer 3rd card revealed")
                print(" ___________    ___ ___ ________")
                print("||||########|  |   |   |        |")
                print("||||########|  |" + dealersHand[0][0] + dealersHand[0][1] + "|" + dealersHand[1][0] + dealersHand[1][1] + "|" + dealersHand[2][0] + dealersHand[2][1] + "     |")
                print("||||########|  |   |   |        |")
                print("||||########|  |   |   |        |")
                print("||||########|  |___|___|________|")
                print("                ___ ________")
                print("               |   |        |")
                print("               |" + playersHand[0][0] + playersHand[0][1] + "|" + playersHand[1][0] + playersHand[1][1] + "     |")
                print("               |   |        |")
                print("               |   |        |")
                print("               |___|________|")
                time.sleep(10)

                #TODO: Dealer bust check, victory check
            else:
                #TODO: Victory Check
                pass

            pass









        #End
        choice = input("Play again? (y/n)")
        if(choice == 'y'):
            state=1
        else:
            state=9


    while(state==9): #Program end
        clear()
        print("Game ended")
        print("Thanks for playing!")
        game = False