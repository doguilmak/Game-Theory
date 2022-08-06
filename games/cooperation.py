# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 00:50:41 2022

@author: dogilmak

Cooperation-Cooperation Game

Here's the other extreme, of games of pure coordination or pure cooperation. 
In this case, all agents have exactly the same interest. In other words, the 
payoffs for every action vector that they take is the same. And so the utility 
for player 'i' is always the same as the utility for player 'j' for every 
action vector that they choose. And so again we here, too, will need to write 
each cell of matrix only one number because it's common to all the players. 
It's drives home that perhaps the unfortunate term "noncooperate" game theory 
that describes this dominant strand of game theory that we are discussing for 
now It's, the name was suggested these are games for, that descibe situations 
that are inherently conflictual but as we see they apply also to games in which 
the interests of the players coincide. So here's a game that describes the 
purely cooperative situation. You and I walk towards each other on the sidewalk. 
We can each decide whether to go to our respective left or respective right. 
And if we pick the same side then all is good. We avoid a collision. If we 
don't, then we do collide and that's equally bad for both of us. Of course in 
general, games will be neither purelly cooperative nor purely conflictual and 
here's a game that exemplifies that.

References:
    -https://en.wikipedia.org/wiki/Coordination_game
    -Game Theory - https://www.coursera.org/learn/game-theory-1
"""
import random
your_desicion=0
person_desicion=0      
    
games2play = int(input('How many games would you like to play?\n'))
possible_actions = ["left", "right"] 
while True:
    
    if games2play == 0:
        print("\nRANDOM SELECTION")
        print(f"You and your friend choose the same way {your_desicion} times.")
        break   
        
    person_action_random = random.choice(possible_actions)
    print("\n --------------------------\n")
    user_action = input("Enter a choice (left, right): \n")
    print(f"You chose {user_action}, person chose {person_action_random}.")
    if user_action == "left" and person_action_random == "left":
        print("You both took the same way!")
        your_desicion+=1
        person_desicion+=1
        
    elif user_action == "left" and person_action_random == "right":
        print("Unfortunately you both didn't choose the same way.")

    elif user_action == "right" and person_action_random == "left":
        print("Unfortunately you both didn't choose the same way.")
        
    elif user_action == "right" and person_action_random == "right":
        print("You both took the same way!")
        your_desicion+=1
        person_desicion-=1
        
    else:
        print("Unexpected input.")
        
    games2play-=1