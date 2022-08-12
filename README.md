
# Game Theory

## Project Description

In this project, you will be able to access the games and codes that I made which are shown to us in the Game Theory lecture. These games were created in Python. Within the scope of this project, information will be given about the rules and some details of **TCP Backoff, Prisoner's dilemma, Matching Pennies, Coordination, and Battle of the Sexes game**.

---


### Key Ingredients

#### Players

Players are the desicion makers. It might be people, goverments, companies or etc.

#### Actions

It is about what players can do in a game or auction. It is about what are you going to do in spesific situation. For example, decide how to vote or vote to who.

#### Payoffs

For example, do players care about some profit? Do they care about other players?

<br>

### Two Standart Representations

#### Normal Form

List what payoffs as a function or their actions. Players moved simultaneously.

Finite, $n$-person normal game: $\langle N, A, u \rangle:$

 - Players $N = \{ 1, 2, ... , n \}$ is a finite set of $n$, indexed by $i$.

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

<br>

|  | $$C$$ | $$D$$ |
|:--:|:--:|:--:|
| **$$C$$** | $-1$, $-1$ | $-4$, $0$ |
| **$$D$$** | $0$, $-4$ | $-3$, $-3$ |

#### A Large Collective Action Game

 - Player: $N = \{1, 2, ... , 100.000.000\}$ 
   
 - Action set for player $i A_i = \{ Revolt, Not \}$
   
 - Utility function for player 

   $i$: $u_i(a) = 1$ if # $\{ j : a_j =    Revolt \} \ge 2,000,000$    
   $u_i(a) = -1$ if # $\{ j : a_j = Revolt \}    \lt 2,000,000$    
   $u_i(a) = 0$ if  # $\{ j : a_j = Revolt \} \lt    2,000,000$ and $a_i = Not$


### Best Response

the best response is **the strategy (or strategies) which produces the most favorable outcome for a player, taking other players' strategies as given.**

Let $a_{-i}$ = $\langle a_1, ...\ , a_{i-1}, a_{i+1}, ...\ , a_n \rangle$, now $a = (a_{-i}, a_i)$:

$$a^*_{i} \in BR(a_{-i}) \iff \forall a_i \in A_i, u_i(a^*_{i}, a_{-i}) \ge u_i(a_{i}, a_{-i}).$$

### Nash Equilibrium

Nash equilibrium is a concept within game theory where the optimal outcome of a game is where there is no incentive to deviate from the initial strategy. More specifically, the Nash equilibrium is a concept of game theory where the optimal outcome of a game is one where no player has an incentive to deviate from their chosen strategy after considering an opponent's choice.1

Overall, an individual can receive no incremental benefit from changing actions, assuming other players remain constant in their strategies. A game may have multiple Nash equilibria or none at all.

$a = \langle a_1, ...\ , a_n \rangle$ is a **Pure Strategy** Nash Equilibrium $\iff \forall_i, a_i \in BR(a_{-i}).$

