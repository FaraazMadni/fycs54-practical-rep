from tkinter import *
root=Tk()
def display():
    print("Username : "+ent1.get())

l1=Label(root,text='Enter Username')
ent1=Entry(root)
b=Button(root,text='Submit',command=display)
l1.grid(row=0,column=0)
ent1.grid(row=0,column=1)
b.grid(row=0,column=2)
root.mainloop()
