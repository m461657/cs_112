# -*- coding: utf-8 -*-
import random
class Card:
    def __init__(self,r,s,v):
        
        self.rank = r
        self.suit = s
        self.value = v
    
    def __str__(self):
        return("Rank: " + str(self.rank) + " Suit: " + str(self.suit) + " Blackjack Value: " + str(self.value))
        
def makeADeckOf52():
    
    NUM_OF_CARDS_IN_DECK=52
    deck = []
    
    for i in range (0,NUM_OF_CARDS_IN_DECK):
        deck.append(i)
    random.shuffle(deck)
    
    #print(deck)
    #print()
    #print(sorted(deck))
    
    return(deck)
    
def instructions():
    
    print("This is a blackjack game.\nYou will get two cards per hand.\nThe goal is to add the cards up to 21.\n")
    print("If you choose to draw another hand that goes over than 21, you lose the game.\n")
    
def dealAHand(deck):
    
    i=0
    hand = []
    for i in range(2):
        hand.append(deck.pop())
    #print(*hand)
    
    return(hand)
    
def main():
    
    instructions()
    deck = makeADeckOf52()
    hand= dealAHand(deck)
    bJValue = 0
    for card in hand:
        
        suit = getSuit(card)
        rank = getRank(card)
        value = getValue(rank, bJValue)
    
        for i in hand:
            card = Card(rank, suit, value)
        bJValue += card.value
        
        print(card)
    print("Blackjack value sum: " + str(bJValue))
    
    continueG = input("Would you like to get another card? (y/n)")
    if continueG == "y":
        continueGame(continueG, bJValue, deck)
    else:
        print("Game over")
    
def getSuit(card):
    
    card+=1
    if card in range(1,14):
        suit = "♣"
    if card in range(14,27):
        suit = "♦"
    if card in range(27,40):
        suit = "♥"
    if card in range(40,53):
        suit = "♠" 
    
    return(suit)
        
def getRank(card):
    
    ace = [1,14,27,40]
    jacks = [11,24,37,50]
    queens = [12,25,38,51]
    kings = [13,26,39,52]

    card +=1
    #print(card)
    if card in ace:
        rank = "A"
    if card in range(2,11):
        rank = card
    if card in range(15,24) or card in range(28,37) or card in range(41,50):
        rank = card%13
    if card in jacks:
        rank = "J"
    if card in queens:
        rank = "Q"
    if card in kings:
        rank = "K"
        card = 0
    #print(rank)
    return(rank)
    
def getValue(rank, bJValue):
    #print(rank)
    if rank == "K" or rank == "Q" or rank == "J":
        value = 10
    else:
        value = rank
        if value == "A":
            if bJValue + 10 <= 21:
                value = 10
            else:
                value = 1
    return(value)
    
def getAnotherCard(deck):
    for i in range(1):
        anotherCard = deck.pop()
        return(anotherCard)
        
def continueGame(continueG, bJValue, deck):

    while continueG == "y":
        
        card = getAnotherCard(deck)
        suit = getSuit(card)
        rank = getRank(card)
        value = getValue(rank, bJValue)
        card = Card(rank, suit, value)
        
        print(card)
        
        bJValue += card.value
        
        if bJValue < 21:
            print("Blackjack value sum: " + str(bJValue))
            continueG = input("Would you like another card? (y/n)")
        elif bJValue == 21:
            print("You've won the game!!")
            continueG == "n"
            return(continueG)
        elif bJValue >21:
            print("Blackjack value sum: " + str(bJValue) + ", is >21")
            continueG = "n"
        
    print("Game over")


main()        