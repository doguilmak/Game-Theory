# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 23:55:43 2022

@author: dogilmak

Matching Pennies

Matching pennies is the name for a simple game used in game theory. 
It is played between two players, Even and Odd. Each player has a penny 
and must secretly turn the penny to heads or tails. The players then reveal 
their choices simultaneously. If the pennies match (both heads or both tails), 
then Even keeps both pennies, so wins one from Odd (+1 for Even, −1 for Odd). 
If the pennies do not match (one heads and one tails) Odd keeps both pennies, 
so receives one from Even (−1 for Even, +1 for Odd).

Matching Pennies is a zero-sum game because each participant's gain or loss of 
utility is exactly balanced by the losses or gains of the utility of the other 
participants. If the participants' total gains are added up and their total 
losses subtracted, the sum will be zero.

The game can be written in a payoff matrix (pictured right - from Even's point
of view). Each cell of the matrix shows the two players' payoffs, with Even's 
payoffs listed first.

Matching pennies is used primarily to illustrate the concept of mixed 
strategies and a mixed strategy Nash equilibrium.

References:
    -https://en.wikipedia.org/wiki/Matching_pennies
"""
import random
your_penny=0
person_penny=0      
    
games2play = int(input('How many games would you like to play?\n'))
possible_actions = ["heads", "tails"] 
while True:
    
    if games2play == 0:
        print("\nRANDOM SELECTION")
        print(f"Your penny: {your_penny}")
        print(f"Person's penny': {person_penny}")
        break   
        
    person_action_random = random.choice(possible_actions)
    print("\n --------------------------\n")
    user_action = input("Enter a choice (heads, tails): \n")
    print(f"You chose {user_action}, person chose {person_action_random}.")
    if user_action == "heads" and person_action_random == "heads":
        print("You took a penny.")
        your_penny+=1
        person_penny-=1
        
    elif user_action == "heads" and person_action_random == "tails":
        print("You lost a penny.")
        your_penny-=1
        person_penny+=1

    elif user_action == "tails" and person_action_random == "heads":
        print("You lost a penny")
        your_penny-=1
        person_penny+=1
        
    elif user_action == "tails" and person_action_random == "tails":
        print("You took a penny.")
        your_penny+=1
        person_penny-=1
        
    else:
        print("Unexpected input.")
        
    games2play-=1