# Import appJar module

from appJar import gui, appjar    # Imports all components of appJar

# Create an app instance to get the screen dimensions
root = appjar.Tk()

# Save the screen dimensions
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Destroy the app instance after retrieving the screen dimensions
root.destroy()

program = gui("Welcome!", str(width) + "x" + str(height))  # Sets size and title of main GUI

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def Start(select):
# Start
    if select == "Start Voting":       # First button of the GUI (to start the voting process)
        program.showSubWindow(select)
    elif select == "Exit":             # Last button of the GUI (to reboot the GUI)
        Clean()
        ResetSummary()

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def Instructions(select):
# Instructions
    if select == "I understood":
        program.showSubWindow(select)                                # "I understood" is the subWindow name for our first question
        program.hideSubWindow("Start Voting", useStopFunction=False) # Hide it in case we need to go back
        program.confirmHideSubWindow("Start Voting")
    elif select == "Out":
        Clean()
        

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
def ResetSummary():
    program.destroySubWindow("Done")                 # Destroy Done because this page need to be updated everytime

def Clean():
# Reboot the GUI
    program.clearAllRadioButtons(callFunction=False) # Clear all radio buttons
    program.clearAllEntries(callFunction=False)      # Clear all entries
    program.hideAllSubWindows()                      # Hide all subwindows

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def Final(select):
# Take voter to the very last page with the survey and exit
    if select == "Submit":                   # Take the voter to the last page and allow the GUI to reboot   
        program.showSubWindow(select)
    elif select == "Change Question 1":      # Take the voter back to question 1 to allow them to change it
        program.showSubWindow("I understood")
        ResetSummary()
        # Destroyed as it needs to update
    elif select == "Change Question 2":      # Take the voter back to question 2 to allow them to change it
        program.showSubWindow("Next")
        ResetSummary()
        # Destroyed as it needs to update
    elif select == "Change Question 3":      # Take the voter back to question 3 to allow them to change it
        program.showSubWindow(" Next ")
        ResetSummary()
        # Destroyed as it needs to update
    elif select == "Discard Vote":           # If the ballot is discard, the GUI will reboot
        Clean()
        ResetSummary()

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def Special():
    program.setSize(600, 600)                                             # Sets size
    program.setBg("white")                                                # Sets background colour
    program.addLabel("last", "Summary")                                   # This is for the Summary
    program.getLabelWidget("last").config(font="Times 30 roman underline")# Make Summary the top and biggest in the page
#-----------------------------------------------------------------------------------
    if (program.getRadioButton("option") == "Others"):
    # If the choice was a Others option, it will prints out whatever the voter typed in
        program.addLabel("comment3", "Your choice for the first place project is : " + program.getEntry("1st Place: "))
        program.getLabelWidget("comment3").config(font="Times 15 roman bold")
    elif (program.getRadioButton("option") != "Others"):
    # If the choice was one of the button, it will prints out that button
        program.addLabel("comment3", "Your choice for the first place project is : " + program.getRadioButton("option"))
        program.getLabelWidget("comment3").config(font="Times 15 roman bold")
#-----------------------------------------------------------------------------------    
    if (program.getRadioButton("option5") == "Others"):
    # If the choice was a Others option, it will prints out whatever the voter typed in
        program.addLabel("comment4", "Your choice for the second place project is : " + program.getEntry("2nd Place: "))
        program.getLabelWidget("comment4").config(font="Times 15 roman bold")
    elif (program.getRadioButton("option5") != "Others"):
    # If the choice was one of the button, it will prints out that button
        program.addLabel("comment4", "Your choice for the second place project is : " + program.getRadioButton("option5"))
        program.getLabelWidget("comment4").config(font="Times 15 roman bold")
