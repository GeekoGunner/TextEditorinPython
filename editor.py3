from tkinter import *
from tkinter.filedialog import asksaveasfilename

root = Tk("Text Editor")
txt=Text(root)

txt.grid()

def save():
    global txt
    t=txt.get("1.0", "end-1c")
    
    saveloc = asksaveasfilename()
    f1=open(saveloc,"w+")
    f1.write(t)
    f1.close()

button = Button(root,text="Save",command=save)
button.pack(packy=12)
button1 = Button(root,text="Erase")
button.grid()

root.title("Editor by Atharv")
root.mainloop()
