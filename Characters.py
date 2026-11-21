# Base file for all Character Instances in the game
# Updated on 11/17/2026

class Character:
    
    def __init__(self, name, description, answers):
        self.name =name
        self.description = description 
        self.answers = answers
    
    def answerQuestion(self, question):
        return self.answers.get(question, "I am not sure")