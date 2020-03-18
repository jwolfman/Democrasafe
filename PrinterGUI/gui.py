#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import json
import popup
import printer
import reading
import change_vote
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.helv28 = tkfont.Font(family='Helvetica', size=15)
        self.title_font = tkfont.Font(family='Helvetica', size=30, weight='bold', slant='italic')
        self.header_font = tkfont.Font(family='Helvetica', size=30, weight='bold')
        self.helv28b = tkfont.Font(family='Helvetica', size=15, weight='bold')
        self.helv28i = tkfont.Font(family='Helvetica', size=13, slant='italic')

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others

        self.container = tk.Frame(self)
        self.container.pack(side='top', fill='both', expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Tkinter string variable # able to store any string value

        self.shared_data = {'1stplace': tk.StringVar(value='1'),
                            '2ndplace': tk.StringVar(value='1'),
                            '3rdplace': tk.StringVar(value='1')}

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

        frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(page_name.__name__)

    def restart_program(self):

        # Restarts the current program.
        # Note: this function does not return. Any cleanup action (like
        # saving data) must be done before calling this function."""

        # making sure all the entry are cleared and disable

        self.show_frame('StartPage')

        if 'PageTwo' in self.frames:
            self.shared_data['1stplace'].set('No Vote')
            for label in self.frames['PageTwo'].winfo_children():
                if isinstance(label, tk.Entry):
                    label.delete(0, tk.END)
                    label.configure(state='disabled')
                    label.update()
        if 'PageThree' in self.frames:
            self.shared_data['2ndplace'].set('No Vote')
            for label in self.frames['PageThree'].winfo_children():
                if isinstance(label, tk.Entry):
                    label.delete(0, tk.END)
                    label.configure(state='disabled')
                    label.update()
        if 'PageFour' in self.frames:
            self.shared_data['3rdplace'].set('No Vote')
            for label in self.frames['PageFour'].winfo_children():
                if isinstance(label, tk.Entry):
                    label.delete(0, tk.END)
                    label.configure(state='disabled')
                    label.update()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='DemocraSafe',
                         font=controller.title_font)
        label.pack(side='top', fill='x', pady=0)

        button1 = tk.Button(self, text='Start Voting',
                            font=controller.helv28, command=lambda :
                            controller.new_frame(PageOne))

        button1.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.2)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Voting Instructions',
                         font=controller.title_font)
        label.pack(side='top', fill='x', pady=20)

        label = tk.Label(self,
                         text='1. Read the questions carefully before casting your vote.'
                         , font=controller.helv28i)
        label.pack(fill='x', pady=5)
        label = tk.Label(self,
                         text="2. After you make your choice, proceed by clicking 'Next'."
                         , font=controller.helv28i)
        label.pack(fill='x', pady=5)
        label = tk.Label(self,
                         text="3. Click on 'More Info' for the summary of the projects."
                         , font=controller.helv28i)
        label.pack(fill='x', pady=5)
        label = tk.Label(self,
                         text="4. You can discard your ballot anytime during this process by clicking 'Discard Ballot'."
                         , font=controller.helv28i)
        label.pack(fill='x', pady=5)
        label = tk.Label(self,
                         text="5. Review your choices in the Summary page before you 'Print Ballot'."
                         , font=controller.helv28i)
        label.pack(fill='x', pady=5)
        label = tk.Label(self,
                         text='6. Wait for the ballot to print and insert it into the scanner to cast your vote.'
                         , font=controller.helv28i)
        label.pack(fill='x', pady=5)
        label = tk.Label(self,
                         text=' -- Please do not leave your machine unattended --'
                         , font=controller.helv28b)
        label.pack(fill='x', pady=5)

        button1 = tk.Button(self, text='I understand',
                            font=controller.helv28, command=lambda : \
                            self.next())
        button2 = tk.Button(self, text='Quit', font=controller.helv28,
                            command=lambda : controller.restart_program())
        button1.place(relx=0.25, rely=0.75, relwidth=0.2, relheight=0.2)
        button2.place(relx=0.55, rely=0.75, relwidth=0.2, relheight=0.2)

    def next(self):
        if 'PageTwo' in self.controller.frames:
            self.controller.show_frame('PageTwo')
        else:
            self.controller.new_frame(PageTwo)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        reading.read(self, '1', controller.shared_data["1stplace"])
        controller.shared_data["1stplace"].set("No Vote")

        button1 = tk.Button(self, text="Previous",
                           command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Next",
                           command=lambda: self.next())
        button3 = tk.Button(self, text="Discard Ballot",
                           command=lambda: controller.restart_program())
        button4 = tk.Button(self, text="More Info",
                           command=lambda: popup.popupmsg(self,self.controller.helv28b))

        button1.place(relx = 0.1, rely = 0.75, relwidth = 0.2, relheight = 0.1)
        button2.place(relx = 0.3, rely = 0.75, relwidth = 0.2, relheight = 0.1)
        button3.place(relx = 0.7, rely = 0.75, relwidth = 0.2, relheight = 0.1)
        button4.place(relx = 0.5, rely = 0.75, relwidth = 0.2, relheight = 0.1)

    def next(self):
        if self.controller.shared_data['1stplace'].get() == 'Others':
            if reading.get(self,'1') == '':
                popup.popupmsg2(self, self.controller.helv28b)
                return
            else:
                self.controller.shared_data['1stplace'
                        ].set(reading.get(self,'1'))
        
        if 'PageThree' in self.controller.frames:
            self.controller.show_frame('PageThree')
        else:
            self.controller.new_frame(PageThree)


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        reading.read(self, '2', controller.shared_data["2ndplace"])
        controller.shared_data['2ndplace'].set('No Vote')

        button1 = tk.Button(self, text='Previous', command=lambda : \
                            self.previous())
        button2 = tk.Button(self, text='Next', command=lambda : \
                            self.next())
        button3 = tk.Button(self, text='Discard Ballot',
                            command=lambda : controller.restart_program())
        button4 = tk.Button(self, text='More Info', command=lambda : \
                            popup.popupmsg(self,controller.helv28b))

        button1.place(relx=0.1, rely=0.75, relwidth=0.2, relheight=0.1)
        button2.place(relx=0.3, rely=0.75, relwidth=0.2, relheight=0.1)
        button3.place(relx=0.7, rely=0.75, relwidth=0.2, relheight=0.1)
        button4.place(relx=0.5, rely=0.75, relwidth=0.2, relheight=0.1)
    
    def previous(self):
        if 'PageTwo' in self.controller.frames:
            self.controller.shared_data['1stplace'].set(self.controller.shared_data['1stplace'].get())
        if 'PageThree' in self.controller.frames:
            self.controller.shared_data['2ndplace'].set(self.controller.shared_data['2ndplace'].get())
        if 'PageFour' in self.controller.frames:
            self.controller.shared_data['3rdplace'].set(self.controller.shared_data['3rdplace'].get())
        self.controller.show_frame('PageTwo')

    def next(self):
        if self.controller.shared_data['2ndplace'].get() == 'Others':
            if reading.get(self,'2') == '':
                popup.popupmsg2(self,controller.helv28b)
            else:
                self.controller.shared_data['2ndplace'].set(reading.get(self,'2'))

        if 'PageFour' in self.controller.frames:
            self.controller.show_frame('PageFour')
        else:
            self.controller.new_frame(PageFour)


