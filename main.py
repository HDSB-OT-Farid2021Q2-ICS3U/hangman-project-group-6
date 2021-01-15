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


def wordbank(userinputletter):
    wordbank = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    newbank = [wordbank[x] if userinputletter not in wordbank[x] else '_' for x in range(len(wordbank))]
    
    print(newbank)

lettertoguess = input('Which letter would you like to guess? ')
wordbank(lettertoguess)