#-----------------------------------------------------------------------------------    
    if (program.getRadioButton("option6") == "Others"):
    # If the choice was a Others option, it will prints out whatever the voter typed in
        program.addLabel("comment5", "Your choice for the third place project is : " + program.getEntry("3rd Place: "))
        program.getLabelWidget("comment5").config(font="Times 15 roman bold")
    elif (program.getRadioButton("option6") != "Others"):      
    # If the choice was one of the button, it will prints out that button  
        program.addLabel("comment5", "Your choice for the third place project is : " + program.getRadioButton("option6"))
        program.getLabelWidget("comment5").config(font="Times 15 roman bold")

    program.addButtons(["Change Question 1", "Change Question 2", "Change Question 3"], Final)
    program.addButtons(["Submit", "Discard Vote"], Final)
    program.showSubWindow("Done")
    # Add buttons and show the subWindow

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def MoreInfo(): 
# For "I understood" subWindow (Question 1)
    program.setSize(600, 600)                                              # Sets size
    program.setBg("white")                                                 # Sets background colour
    program.addLabel("info2", "Voting Instructions")                       # Title
    program.getLabelWidget("info2").config(font="Times 20 roman underline")# Make it the biggest and boldest

    program.addLabel("info3","1. Read the questions carefully before casting your vote")
    program.addLabel("info4", "2. After you make your choice, proceed and it will take your to the Next")
    program.addLabel("info5", "3. More Info for the summary of the projects, Close if you want to Exit")
    program.addLabel("info6","4. Review your choices in the Summary page and click Submit")
    program.addLabel("info7","5. Take the ballot to the scanner to cast your vote")
    program.getLabelWidget("info7").config(font="Times 18 roman bold")
    program.addButton("  Close  ", ButtonHandler1)
    # If Close if pressed, it will go to the function ButtonHandler1

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def MoreInfo2():
# For "Next" subWindow (Question 2)
    program.setSize(600, 600)                                              # Sets size
    program.setBg("white")                                                 # Sets background colour
    program.addLabel("info2", "Voting Instructions")                       # Title
    program.getLabelWidget("info2").config(font="Times 20 roman underline")# Make it the biggest and boldest

    program.addLabel("info3","1. Read the questions carefully before casting your vote")
    program.addLabel("info4", "2. After you make your choice, proceed and it will take your to the Next")
    program.addLabel("info5", "3. More Info for the summary of the projects, Close if you want to Exit")
    program.addLabel("info6","4. Review your choices in the Summary page and click Submit")
    program.addLabel("info7","5. Take the ballot to the scanner to cast your vote")
    program.getLabelWidget("info7").config(font="Times 18 roman bold")
    program.addButton("   Close  ", ButtonHandler1)
    # If Close if pressed, it will go to the function ButtonHandler1

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def MoreInfo3():
# For " Next " subWindow (Question 3)
    program.setSize(600, 600)                                              # Sets size
    program.setBg("white")                                                 # Sets background colour
    program.addLabel("info2", "Voting Instructions")                       # Title
    program.getLabelWidget("info2").config(font="Times 20 roman underline")# Make it the biggest and boldest

    program.addLabel("info3","1. Read the questions carefully before casting your vote")
    program.addLabel("info4", "2. After you make your choice, proceed and it will take your to the Next")
    program.addLabel("info5", "3. More Info for the summary of the projects, Close if you want to Exit")
    program.addLabel("info6","4. Review your choices in the Summary page and click Submit")
    program.addLabel("info7","5. Take the ballot to the scanner to cast your vote")
    program.getLabelWidget("info7").config(font="Times 18 roman bold")
    program.addButton("   Close   ", ButtonHandler1)
    # If Close if pressed, it will go to the function ButtonHandler1

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------
def Pop1(rb):
    if program.getRadioButton("option") == "Others":
        if program.getEntry("1st Place: ") == "":
            program.showSubWindow("Change Write In")

def Pop2(rb):
    if program.getRadioButton("option5") == "Others":
        if program.getEntry("2nd Place: ") == "":
            program.showSubWindow("Change Write In ")

def Pop3(rb):
    if program.getRadioButton("option6") == "Others":
        if program.getEntry("3rd Place: ") == "":
            program.showSubWindow(" Change Write In ")

