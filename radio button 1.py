from tkinter import *
root=Tk()

v=StringVar()
v.set(0)
lang_list=[("Python",0),("Java",1),("C",2),("DOTNET",3),("PHP",4)]

def ShowChoice():
    print("Your selected choice is:",v.get())

l=Label(root,text="Select your Favourite Programming Language")
l.pack()

for txt,val in lang_list:
    r=Radiobutton(root,text=txt,variable=v,command=ShowChoice,value=val)
    r.pack()
root.mainloop()

