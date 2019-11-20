# Import appJar module

from appJar import gui    # Imports all components of appJar
import os
import sys

def Start(select):
    if select == "Start Voting":  # If user clicks 'Submit'
        program.showSubWindow(select)
    elif select == "Exit":  # If user clicks 'Close'
        quit()  # Close program

def Instructions(select):
    if select == "I understood":
        program.showSubWindow(select)
        program.hideSubWindow("Start Voting", useStopFunction=False)
        program.confirmHideSubWindow("Start Voting")
    elif select == "Out":
        quit()

def Switch1(rb):
    print(program.getRadioButton("option"))

def Switch2(rb):
    print(program.getRadioButton("option5"))

def Switch3(rb):
    program.startSubWindow("Done",modal = True)
    program.setSize(600, 600)

    program.setBg("light blue")  # Sets background colour

    program.addLabel("commentt", "Summary")
    program.getLabelWidget("commentt").config(font="Times 30 roman underline")

    program.addLabel("comment3", "Your choice for the first place project is : " + program.getRadioButton("option"))
    program.getLabelWidget("comment3").config(font="Times 15 roman bold")
    program.addLabel("comment4", "Your choice for the second place project is : " + program.getRadioButton("option5"))
    program.getLabelWidget("comment4").config(font="Times 15 roman bold")
    program.addLabel("comment5", "Your choice for the third place project is : " + program.getRadioButton("option6"))
    program.getLabelWidget("comment5").config(font="Times 15 roman bold")

    program.addLabel("question4", "How would you rate your voting experience?")
    program.addLabelScale("Scale")

    program.addLabel("comment", "Please hold on to this paper and insert this voting record receipt directly")  # Title
    program.addLabel("comment2", "into the Voting Scanner. Confidentiality and integrity are ensured in this process.")
    program.getLabelWidget("comment").config(font="Times 15 italic normal")
    program.getLabelWidget("comment2").config(font="Times 15 italic normal")

    program.addButtons(["Final Cast", "Change Vote", "Leave"], Round2)
    program.stopSubWindow()

def Round2(select):
    if select == "Final Cast":
        program.infoBox("Message", "You have succesfully finish making your choices! Thank you for choosing DemocraSafe.")  # Displays message box
        quit()
    elif select == "Change Vote":
        program.infoBox("Message", "We will take you back to the main screen shortly")  # Displays message box
        quit()
    elif select == "Leave":
        quit()  # Close program