def ButtonHandler1(select):  
# Called if buttons are associated with ButtonHandler1
    if select == "Next":  
    # If voter click "Next"
        if program.getRadioButton("option") == "No Vote":
            program.showSubWindow(select)
            program.hideSubWindow("I understood", useStopFunction=False)
            program.confirmHideSubWindow("I understood")

        elif program.getRadioButton("option") == "Others":
            if program.getEntry("1st Place: ") != "":
                program.showSubWindow(select)
                program.hideSubWindow("I understood", useStopFunction=False)
                program.confirmHideSubWindow("I understood")
            elif program.getEntry("1st Place: ") == "":
                program.showSubWindow("Change Write In")
        else:
            program.showSubWindow(select)
            program.hideSubWindow("I understood", useStopFunction=False)
            program.confirmHideSubWindow("I understood")
#-----------------------------------------------------------------------------------
    elif select == " Next ": 
    # If voter click " Next "
        if program.getRadioButton("option5") == "No Vote":
            program.showSubWindow(select)
            program.hideSubWindow("Next", useStopFunction=False)
            program.confirmHideSubWindow("Next")

        elif program.getRadioButton("option5") == "Others":
            if program.getEntry("2nd Place: ") != "":
                program.showSubWindow(select)
                program.hideSubWindow("Next", useStopFunction=False)
                program.confirmHideSubWindow("Next")
            elif program.getEntry("2nd Place: ") == "":
                program.showSubWindow("Change Write In ")
        else:
            program.showSubWindow(select)
            program.hideSubWindow("Next", useStopFunction=False)
            program.confirmHideSubWindow("Next")
#-----------------------------------------------------------------------------------    
    elif select == "Done": 
    # If voter click "Done"        

        if program.getRadioButton("option6") == "No Vote":
            program.startSubWindow("Done", modal = True)
            Special()
            program.hideSubWindow(" Next ", useStopFunction=False)
            program.confirmHideSubWindow(" Next ")
        elif program.getRadioButton("option6") == "Others":
            if program.getEntry("3rd Place: ") != "":
                program.startSubWindow("Done", modal = True)
                Special()
                program.hideSubWindow(" Next ", useStopFunction=False)
                program.confirmHideSubWindow(" Next ")
            elif program.getEntry("3rd Place: ") == "":
                program.showSubWindow(" Change Write In ")
        else:
            program.startSubWindow("Done", modal = True)
            Special()
            program.hideSubWindow(" Next ", useStopFunction=False)
            program.confirmHideSubWindow(" Next ")
#-----------------------------------------------------------------------------------
    elif select == "More Info":  
    # If user clicks 'More Info'
        program.startSubWindow("More Info", modal = True) # Displays message box
        MoreInfo()
        program.showSubWindow("More Info")
#-----------------------------------------------------------------------------------
    elif select == "Close":  
    # If user clicks 'Close'
        Clean() 
#-----------------------------------------------------------------------------------
    elif select == "More Info ":
    # If user clicks 'More Info '
        program.startSubWindow("More Info", modal = True) # Displays message box
        MoreInfo2()
        program.showSubWindow("More Info")
#-----------------------------------------------------------------------------------
    elif select == "Close ":
    # If user clicks 'Close ' 
        Clean()
#-----------------------------------------------------------------------------------
    elif select == " More Info ":
    # If user clicks ' More Info '
        program.startSubWindow("More Info", modal = True) # Displays message box
        MoreInfo3()
        program.showSubWindow("More Info")
#-----------------------------------------------------------------------------------   
    elif select == " Close ":
    # If user clicks ' Close '
        Clean()  
#-----------------------------------------------------------------------------------
    elif select == "Previous":
    # If user clicks 'Previous' (First question)
        program.showSubWindow("Start Voting")
        program.hideSubWindow("I understood", useStopFunction=False)
        program.confirmHideSubWindow("I understood")
#-----------------------------------------------------------------------------------  
    elif select == "Previous ":
    # If user clicks 'Previous' (Second question)
        program.showSubWindow("I understood")
        program.hideSubWindow("Next", useStopFunction=False)
        program.confirmHideSubWindow("Next")
#-----------------------------------------------------------------------------------
    elif select == " Previous ":
    # If user clicks 'Previous' (Third question)
        program.showSubWindow("Next")
        program.hideSubWindow(" Next ", useStopFunction=False)
        program.confirmHideSubWindow(" Next ")
