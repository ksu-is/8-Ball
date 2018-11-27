'''

'''

import random
import sys

ans = True

while ans:
    question =input ("Ask the magic 8 ball a question: (press enter to quit) ")
    
    answers = random.randint(1,8)
    
    if question == "":
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

def Replay():
    print ('Do you have another question? [Y/N] ')
    reply = input()
    if reply == 'Y':
        Magic8Ball()
    elif reply == 'N':
        exit()
    else:
        print('I apologies, I did not catch that. Please repeat.')
        Replay()
