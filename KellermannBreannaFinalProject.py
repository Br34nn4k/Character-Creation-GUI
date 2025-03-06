"""

Author:  Breannna Kellermann
Date written: 3/4/25
Assignment:   Module 08 Final Project Submission
Short Desc:   This program is an interactive personality quiz that suggests a base character model for new players of tabletop gaming.
10 multiple choice questions are displayed. Answer each question. Click "display my results" to view quiz results.


"""


from random import randrange
from breezypythongui import EasyFrame
from breezypythongui import EasyCanvas
from breezypythongui import TextField
from tkinter import *
import tkinter
Tkinter = tkinter

#general window

class CharacterCreator(EasyFrame):
 
    #questions and answers pertaining to the character's race result
    QuestionsRace = [["1. What is your character's preferred method of communication?", " With their fists", 
                          " Eloquent words and maybe a little snark", 
                          " Memes and hand gestures", 
                          " Straight-forward and to the point"],
              
              ["2. Where does your character feel most comfortable?", " Surrounded by corpses", 
                          " A beautiful sunlit meadow", 
                          " A Crowded City", 
                          " Underground"],
              
              ["3. How would you describe your ideal character appearance?" ," BIG STRONG",
                          " Ethereally Beautiful/Handsome", 
                          " Just a little guy",
                          " Sturdy and rather hairy"],

              ["4. Which companion would you prefer?", " Wolf", 
                          " Cat", 
                          " Bird", 
                          " Pet rock"],
              
              ["5.  What job might you enjoy?", " Butcher", 
                          " Selling hand-made crafts on Etsy", 
                          " Counting cards at the poker table", 
                          " Blacksmith"]]

    #questions and answers pertaining to the characters skill/class result
    QuestionsSkill = [["6. Which element resonates with you the most?", " Water", 
                          " Surprise", 
                          " Earth", 
                          " Fire"],

              ["7. Oh no, confrontation! What's your weapon of choice?", " I'd rather help than harm", 
                          " Daggers or crossbows", 
                          " The largest object I can find (or my own body)", 
                          " Fireball (not the alcohol)"],

              ["8. What kind of book are you most likely to read?", " Non-fiction/Scholarly material", 
                          " Murder-Mystery", 
                          " I hate reading", 
                          " Science-Fiction/Fantasy"],

              ["9. What do you hope to gain from your adventures?", " A sense of divine accomplishment", 
                          " Cool stories to add to my lore (also money)", 
                          " A higher body count", 
                          " Knowledge"],

              ["10. If you don't like the results you receive, are you going to try again?", " No, this is my destiny", 
                          " Absolutely", 
                          " No, but I'll be mad about it", 
                          " Depends on what I get"]]


    #array of button sets
    ButtonSetRace = []
    ButtonSetSkill = []

    #array of values
    ValuesRace = []
    ValuesSkill = []

    #canvas and textfield variables
    RaceCanvas = EasyCanvas
    SkillCanvas = EasyCanvas
    RaceCaption = TextField
    SkillCaption = TextField

    #array of images
    RaceImages = []
    SkillImages = []

    #file paths to pull the race result image from Character Creator Images folder
    RaceImagePaths = ["./Character Creator Images/orc-head.png", 
                      "./Character Creator Images/woman-elf-face.png",
                      "./Character Creator Images/kenku-head.png",
                      "./Character Creator Images/dwarf-face.png"]
    
    #file paths to pull the skill result image from Character Creator Images folder
    SkillImagePaths = ["./Character Creator Images/health-potion.png",
                       "./Character Creator Images/rogue.png",
                       "./Character Creator Images/fist.png",
                       "./Character Creator Images/orb-wand.png"]

        
    #text result displayed depending on file path used
    #race text result
    RaceImageCaptions = ["Orc", 
                         "Elf", 
                         "Kenku", 
                         "Dwarf"]
    #skill/class text result
    SkillImageCaptions = ["Cleric", 
                          "Rogue", 
                          "Barbarian", 
                          "Wizard"]

    
    def __init__(self):
        #window name
        EasyFrame.__init__(self, title = "Character Creation Quiz! What fanstasy character should you play?")


        #generate question buttonsets
        Column = 0
        RowCount = 0
        for x in self.QuestionsRace:
            self.ButtonSetRace.append(self.addButtonSet(RowCount, Column, x[0],x[1],x[2],x[3],x[4]))
            RowCount += 2

        #shift the column to +4, as the button sets have a columnspan of 4
        Column = 4
        RowCount = 0
        for x in self.QuestionsSkill:
            self.ButtonSetSkill.append(self.addButtonSet(RowCount, Column, x[0],x[1],x[2],x[3],x[4]))
            RowCount += 2

        #row tally of button sets
        ButtonRowCount = max(len(self.QuestionsRace), len(self.QuestionsSkill))*4

        #Output field and button for results
        self.addButton("Display My Results!", row = ButtonRowCount, column = 0,
                       command = self.displayResults)
        #Help button
        self.addButton("Help!", row = ButtonRowCount, column = 2,
                command = self.helpPopUp)
        #close window button
        self.addButton("Exit", row = ButtonRowCount, column = 4,
                command = self.close_window)

        #Load images
        self.genImages()

        #Create the canvas and text field for race result
        self.RaceCanvas = self.addCanvas( row = ButtonRowCount+1, column = 0, columnspan = 1, width = 200, height = 200)
        self.RaceCaption = self.addTextField("Caption Race", row = ButtonRowCount+2, column = 0, columnspan = 4, sticky = W+E)
        #sticky: a combination of N S E W used for extents positioning
        #W+E will make it fill the space horizontally
        
        #Create the canvas and text field for skill result
        self.SkillCanvas = self.addCanvas( row = ButtonRowCount+1, column = 4, columnspan = 1, width = 200, height = 200)
        self.SkillCaption = self.addTextField("Caption Skill", row = ButtonRowCount+2, column = 4, columnspan = 4, sticky = W+E)

    #updates the canvas to display the results
    def displayResults(self):
        temp = self.gatherValues()

        #Race results, displays image and text related to race result
        self.RaceCanvas.drawImage(self.RaceImages[temp[0]], x = 100, y = 100)
        self.RaceCaption.setText(self.RaceImageCaptions[temp[0]])

        #Skill results, displays image and text related to skill result
        self.SkillCanvas.drawImage(self.SkillImages[temp[1]], x = 100, y = 100)
        self.SkillCaption.setText(self.SkillImageCaptions[temp[1]])

    #help box popup, displays instructions for user
    def helpPopUp(self):
        self.messageBox(title = "Help!",
                        message = "Interested in fantasy tabletop gaming, but unsure where to start? \
                        You're 10 questions away from a decent suggestion.\
                        Simply left click the dot next to the answer you most agree with for all 10 questions provided. \
                        After you have chosen your answers, click the button that says ""Display my results!"" \
                        Based on your answers, two labeled pictures will be displayed, showing a fantasy race and class suggestion for your new character!")

    #Creates and adds the images to an array
    def genImages(self):
        for i in range(0,len(self.RaceImagePaths)):
             self.RaceImages.append(Tkinter.PhotoImage(file=self.RaceImagePaths[i]))
        for i in range(0,len(self.SkillImagePaths)):
             self.SkillImages.append(Tkinter.PhotoImage(file=self.SkillImagePaths[i]))

    #Gathers the results of the questions and returns the highest result or a random result from the equip top results
    def gatherValues(self):
        ValuesRaceTemp = ""
        ValuesSkillTemp = ""
        for x in self.ButtonSetRace:
            ValuesRaceTemp += (x.getSelectedButton()["value"])[:1]
        for x in self.ButtonSetSkill:
            ValuesSkillTemp += (x.getSelectedButton()["value"])[:1]

        #returns 2 numbers, [Race, Skill]
        return (self.convertAlphaToNumber(self.processOutput(ValuesRaceTemp)),self.convertAlphaToNumber(self.processOutput(ValuesSkillTemp)))

    #Converts alpha to numeric with a == 0
    def convertAlphaToNumber(self, var):
        return ord(var.lower()) - 97

    #takes a string input and returns the character with the heights occurences or the equal top characters
    def processOutput(self, ValuesArray):
        #makes an map that tallys up the characters and their instances [character, counter]
        ValueCounter = []
        for x in ValuesArray:
            TopValue = 1
            for y in ValueCounter:
                if y[0] == x:
                    y[1] +=1
                    TopValue = 0
            if TopValue == 1: ValueCounter.append([x,1])

        #sets the character with the heighest counter as the top value unless it finds another with an equal, then both are in the TopValues array
        #uses randrange to randomly select winner from values as a tie-breaker, if there is more than one TopValues
        TopValues = [[0,0]]
        for x in ValueCounter:
            if x[1] > TopValues[0][1]:
                TopValue = x;
                TopValues = [x] 
            elif x[1] == TopValues[0][1]:
                TopValues.append(x)
        if len(TopValues) > 1:            
            return TopValues[randrange(0, len(TopValues))][0]
        else:
            return TopValues[0][0]


    #formatting for each question. One question and four answer options, one per radio button
    def addButtonSet(self,RowCount, Column, QuestionLabel, QuestionADescription, QuestionBDescription, QuestionCDescription, QuestionDDescription):
        
        #Creates the question label
        self.addLabel(QuestionLabel, RowCount, Column)

        #Add the button group
        self.group = self.addRadiobuttonGroup(RowCount+1, Column, columnspan = 4, orient = VERTICAL)

        #Add the radio buttons to the group
        self.group.setSelectedButton(self.group.addRadiobutton(f"a) {QuestionADescription}")) #creates the first button and sets it as the selected button
        self.group.addRadiobutton(f"b) {QuestionBDescription}")
        self.group.addRadiobutton(f"c) {QuestionCDescription}")
        self.group.addRadiobutton(f"d) {QuestionDDescription}")
        return self.group
    
    #close window
    def close_window(self):
        self.quit()


#starts the code
CharacterCreator().mainloop()






