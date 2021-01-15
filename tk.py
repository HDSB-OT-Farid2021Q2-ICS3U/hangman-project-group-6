
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
word = random.choice(words)
word = list(word)

while guesses > 0:
  hidden_word = [print("-", end = "") for x in word]
  guess = input("\nEnter a letter: ")
  if guess in word:
    print("You have guessed a correct letter!")
    if guess in hidden_word: hidden_word.replace(guess)
  else:
    guesses -= 1
    print("Sorry, you have entered an incorrect letter.")
    print("You have {} guesses left.".format(guesses))
    time.sleep(3)
    clear()
  if guesses == 0:
    word = [print(x) for x in word]
    print("Sorry, the word was \"{}\"".format(word))
    print("Better luck next time!")
