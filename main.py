# TODO @austin create randomizing word function
# TODO @TK create user input letter + check if letter is in string function
# TODO @clarrie create draw hangman function

import random #Importing random


#Word bank fille with many words
def wordbank ():
    words = ['butterball','elephant','tree','computer','bank','apple','house','orange','Albania','Armenia','Austria','Belgium','Bulgaria','Lamborghini','Toyota','Mercedes','Honda','Nissan','Chile','Pear','Calculater','Oven','Cat','Llizzard','Iguana','Google','Phone','Wheels','Mouse','Lion','Leafs','Montreal','Toronto','California','Stump','Japan','Tokyo','Fast','Furious','Supra','super','Skyline','dinosaur','Case','Dirtbike','Yamaha','Mercury','Volvo','Suzuki','Boat','buffalo','supreme']

    randWord = random.choice(words) #Assiogning a random word to this variable so that Tk can use it when deciding if the charater is in the word

    print(random.choice(words)) #printintg im not sure if this is needed but its here anyways

wordbank()#Calling word bank