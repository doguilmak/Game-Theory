"""
Created on Fri Aug 12 18:14:22 2022

@author: dogilmak

Battle of Sexes

In game theory, the battle of the sexes is a two-player coordination game 
that also involves elements of conflict. The game was introduced in 1957 
by R. Duncan Luce and Howard Raiffa in their classic book, Games and 
Decisions. Some authors prefer to avoid assigning sexes to the players and 
instead use Players 1 and 2, and some refer to the game as Bach or Stravinsky, 
using two concerts as the two events.[2] The game description here follows 
Luce and Raiffa's original story.

Imagine that a man and a woman hope to meet this evening, but have a choice 
between two events to attend, a prize fight and a ballet. The man would prefer 
to go to prize fight. The woman would prefer the ballet. Both would prefer to 
go to the same event rather than different ones. If they cannot communicate, 
where should they go?

References:
    -https://en.wikipedia.org/wiki/Battle_of_the_sexes_(game_theory)
    -Game Theory - https://www.coursera.org/learn/game-theory-1
"""
import random
your_desicion=0
woman_desicion=0      
    
games2play = int(input('How many games would you like to play?\n'))
possible_actions = ["prize fight", "ballet"] 
while True:
    
    if games2play == 0:
        print("\nRANDOM SELECTION")
        print(f"Your reward: {your_desicion}.")
        print(f"Women's reward: {woman_desicion}.")
        break   
        
    person_action_random = random.choice(possible_actions)
    print("\n --------------------------\n")
    user_action = input("Enter a choice (prize fight, ballet): \n")
    print(f"You chose {user_action}, women chose {person_action_random}.")
    if user_action == "prize fight" and person_action_random == "prize fight":
        print("You both decided to go to Prize Fight.")
        your_desicion+=10
        woman_desicion+=7
        
    elif user_action == "prize fight" and person_action_random == "ballet":
        print("You both didn't satisfied.")

    elif user_action == "ballet" and person_action_random == "prize fight":
        print("You both didn't satisfied.")
        
    elif user_action == "ballet" and person_action_random == "ballet":
        print("You both decided to go to Ballet.")
        your_desicion+=7
        woman_desicion+=10
        
    else:
        print("Unexpected input.")
        
    games2play-=1