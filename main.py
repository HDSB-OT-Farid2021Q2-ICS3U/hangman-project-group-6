# Clarrie,Tk,Austin
# date and time completed: Jn 18 2021
#We have created a hangman project that asks the user to guess letters to see if they can get the word that we have pulled from our wordbank


#importing all of the libraries we need
import random
import os
import time

#Here we are creating the clear fucntion to clear the screen for both windows and mac os.


def clear():
    """Fucntion to clear the screen"""
    if os.name == 'posix':#This part here is to clear for mac and repl
        os.system('clear')
    else:
        os.system('cls')#This clears the screen for windows

def startScreen():
    """Start Screen For user"""
    print('To win the game you have to guess the word before the whole hangman is drawn.')
    time.sleep(3)
    clear()


#Here we have created the fucntion to draw the hangman so depending on the amount of incorrect guesses the user has left determines how much of the hangman will be drawn.  The hangman was created by using ascii art.
def whichdrawing(guessesleft):
    """Deciding which drawing to use"""
    if guessesleft == 6:
        start()
    elif guessesleft == 5:
        head()
    elif guessesleft == 4:
        torso()
    elif guessesleft == 3:
        leftarm()
    elif guessesleft == 2:
        rightarm()
    elif guessesleft == 1:
        leftleg()
    elif guessesleft == 0:
        rightleg()
#All the hangman ascii art
def start():
    """hanging part"""
    print(r"""_______           
|     |
|
|
|
|
|
|
-----------""")

def head():
    """head"""
    print(r"""_______           
|     |
|     O
|
|
|
|
|
-----------""")

def torso():
    """Head and body"""
    print(r"""_______           
|     |
|     O
|     |
|     |
|
|
|
-----------""")

def leftarm():
    """Head,body,left arm"""
    print(r"""_______           
|     |
|     O
|    /|
|   / |
|
|
|
-----------""")

def rightarm():
    """Head,body,left arm,right arm"""
    print(r"""_______           
|     |
|     O
|    /|\
|   / | \
|    
|      
|
-----------""")

def leftleg():
    """Head,body,left arm,right arm,left leg"""
    print(r"""_______           
|     |
|     O
|    /|\
|   / | \
|    / 
|   /  
|
-----------""")

def rightleg():
    """Full Body"""
    print(r"""_______           
|     |
|     O
|    /|\
|   / | \
|    / \
|   /   \
|
-----------""")



clear()
startScreen()

#Setting the variable play to y so that the first time the user loads up the game they will automatically be entered into the game
play = 'Y'
#Loop will continue as long as the user still would like to play.
while play == 'Y':
    #Here we have created a word bank for all of the possible words to be used in our hangman game
  words = ('butterball','elephant','tree','computer','bank','apple',
          'house','orange','Albania','Armenia','Austria','Belgium',
          'Bulgaria','Lamborghini','Toyota','Mercedes','Honda',
          'Nissan','Chile','Pear','Calculator','Oven','Cat',
          'Llizard','Iguana','Google','Phone','Wheels','Mouse',
          'Lion','Leafs','Montreal','Toronto','California','Stump',
          'Japan','Tokyo','Fast','Furious','Supra','super','Skyline',
          'dinosaur','Case','Dirtbike','Yamaha','Mercury','Volvo',
          'Suzuki','Boat','buffalo','canada','spelling'
          )

  wrongguesses = 6   #Setting the amount of wrong guesses the user has to 6 
  word = random.choice(words).lower() #making sure all of the words from the list are lower
  word = list(word)#making the variable a list
  guessed_letters = []#creating a list so we can add all of the guessed letter to it.
      
  while wrongguesses > 0:#While guesses is above 0 the loop will continue
      time.sleep(3)#Giving the user 3 second to look things over before clearing the screen
      clear()#clearing the screen
      hidden_word = [x if x in guessed_letters else '-' for x in word]#goes throught he hidden word and prints the letter if the letter is in the guessesd letters list otherwise it prints a dash
      
      if '-' not in hidden_word:
        break
      
      print(" ".join(hidden_word))
      whichdrawing(wrongguesses)#Calling whichdrawing and having it draw depending the amount of guesses left
      if guessed_letters != []:
        print(guessed_letters)#Printing the letters the user has already guessed so they can see them
      
      guess = input("\nEnter a letter: ").lower()#Having the user enter their input and lowercasing the user's guess
      
      if guess.isalpha() == True and len(guess) == 1:#Here we are making sure the users input is a letter and not more than one digit
        if guess not in guessed_letters:
            guessed_letters.append(guess)#Adding the users letter to the list of guessed letters
            if guess in word:#If the users guess is in the word from the wordbank tell them it is correct
              print("You have guessed a correct letter!")
            else:
                wrongguesses -= 1#If the user guessed an inccorect letter than they come here and we take away one of their lives
                print("Sorry, you have entered an incorrect letter.")
                print("You have {} wrong guesses left.".format(wrongguesses))#telling them how many lives they have left
        else:
          print("You have typed a letter that you already guessed. Please try again.")
      else:
            print('You have entered an invalid input please try again')#If the users input is not a letter or longer than a digit telling them that then they just retart without taking away any lives
  
  time.sleep(3)#Giving the user 3 seconds to look things over before clearing the screen
  clear()#clearing the screen

  if wrongguesses == 0:#If they have exhausted all their lives they are here
    print("Sorry, the word was:") 
    word = [print(x, end = "") for x in word]#printing the word the user was trying to guess
    print("\nBetter luck next time!")
  else:#Otherwise if they are here that is because we broke the loop above when they guessed the word
    print('You win!')#telling them they won

  play = input('Would you like to play again? [Y/N] ').upper()#Asking them if they would like to play again and uppercasing the letter
  if play == 'N':#If play is n then the loop will not retart
    clear()
    print('Bye!')
  elif play == 'Y':#If they input Y then the loop will continue as it should
    continue#having the loop continue again as there needed teh