
# Game Theory

## Project Description

In this project, you will be able to access the games and codes that I made which are shown to us in the Game Theory lecture. These games were created in Python. Within the scope of this project, information will be given about the rules and some details of **TCP Backoff, Prisoner's dilemma, Matching Pennies, Coordination, and Battle of the Sexes game**.

### Key Ingredients

#### Players

Players are the desicion makers. It might be people, goverments, companies or etc.

#### Actions

It is about what players can do in a game or auction. It is about what are you going to do in spesific situation. For example, decide how to vote or vote to who.

#### Payoffs

For example, do players care about some profit? Do they care about other players?

### Two Standart Representations

#### Normal Form

List what payoffs as a function or their actions. Players moved simultaneously.

Finite, $n$-person normal game: $\langle N, A, u \rangle:$

Players $N = \{ 1, 2, ... , n\}$ is a finite set of $n$, indexed by $i$.

Actions set for player $i$ $A_i$:

 - $a = (a_1, a_2, ... , a_n) \in A = A_1 x ... x A_n$ is an action
   profile.

Utility function of payoff function for player $i: u_i : A \mapsto \mathbb{R}.$

 - $u = (u_1, u_2, ... , u_n)$, is a profile of utility functions.

####  Extensive Form

Players move sequentially, represented as a tree like chess for example. We will keep track of what each player knows when he or she makes each desicion.

#### Standart Matrix Representation

Writing a 2-player game as a matrix:

 - Row: Player 1, it correspounds to actions $a_1 \in A_1$.
   
 -  Column: Player 2, it correspounds to actions $a_2 \in A_2$.
   
  - Cells listing utility or payoff values for each player; the row
   player first and then the column.

TCP Backoff Game written as matrix (more information about game on below).
|  | C | D |
|--|--|--|
| **C** | -1, -1 | -4, 0 |
| **D** | 0, -4 | -3, -3 |

#### A Large Collective Action Game

 - Player: $N = \{ 1, 2, ... , 100,000,000 \}$ 
   
  - Action set for player $i A_i = \{ Revolt, Not \}$
   
 - Utility function for player 
 
   $i$: $u_i(a) = 1$ if # $\{ j : a_j =    Revolt \} \ge 2,000,000$    
   $u_i(a) = -1$ if # $\{ j : a_j = Revolt \}    \lt 2,000,000$    
   $u_i(a) = 0$ if  # $\{ j : a_j = Revolt \} \lt    2,000,000$ and $a_i
   = Not$

## TCP Backoff

Internet traffic is governed by the TCP protocol. When the protocol is correctly implemented, it includes a “backoff mechanism”: if the rates at which a sender sends information packets into the network causes congestion, the sender reduces this rate for a while until the congestion subsides. A defective implementation of TCP does not back off when congestion occurs. Imagine that you and a colleague are the only people using the internet. You each have two possible strategies: C (using a correct implementation) and D (using a defective one). If both you and your colleague adopt C then you will both experience an average packet delay of 1 ms. If you both adopt D you will both experience a delay of 3 ms, because you will both experience more lost packets. If one of you adopts D and the other adopts C then the D adopter will experience no delay at all, and the C adopter will experience a delay of 4 ms. Of course, both you and your colleague want to minimize these delays.

|  | C | D |
|--|--|--|
| **C** | -1, -1 | -4, 0 |
| **D** | 0, -4 | -3, -3 |

Questions:

 - What action should a player of the game take?  
 - Would all users behave the same in this scenario?  
 - What global patterns of behaviour should the system designer expect?  
 - Under what changes to the delay numbers would behavior be the same?  
 - What effect would communication have? 
 - Repetitions? (finite? infinite?)
 - Does it matter if I believe that my opponent is rational?

Reference: [The University of British Columbia CS ISCI 330 Lecture 3](https://www.cs.ubc.ca/~kevinlb/teaching/isci330%20-%202006-7/Lectures/lect3.pdf) 


[Game code on Python 3.9](https://github.com/doguilmak/Game-Theory/blob/main/games/TCPgame.py):

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

Play the TCP Backoff game: http://gametheory.cs.ubc.ca/tcpbackoff?

## Prisoner's Dilemma


The prisoner's dilemma is a paradox in decision analysis in which two individuals acting in their own self-interests do not produce the optimal outcome. The prisoner's dilemma is a standard example of a game analyzed in game theory that shows why two completely rational individuals might not  cooperate, even if it appears that it is in their best interests to do so. It was originally framed by Merrill Flood and Melvin Dresher while working at RAND in 1950. Albert W. Tucker formalized the game with prison sentence rewards and named it "prisoner's dilemma", a version of which was stated by William Poundstone in his 1993 book Prisoner's Dilemma as:

Two members of a criminal gang are arrested and imprisoned. Each prisoner is in solitary confinement with no means of speaking to or exchanging messages with the other. The police admit they don't have enough evidence to convict the pair on the principal charge. They plan to sentence both to a year in prison on a lesser charge. Simultaneously, the police offer each prisoner a Faustian bargain.

It is implied that the prisoners will have no opportunity to reward or punish their partner other than the prison sentences they get and that their decision by itself will not affect their reputation in the future. As betraying a partner offers a greater reward than cooperating with them, all purely rational self-interested prisoners will betray the other, meaning the only possible outcome for two purely rational prisoners is for them to betray each other, even though mutual cooperation would yield greater reward. 

|  | B stays silent | B betrays |
|--|--|--|
| **A stays silent** | R, R | S, T |
| **A betrays** | T, S | P, P |

$T \gt R \gt P \gt S$

The payoff relation $R \gt P$ implies that mutual cooperation is superior to mutual defection, while the payoff relationships $T \gt R$ and $P \gt S$ imply that **defection is the dominant strategy for both agents**.

|  | B stays silent | B betrays |
|--|--|--|
| **A stays silent** | -1, -1 | -3, 0 |
| **A betrays** | 0, -3 | -2, -2 |

The possible outcomes are:

 - If A and B each betray the other, each of them serves two years in
   prison 
 - If A betrays B but B remains silent, A will be set free and B
   will serve three years in prison 
 - If A remains silent but B betrays A,    A will serve three years in
   prison and B will be set free    
 -  If A and B    both remain silent, both of them will serve one year in
   prison (on    the lesser charge).

References:
    -https://en.wikipedia.org/wiki/Prisoner's_dilemma
    -https://www.investopedia.com/terms/p/prisoners-dilemma.asp#:~:text=A%20prisoner's%20dilemma%20is%20a,many%20aspects%20of%20the%20economy.


## Matching Pennies

To be added soon...

## Coordination Game

To be added soon...

## Battle of the Sexes

To be added soon...

## Contact Me

If you have something to say to me please contact me: 

 - Twitter: [Doguilmak](https://twitter.com/Doguilmak)  
 - Mail address: doguilmak@gmail.com
 
