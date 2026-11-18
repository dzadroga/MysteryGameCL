#This class tracks the notes written 

class Notebook():

    def __init__(self):
        self.notes = []

    def writeNote(self): 
            note = input("Write your note: ").strip()

            if note: 
                self.notes.append(note)
                print("Note Saved!")

    def readNotes(self):
        if not self.notes:
            print("You do not have any saved notes quite yet")

        else:
            for number, note in enumerate(self.notes, start = 1):
                print(f"{number}. {note}")