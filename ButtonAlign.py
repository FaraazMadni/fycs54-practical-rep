from tkinter import *
root=Tk()

def callback():
    print("Click!")

button1=Button(root,text="ONE",command=callback,bg="Red",fg="Green")
button2=Button(root,text="TWO",command=callback,bg="Red",fg="Green")

w=root.winfo_screenwidth()
h=root.winfo_screenheight()
print("Screen width", w)
print("Screen height", h)
root.geometry(str(w)+"x"+str(h))

button1.place(x=200,y=200)
button2.place(x=00,y=500)
root.mainloop()
