# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 23:54:55 2022

@author: dogilmak

Prisoner's Dilemma

The prisoner's dilemma is a paradox in decision analysis in which two 
individuals acting in their own self-interests do not produce the optimal 
outcome. The prisoner's dilemma is a standard example of a game analyzed in 
game theory that shows why two completely rational individuals might not 
cooperate, even if it appears that it is in their best interests to do so. 
It was originally framed by Merrill Flood and Melvin Dresher while working 
at RAND in 1950. Albert W. Tucker formalized the game with prison sentence 
rewards and named it "prisoner's dilemma",[1] a version of which was stated 
by William Poundstone in his 1993 book Prisoner's Dilemma as:

Two members of a criminal gang are arrested and imprisoned. Each prisoner is 
in solitary confinement with no means of speaking to or exchanging messages 
with the other. The police admit they don't have enough evidence to convict 
the pair on the principal charge. They plan to sentence both to a year in 
prison on a lesser charge. Simultaneously, the police offer each prisoner a 
Faustian bargain.

The possible outcomes are:

If A and B each betray the other, each of them serves two years in prison
If A betrays B but B remains silent, A will be set free and B will serve three years in prison
If A remains silent but B betrays A, A will serve three years in prison and B will be set free
If A and B both remain silent, both of them will serve one year in prison (on the lesser charge).

References:
    -https://en.wikipedia.org/wiki/Prisoner's_dilemma
    -https://www.investopedia.com/terms/p/prisoners-dilemma.asp#:~:text=A%20prisoner's%20dilemma%20is%20a,many%20aspects%20of%20the%20economy.
"""
import random
you_as_prisoner=0
another_prisoner=0      
    
games2play = int(input('How many games would you like to play?\n'))
possible_actions = ["silent", "betrays"] 
while True:
    
    if games2play == 0:
        print("\nRANDOM SELECTION")
        print(f"Your serves in prison as year: {you_as_prisoner}")
        print(f"Prisoners serves in prison as year: {another_prisoner}")
        break   
        
    prisoner_action_random = random.choice(possible_actions)
    print("\n --------------------------\n")
    user_action = input("Enter a choice (silent, betrays): \n")
    print(f"You chose {user_action}, prisoner chose {prisoner_action_random}.")
    if user_action == "silent" and prisoner_action_random == "silent":
        print("Each of you serves 1 years in prison.")
        you_as_prisoner+=1
        another_prisoner+=1
        
    elif user_action == "silent" and prisoner_action_random == "betrays":
        print("You will will serve three years in prison and prisoner will be set free.")
        you_as_prisoner+=3
        another_prisoner+=0

    elif user_action == "betrays" and prisoner_action_random == "silent":
        print("You will be set free and another prisoner will serve three years in prison.")
        you_as_prisoner+=0
        another_prisoner+=3
        
    elif user_action == "betrays" and prisoner_action_random == "betrays":
        print("Each of you serves two years in prison.")
        you_as_prisoner+=2
        another_prisoner+=2
        
    else:
        print("Unexpected input.")
        
    games2play-=1