#Holds the logic and interactions for the museum game

from museum_game.museum_characters import MuseumCharacters

class MueseumGameMenu:
    
    #starting variables for tracking
    guilityPerson = MuseumCharacters.Amanda
    temp= ""
    
    def start(self):
        print("Welcome to the Museum Mystery Game")
        playerName = input("What is your name?")
        print("Hi" + playerName + "We need your help for an important mission.")
        
        temp = input("Are you in? (Enter Y to start or N to exit")
        
        if temp == "y" or temp == "Y":
            continue
        elif temp == 'n' or temp == "N":
            print("Why did you bother wasting my time then!!!")
        else: 
            print("I am not sure I understand")


    def MenuCall(self):
        print("A $1 million painting went missing last night around 9:15pm and we need to find it")
        print("The only problem is, the camera footage seems to have been deleted.  While our security gaurd Jason")
        print("was locking down the place, we checked the cameras at the front desk.  Turns out, the footage was gone!")
        
        
        
        