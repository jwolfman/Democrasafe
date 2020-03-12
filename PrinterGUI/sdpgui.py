#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import random
import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.helv28 = tkfont.Font(family='Helvetica', size=15)
        self.title_font = tkfont.Font(family='Helvetica', size=30,
                weight='bold', slant='italic')
        self.header_font = tkfont.Font(family='Helvetica', size=30,
                weight='bold')
        self.helv28b = tkfont.Font(family='Helvetica', size=15,
                                   weight='bold')
        self.helv28i = tkfont.Font(family='Helvetica', size=13,
                                   slant='italic')

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

    def popupmsg(self):
        self.update_idletasks()

        popup = tk.Tk()
        popup.wm_title('Summary of Projects')

        w = self.winfo_reqwidth()
        h = self.winfo_reqheight()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()

        x = ws / 2 - w / 2
        y = hs / 2 - h / 2

        popup.geometry('+%d+%d' % (x, y))

        f = open('SDP_projects_summary.txt', 'r')
        for x in f:
            label = tk.Label(popup, text=x, font=self.helv28b)
            label.pack(side='top', fill='x', pady=20)
        B1 = ttk.Button(popup, text='Close', command=popup.destroy)
        B1.pack()
        popup.mainloop()

    def popupmsg2(self):
        self.update_idletasks()

        popup = tk.Tk()
        popup.wm_title('Error!')

        w = self.winfo_reqwidth()
        h = self.winfo_reqheight()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()

        x = ws / 2 - w / 2
        y = hs / 2 - h / 2

        popup.geometry('+%d+%d' % (x, y))

        label = tk.Label(popup,
                         text="Please fill out your choice for 'Other'"
                         , font=self.helv28b)
        label.pack(side='top', fill='x', pady=10)
        B1 = ttk.Button(popup, text='Close', command=popup.destroy)
        B1.pack()
        popup.mainloop()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='DemocraSafe',
                         font=controller.title_font)
        label.pack(side='top', fill='x', pady=0)

        button1 = tk.Button(self, text='Start Voting',
                            font=controller.helv28, command=lambda : \
                            controller.new_frame(PageOne))

        # button2 = tk.Button(self, text="Go to Page Two",
        #                     command=lambda: controller.show_frame("PageTwo"))

        button1.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.2)


        # button2.pack()

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
                            command=lambda : self.restart())
        button1.place(relx=0.25, rely=0.75, relwidth=0.2, relheight=0.2)
        button2.place(relx=0.55, rely=0.75, relwidth=0.2, relheight=0.2)

    def next(self):
        if 'PageTwo' in self.controller.frames:
            self.controller.show_frame('PageTwo')
        else:
            self.controller.new_frame(PageTwo)

    def restart(self):
        self.controller.restart_program()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,
                         text='What is your choice for First Place? ',
                         font=controller.header_font)
        label.pack(side='top', fill='x', pady=10)

        # Dictionary to create multiple buttons

        values = {
            'No Vote': 'No Vote',
            'Project 1': 'Project 1',
            'Project 2': 'Project 2',
            'Project 3': 'Project 3',
            'Project 4': 'Project 4',
            }

        self.entry1 = tk.Entry(self, width=20)
        self.entry1.place(relx=0.53, rely=0.616)

        self.disableEntry()

        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately

        for (text, value) in values.items():

            tk.Radiobutton(self, text=text,
                           variable=controller.shared_data['1stplace'],
                           value=value,
                           command=self.disableEntry).pack(side='top',
                    ipady=10)

        tk.Radiobutton(self, text='Other: ',
                       variable=controller.shared_data['1stplace'],
                       value='Write-In1',
                       command=self.enableEntry).pack(side='top',
                ipady=10)

        controller.shared_data['1stplace'].set('No Vote')

        button1 = tk.Button(self, text='Previous', command=lambda : \
                            controller.show_frame('PageOne'))
        button2 = tk.Button(self, text='Next', command=lambda : \
                            self.next())
        button3 = tk.Button(self, text='Discard Ballot',
                            command=lambda : self.restart())
        button4 = tk.Button(self, text='More Info', command=lambda : \
                            controller.popupmsg())

        button1.place(relx=0.1, rely=0.75, relwidth=0.2, relheight=0.1)
        button2.place(relx=0.3, rely=0.75, relwidth=0.2, relheight=0.1)
        button3.place(relx=0.7, rely=0.75, relwidth=0.2, relheight=0.1)
        button4.place(relx=0.5, rely=0.75, relwidth=0.2, relheight=0.1)

    def next(self):
        self.write_in()
        if 'PageThree' in self.controller.frames:
            self.controller.show_frame('PageThree')
        else:
            self.controller.new_frame(PageThree)

    def write_in(self):
        if self.controller.shared_data['1stplace'].get() == 'Write-In1':
            if self.entry1.get() == '':
                self.controller.popupmsg2()
                return
            else:
                self.controller.shared_data['1stplace'
                        ].set(self.entry1.get())

    def enableEntry(self):
        self.entry1.configure(state='normal')
        self.entry1.update()

    def disableEntry(self):
        self.entry1.delete(0, 'end')
        self.entry1.configure(state='disabled')
        self.entry1.update()

    def restart(self):
        self.controller.restart_program()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,
                         text='What is your choice for Second Place?',
                         font=controller.header_font)
        label.pack(side='top', fill='x', pady=10)

        # Dictionary to create multiple buttons

        values = {
            'No Vote': 'No Vote',
            'Project 1': 'Project 1',
            'Project 2': 'Project 2',
            'Project 3': 'Project 3',
            'Project 4': 'Project 4',
            }

        self.entry2 = tk.Entry(self, width=20)
        self.entry2.place(relx=0.53, rely=0.616)

        self.disableEntry()

        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately

        for (text, value) in values.items():

            tk.Radiobutton(self, text=text,
                           variable=controller.shared_data['2ndplace'],
                           value=value,
                           command=self.disableEntry).pack(side='top',
                    ipady=10)

        tk.Radiobutton(self, text='Other: ',
                       variable=controller.shared_data['2ndplace'],
                       value='Write-In2',
                       command=self.enableEntry).pack(side='top',
                ipady=10)

        controller.shared_data['2ndplace'].set('No Vote')

        button1 = tk.Button(self, text='Previous', command=lambda : \
                            self.previous())
        button2 = tk.Button(self, text='Next', command=lambda : \
                            self.next())
        button3 = tk.Button(self, text='Discard Ballot',
                            command=lambda : self.restart())
        button4 = tk.Button(self, text='More Info', command=lambda : \
                            controller.popupmsg())

        button1.place(relx=0.1, rely=0.75, relwidth=0.2, relheight=0.1)
        button2.place(relx=0.3, rely=0.75, relwidth=0.2, relheight=0.1)
        button3.place(relx=0.7, rely=0.75, relwidth=0.2, relheight=0.1)
        button4.place(relx=0.5, rely=0.75, relwidth=0.2, relheight=0.1)

    def previous(self):
        if self.controller.shared_data['1stplace'].get() != 'No Vote' \
            and self.controller.shared_data['1stplace'].get() \
            != 'Project 1' and self.controller.shared_data['1stplace'
                ].get() != 'Project 2' \
            and self.controller.shared_data['1stplace'].get() \
            != 'Project 3' and self.controller.shared_data['1stplace'
                ].get() != 'Project 4':
            self.controller.shared_data['1stplace'].set('Write-In1')

        self.controller.show_frame('PageTwo')

    def next(self):
        self.write_in()

        if 'PageFour' in self.controller.frames:
            self.controller.show_frame('PageFour')
        else:
            self.controller.new_frame(PageFour)

    def write_in(self):
        if self.controller.shared_data['2ndplace'].get() == 'Write-In2':
            if self.entry2.get() == '':
                self.controller.popupmsg2()
            else:
                self.controller.shared_data['2ndplace'
                        ].set(self.entry2.get())

    def enableEntry(self):
        self.entry2.configure(state='normal')
        self.entry2.update()

    def disableEntry(self):
        self.entry2.delete(0, 'end')
        self.entry2.configure(state='disabled')
        self.entry2.update()

    def restart(self):
        self.controller.restart_program()


