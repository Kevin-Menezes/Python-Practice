from tkinter import *

window = Tk()

# Function on click of button
def kg_to_others():
    gram=float(e1_value.get())*1000
    pound=float(e1_value.get())*2.20462
    ounce=float(e1_value.get())*35.274

    t1.delete("1.0", END) # Deletes if any previous text is there
    t1.insert(END,gram)

    t2.delete("1.0", END) # Deletes if any previous text is there
    t2.insert(END,pound)

    t3.delete("1.0", END) # Deletes if any previous text is there
    t3.insert(END,ounce)



# Label
l1=Label(window,text="Kg ->")
l1.grid(row=0,column=0) 

# EntryBox
e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

# Button
b1 = Button(window,text="Convert",command=kg_to_others)
b1.grid(row=0,column=2)

# -------------------------

# Label
l2=Label(window,text="g")
l2.grid(row=1,column=0) 

# Label
l3=Label(window,text="£")
l3.grid(row=1,column=1)

# Label
l4=Label(window,text="℥")
l4.grid(row=1,column=2)

# -------------------------

# TextBox
t1 = Text(window,height=1,width=20)
t1.grid(row=2,column=0)

# TextBox
t2 = Text(window,height=1,width=20)
t2.grid(row=2,column=1)

# TextBox
t3 = Text(window,height=1,width=20)
t3.grid(row=2,column=2)
 
window.mainloop()