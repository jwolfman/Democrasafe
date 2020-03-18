import tkinter as tk
from tkinter import font as tkfont
import json
import gui

def read(self, file, variable):        
    f = open('ballot.json')
    read = json.load(f)
    question = read[file]['QUESTION']
    label = tk.Label(self, text=question, font=tkfont.Font(family='Helvetica', size=30, weight='bold'))
    label.pack(side="top", fill="x", pady=10)

    canvas = tk.Canvas(self)
    scrollbar = tk.Scrollbar(canvas, orient='vertical', command=canvas.yview)

    # Dictionary to create multiple buttons 
    values = read[file]['OPTIONS']

    if (file == '1'):
        if (read[file]['ENABLE_WRITE_IN'] == True):
            self.entry1= tk.Entry(self, width = 20)
            self.entry1.place(relx = 0.43,rely = 0.6)
    elif (file == '2'):
        if (read[file]['ENABLE_WRITE_IN'] == True):
            self.entry2= tk.Entry(self, width = 20)
            self.entry2.place(relx = 0.43,rely = 0.6)
    else:
        if (read[file]['ENABLE_WRITE_IN'] == True):
            self.entry3= tk.Entry(self, width = 20)
            self.entry3.place(relx = 0.43,rely = 0.6)

    # Loop is used to create multiple Radiobuttons 
    # rather than creating each button separately 
    i = 0

    for text in values:    
        if (text != 'Others'):
            if (file == '1'):
                label = tk.Radiobutton(canvas, text = text, value = text, variable = variable)
            elif (file == '2'):
                label = tk.Radiobutton(canvas, text = text, value = text, variable = variable)
            else:
                label = tk.Radiobutton(canvas, text = text, value = text, variable = variable)
        
        if (read[file]['ENABLE_WRITE_IN'] == True):
            if (text == 'Others'):
                if (file == '1'):
                    label = tk.Radiobutton(canvas, text = text, value = text, variable = variable)
                elif (file == '2'):
                    label = tk.Radiobutton(canvas, text = text, value = text, variable = variable)
                else:
                    label = tk.Radiobutton(canvas, text = text, value = text, variable = variable)

        canvas.create_window(0, 50 * i, window=label, anchor = 'w')
        i = i + 1 

    canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrollbar.set)

    canvas.place(relwidth = .2, relheight = .5, relx=.56, rely=.35, anchor="center")
    scrollbar.pack(fill='y', side='right')

    f.close()

def get(self, file):
    if (file == '1'):
        return self.entry1.get()
    elif (file == '2'):
        return self.entry2.get()
    else:
        return self.entry3.get()

def enableEntry():
    self.entry1.configure(state='normal')
    self.entry1.update()
    
def disableEntry():
    self.entry1.delete(0, 'end')
    self.entry1.configure(state='disabled')
    self.entry1.update()