Reference: 
 - [Investopedia](https://www.cs.ubc.ca/~kevinlb/teaching/isci330%20-%202006-7/Lectures/lect3.pdf)
 - [Coursera Game Theory](https://www.coursera.org/learn/game-theory-1)


## TCP Backoff

Internet traffic is governed by the TCP protocol. When the protocol is correctly implemented, it includes a **backoff mechanism**: if the rates at which a sender sends information packets into the network causes congestion, the sender reduces this rate for a while until the congestion subsides. A defective implementation of TCP does not back off when congestion occurs. Imagine that you and a colleague are the only people using the internet. You each have two possible strategies: $C$ (using a correct implementation) and $D$ (using a defective one). If both you and your colleague adopt $C$ then you will both experience an average packet delay of 1 ms. If you both adopt $D$ you will both experience a delay of 3 ms, because you will both experience more lost packets. If one of you adopts $D$ and the other adopts $C$ then the $D$ adopter will experience no delay at all, and the $C$ adopter will experience a delay of 4 ms. Of course, both you and your colleague want to minimize these delays.

|  | $$C$$ | $$D$$ |
|:--:|:--:|:--:|
| **$$C$$** | $-1$, $-1$ | $-4$, $0$ |
| **$$D$$** | $0$, $-4$ | $-3$, $-3$ |

Questions:

 - What action should a player of the game take?  
 - Would all users behave the same in this scenario?  
 - What global patterns of behaviour should the system designer expect?  
 - Under what changes to the delay numbers would behavior be the same?  
 - What effect would communication have? 
 - Repetitions? (finite? infinite?)
 - Does it matter if I believe that my opponent is rational?

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

Reference: 
 - [The University of British Columbia CS ISCI 330 Lecture 3](https://www.cs.ubc.ca/~kevinlb/teaching/isci330%20-%202006-7/Lectures/lect3.pdf) 

## Prisoner's Dilemma

The prisoner's dilemma is a paradox in decision analysis in which two individuals acting in their own self-interests do not produce the optimal outcome. The prisoner's dilemma is a standard example of a game analyzed in game theory that shows why two completely rational individuals might not  cooperate, even if it appears that it is in their best interests to do so. It was originally framed by Merrill Flood and Melvin Dresher while working at RAND in 1950. Albert W. Tucker formalized the game with prison sentence rewards and named it **prisoner's dilemma**, a version of which was stated by William Poundstone in his 1993 book Prisoner's Dilemma as:

Two members of a criminal gang are arrested and imprisoned. Each prisoner is in solitary confinement with no means of speaking to or exchanging messages with the other. The police admit they don't have enough evidence to convict the pair on the principal charge. They plan to sentence both to a year in prison on a lesser charge. Simultaneously, the police offer each prisoner a Faustian bargain.

It is implied that the prisoners will have no opportunity to reward or punish their partner other than the prison sentences they get and that their decision by itself will not affect their reputation in the future. As betraying a partner offers a greater reward than cooperating with them, all purely rational self-interested prisoners will betray the other, meaning the only possible outcome for two purely rational prisoners is for them to betray each other, even though mutual cooperation would yield greater reward. 

|  | $$B\ stays\ silent$$ | $$B\ betrays$$ |
|:--:|:--:|:--:|
| **$$A\ stays\ silent$$** | $R$, $R$ | $S$, $T$ |
| **$$A\ betrays$$** | $T$, $S$ | $P$, $P$ |

<br>

$T \gt R \gt P \gt S$

The payoff relation $R \gt P$ implies that mutual cooperation is superior to mutual defection, while the payoff relationships $T \gt R$ and $P \gt S$ imply that **defection is the dominant strategy for both agents**.

|  | $B\ stays\ silent$ | $B\ betrays$ |
|:--:|:--:|:--:|
| **$A\ stays\ silent$** | $-1$, $-1$ | $-3$, $0$ |
| **$A\ betrays$** | $0$, $-3$ | $-2$, $-2$ |

The possible outcomes are:

 - If $A$ and $B$ each betray the other, each of them serves two years in
   prison 
 - If $A$ betrays $B$ but $B$ remains silent, $A$ will be set free and $B$
   will serve three years in prison 
 - If $A$ remains silent but $B$ betrays $A$, $A$ will serve three years in
   prison and $B$ will be set free    
 -  If $A$ and $B$ both remain silent, both of them will serve one year in
   prison (on    the lesser charge).


[Game code on Python 3.9](https://github.com/doguilmak/Game-Theory/blob/main/games/prisoners_dilemma.py):

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

References:

- [Wikipedia](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma)

- [Investopedia](https://www.investopedia.com/terms/p/prisoners-dilemma.asp#:~:text=A%20prisoner%27s%20dilemma%20is%20a,many%20aspects%20of%20the%20economy.)

## Matching Pennies

Matching pennies is the name for a simple game used in [game theory](https://en.wikipedia.org/wiki/Game_theory "Game theory"). It is played between two players, Even and Odd. One player wants to match, the other wants to mismatch. Each player has a [penny](https://en.wikipedia.org/wiki/Penny "Penny") and must secretly turn the penny to heads or tails. The players then reveal their choices simultaneously. If the pennies match (both heads or both tails), then Even keeps both pennies, so wins one from Odd ( $+1$ for Even, $−1$ for Odd). If the pennies do not match (one heads and one tails) Odd keeps both pennies, so receives one from Even ( $−1$ for Even, $+1$ for Odd).

<br>

|  | $$Heads$$ | $$Tails$$ |
|:--:|:--:|:--:|
| **$$Heads$$** | $1$, $-1$ | $-1$, $1$ |
| **$$Tails$$** | $-1$, $1$ | $1$, $-1$ |

<br>

Matching Pennies is a  [zero-sum game](https://en.wikipedia.org/wiki/Zero-sum_game "Zero-sum game")  because each participant's gain or loss of utility is exactly balanced by the losses or gains of the utility of the other participants. If the participants' total gains are added up and their total losses subtracted, the sum will be zero. The game can be written in a  [payoff matrix](https://en.wikipedia.org/wiki/Payoff_matrix "Payoff matrix")  (pictured right - from Even's point of view). Each cell of the matrix shows the two players' payoffs, with Even's payoffs listed first. Matching pennies is used primarily to illustrate the concept of  [mixed strategies](https://en.wikipedia.org/wiki/Mixed_strategy "Mixed strategy")  and a mixed strategy  [Nash equilibrium](https://en.wikipedia.org/wiki/Nash_equilibrium "Nash equilibrium").[[1]](https://en.wikipedia.org/wiki/Matching_pennies#cite_note-1) This game has no  [pure strategy](https://en.wikipedia.org/wiki/Pure_strategy "Pure strategy")  [Nash equilibrium](https://en.wikipedia.org/wiki/Nash_equilibrium "Nash equilibrium")  since there is no pure strategy (heads or tails) that is a  [best response](https://en.wikipedia.org/wiki/Best_response "Best response")  to a best response. In other words, there is no pair of pure strategies such that neither player would want to switch if told what the other would do. Instead, the unique Nash equilibrium of this game is in  [mixed strategies](https://en.wikipedia.org/wiki/Mixed_strategy "Mixed strategy"): each player chooses heads or tails with equal probability. In this way, each player makes the other indifferent between choosing heads or tails, so neither player has an incentive to try another strategy.

[Game code on Python 3.9](https://github.com/doguilmak/Game-Theory/blob/main/games/matching_pennies.py):

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

References:

 - [Wikipedia](https://en.wikipedia.org/wiki/Matching_pennies)
 - [Stanford University](http://web.stanford.edu/~rjohari/teaching/notes/336_lecture7_2007.pdf)

## Coordination Game

Here's the other extreme, of games of pure coordination or pure cooperation. In this case, all agents have exactly the same interest. In other words, the payoffs for every action vector that they take is the same. And so the utility for player $i$ is always the same as the utility for player $j$ for every action vector that they choose. And so again we here, too, will need to write each cell of matrix only one number because it's common to all the players. It's drives home that perhaps the unfortunate term **noncooperate** game theory that describes this dominant strand of game theory that we are discussing for now It's, the name was suggested these are games for, that descibe situations that are inherently conflictual but as we see they apply also to games in which the interests of the players coincide. So here's a game that describes the purely cooperative situation. We can each decide whether to go to our respective left or respective right. And if we pick the same side then it is all good for us. We are trying to avoid a collision in coordination game. If we don't do that, then we do collide and that's equally bad for both of us. We do not punish but we can't earn any payoff if we do collide. Of course in general, games will be neither purelly cooperative nor purely conflictual and here's a game that exemplifies that.

In this game, players have **exactly the same interests:**

 - No conflicts: all players wants to do or choose same things.
 - $\forall a \in A, \forall i, j, u_i(a) = u_j(a)$

<br>

|  | $$Left$$ | $$Right$$ |
|:--:|:--:|:--:|
| **$$Left$$** | $1$, $1$ | $0$, $0$ |
| **$$Right$$** | $0$, $0$ | $1$, $1$ |

<br>

[Game code on Python 3.9](https://github.com/doguilmak/Game-Theory/blob/main/games/cooperation.py):

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
	        person_desicion+=1
	        
	    else:
	        print("Unexpected input.")
	        
	    games2play-=1

References:

 - [Wikipedia](https://en.wikipedia.org/wiki/Coordination_game)
 - [Coursera Game Theory](https://www.coursera.org/learn/game-theory-1)

## Battle of the Sexes

Battle of sexes is the most interesting game combine elements of cooperation and
competition. In  game theory, the **battle of the sexes**  is a two-player coordination that also involves elements of conflict. The game was introduced in 1957 by  [R. Duncan Luce](https://en.wikipedia.org/wiki/R._Duncan_Luce "R. Duncan Luce")  and  [Howard Raiffa](https://en.wikipedia.org/wiki/Howard_Raiffa "Howard Raiffa")  in their classic book,  some authors prefer to avoid assigning sexes to the players and instead use Players 1 and 2, and some refer to the game as  **Bach or Stravinsky**, using two concerts as the two events. The game description here follows Luce and Raiffa's original story.

Imagine that a man and a woman hope to meet this evening, but have a choice between two events to attend, a prize fight. The man would prefer to go to prize fight. The woman would prefer the ballet. Both would prefer to go to the same event rather than different ones. If they cannot communicate, where should they go?

The  [payoff matrix](https://en.wikipedia.org/wiki/Payoff_matrix "Payoff matrix")  labeled **Battle of the Sexes** shows the payoffs when the man chooses a row and the woman chooses a column. In each cell, the first number represents the man's payoff and the second number the woman's.

<br>

|  | $$Prize\ Fight$$ | $$Ballet$$ |
|:--:|:--:|:--:|
| **$$Prize\ Fight$$** | $+10$, $+7$ | $0$, $0$ |
| **$$Ballet$$** | $0$, $0$ | $+7$, $+10$ |

<br>

[Game code on Python 3.9](https://github.com/doguilmak/Game-Theory/blob/main/games/battle_of_sexes.py):

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

References:

 - [Wikipedia](https://en.wikipedia.org/wiki/Battle_of_the_sexes_%28game_theory%29)
 - [Coursera Game Theory](https://www.coursera.org/learn/game-theory-1)

## Contact Me

If you have something to say to me please contact me: 

 - Twitter: [Doguilmak](https://twitter.com/Doguilmak)  
 - Mail address: doguilmak@gmail.com
 