class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        reading.read(self, '3', controller.shared_data["3rdplace"])
        controller.shared_data['3rdplace'].set('No Vote')

        button1 = tk.Button(self, text='Previous', command=lambda :
                            self.previous())
        button2 = tk.Button(self, text='Next', command=lambda :
                            self.next())
        button3 = tk.Button(self, text='Discard Ballot',
                            command=lambda : controller.restart_program())
        button4 = tk.Button(self, text='More Info', command=lambda :
                            popup.popupmsg(self,controller.helv28b))

        button1.place(relx=0.1, rely=0.75, relwidth=0.2, relheight=0.1)
        button2.place(relx=0.3, rely=0.75, relwidth=0.2, relheight=0.1)
        button3.place(relx=0.7, rely=0.75, relwidth=0.2, relheight=0.1)
        button4.place(relx=0.5, rely=0.75, relwidth=0.2, relheight=0.1)
    
    def previous(self):
        if 'PageTwo' in self.controller.frames:
            self.controller.shared_data['1stplace'].set(self.controller.shared_data['1stplace'].get())
        if 'PageThree' in self.controller.frames:
            self.controller.shared_data['2ndplace'].set(self.controller.shared_data['2ndplace'].get())
        if 'PageFour' in self.controller.frames:
            self.controller.shared_data['3rdplace'].set(self.controller.shared_data['3rdplace'].get())
        self.controller.show_frame('PageThree')

    def next(self):
        if self.controller.shared_data['3rdplace'].get() == 'Others':
            if reading.get(self,'3') == '':
                popup.popupmsg2(self,controller.helv28b)
            else:
                self.controller.shared_data['3rdplace'].set(reading.get(self,'3'))
        else:
            self.controller.shared_data['3rdplace'].set(self.controller.shared_data['3rdplace'].get())
        
        self.controller.new_frame(PageFive)


