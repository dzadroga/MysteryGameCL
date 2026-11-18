# This class is responsible for all character interactions
from notebook import Notebook


class Interviews:

    #Global Variables that are reused thoughout interview's
    Question1 = "1. How are you when it comes to working with Computers"
    Question2 = "2. " 
    Question3 = ""
    Question4 = ""
    Question5 = ""

    def Interview():
        menuInput = ''
        inputTrack = 0

        menuInput = print("Who would you like to Interview? (Select a Number 1 - 4)")

        print("1. Jason the Security Guard")
        print("2. Amanda the Curator")
        print("3. Lane the Artist")
        print("4. Sam the Barista")

        if menuInput == "1":

            inputTrack += 1

        elif menuInput == "2":

            inputTrack += 1

        elif menuInput == "3":

            inputTrack += 1

        elif menuInput == "4":

            inputTrack += 1

        elif menuInput == "W":

        
        elif menuInput == "N":


        elif menuInput == "E":

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


    def InterviewAmanda(self):


    def InterviewLane(self):


    def InterviewSam(self):
