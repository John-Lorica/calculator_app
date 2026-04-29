import tkinter as tk

# To create the main window
root = tk.Tk()
# The title
root.title('My First Project')
# The size
root.geometry('300x400')

label = tk.Label(root, text='Hello, TKinter!')
label.place(x=110, y=40)

button = tk.Button(root, text='Click Me', command=lambda: label.config(
    text='You clicked the button!'))
button.place(x=110, y=80)

# GUI event loop
root.mainloop()

# study TKinter Entry Widget and TKinter Button
