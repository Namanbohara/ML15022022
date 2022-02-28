import tkinter as tkr

app=tkr.Tk(__name__)
app.title('CALCULATOR')
app.geometry('400x600')


######## FUNCTIONS######

def show():
    print('VALUE 1: ',en1.get())
    print('VALUE 2: ',en2.get())
    print('Operation performed: ',rb1.get())    
    cal()
def cal(): 
    c=str(en1.get())
    d=str(en2.get())
    exp=eval(c+rb1.get()+d)
    print('Calculation: ',exp)
    tkr.Label(app,text=exp,font=(80)).pack()


######## ENTRY BOXES######

en1=tkr.IntVar(app,'1')
en2=tkr.IntVar(app,'1')

tkr.Label(app,text='ENTER VALUE 1').pack()

tkr.Entry(app,textvariable=en1,font=(30),width=15).pack()

tkr.Label(app,text='ENTER VALUE 2').pack()

tkr.Entry(app,textvariable=en2,font=(30),width=15).pack()

######## RADIO BUTTON ######

rb1 =tkr.Variable(app,'+')
rb_values = {'+':'+','-':'-','%':'%','/':'/','*':'*'}
for k,v in rb_values.items():
    tkr.Radiobutton(app,text=k,variable=rb1,value=v).pack()
    
######## BUTTON #####

tkr.Button(app,text='CALCULATE',command=show).pack()


######## RESULT BUTTON #####

tkr.Label(app,text='**RESULT**',font=(100)).pack()
app.mainloop()
