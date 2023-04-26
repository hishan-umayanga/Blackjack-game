from art import logo

import time, sys
#The time module in Python provides functions for handling time-related tasks.
#The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment. It allows operating on 
# the interpreter as it provides access to the variables and functions that interact strongly with the interpreter
import random


import os
clear = lambda: os.system('cls')




def animetion(str):
 for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    # Python’s standard out is buffered. This means that it collects some data before it is written to standard out and 
    # when the buffer gets filled, then it is written on the terminal or any other output stream.

    time.sleep(0.0001)


def deal_cards():
    """ return the random card from the deck """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
   
def calculate_score(cards):
    """ take a list of cardas  and return the score calculated frem the cards """
#check  if the sum of the cards is 21 or not to identified this is the blackJack
    if sum(cards)==21 and len(cards)== 2:
           return 0

    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)  

#hint 15
def compare(user_score,computer_score):
    if user_score== computer_score:
        return "Draw !!!"
    elif computer_score==0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "win with the Blackjack"
    elif user_score > 21:
        return "you went over you loose !!!!"
    elif   computer_score >21:
        return "Opponent went over, You win !!" 
    elif user_score> computer_score:
        return "you win"
    else:
         return "you lose !!"     

def play_game():

    print(logo)

    user_cards=[]
    computer_cards=[]   
    is_game_over=False

    #get two random cards into user and computer
    for _ in range(2):
        
        #add single item to a list we use append
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not  is_game_over:
    #calculate the score both user and computer
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        animetion(f"Your cards : {user_cards}, current score: {user_score}\n")
        animetion(f"Computer's first card:{computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score >21:
            is_game_over=True

        else:
            user_should_deal=input("\nType 'y' to get another card, type 'n to pass: ")
            if user_should_deal =="y":
                user_cards.append(deal_cards())
            else:
                is_game_over=True
        
    while computer_score != 0 and computer_score<17:
        computer_cards.append(deal_cards())
        computer_score=calculate_score(computer_cards)

    print(f"   your final hand: {user_cards}, final score: {user_score} \n")
    print(f"   computer's finale hand : {computer_cards},   finale score : {computer_score}\n")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack ? Type 'y' or 'n':  " ):
     clear()
     play_game()