class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,
                         text='What is your choice for Third Place?',
                         font=controller.header_font)
        label.pack(side='top', fill='x', pady=10)

        # Dictionary to create multiple buttons

        values = {
            'No Vote': 'No Vote',
            'Project 1': 'Project 1',
            'Project 2': 'Project 2',
            'Project 3': 'Project 3',
            'Project 4': 'Project 4',
            }

        self.entry3 = tk.Entry(self, width=20)
        self.entry3.place(relx=0.53, rely=0.616)

        self.disableEntry()

        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately

        for (text, value) in values.items():

            tk.Radiobutton(self, text=text,
                           variable=controller.shared_data['3rdplace'],
                           value=value,
                           command=self.disableEntry).pack(side='top',
                    ipady=10)

        tk.Radiobutton(self, text='Other: ',
                       variable=controller.shared_data['3rdplace'],
                       value='Write-In3',
                       command=self.enableEntry).pack(side='top',
                ipady=10)

        controller.shared_data['3rdplace'].set('No Vote')

        button1 = tk.Button(self, text='Previous', command=lambda : \
                            self.previous())
        button2 = tk.Button(self, text='Next', command=lambda : \
                            self.next())
        button3 = tk.Button(self, text='Discard Ballot',
                            command=lambda : self.restart())
        button4 = tk.Button(self, text='More Info', command=lambda : \
                            controller.popupmsg())

        button1.place(relx=0.1, rely=0.75, relwidth=0.2, relheight=0.1)
        button2.place(relx=0.3, rely=0.75, relwidth=0.2, relheight=0.1)
        button3.place(relx=0.7, rely=0.75, relwidth=0.2, relheight=0.1)
        button4.place(relx=0.5, rely=0.75, relwidth=0.2, relheight=0.1)

    def previous(self):
        if self.controller.shared_data['1stplace'].get() != 'No Vote' \
            and self.controller.shared_data['1stplace'].get() \
            != 'Project 1' and self.controller.shared_data['1stplace'
                ].get() != 'Project 2' \
            and self.controller.shared_data['1stplace'].get() \
            != 'Project 3' and self.controller.shared_data['1stplace'
                ].get() != 'Project 4':
            self.controller.shared_data['1stplace'].set('Write-In1')

        if self.controller.shared_data['2ndplace'].get() != 'No Vote' \
            and self.controller.shared_data['2ndplace'].get() \
            != 'Project 1' and self.controller.shared_data['2ndplace'
                ].get() != 'Project 2' \
            and self.controller.shared_data['2ndplace'].get() \
            != 'Project 3' and self.controller.shared_data['2ndplace'
                ].get() != 'Project 4':
            self.controller.shared_data['2ndplace'].set('Write-In2')

        self.controller.show_frame('PageThree')

    def next(self):
        self.write_in()
        self.controller.new_frame(PageFive)

    def write_in(self):
        if self.controller.shared_data['3rdplace'].get() == 'Write-In3':
            if self.entry3.get() == '':
                self.controller.popupmsg2()
            else:
                self.controller.shared_data['3rdplace'
                        ].set(self.entry3.get())

    def enableEntry(self):
        self.entry3.configure(state='normal')
        self.entry3.update()

    def disableEntry(self):
        self.entry3.delete(0, 'end')
        self.entry3.configure(state='disabled')
        self.entry3.update()

    def restart(self):
        self.controller.restart_program()


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
                            command=lambda : self.change1())
        button2 = tk.Button(self, text='Change', font=10,
                            command=lambda : self.change2())
        button3 = tk.Button(self, text='Change', font=10,
                            command=lambda : self.change3())

        label = tk.Label(self,
                         text="-- Please review your votes above carefully as you cannot go back once you click 'Print Ballot' --"
                         , font=controller.helv28i)
        label.pack(fill='x', pady=20)

        button4 = tk.Button(self, text='Print Ballot',
                            font=controller.helv28, command=lambda : \
                            self.ballot())
        button5 = tk.Button(self, text='Discard Ballot',
                            font=controller.helv28, command=lambda : \
                            self.restart())

        button1.place(relx=0.65, rely=0.21, relwidth=0.1,
                      relheight=0.05)
        button2.place(relx=0.65, rely=0.35, relwidth=0.1,
                      relheight=0.05)
        button3.place(relx=0.65, rely=0.5, relwidth=0.1, relheight=0.05)
        button4.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.2)
        button5.place(relx=0.6, rely=0.7, relwidth=0.3, relheight=0.2)

    def getID(self):
        out = ''
        options = \
            '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTTUVWXYZ'
        out += options[random.randint(0, 62)]
        out += options[random.randint(0, 62)]
        out += options[random.randint(0, 62)]
        out += options[random.randint(0, 62)]
        out += options[random.randint(0, 62)]
        out += options[random.randint(0, 62)]
        return out

    def ballot(self):
        self.controller.new_frame(PageSix)

        rows = 0
        results = []
        random = getID()
        for input in [self.controller.shared_data['1stplace'].get(),
                      self.controller.shared_data['2ndplace'].get(),
                      self.controller.shared_data['3rdplace'].get()]:
            output = ''
            while len(input) > 32:
                rows = rows + 1
                lastSpace = str.rindex(input, beg=0, end=32)
                if lastSpace != -1 and 32 - lastSpace < 5:
                    if str.rindex(input, beg=33, end=33) != -1:
                        output += input[0:32] + '\n'
                        input = input[33:len(input)]
                    else:
                        output += input[0:lastSpace] + '\n'
                        input = input[lastSpace + 1:len(input)]
                else:
                    output += input[0:31] + '-'
                    input = input[32:len(input)]

            output += input
            results.append(output)

        os.system("echo \"" + chr(0xFF) + (" " * 12) + randomID + (" " * 12)
                  + chr(0xCD) + "\n\" > /dev/serial0")
        rows += 1

        os.system("echo \"1st:" + results[0] + "\n\" > /dev/serial0")
        rows += 2

        os.system("echo \"2nd:" + results[1] + "\n\" > /dev/serial0")
        rows += 2

        os.system("echo \"3rd:" + results[2] + "\n\" > /dev/serial0")
        rows += 2

        os.system("echo \"" + chr(0xDB) + (" " * 12) + randomID + (" " * 12)
                  + chr(0x8D) + "\n\" > /dev/serial0")
        rows += 1

        os.system('echo \"Thank you for voting. Hold on to'
                  + 'this reciept and insert it to\n'
                  + 'the scanning unit to cast your\n'
                  + 'Vote. Thank you for voting.\n\" > /dev/serial0')
        rows += 5
        os.system('echo "This system has been brought to\n'
                  + 'you by Team 26: DemocraSafe." > /dev/serial0')
        rows += 2
        while rows < 28:  # about 10.5CM
            os.system('echo "" > /dev/serial0')
            rows = rows + 1

    def change1(self):
        if self.controller.shared_data['1stplace'].get() != 'No Vote' \
            and self.controller.shared_data['1stplace'].get() \
            != 'Project 1' and self.controller.shared_data['1stplace'
                ].get() != 'Project 2' \
            and self.controller.shared_data['1stplace'].get() \
            != 'Project 3' and self.controller.shared_data['1stplace'
                ].get() != 'Project 4':
            self.controller.shared_data['1stplace'].set('Write-In1')

        if self.controller.shared_data['2ndplace'].get() != 'No Vote' \
            and self.controller.shared_data['2ndplace'].get() \
            != 'Project 1' and self.controller.shared_data['2ndplace'
                ].get() != 'Project 2' \
            and self.controller.shared_data['2ndplace'].get() \
            != 'Project 3' and self.controller.shared_data['2ndplace'
                ].get() != 'Project 4':
            self.controller.shared_data['2ndplace'].set('Write-In2')

        if self.controller.shared_data['3rdplace'].get() != 'No Vote' \
            and self.controller.shared_data['3rdplace'].get() \
            != 'Project 1' and self.controller.shared_data['3rdplace'
                ].get() != 'Project 2' \
            and self.controller.shared_data['3rdplace'].get() \
            != 'Project 3' and self.controller.shared_data['3rdplace'
                ].get() != 'Project 4':
            self.controller.shared_data['3rdplace'].set('Write-In3')

        self.controller.show_frame('PageTwo')

    def change2(self):
        if self.controller.shared_data['2ndplace'].get() != 'No Vote' \
            and self.controller.shared_data['2ndplace'].get() \
            != 'Project 1' and self.controller.shared_data['2ndplace'
                ].get() != 'Project 2' \
            and self.controller.shared_data['2ndplace'].get() \
            != 'Project 3' and self.controller.shared_data['2ndplace'
                ].get() != 'Project 4':
            self.controller.shared_data['2ndplace'].set('Write-In2')

        if self.controller.shared_data['3rdplace'].get() != 'No Vote' \
            and self.controller.shared_data['3rdplace'].get() \
            != 'Project 1' and self.controller.shared_data['3rdplace'
                ].get() != 'Project 2' \
            and self.controller.shared_data['3rdplace'].get() \
            != 'Project 3' and self.controller.shared_data['3rdplace'
                ].get() != 'Project 4':
            self.controller.shared_data['3rdplace'].set('Write-In3')

        self.controller.show_frame('PageThree')

    def change3(self):
        if self.controller.shared_data['3rdplace'].get() != 'No Vote' \
            and self.controller.shared_data['3rdplace'].get() \
            != 'Project 1' and self.controller.shared_data['3rdplace'
                ].get() != 'Project 2' \
            and self.controller.shared_data['3rdplace'].get() \
            != 'Project 3' and self.controller.shared_data['3rdplace'
                ].get() != 'Project 4':
            self.controller.shared_data['3rdplace'].set('Write-In3')

        self.controller.show_frame('PageFour')

    def restart(self):
        self.controller.restart_program()


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
                            command=lambda : self.restart())

        button2.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.2)

    def restart(self):
        self.controller.restart_program()


def main():
    app = SampleApp()

    app.attributes('-fullscreen', True)
    app.bind('<f>', lambda event: app.attributes('-fullscreen', True))
    app.bind('<Escape>', lambda event: app.attributes('-fullscreen',
             False))

    app.mainloop()


if __name__ == '__main__':
    os.system('stty -F /dev/serial0 19200')
    main()
