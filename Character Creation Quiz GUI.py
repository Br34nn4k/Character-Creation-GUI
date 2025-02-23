from breezypythongui import EasyFrame
from tkinter import *
import tkinter
Tkinter = tkinter
class PythonApplication1(EasyFrame):
 
    RowCount = 0
    Column = 0
    Width = 800
    Height = 800
    def __init__(self):
        EasyFrame.__init__(self, title = "Character Creation Quiz")
        #self.CreateFrame()
        self.addButtonSet("1. What is your character’s preferred method of communication?", "With their fists", 
                          "Eloquent words and maybe a little snark", 
                          "Memes and hand gestures", 
                          "Straight-forward and to the point")
        self.addButtonSet("2. Where does your character feel most comfortable?", "Surrounded by corpses", 
                          "A beautiful sunlit meadow", 
                          "A crowded city", 
                          "Underground")
        self.addButtonSet("3. How would you describe your ideal physical appearance?", "BIG STRONG", 
                          "Ethereally Beautiful/Handsome", 
                          "Just A Little Guy", 
                          "Sturdy and rather hairy")
        self.addButtonSet("4. Which companion would you prefer?", "Wolf", 
                          "Cat", 
                          "Bird", 
                          "Pet rock")
        self.addButtonSet("5.  What job might you enjoy?", "Butcher", 
                          "Selling handmade crafts on Etsy", 
                          "Counting cards at the poker table", 
                          "Blacksmith")
        self.Column = 5
        self.RowCount = 0
        self.addButtonSet("6. Which element resonates with you the most?", "Water",  
                          "Surprise", 
                          "Earth", 
                          "Fire")
        self.addButtonSet("7. Oh no, confrontation! What’s your weapon of choice?", "I’d rather help than harm", 
                          "Daggers or crossbows", 
                          "The largest object I can find (or my own body)", 
                          "Fireball (not the alcohol)")
        self.addButtonSet("8. What kind of book are you most likely to read?", "Non-fiction/Scholarly material", 
                          "Murder-Mystery", 
                          "I hate reading", 
                          "Science-Fiction/Fantasy")
        self.addButtonSet("9. What do you hope to gain from your adventures?", "A sense of divine accomplishment", 
                          "Cool stories to add to my lore (also money)", 
                          "A higher body count", 
                          "Knowledge")
        self.addButtonSet("10. If you don’t like the results you receive, are you going to try again?", "No, this is my destiny", 
                          "Absolutely", 
                          "No, but I’ll be mad about it", 
                          "Depends on what I get")


    def addButtonSet(self, QuestionLabel, QuestionADescription, QuestionBDescription, QuestionCDescription, QuestionDDescription):
        self.addLabel(QuestionLabel, self.RowCount, self.Column)
        self.RowCount += 1
        # Add the button group
        self.group = self.addRadiobuttonGroup(self.RowCount, self.Column, columnspan = 4, orient = VERTICAL)
        self.RowCount += 1
        # Add the radio buttons to the group
        self.group.addRadiobutton(f"a) {QuestionADescription}")
        self.group.addRadiobutton(f"b) {QuestionBDescription}")
        self.group.addRadiobutton(f"c) {QuestionCDescription}")
        self.group.addRadiobutton(f"d) {QuestionDDescription}")

    def CreateFrame(self):
        #frame=Frame(self,width=self.Width,height=self.Height)
        #frame.pack(expand=True, fill=BOTH) #.grid(row=0,column=0)
        canvas=Canvas(self,bg='#FFFFFF',width=self.Width,height=self.Height,scrollregion=(0,0,500,500))
        vbar=Scrollbar(self,orient=VERTICAL)
        vbar.pack(side=RIGHT,fill=Y)
        vbar.config(command=canvas.yview)
        canvas.config(width=self.Width,height=self.Height)
        canvas.config(yscrollcommand=vbar.set)
        canvas.pack(side=LEFT,expand=True,fill=BOTH)

PythonApplication1().mainloop()