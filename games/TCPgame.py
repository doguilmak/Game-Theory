# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 17:49:47 2022

@author: dogilmak

TCP Backoff Game

Internet traffic is governed by the TCP protocol. 
When the protocol is correctly implemented, it includes a “backoff mechanism”: 
if the rates at which a sender sends information packets into the network 
causes congestion, the sender reduces this rate for a while until the 
congestion subsides. A defective implementation of TCP does not back off when
congestion occurs. Imagine that you and a colleague are the only people using
the internet. You each have two possible strategies: C 
(using a correct implementation) and D (using a defective one). If both you 
and your colleague adopt C then you will both experience an average packet 
delay of 1 ms. If you both adopt D you will both experience a delay of 3 ms, 
because you will both experience more lost packets. If one of you adopts D 
and the other adopts C then the D adopter will experience no delay at all, 
and the C adopter will experience a delay of 4 ms. Of course, both you and 
your colleague want to minimize these delays.

"""
import random
your_adopter=0
another_adopter=0      
    
games2play = int(input('How many games would you like to play?\n'))
possible_actions = ["correct", "defective"] 
while True:
    
    if games2play == 0:
        print("\nRANDOM SELECTION")
        print(f"Your adopter's delay in total: {your_adopter} ms.")
        print(f"Another adopter's delay in total: {another_adopter} ms.")
        break   
        
    computer_action_random = random.choice(possible_actions)
    print("\n --------------------------\n")
    user_action = input("Enter a choice (correct, defective): \n")
    print(f"You chose {user_action}, computer chose {computer_action_random}.")
    if user_action == "correct" and computer_action_random == "correct":
        print("Users are going to experience an average packet delay of 1 ms.")
        your_adopter+=1
        another_adopter+=1
        
    elif user_action == "defective" and computer_action_random == "correct":
        print("You will experience no delay at all, and the other adopter will experience a delay of 4 ms.")
        your_adopter+=0
        another_adopter+=4

    elif user_action == "correct" and computer_action_random == "defective":
        print("You will experience a delay of 4 ms, and the other adopter will experience no delay at all.")
        your_adopter+=4
        another_adopter+=0
        
    elif user_action == "defective" and computer_action_random == "defective":
        print("Your colleague choone defective implementation too. Users are going to experience an average packet delay of 3 ms.")
        your_adopter+=3
        another_adopter+=3
        
    else:
        print("Unexpected input.")
        
    games2play-=1
