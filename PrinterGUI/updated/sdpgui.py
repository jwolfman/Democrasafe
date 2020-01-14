import sys
import os
import tkinter as tk                
from tkinter import font  as tkfont 
from tkinter import ttk

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.helv28 = tkfont.Font(family = 'Helvetica', size = 20) 
        self.title_font = tkfont.Font(family='Helvetica', size=40, weight="bold", slant="italic") 
        self.header_font = tkfont.Font(family='Helvetica', size=36, weight="bold") 
        self.helv28b = tkfont.Font(family = 'Helvetica', size = 20, weight = "bold") 
        self.helv28i = tkfont.Font(family = 'Helvetica', size = 20, slant = "italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        #Tkinter string variable # able to store any string value 
        self.shared_data = { "1stplace": tk.StringVar(value = "1"), 
                             "2ndplace": tk.StringVar(value = "1"), 
                             "3rdplace": tk.StringVar(value = "1") }

        self.frames = {}

        self.new_frame(StartPage)

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def destroy_frame(self, page_name):
        frame = self.frames[page_name]
        frame.grid_remove()

    def new_frame(self, page_name):
        frame = page_name(parent=self.container, controller=self)
        self.frames[page_name.__name__] = frame
        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
        frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(page_name.__name__)  
    
    def restart_program(self):
        # Restarts the current program.
        # Note: this function does not return. Any cleanup action (like
        # saving data) must be done before calling this function."""
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def popupmsg(self):
        popup = tk.Tk()
        popup.wm_title("Summary of Projects")

        f = open ('SDP_projects_summary.txt', 'r')
        for x in f:
            label = tk.Label(popup, text= x, font = self.helv28b)
            label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Done", command = popup.destroy)
        B1.pack()
        popup.mainloop()
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="DemocraSafe", font=controller.title_font)
        label.pack(side="top", fill="x", pady=300)

        button1 = tk.Button(self, text="Start Voting", font = controller.helv28,
                            command=lambda: controller.new_frame(PageOne))
        # button2 = tk.Button(self, text="Go to Page Two",
        #                     command=lambda: controller.show_frame("PageTwo"))
        button1.place(relx = 0.35, rely = 0.5, relwidth = 0.3, relheight = 0.2)
        # button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Voting Instructions", font=controller.title_font)
        label.pack(side="top", fill="x", pady=50)

        label = tk.Label(self, text="1. Read the questions carefully before casting your vote.", font=controller.helv28i)
        label.pack(fill="x", pady=20)
        label = tk.Label(self, text="2. After you make your choice, proceed by clicking 'Next'.", font=controller.helv28i)
        label.pack(fill="x", pady=20)
        label = tk.Label(self, text="3. Click on 'More Info' for the summary of the projects.", font=controller.helv28i)
        label.pack(fill="x", pady=20)
        label = tk.Label(self, text="4. You can discard your ballot anytime during this process by clicking 'Discard Ballot'.", font=controller.helv28i)
        label.pack(fill="x", pady=20)
        label = tk.Label(self, text="5. Review your choices in the Summary page before you 'Print Ballot'.", font=controller.helv28i)
        label.pack(fill="x", pady=20)
        label = tk.Label(self, text="6. Wait for the ballot to print and insert it into the scanner to cast your vote.", font=controller.helv28i)
        label.pack(fill="x", pady=20)
        label = tk.Label(self, text=" -- Please do not leave your machine unattended --", font=controller.helv28b)
        label.pack(fill="x", pady=20)

        button1 = tk.Button(self, text="I understood", font = controller.helv28,
                           command=lambda: controller.new_frame(PageTwo))
        button2 = tk.Button(self, text="Quit", font = controller.helv28,
                           command=lambda: controller.restart_program())
        button1.place(relx = 0.25, rely = 0.75, relwidth = 0.2, relheight = 0.2)
        button2.place(relx = 0.55, rely = 0.75, relwidth = 0.2, relheight = 0.2)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="What is your choice for First Place? ", font=controller.header_font)
        label.pack(side="top", fill="x", pady=10)

        # Dictionary to create multiple buttons 
        values = {"No Vote" : "No Vote", 
                  "Project 1" : "Dog", 
                  "Project 2" : "Mouse", 
                  "Project 3" : "Giraffe", 
                  "Project 4" : "Bird"} 
        
        self.entry1 = tk.Entry(self, width = 20)
        self.entry1.place(relx = 0.53,rely = 0.616)

        self.disableEntry()

        # Loop is used to create multiple Radiobuttons 
        # rather than creating each button separately 
        for (text, value) in values.items(): 
            tk.Radiobutton(self, text = text, variable = controller.shared_data["1stplace"], 
                        value = value, command=self.disableEntry).pack(side = 'top', ipady = 35)
        tk.Radiobutton(self, text = "Other: ", variable = controller.shared_data["1stplace"],
                       value = "Write-In1", command=self.enableEntry).pack(side = 'top', ipady = 30)

        controller.shared_data["1stplace"].set("No Vote")

        button1 = tk.Button(self, text="Previous",
                           command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Next",
                           command=lambda: self.next())
        button3 = tk.Button(self, text="Discard Ballot",
                           command=lambda: controller.restart_program())
        button4 = tk.Button(self, text="More Info",
                           command=lambda: controller.popupmsg())

        button1.place(relx = 0.1, rely = 0.75, relwidth = 0.2, relheight = 0.1)
        button2.place(relx = 0.3, rely = 0.75, relwidth = 0.2, relheight = 0.1)
        button3.place(relx = 0.7, rely = 0.75, relwidth = 0.2, relheight = 0.1)
        button4.place(relx = 0.5, rely = 0.75, relwidth = 0.2, relheight = 0.1)

    def next(self):
        self.write_in()

        if "PageThree" in self.controller.frames:
            self.controller.show_frame("PageThree") 
        else:
            self.controller.new_frame(PageThree)

    def write_in(self):
        if (self.controller.shared_data["1stplace"].get() == "Write-In1"):
            self.controller.shared_data["1stplace"].set(self.entry1.get())

    def enableEntry(self):
        self.entry1.configure(state="normal")
        self.entry1.update()

    def disableEntry(self):
        self.entry1.configure(state="disabled")
        self.entry1.update()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="What is your choice for Second Place?", font=controller.header_font)
        label.pack(side="top", fill="x", pady=10)

        # Dictionary to create multiple buttons 
        values = {"No Vote" : "No Vote", 
                  "Project 1" : "Dog", 
                  "Project 2" : "Mouse", 
                  "Project 3" : "Giraffe", 
                  "Project 4" : "Bird"} 

        self.entry2 = tk.Entry(self, width = 20)
        self.entry2.place(relx = 0.53,rely = 0.616)

        self.disableEntry()

        # Loop is used to create multiple Radiobuttons 
        # rather than creating each button separately 
        for (text, value) in values.items(): 
            tk.Radiobutton(self, text = text, variable = controller.shared_data["2ndplace"], 
                        value = value, command=self.disableEntry).pack(side = 'top', ipady = 35) 
        tk.Radiobutton(self, text = "Other: ", variable = controller.shared_data["2ndplace"],
                    value = "Write-In2", command=self.enableEntry).pack(side = 'top', ipady = 30)

        controller.shared_data["2ndplace"].set("No Vote")

        button1 = tk.Button(self, text="Previous",
                           command=lambda: controller.show_frame("PageTwo"))
        button2 = tk.Button(self, text="Next",
                           command=lambda: self.next())
        button3 = tk.Button(self, text="Discard Ballot",
                           command=lambda: controller.restart_program())
        button4 = tk.Button(self, text="More Info",
                           command=lambda: controller.popupmsg())

        button1.place(relx = 0.1, rely = 0.75, relwidth = 0.2, relheight = 0.1)
        button2.place(relx = 0.3, rely = 0.75, relwidth = 0.2, relheight = 0.1)
        button3.place(relx = 0.7, rely = 0.75, relwidth = 0.2, relheight = 0.1)
        button4.place(relx = 0.5, rely = 0.75, relwidth = 0.2, relheight = 0.1)

    def next(self):
        self.write_in()  

        if "PageFour" in self.controller.frames:
            self.controller.show_frame("PageFour") 
        else:
            self.controller.new_frame(PageFour)

    def write_in(self):
        if (self.controller.shared_data["2ndplace"].get() == "Write-In2"):
            self.controller.shared_data["2ndplace"].set(self.entry2.get())

    def enableEntry(self):
        self.entry2.configure(state="normal")
        self.entry2.update()

    def disableEntry(self):
        self.entry2.configure(state="disabled")
        self.entry2.update()

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="What is your choice for Third Place?", font=controller.header_font)
        label.pack(side="top", fill="x", pady=10)

        # Dictionary to create multiple buttons 
        values = {"No Vote" : "No Vote", 
                  "Project 1" : "Dog", 
                  "Project 2" : "Mouse", 
                  "Project 3" : "Giraffe", 
                  "Project 4" : "Bird"} 
        
        self.entry3 = tk.Entry(self, width = 20)
        self.entry3.place(relx = 0.53,rely = 0.616)

        self.disableEntry()

        # Loop is used to create multiple Radiobuttons 
        # rather than creating each button separately 
        for (text, value) in values.items(): 
            tk.Radiobutton(self, text = text, variable = controller.shared_data["3rdplace"], 
                        value = value, command=self.disableEntry).pack(side = 'top', ipady = 35) 
        tk.Radiobutton(self, text = "Other: ", variable = controller.shared_data["3rdplace"],
                    value = "Write-In3", command=self.enableEntry).pack(side = 'top', ipady = 30)

        controller.shared_data["3rdplace"].set("No Vote")

        button1 = tk.Button(self, text="Previous",
                           command=lambda: controller.show_frame("PageThree"))
        button2 = tk.Button(self, text="Next",
                           command=lambda: self.next())
        button3 = tk.Button(self, text="Discard Ballot",
                           command=lambda: controller.restart_program())
        button4 = tk.Button(self, text="More Info",
                           command=lambda: controller.popupmsg())

        button1.place(relx = 0.1, rely = 0.75, relwidth = 0.2, relheight = 0.1)
        button2.place(relx = 0.3, rely = 0.75, relwidth = 0.2, relheight = 0.1)
        button3.place(relx = 0.7, rely = 0.75, relwidth = 0.2, relheight = 0.1)
        button4.place(relx = 0.5, rely = 0.75, relwidth = 0.2, relheight = 0.1)

    def next(self):
        self.write_in()  
        self.controller.new_frame(PageFive)

    def write_in(self):
        if (self.controller.shared_data["3rdplace"].get() == "Write-In3"):
            self.controller.shared_data["3rdplace"].set(self.entry3.get())
        
    def enableEntry(self):
        self.entry3.configure(state="normal")
        self.entry3.update()

    def disableEntry(self):
        self.entry3.configure(state="disabled")
        self.entry3.update()

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Ballot Summary", font=controller.header_font)
        label.pack(side="top", fill="x", pady=50)

        label = tk.Label(self, text="1st Place: " + controller.shared_data["1stplace"].get(), font=controller.helv28b)
        label.pack(fill="x", pady=50)

        label = tk.Label(self, text="2nd Place: " + controller.shared_data["2ndplace"].get(), font=controller.helv28b)        
        label.pack(fill="x", pady=50)

        label = tk.Label(self, text="3rd Place: " + controller.shared_data["3rdplace"].get(), font=controller.helv28b)
        label.pack(fill="x", pady=50)

        button1 = tk.Button(self, text="Change", font = 15,
                           command=lambda: self.change1())
        button2 = tk.Button(self, text="Change", font = 15,
                           command=lambda: self.change2())
        button3 = tk.Button(self, text="Change", font = 15,
                           command=lambda: self.change3())

        label = tk.Label(self, text="-- Please review your votes above carefully as you cannot go back once you click 'Print Ballot' --", font=controller.helv28i)                
        label.pack(fill="x", pady=20)

        button4 = tk.Button(self, text="Print Ballot", font = controller.helv28,
                           command=lambda: controller.new_frame(PageSix))  
        button5 = tk.Button(self, text="Discard Ballot", font = controller.helv28,
                           command=lambda: controller.restart_program())                 

        button1.place(relx = 0.6, rely = 0.21, relwidth = 0.05, relheight = 0.05)
        button2.place(relx = 0.6, rely = 0.35, relwidth = 0.05, relheight = 0.05)
        button3.place(relx = 0.6, rely = 0.5, relwidth = 0.05, relheight = 0.05)
        button4.place(relx = 0.1, rely = 0.7, relwidth = 0.3, relheight = 0.2)
        button5.place(relx = 0.6, rely = 0.7, relwidth = 0.3, relheight = 0.2)

    def change1(self):
        if(self.controller.shared_data["1stplace"].get() != "No Vote" and 
           self.controller.shared_data["1stplace"].get() != "Dog" and 
           self.controller.shared_data["1stplace"].get() != "Mouse" and 
           self.controller.shared_data["1stplace"].get() !="Giraffe" and 
           self.controller.shared_data["1stplace"].get() !="Bird"):
            self.controller.shared_data["1stplace"].set("Write-In1")  

        if(self.controller.shared_data["2ndplace"].get() != "No Vote" and 
           self.controller.shared_data["2ndplace"].get() != "Dog" and 
           self.controller.shared_data["2ndplace"].get() != "Mouse" and 
           self.controller.shared_data["2ndplace"].get() != "Giraffe" and 
           self.controller.shared_data["2ndplace"].get() != "Bird"):
            self.controller.shared_data["2ndplace"].set("Write-In2")

        if(self.controller.shared_data["3rdplace"].get() != "No Vote" and 
           self.controller.shared_data["3rdplace"].get() != "Dog" and 
           self.controller.shared_data["3rdplace"].get() != "Mouse" and 
           self.controller.shared_data["3rdplace"].get() !="Giraffe" and 
           self.controller.shared_data["3rdplace"].get() !="Bird"):
            self.controller.shared_data["3rdplace"].set("Write-In3")   

        self.controller.show_frame("PageTwo")

    def change2(self):
        if(self.controller.shared_data["2ndplace"].get() != "No Vote" and 
           self.controller.shared_data["2ndplace"].get() != "Dog" and 
           self.controller.shared_data["2ndplace"].get() != "Mouse" and 
           self.controller.shared_data["2ndplace"].get() != "Giraffe" and 
           self.controller.shared_data["2ndplace"].get() != "Bird"):
            self.controller.shared_data["2ndplace"].set("Write-In2") 

        if(self.controller.shared_data["3rdplace"].get() != "No Vote" and 
           self.controller.shared_data["3rdplace"].get() != "Dog" and 
           self.controller.shared_data["3rdplace"].get() != "Mouse" and 
           self.controller.shared_data["3rdplace"].get() !="Giraffe" and 
           self.controller.shared_data["3rdplace"].get() !="Bird"):
            self.controller.shared_data["3rdplace"].set("Write-In3") 

        self.controller.show_frame("PageThree")  

    def change3(self):
        if(self.controller.shared_data["3rdplace"].get() != "No Vote" and 
           self.controller.shared_data["3rdplace"].get() != "Dog" and 
           self.controller.shared_data["3rdplace"].get() != "Mouse" and 
           self.controller.shared_data["3rdplace"].get() !="Giraffe" and 
           self.controller.shared_data["3rdplace"].get() !="Bird"):
            self.controller.shared_data["3rdplace"].set("Write-In3")   

        self.controller.show_frame("PageFour")

class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="- Ballot Printing -", font=controller.title_font)
        label.pack(side="top", fill="x", pady=50)

        label = tk.Label(self, text="Thank you for choosing DemocraSafe!", font=controller.title_font)
        label.pack(fill="x", pady=20)
        label = tk.Label(self, text="Please do not forget to take your ballot below and insert it into the scanner.", font=controller.helv28i)
        label.pack(fill="x", pady=20)
        label = tk.Label(self, text="Happy Voting!", font=controller.helv28b)
        label.pack(fill="x", pady=20)

        button2 = tk.Button(self, text="Quit", font = controller.helv28,
                           command=lambda: controller.restart_program())

        button2.place(relx = 0.35, rely = 0.5, relwidth = 0.3, relheight = 0.2)

def main():
    app = SampleApp()

    app.attributes("-fullscreen",True)
    app.bind("<f>", lambda event: app.attributes("-fullscreen",True))
    app.bind("<Escape>", lambda event: app.attributes("-fullscreen", False))

    app.mainloop()

if __name__ == "__main__":
    main()