from tkinter import *
root=Tk()
def var_states():
    print("swimming%d, \n reading%d"%(var1.get(),var2.get()))

var1=IntVar()
c1=Checkbutton(root, text="swimming",variable=var1)

var2=IntVar()
c2=Checkbutton(root, text="reading",variable=var2)
b=Button(root, text="show", command=var_states)

c1.pack(side=LEFT)
c2.pack(side=LEFT)
b.pack(side=LEFT)