def ButtonHandler1(select):  # Called when user clicks button
    if select == "Next Question":  # If user clicks 'Submit'
        if program.getRadioButton("option") == "Hung":  # If user had chosen 'Hung'
            # program.infoBox("Message", "You have succesfully voted for Hung for first place! Thank you for your vote.")  # Displays message box
            program.showSubWindow(select)
            program.hideSubWindow("I understood", useStopFunction=False)
            program.confirmHideSubWindow("I understood")
            #program.setRadioButton("option","Josh",callFunction=False)
            #quit()
        elif program.getRadioButton("option") == "Josh": # If user had chosen 'Josh'
            # program.infoBox("Message", "You have succesfully voted for Josh for first place! Thank you for your vote.")
            program.showSubWindow(select)
            program.hideSubWindow("I understood", useStopFunction=False)
            program.confirmHideSubWindow("I understood")
            #program.setRadioButton("option","Josh",callFunction=False)
            #quit()
        elif program.getRadioButton("option") == "Samuel":# If user had chosen 'Sam'
            # program.infoBox("Message", "You have succesfully voted for Samuel for first place! Thank you for your vote.")
            program.showSubWindow(select)
            program.hideSubWindow("I understood", useStopFunction=False)
            program.confirmHideSubWindow("I understood")
            #program.setRadioButton("option","Josh",callFunction=False)
            #quit()
        elif program.getRadioButton("option") == "Rishabh":  # If user had chosen 'Rishabh'
            # program.infoBox("Message", "You have succesfully voted for Rishabh for first place! Thank you for your vote.")  # Displays message box
            program.showSubWindow(select)
            program.hideSubWindow("I understood", useStopFunction=False)
            #program.setRadioButton("option","Josh",callFunction=False)
            #quit()
        elif program.getRadioButton("option") == "Don't select this box":
            program.infoBox("Message", "Your selection is not valid. Please pick another option.")  # Displays message box

    elif select == "Last Question":  # If user clicks 'Submit'
        if program.getRadioButton("option5") == "Hung":  # If user had chosen 'Hung'
            #program.setRadioButton("option5","Hung",callFunction=True)
            # program.infoBox("Message", "You have succesfully voted for Hung for second place! Thank you for your vote.")  # Displays message box
            program.showSubWindow(select)
            program.hideSubWindow("Next Question", useStopFunction=False)
            program.confirmHideSubWindow("Next Question")
            #quit()
        elif program.getRadioButton("option5") == "Josh": # If user had chosen 'Josh'
            # program.infoBox("Message", "You have succesfully voted for Josh for second place! Thank you for your vote.")
            program.showSubWindow(select)
            program.hideSubWindow("Next Question", useStopFunction=False)
            program.confirmHideSubWindow("Next Question")
            #quit()
        elif program.getRadioButton("option5") == "Samuel":# If user had chosen 'Sam'
            # program.infoBox("Message", "You have succesfully voted for Samuel for second place! Thank you for your vote.")
            program.showSubWindow(select)
            program.hideSubWindow("Next Question", useStopFunction=False)
            program.confirmHideSubWindow("Next Question")
            #quit()
        elif program.getRadioButton("option5") == "Rishabh": # If user had chosen 'Rishabh'
            # program.infoBox("Message", "You have succesfully voted for Rishabh for second place! Thank you for your vote.")  # Displays message box
            program.showSubWindow(select)
            program.hideSubWindow("Next Question", useStopFunction=False)
            program.confirmHideSubWindow("Next Question")
            #quit()
        elif program.getRadioButton("option5") == "Don't select this box":
            program.infoBox("Message", "Your selection is not valid. Please pick another option.")  # Displays message box
    
    if select == "Done":  # If user clicks 'Submit'
        if program.getRadioButton("option6") == "Hung":  # If user had chosen 'Hung'
            # program.infoBox("Message", "You have succesfully voted for Hung for third place! Thank you for your vote.")  # Displays message box
            program.showSubWindow(select)
            program.hideSubWindow("Last Question", useStopFunction=False)
            program.confirmHideSubWindow("Last Question")
            #quit()
        elif program.getRadioButton("option6") == "Josh": # If user had chosen 'Josh'
            # program.infoBox("Message", "You have succesfully voted for Josh for third place! Thank you for your vote.")
            program.showSubWindow(select)
            program.hideSubWindow("Last Question", useStopFunction=False)
            program.confirmHideSubWindow("Last Question")
            #quit()
        elif program.getRadioButton("option6") == "Samuel":# If user had chosen 'Sam'
            # program.infoBox("Message", "You have succesfully voted for Samuel for third place! Thank you for your vote.")
            program.showSubWindow(select)
            program.hideSubWindow("Last Question", useStopFunction=False)
            program.confirmHideSubWindow("Last Question")
            #quit()
        elif program.getRadioButton("option6") == "Rishabh":  # If user had chosen 'Rishabh'
            # program.infoBox("Message", "You have succesfully voted for Rishabh for third place! Thank you for your vote.")  # Displays message box
            program.showSubWindow(select)
            program.hideSubWindow("Last Question", useStopFunction=False)
            program.confirmHideSubWindow("Last Question")
            #quit()
        elif program.getRadioButton("option6") == "Don't select this box":
            program.infoBox("Message", "Your selection is not valid. Please pick another option.")  # Displays message box

    elif select == "More Info":  # If user clicks 'More Info'
        program.infoBox("More Info", "This is a demo of the GUI of DemocraSafe. For demo day, there will be description about each project") # Displays message box

    elif select == "Close":  # If user clicks 'Close'
        quit()  # Close program

    elif select == "More Info ":
        program.infoBox("More Info", "This is a demo of the GUI of DemocraSafe. For demo day, there will be description about each project") # Displays message box

    elif select == "Close ":
        quit()  # Close program

    elif select == " More Info ":
        program.infoBox("More Info", "This is a demo of the GUI of DemocraSafe. For demo day, there will be description about each project") # Displays message box
   
    elif select == " Close ":
        quit()  # Close program

