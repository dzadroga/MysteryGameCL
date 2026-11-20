# This class is responsible for all character interactions
from notebook import Notebook
from Museum_Game.Museum_Characters import MuseumCharacters


class Interviews:

    #Global Variables that are reused thoughout interview's
    Question1 = "1. How are you when it comes to working with Computers?"
    Question2 = "2. " 
    Question3 = ""
    Question4 = ""
    Question5 = ""

    def Interview(self):
        menuInput = ''
        inputTrack = 0

        menuInput = print("Who would you like to Interview? (Select a Number 1 - 4)")

        print("1. Jason the Security Guard")
        print("2. Amanda the Curator")
        print("3. Lane the Artist")
        print("4. Sam the Barista")
        print("M. Return to Menu")

        if menuInput == "1":
            self.InterviewJason()
            inputTrack += 1

        elif menuInput == "2":
            self.InterviewAmanda()
            inputTrack += 1

        elif menuInput == "3":
            self.InterviewLane()
            inputTrack += 1

        elif menuInput == "4":
            self.InterviewSam()
            inputTrack += 1

        elif menuInput == "W" or menuInput == "w":

            inputTrack += 1
        elif menuInput == "N" or menuInput == "n":

            inputTrack += 1

        elif menuInput == "E" or menuInput == "e":

            inputTrack += 1
        elif menuInput == "M" or menuInput == "m":

            inputTrack += 1
        else:
            print("I am not sure I understand")

    def InterviewJason(self):
        menuInput = ''
        inputTrack = 0

        menuInput = input("What Question do you want to ask?")
        print(self.Question1)
        print(self.Question2)
        print(self.Question3)
        print(self.Question4)
        print(self.Question5)

        if menuInput == "1":
            print(Jason.answers("technology"))
            inputTrack += 1
        
        elif menuInput == "2":
            self.InterviewAmanda()
            inputTrack += 1
        
        elif menuInput == "3":
            self.InterviewLane()
            inputTrack += 1
        
        elif menuInput == "4":
            self.InterviewSam()
            inputTrack += 1
        
        elif menuInput == "W" or menuInput == "w":
        
            inputTrack += 1
        elif menuInput == "N" or menuInput == "n":
        
            inputTrack += 1
        
        elif menuInput == "E" or menuInput == "e":
        
            inputTrack += 1
        elif menuInput == "M" or menuInput == "m":
        
            inputTrack += 1
        else:
            print("I am not sure I understand")
        

    def InterviewAmanda(self):


    def InterviewLane(self):


    def InterviewSam(self):
