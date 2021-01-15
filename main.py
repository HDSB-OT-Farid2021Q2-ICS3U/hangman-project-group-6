# TODO @austin create randomizing word function
# TODO @TK create user input letter + check if letter is in string function
# TODO @clarrie create draw hangman function + display letter bank

def whichdrawing(wrongguesses):
    if wrongguesses == 0:
        start()
    elif wrongguesses == 1:
        head()
    elif wrongguesses == 2:
        torso()
    elif wrongguesses == 3:
        leftarm()
    elif wrongguesses == 4:
        rightarm()
    elif wrongguesses == 5:
        leftleg()
    elif wrongguesses == 6:
        rightleg()

def start():
    print(r"""_______           
    |
    |
    |
    |
    |
    |
    |
    -----------""")

def head():
    print(r"""_______           
    |
    |     O
    |
    |
    |
    |
    |
    -----------""")

def torso():
    print(r"""_______           
    |
    |     O
    |     |
    |     |
    |
    |
    |
    -----------""")

def leftarm():
    print(r"""_______           
    |
    |     O
    |    /|
    |   / |
    |
    |
    |
    -----------""")

def rightarm():
    print(r"""_______           
    |
    |     O
    |    /|\
    |   / | \
    |    
    |      
    |
    -----------""")

def leftleg():
    print(r"""_______           
    |
    |     O
    |    /|\
    |   / | \
    |    / 
    |   /  
    |
    -----------""")

def rightleg():
    print(r"""_______           
    |
    |     O
    |    /|\
    |   / | \
    |    / \
    |   /   \
    |
    -----------""")


def letterbank(userinputletter):
    letterbank = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    newbank = [letterbank[x] if userinputletter not in letterbank[x] else '_' for x in range(len(letterbank))]
    
    print(newbank)

lettertoguess = input('Which letter would you like to guess? ')
letterbank(lettertoguess)

import random
import os
import time

def clear():
  os.system("clear")

words = ['butterball','elephant','tree','computer','bank','apple',
         'house','orange','Albania','Armenia','Austria','Belgium',
         'Bulgaria','Lamborghini','Toyota','Mercedes','Honda',
         'Nissan','Chile','Pear','Calculator','Oven','Cat',
         'Llizzard','Iguana','Google','Phone','Wheels','Mouse',
         'Lion','Leafs','Montreal','Toronto','California','Stump',
         'Japan','Tokyo','Fast','Furious','Supra','super','Skyline',
         'dinosaur','Case','Dirtbike','Yamaha','Mercury','Volvo',
         'Suzuki','Boat','buffalo'
        ]

guesses = 6
word = random.choice(words).lower()
word = list(word)

while guesses > 0:
  hidden_word = [print("-", end = "") for x in word]
  guess = input("\nEnter a letter: ").lower()
  if guess in word:
    print("You have guessed a correct letter!")
    if guess in hidden_word: hidden_word.replace(guess)
  else:
    guesses -= 1
    print("Sorry, you have entered an incorrect letter.")
    whichdrawing(guesses)
    print("You have {} guesses left.".format(guesses))
    time.sleep(3)
    clear()
  if guesses == 0:
    word = [print(x) for x in word]
    print("Sorry, the word was \"{}\"".format(word))
    print("Better luck next time!")
