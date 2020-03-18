import tkinter as tk
from tkinter import ttk

def popupmsg(self, font):
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
        label = tk.Label(popup, text=x, font=font)
        label.pack(side='top', fill='x', pady=20)
    B1 = ttk.Button(popup, text='Close', command=popup.destroy)
    B1.pack()
    popup.mainloop()

def popupmsg2(self, font):
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
                     , font=font)
    label.pack(side='top', fill='x', pady=10)
    B1 = ttk.Button(popup, text='Close', command=popup.destroy)
    B1.pack()
    popup.mainloop()