# Widgets
program = gui("Welcome!", "600x600")  # Sets size and title of main GUI

program.addLabel("title","DemocraSafe")  # Title
program.getLabelWidget("title").config(font="Times 30 roman underline")
program.addButtons(["Start Voting", "Exit"], Start)
program.setButtonFont(size=50)

program.setBg("light blue")  # Sets background colour

program.startSubWindow("Start Voting", modal = True)
program.setSize(600, 600)
program.setBg("light blue")  # Sets background colour

program.addLabel("option1", "Voting Instructions")  # Title
program.getLabelWidget("option1").config(font="Times 30 roman underline")
program.addLabel("optio","1. Read the questions carefully before casting your vote")
program.addLabel("option2", "2. After you make your choice, proceed and it will take your to the next question")
program.addLabel("option3", "3. More Info for the summary of the projects, Close if you want to Exit")
program.addLabel("opti","4. Review your choices in the Summary page and click Submit")
# program.addLabel("option4", "6. We would appreciate your feedback by filling out the survey at the end")
program.addLabel("opt","5. Take the ballot to the scanner to cast your vote")
program.getLabelWidget("opt").config(font="Times 18 roman bold")
program.addButtons(["I understood", "Out"], Instructions)
program.stopSubWindow()

# Image
# Remove the # at the start of the next two lines once you have specified a file path
# appJar prefers .gif files, so convert images to .gif before you use them
# A good converter can be found here: https://image.online-convert.com/convert-to-gif
#program.addImage("logo", "/path/to/file")
#program.zoomImage("logo", -10)  # Shrinks image

program.startSubWindow("I understood", modal = True)
program.setSize(600, 600)
program.setBg("light blue")  # Sets background colour

# Labels
program.addLabel("option", "DemocraSafe GUI")  # Title
program.setLabelBg("option", "light yellow")  # Sets title background
program.getLabelWidget("option").config(font="Times 20 roman underline")

program.addLabel("question", "What is your choice for First Place?")  # Label

# Radiobuttons
program.setFont(15)
program.addRadioButton("option","No Vote")
program.addRadioButton("option","Hung")
program.addRadioButton("option","Josh")
program.addRadioButton("option","Samuel")
program.addRadioButton("option","Rishabh")

# Buttons
program.addButtons(["Next Question", "More Info", "Close"], ButtonHandler1)
program.stopSubWindow()

program.startSubWindow("Next Question", modal = True)
program.setSize(600, 600)
program.setBg("light blue")  # Sets background colour

# Labels
program.addLabel("option5", "DemocraSafe GUI")  # Title
program.setLabelBg("option5", "light yellow")  # Sets title background
program.getLabelWidget("option5").config(font="Times 20 roman underline")

program.addLabel("question2", "What is your choice for Second Place?")  # Label

# Radiobuttons
program.setFont(15)
program.addRadioButton("option5","No Vote")
program.addRadioButton("option5","Hung")
program.addRadioButton("option5","Josh")
program.addRadioButton("option5","Samuel")
program.addRadioButton("option5","Rishabh")
program.deselectAllListItems 

program.addButtons(["Last Question", "More Info ", "Close "], ButtonHandler1)
program.stopSubWindow()

program.startSubWindow("Last Question", modal = True)
program.setSize(600, 600)
program.setBg("light blue")  # Sets background colour

# Labels
program.addLabel("option6", "DemocraSafe GUI")  # Title
program.setLabelBg("option6", "light yellow")  # Sets title background
program.getLabelWidget("option6").config(font="Times 20 roman underline")

program.addLabel("question3", "What is your choice for Third Place?")  # Label

# Radiobuttons
program.setFont(15)
program.addRadioButton("option6","No Vote")
program.addRadioButton("option6","Hung")
program.addRadioButton("option6","Josh")
program.addRadioButton("option6","Samuel")
program.addRadioButton("option6","Rishabh")

program.addButtons(["Done", " More Info ", " Close "], ButtonHandler1)

program.setRadioButtonChangeFunction("option", Switch1) 
program.setRadioButtonChangeFunction("option5", Switch2)
program.setRadioButtonChangeFunction("option6", Switch3)

program.stopSubWindow()
program.go()

