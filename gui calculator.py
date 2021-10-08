
from tkinter import *
 
# Creating frame for calculator
def iCalc(source, side):
    storeObj = Frame(source, borderwidth=14, bd=14, bg="black")
    storeObj.pack(side=side, expand =YES, fill =BOTH)
    return storeObj
 
# Creating Button
def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand = YES, fill=BOTH)
    return storeObj
 
class app(Frame):
    
                
# Start the GUI
if __name__=='__main__':
 app().mainloop()