#-----------------------------------------------------------------------------------
    elif select == "  Close  ":
    # If user clicks '  Close  ', this is for the 'More Info' in the first question
        program.showSubWindow("I understood")
        program.destroySubWindow("More Info")
#-----------------------------------------------------------------------------------
    elif select == "   Close  ":
    # If user clicks ' Close ', this is for the 'More Info' in the second question
        program.showSubWindow("Next")
        program.destroySubWindow("More Info")
#-----------------------------------------------------------------------------------
    elif select == "   Close   ":
    # If user clicks 'Close', this is for the 'More Info' in the third question
        program.showSubWindow(" Next ")
        program.destroySubWindow("More Info")
#-----------------------------------------------------------------------------------
    elif select == "Change Write In":
        program.setRadioButton("option","Others")
        program.showSubWindow("Change Write In")
    
    elif select == "Change Write In ":
        program.setRadioButton("option5","Others")
        program.showSubWindow("Change Write In ")
    
    elif select == " Change Write In ":
        program.setRadioButton("option6","Others")
        program.showSubWindow(" Change Write In ")
#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def Others(select):
# This is for the Others option

    # Others option for the first question
    if select == "Save":
        program.hideSubWindow("Change Write In")
        program.showSubWindow("I understood")
    elif select == "Cancel":
        program.hideSubWindow("Change Write In")
        program.showSubWindow("I understood")
#-----------------------------------------------------------------------------------
    # Others option for the second question
    elif select == "Save ":
        program.hideSubWindow("Change Write In ")
        program.showSubWindow("Next")
    elif select =="Cancel ":
        program.hideSubWindow("Change Write In ")
        program.showSubWindow("Next")
#-----------------------------------------------------------------------------------
    # Others option for the third question
    elif select ==" Save ":
        program.hideSubWindow(" Change Write In ")
        program.showSubWindow(" Next ")
    elif select ==" Cancel ":
        program.hideSubWindow(" Change Write In ")
        program.showSubWindow(" Next ")

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

def main():
# Widgets
    program.addLabel("title","DemocraSafe")  # Title
    program.getLabelWidget("title").config(font="Times 30 roman underline bold")
    program.addButton("Start Voting", Start)
    program.setButtonFont(size=50)
    program.setBg("white")  # Sets background colour
#-----------------------------------------------------------------------------------
    program.startSubWindow("Start Voting", modal = True)
    program.setSize(width, height)
    program.setBg("white")  # Sets background colour

    program.addLabel("option1", "Voting Instructions")  # Title
    program.getLabelWidget("option1").config(font="Times 30 roman underline")
    program.addLabel("optio","1. Read the questions carefully before casting your vote")
    program.addLabel("option2", "2. After you make your choice, proceed and it will take your to the Next")
    program.addLabel("option3", "3. More Info for the summary of the projects, Close if you want to Exit")
    program.addLabel("opti","4. Review your choices in the Summary page and click Submit")
    program.addLabel("opt","5. Take the ballot to the scanner to cast your vote")
    program.getLabelWidget("opt").config(font="Times 18 roman bold")
    program.addButtons(["I understood", "Out"], Instructions)
    program.stopSubWindow()
#-----------------------------------------------------------------------------------
    program.startSubWindow("I understood", modal = True)
    program.setSize(width, height)
    program.setBg("white")  # Sets background colour

    # Labels
    program.addLabel("option", "DemocraSafe GUI")  # Title
    program.getLabelWidget("option").config(font="Times 25 roman normal")

    program.addLabel("question", "Question 1. What is your choice for First Place?", 1)  # Label
    program.getLabelWidget("question").config(font="Times 20 roman underline bold")

    # Radiobuttons
    program.setFont(15)
    program.addRadioButton("option","No Vote")
    program.addRadioButton("option","Project 1")
    program.addRadioButton("option","Project 2")
    program.addRadioButton("option","Project 3")
    program.addRadioButton("option","Project 4")
    program.addRadioButton("option","Others")       

    program.setRadioButtonChangeFunction("option", Pop1)
