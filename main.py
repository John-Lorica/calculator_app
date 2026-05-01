import tkinter as tk

# To create the main window
root = tk.Tk()
# The title
root.title('My First Project')
# The size
root.geometry('300x400')

label = tk.Label(root, text='Hello, TKinter!')
label.place(x=110, y=40)

button = tk.Button(root, text='Start', command=lambda: label.config(
    text='Welcome!'))
button.place(x=120, y=80)

label = tk.Label(root, text='Placeholder')
label.place(x=110, y=200)

# GUI event loop
root.mainloop()

# study TKinter Entry Widget and TKinter Button
# realized that I have specific things I need to study in TKinter instead of all of it
