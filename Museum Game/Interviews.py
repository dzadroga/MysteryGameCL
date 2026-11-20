# This class is responsible for all character interactions
from notebook import Notebook
from Museum_Game.Museum_Characters import MuseumCharacters


class Interviews:

    #Creates dictionary for the interview questions
    questions = { 
        "1" : ("technology", "1. How are you when it comes to working with Computers?"),
        "2" : ("alibi", "2. Can anyone confirm where you were last night?"), 
        "3" : ("suspect", "3. Who do you think is responible for stealing the painting?"),
        "4" : ("noise", "4. Did you hear any odd noises?"),
        "5" : ("painting", "5. When was the last time you saw the painting?")
    }


    def Interview(self):
        characters = {
            "1" : MuseumCharacters.Jason,
            "2" : MuseumCharacters.Amanda,
            "3" : MuseumCharacters.Lane,
            "4" : MuseumCharacters.Sam
        }

        while True:
            print("\nWho would you like to Interview?")

            for number, character in character.items():
                print(f"{number}: {character.name} the {character.description}")
            print("M. Return to Menu")

            menuInput = print("Select a Number 1 - 4: ").strip().lower()

            if menuInput == "W" or menuInput == "w":
                Notebook.writeNote()
            elif menuInput == "N" or menuInput == "n":
                Notebook.readNotes()

            elif menuInput == "E" or menuInput == "e":
                return
            elif menuInput == "M" or menuInput == "m":
                return

            if menuInput in character:
                self.InterviewCharacter(character[menuInput])
            else: 
                print(" I am not sure I understand")

    def InterviewCharacter(self, character):
        while True: 
            print(f"You are now interviewing {character.name} the {character.description}")
            print("What would you like to ask?")

            for number, (_, self.questions) in self.questions.items():
                print(f"{number}. {questions}")
            print("M. Return to Menu") 

            menuInput = print("Select a Number 1 - 5: ").strip().lower()

            if menuInput == "W" or menuInput == "w":
                Notebook.writeNote()
            elif menuInput == "N" or menuInput == "n":
                Notebook.readNotes()  
            elif menuInput == "E" or menuInput == "e":
                return
            elif menuInput == "M" or menuInput == "m":
                return

            if menuInput in self.questions:
                answer_key, _ = self.questions(menuInput)
                print(character.answerQuestion(answer_key))
            else: 
                print("I am not sure I understand")