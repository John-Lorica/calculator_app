import tkinter as tk
from tkinter import messagebox


class MyGUI:

    def __init__(self):

        # To create the main window
        root = tk.Tk()
        # The title
        root.title('My First Project')
        # The size
        root.geometry('300x400')

        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close Without Question", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(
            label="Show Message", command=self.show_message)

        label = tk.Label(root, text='Hello, TKinter!')
        label.place(x=110, y=40)

        button = tk.Button(root, text='Start', command=lambda: label.config(
            text='Welcome!'))
        button.place(x=120, y=80)

        buttonframe = tk.Frame(root)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)

        btn1 = tk.Button(buttonframe, text='1', font=('Arial', 18))
        btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

        btn2 = tk.Button(buttonframe, text='1', font=('Arial', 18))
        btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

        btn3 = tk.Button(buttonframe, text='1', font=('Arial', 18))
        btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

        btn4 = tk.Button(buttonframe, text='1', font=('Arial', 18))
        btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

        btn5 = tk.Button(buttonframe, text='1', font=('Arial', 18))
        btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

        btn6 = tk.Button(buttonframe, text='1', font=('Arial', 18))
        btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

        btn7 = tk.Button(buttonframe, text='1', font=('Arial', 18))
        btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

        btn8 = tk.Button(buttonframe, text='1', font=('Arial', 18))
        btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

        btn9 = tk.Button(buttonframe, text='1', font=('Arial', 18))
        btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

        label = tk.Label(root, text='Placeholder')
        label.place(x=110, y=200)

        # GUI event loop
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        root.mainloop()

        # study TKinter Entry Widget and TKinter Button
        # realized that I have specific things I need to study in TKinter instead of all of it


MyGUI()
