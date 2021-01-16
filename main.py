# TODO @austin create randomizing word function
# TODO @TK create user input letter + check if letter is in string function
# TODO @clarrie create draw hangman function + display letter bank

import random
import os
import time

def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

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




words = ['butterball','elephant','tree','computer','bank','apple',
         'house','orange','Albania','Armenia','Austria','Belgium',
         'Bulgaria','Lamborghini','Toyota','Mercedes','Honda',
         'Nissan','Chile','Pear','Calculator','Oven','Cat',
         'Llizard','Iguana','Google','Phone','Wheels','Mouse',
         'Lion','Leafs','Montreal','Toronto','California','Stump',
         'Japan','Tokyo','Fast','Furious','Supra','super','Skyline',
         'dinosaur','Case','Dirtbike','Yamaha','Mercury','Volvo',
         'Suzuki','Boat','buffalo'
        ]

guesses = 6
word = random.choice(words).lower()
word = list(word)
guessed_letters = []
    
while guesses > 0:
  hidden_word = [x if x in guessed_letters else '-' for x in word]
  print(" ".join(hidden_word))
  whichdrawing(guesses)
  guess = input("\nEnter a letter: ")
  guessed_letters.append(guess)
  print(guessed_letters)
  if guess in word:
    print("You have guessed a correct letter!")
    time.sleep(3)
    clear()
  else:
    guesses -= 1
    print("Sorry, you have entered an incorrect letter.")
    print("You have {} guesses left.".format(guesses))
    time.sleep(3)
    clear()
if guesses == 0:
  print("Sorry, the word was:")
  word = [print(x, end = "") for x in word]
  print("\nBetter luck next time!")