#-----------------------------------------------------------------------------------
    program.startSubWindow("Change Write In", modal = True)
    program.setSize(600, 600)
    program.setBg("white")  # Sets background colour
    program.addLabelEntry("1st Place: ")
    program.addButtons(["Save", "Cancel"], Others)
    program.stopSubWindow()

    program.addButton("Change Write In", ButtonHandler1)
    program.addButtons(["Previous","Next", "More Info", "Close"], ButtonHandler1)
    program.stopSubWindow()
#-----------------------------------------------------------------------------------
    program.startSubWindow("Next", modal = True)
    program.setSize(width, height)
    program.setBg("white")  # Sets background colour

    # Labels
    program.addLabel("option5", "DemocraSafe GUI")  # Title
    program.getLabelWidget("option5").config(font="Times 25 roman normal")

    program.addLabel("question2", "Question 2. What is your choice for Second Place?")  # Label
    program.getLabelWidget("question2").config(font="Times 20 roman underline bold")

    # Radiobuttons
    program.setFont(15)
    program.addRadioButton("option5","No Vote")
    program.addRadioButton("option5","Project 1")
    program.addRadioButton("option5","Project 2")
    program.addRadioButton("option5","Project 3")
    program.addRadioButton("option5","Project 4")
    program.addRadioButton("option5","Others")

    program.setRadioButtonChangeFunction("option5", Pop2)
#-----------------------------------------------------------------------------------
    program.startSubWindow("Change Write In ", modal = True)
    program.setSize(600, 600)
    program.setBg("white")  # Sets background colour
    program.addLabelEntry("2nd Place: ")
    program.addButtons(["Save ", "Cancel "], Others)
    program.stopSubWindow()

    program.addButtons(["Change Write In "], ButtonHandler1)
    program.addButtons(["Previous ", " Next ", "More Info ", "Close "], ButtonHandler1)
    program.stopSubWindow()
#-----------------------------------------------------------------------------------
    program.startSubWindow(" Next ", modal = True)
    program.setSize(width, height)
    program.setBg("white")  # Sets background colour

    # Labels
    program.addLabel("option6", "DemocraSafe GUI")  # Title
    program.getLabelWidget("option6").config(font="Times 25 roman normal")

    program.addLabel("question3", "Question 3. What is your choice for Third Place?")  # Label
    program.getLabelWidget("question3").config(font="Times 20 roman underline bold")

    # Radiobuttons
    program.setFont(15)
    program.addRadioButton("option6","No Vote")
    program.addRadioButton("option6","Project 1")
    program.addRadioButton("option6","Project 2")
    program.addRadioButton("option6","Project 3")
    program.addRadioButton("option6","Project 4")
    program.addRadioButton("option6","Others")

    program.setRadioButtonChangeFunction("option6", Pop3)
#-----------------------------------------------------------------------------------
    program.startSubWindow(" Change Write In ", modal = True)
    program.setSize(600, 600)
    program.setBg("white")  # Sets background colour
    program.addLabelEntry("3rd Place: ")
    program.addButtons([" Save ", " Cancel "], Others)
    program.stopSubWindow()

    program.addButtons([" Change Write In "], ButtonHandler1)
    program.addButtons([" Previous ", "Done", " More Info ", " Close "], ButtonHandler1)
    program.stopSubWindow()
#-----------------------------------------------------------------------------------
    program.startSubWindow("Submit",modal = True)
    program.setSize(width, height)

    program.setBg("white")  # Sets background colour
    program.addLabel("question4", "How would you rate your voting experience?")
    program.addLabelScale("Scale")

    program.addLabel("comment", "Please hold on to this paper and insert this voting record receipt directly")  # Title
    program.addLabel("comment2", "into the Voting Scanner. Confidentiality and integrity are ensured in this process.")
    program.getLabelWidget("comment").config(font="Times 20 bold normal")
    program.getLabelWidget("comment2").config(font="Times 20 bold normal")
    program.addLabel("coco", "Thank you for choosing DemocraSafe!")
    program.getLabelWidget("coco").config(font="Times 15 italic normal")
    program.addButton("Exit", Start)
    program.stopSubWindow()
#-----------------------------------------------------------------------------------
    program.go()

#---------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------

main()

