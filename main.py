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

import random #Importing random


#Word bank fille with many words
def wordbank ():
    words = ['butterball','elephant','tree','computer','bank','apple','house','orange','Albania','Armenia','Austria','Belgium','Bulgaria','Lamborghini','Toyota','Mercedes','Honda','Nissan','Chile','Pear','Calculater','Oven','Cat','Llizzard','Iguana','Google','Phone','Wheels','Mouse','Lion','Leafs','Montreal','Toronto','California','Stump','Japan','Tokyo','Fast','Furious','Supra','super','Skyline','dinosaur','Case','Dirtbike','Yamaha','Mercury','Volvo','Suzuki','Boat','buffalo','supreme']

    randWord = random.choice(words) #Assiogning a random word to this variable so that Tk can use it when deciding if the charater is in the word

    print(random.choice(words)) #printintg im not sure if this is needed but its here anyways

wordbank()#Calling word bank

