import random
import os

def clear():
  os.system("clear")

words = ['butterball','elephant','tree','computer','bank','apple','house','orange',
         'Albania','Armenia','Austria','Belgium','Bulgaria','Lamborghini','Toyota',
         'Mercedes','Honda','Nissan','Chile','Pear','Calculater','Oven','Cat','Llizzard','Iguana',
         'Google','Phone','Wheels','Mouse','Lion','Leafs','Montreal','Toronto','California',
         'Stump','Japan','Tokyo','Fast','Furious','Supra','super','Skyline','dinosaur','Case',
         'Dirtbike','Yamaha','Mercury','Volvo','Suzuki','Boat','buffalo'
        ]

guesses = 6


word = random.choice(words)
progress = "-" * len(word)
while guesses > 0:
  guess = input("Enter a letter: ")
  if guess in word:
    print()
  else:
    guesses -= 1