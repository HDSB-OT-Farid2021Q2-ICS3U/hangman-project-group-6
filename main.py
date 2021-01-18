


#importing all of the libraries we need
import random
import os
import time

#Here we are creating the clear fucntion to clear the screen for both windows and mac os.

def clear():
    if os.name == 'posix':#This part here is to clear for windows and mac
        os.system('clear')
    else:
        os.system('cls')#This clears the screen for windows


#Here we have created the fucntion to draw the hangman so depending on the amount of incorrect guesses the user has left determines how much of the hangman will be drawn.  The hangman was created by using ascii art.
def whichdrawing(wrongguesses):
    if wrongguesses == 6:
        start()
    elif wrongguesses == 5:
        head()
    elif wrongguesses == 4:
        torso()
    elif wrongguesses == 3:
        leftarm()
    elif wrongguesses == 2:
        rightarm()
    elif wrongguesses == 1:
        leftleg()
    elif wrongguesses == 0:
        rightleg()
#All the hangman ascii art
def start():
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
  print(r"""_______           
|     |
|     O
|    /|\
|   / | \
|    / \
|   /   \
|
-----------""")

 #Setting the variable play to y so that the first time the user loads up the game they will automatically be entered into the game

play = 'Y'
#Loop will continue as long as the user still would like to play.
while play == 'Y':
    #Here we have created a word bank for all of the possible words to be used in our hangman game
  words = ['butterball','elephant','tree','computer','bank','apple',
          'house','orange','Albania','Armenia','Austria','Belgium',
          'Bulgaria','Lamborghini','Toyota','Mercedes','Honda',
          'Nissan','Chile','Pear','Calculator','Oven','Cat',
          'Llizard','Iguana','Google','Phone','Wheels','Mouse',
          'Lion','Leafs','Montreal','Toronto','California','Stump',
          'Japan','Tokyo','Fast','Furious','Supra','super','Skyline',
          'dinosaur','Case','Dirtbike','Yamaha','Mercury','Volvo',
          'Suzuki','Boat','buffalo','canada','spelling'
          ]

  guesses = 6   #Setting the amount of geusses the user has to 6 
  word = random.choice(words).lower() #making sure all of the words from the list are lower
  word = list(word)#making the variable a list
  guessed_letters = []#creating a list so we can add all of the geussed letter to it.
      
  while guesses > 0:#While guesses is above 0 the loop will continue
      hidden_word = [x if x in guessed_letters else '-' for x in word]
      if '-' not in hidden_word:
        break
      print(" ".join(hidden_word))
      whichdrawing(guesses)#Calling whichdrawing and having it draw depending the amount of guesses left
      guess = input("\nEnter a letter: ")#Having the user enter their input
      guess = guess.lower() #Lowercasing the users geuss
      

      if guess.isalpha() == True and len(guess) == 1:#Here we are making sure the users input is a letter and not more than digit
          guessed_letters.append(guess)#Adding the users letter to the list of guessed letters
          print(guessed_letters)#Printing the letters the user has already geussed so they can see them
          if guess in word:#If the users geuss is in the word from the wordbank tell them it is correct
              print("You have guessed a correct letter!")
              time.sleep(3)#Giving the user 3 second before clearing the screen
              clear()#cleraing the screen
          else:
              guesses -= 1
              print("Sorry, you have entered an incorrect letter.")
              print("You have {} guesses left.".format(guesses))
              time.sleep(3)
              clear()
      else:
          print('You have entered an invalid input please try again')
          time.sleep(3)
          clear()  
  if guesses == 0:
    print("Sorry, the word was:")
    word = [print(x, end = "") for x in word]
    print("\nBetter luck next time!")
  else:
    print('You win!')

  play = input('Would you like to play again? [Y/N] ').upper()
  if play == 'N':
    print('Bye!')
  elif play == 'Y':
    continue