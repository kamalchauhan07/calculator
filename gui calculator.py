
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
    def _init_(self):
        Frame._init_(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand = YES, fill =BOTH)
        self.master.title(' kamal_Calculator')

        display = StringVar()
        Entry( self , relief=RIDGE, textvariable=display,justify='right', bd=30, bg="powder blue").pack(side=TOP,expand=YES, fill=BOTH)
        for clearButton in (["C"]):
                erase = iCalc(self, TOP)
                for ichar in clearButton:
                    button(erase, LEFT, ichar, lambda storeObj=display, q=ichar: storeObj.set(''))

        for numButton in ("789/", "456*", "123-", "0.+"):
            FunctionNum = iCalc(self, TOP)
            for iEquals in numButton:
                button(FunctionNum, LEFT, iEquals, lambda storeObj=display, q=iEquals: storeObj.set(storeObj.get() + q))
             EqualButton = iCalc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e,s=self,storeObj=display: s.calc(storeObj), '+')
                                                            
 
            else:
                btniEquals = button(EqualButton, LEFT, iEquals,lambda storeObj=display, s=' %s ' % iEquals: storeObj.set(storeObj.get() + s))
    def calc(self, display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("ERROR")

                
# Start the GUI
if __name__=='__main__':
 app().mainloop()
# Aditya code 

    form.appendChild(cell)
    let tbl = document.getElementById("display"); 
    tbl.innerHTML = "";
    if(localStorage.getItem(clicked_id+"1")!=null)
    {
        lis=JSON.parse(localStorage.getItem(clicked_id+"1"));
        console.log(lis);
        lis.forEach(myFunction);

        function myFunction(value) {
            let row = document.createElement("tr");
            row.setAttribute("id","display_row");
            let cell = document.createElement("td");
            let cellText = document.createTextNode(value);
            cell.appendChild(cellText);
            row.appendChild(cell);
            tbl.appendChild(row); 



