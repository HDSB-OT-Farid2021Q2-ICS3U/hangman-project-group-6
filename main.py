# Clarrie,Tk,Austin
# date and time completed: Jn 18 2021
#We have creted a hangman project that asks the user to geuss letters to see if they can get the word that we have pulled from our wordbank


#importing all of the libraries we need
import random
import os
import time

#Here we are creating the clear fucntion to clear the screen for both windows and mac os.

def clear():
    if os.name == 'posix':#This part here is to clear for mac and repl
        os.system('clear')
    else:
        os.system('cls')#This clears the screen for windows


#Here we have created the fucntion to draw the hangman so depending on the amount of incorrect guesses the user has left determines how much of the hangman will be drawn.  The hangman was created by using ascii art.
def whichdrawing(guessesleft):
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
  guessed_letters = []#creating a list so we can add all of the guessed letter to it.
      
  while guesses > 0:#While guesses is above 0 the loop will continue
      time.sleep(3)#Giving the user 3 second to look things over before clearign the screen
      clear()#clearing the screen
      hidden_word = [x if x in guessed_letters else '-' for x in word]
      
      if '-' not in hidden_word:
        break
      
      print(" ".join(hidden_word))
      whichdrawing(guesses)#Calling whichdrawing and having it draw depending the amount of guesses left
      guess = input("\nEnter a letter: ")#Having the user enter their input
      guess = guess.lower() #Lowercasing the user's guess
      
      if guess.isalpha() == True and len(guess) == 1:#Here we are making sure the users input is a letter and not more than one digit
        if guess not in guessed_letters:
            guessed_letters.append(guess)#Adding the users letter to the list of guessed letters
            print(guessed_letters)#Printing the letters the user has already geussed so they can see them
            if guess in word:#If the users guess is in the word from the wordbank tell them it is correct
              print("You have guessed a correct letter!")
            else:
                guesses -= 1#If the user guessed an inccorect letter than they come here and we take away one of their lives
                print("Sorry, you have entered an incorrect letter.")
                print("You have {} guesses left.".format(guesses))#telling them how many lives they have left
        else:
          print("You have already typed a letter that you guessed. Please try again.")
      else:
            print('You have entered an invalid input please try again')#If the users input is not a letter or longer than a digit telling them that then they just retart without taking away any lives
  
  time.sleep(3)#Giving the user 3 second to look things over before clearign the screen
  clear()#clearing the screen

  if guesses == 0:#If they have exhausted all their lives they are here
    print("Sorry, the word was:") 
    word = [print(x, end = "") for x in word]#printing the word the user was trying to geuss
    print("\nBetter luck next time!")
  else:#Otherwise if they are here that is because we broke the loop above when they geussed the word
    print('You win!')#telling them they won

  play = input('Would you like to play again? [Y/N] ').upper()#Asking them if they would like to play again and uppercasing the letter
  if play == 'N':#If play is n then the loop will not retart
    print('Bye!')
  elif play == 'Y':#If they input Y then the loop will continue as it should
    continue#having the loop continue again as there needed teh