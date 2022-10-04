from tkinter import *

window = Tk() # Creating a window

# Function on click of button
def km_to_miles():
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)

# ========== Adding widgets to the window ============

# Button
b1 = Button(window,text="Execute",command=km_to_miles)
b1.grid(row=0,column=0)

# EntryBox
e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

# TextBox
t1 = Text(window,height=1,width=20)
t1.grid(row=0,column=2)

window.mainloop()