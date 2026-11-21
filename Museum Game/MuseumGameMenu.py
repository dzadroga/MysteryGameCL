#Holds the logic and interactions for the museum game

from MuseumCharacters import MuseumCharacters
from Notebook import Notebook

class MueseumGameMenu:
    
    #starting variables for tracking
    def __init__(self):
        self.guilityPerson = MuseumCharacters.Amanda
        self.temp= ""
        self.notebook = Notebook()
    
    def start(self):
        print("Welcome to the Museum Mystery Game")
        playerName = input("What is your name?")
        print("Hi" + playerName + "We need your help for an important mission.")
        
        temp = input("Are you in? (Enter Y to start or N to exit")
        
        if temp == "y" or temp == "Y":
            self.IntroCall()
            self.MenuCall()
        elif temp == 'n' or temp == "N":
            print("Why did you bother wasting my time then!!!")
        else: 
            print("I am not sure I understand")


    def IntroCall(self):
        print("A $1 million painting went missing last night around 9:15pm and we need to find it!")
        print("The only problem is, the camera footage seems to have been deleted.  While our security gaurd Jason")
        print("was locking down the place, we checked the cameras at the front desk.  Turns out, the footage was gone!")
        print("At any point access your notebook by entering N, you can keep track of all your findings there!")
        print("Are you ready to start?")
        print("Let's begin!")


    def MenuCall(self):
        
        menuInput = ''
        inputTrack = 0

        menuInput = input("What would you like to do? (select the number/letter corresponding to the menu option)")

        print("1. Explore a Location")
        print("2. Interview a suspect")
        print("3. Review Evidence")
        print("4. Make an Accusation")
        print("N. Read Notes")
        print("E. To exit and return to main menu")


        while(inputTrack == 0):
            if menuInput == "1":

                inputTrack = 1

            elif menuInput == "2":
                self.Interview()
                inputTrack = 1

            elif menuInput == "3":

                inputTrack = 1

            elif menuInput == "4":

                inputTrack = 1

            elif menuInput == "N":

                inputTrack = 1

            elif menuInput == "E":

                inputTrack = 1

            else:
                print("I am not sure I understand")



    




        
        
        