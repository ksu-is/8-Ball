'''
"Project name:8 ball Game"

"Author: Zainab Moshood and Kayla Mitchell"

"Date: December 4th, 2018"



"Description: This 8-ball game will generates random numbers to create a fortune-telling game that provides randomly selected answers to the player's questions."


'''

import random
import sys

print('Hello! My name is 8-Ball. What is your name?')
myname = input()

print( 'Do you want to play? [Y] ')
answer = input()
print( 'press N to quit whenever you are ready to quit the game) ')
answer == 'N'

ans = True

while ans:
    question =input ("Ask the magic 8 ball a question: (press N to quit) ")
    
    answers = random.randint(1,8)
    
    if question == "N":
        print("Thank You for Playing, See you next Time!")
        sys.exit()
    
    elif answers == 1:
        print ("Hahahha, sure")
    
    elif answers == 2:
        print ("If I told you, I'd have to kill you")
    
    elif answers == 3:
        print ("The only way you'll ever get that answer from me is to pry it from my cold, dead hands.")
    
    elif answers == 4:
        print ("If I told you, I'd have to kill you")
    
    elif answers == 5:
        print ("How dare you ask me that!")
    
    elif answers == 6:
        print ("Fear of the unknown is what imprisons us")
    
    elif answers == 7:
        print ("My reply is no")
    
    elif answers == 8:
        print ("My reply is yes")

    else:
        print('I apologies, I did not catch that. Please repeat.')
        Replay()