class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Ballot Summary',
                         font=controller.header_font)
        label.pack(side='top', fill='x', pady=20)

        label = tk.Label(self, text='1st Place: '
                         + controller.shared_data['1stplace'].get(),
                         font=controller.helv28b)
        label.pack(fill='x', pady=16)

        label = tk.Label(self, text='2nd Place: '
                         + controller.shared_data['2ndplace'].get(),
                         font=controller.helv28b)
        label.pack(fill='x', pady=23)

        label = tk.Label(self, text='3rd Place: '
                         + controller.shared_data['3rdplace'].get(),
                         font=controller.helv28b)
        label.pack(fill='x', pady=15)

        button1 = tk.Button(self, text='Change', font=10,
                            command=lambda : change_vote.change1(self))
        button2 = tk.Button(self, text='Change', font=10,
                            command=lambda : change_vote.change2(self))
        button3 = tk.Button(self, text='Change', font=10,
                            command=lambda : change_vote.change3(self))

        label = tk.Label(self,
                         text="-- Please review your votes above carefully as you cannot go back once you click 'Print Ballot' --"
                         , font=controller.helv28i)
        label.pack(fill='x', pady=20)

        button4 = tk.Button(self, text='Print Ballot',
                            font=controller.helv28, command=lambda : \
                            self.ballot())
        button5 = tk.Button(self, text='Discard Ballot',
                            font=controller.helv28, command=lambda : \
                            controller.restart_program())

        button1.place(relx=0.65, rely=0.21, relwidth=0.1,
                      relheight=0.05)
        button2.place(relx=0.65, rely=0.35, relwidth=0.1,
                      relheight=0.05)
        button3.place(relx=0.65, rely=0.5, relwidth=0.1, relheight=0.05)
        button4.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.2)
        button5.place(relx=0.6, rely=0.7, relwidth=0.3, relheight=0.2)

    def ballot(self):
        self.controller.new_frame(PageSix)

        printer.push(self.controller.shared_data['1stplace'].get(),
                     self.controller.shared_data['2ndplace'].get(),
                     self.controller.shared_data['3rdplace'].get())


class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='- Ballot Printing -',
                         font=controller.title_font)
        label.pack(side='top', fill='x', pady=20)

        label = tk.Label(self,
                         text='Thank you for choosing DemocraSafe!',
                         font=controller.title_font)
        label.pack(fill='x', pady=10)
        label = tk.Label(self,
                         text='Please do not forget to take your ballot below and insert it into the scanner.'
                         , font=controller.helv28i)
        label.pack(fill='x', pady=10)
        label = tk.Label(self, text='Happy Voting!',
                         font=controller.helv28b)
        label.pack(fill='x', pady=10)

        button2 = tk.Button(self, text='Quit', font=controller.helv28,
                            command=lambda : controller.restart_program())

        button2.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.2)


def main():
    app = SampleApp()

    app.attributes('-fullscreen', True)
    app.bind('<f>', lambda event: app.attributes('-fullscreen', True))
    app.bind('<Escape>', lambda event: app.attributes('-fullscreen', False))

    app.mainloop()


if __name__ == '__main__':
    os.system('stty -F /dev/serial0 19200')
    main()
