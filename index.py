from tkinter import*
import random
import tkinter.messagebox

root = Tk()
root.geometry("1350x760+0+0")
root.title("Number Puzzle Game")
root.configure(bg = 'Lightgray')



rootFrame = Frame(root, bg='Lightgray', pady =2, padx = 40, width=1350, height=100, relief= "solid" )
rootFrame.grid(row=0,column = 0)

lblTitle = Label(rootFrame,font=('arial',80,'bold'), text="Number Puzzle Game", bd = 10, bg="Cadet Blue", fg='dimgray',justify=CENTER,borderwidth=12,relief="solid",width=19)
lblTitle.grid(row=4,column = 0)

MainFrame = Frame(root, bg='Cadet Blue', bd =10, width=1350, height=600, relief= "solid" )
MainFrame.grid(row=1,column = 0,padx=30)

ButtonFrame = LabelFrame(MainFrame,text="Number Puzzle",font=('arial',12,'bold'),fg='cornsilk',bg='cadet blue',bd=10,width=700,height=500, relief=RAISED)
ButtonFrame.pack(side=LEFT)

ScoreButtonFrame = Frame(MainFrame ,bg='cadet blue',bd=10,padx=1,width=540,height=500, relief=RAISED)
ScoreButtonFrame.pack(side=RIGHT)

NameFrame = LabelFrame(ScoreButtonFrame,text="Player Name",font=('arial',12,'bold'),fg='black',bd=10,width=540,height=110, relief=RAISED,padx=10,pady=2 )
NameFrame.grid(row=0,column = 0)

ScoreFrame = LabelFrame(ScoreButtonFrame,text="Score",font=('arial',12,'bold'),fg='black',bd=10,width=540,height=130, relief=RAISED,padx=10,pady=2 )
ScoreFrame.grid(row=1,column = 0)


ActionFrame = Frame(ScoreButtonFrame,bd=10,width=540,height=230, relief=RAISED,padx=10,pady=2 )
ActionFrame.grid(row=2,column = 0)


NameVariable = StringVar()
NameVariable.set("PLayer Name")

clickCounter = 0
displayClicks = StringVar()
displayClicks .set("Currunt Score" +"\n"+"0")

highScoreString = StringVar()
highScoreString .set("High Score" +"\n"+"20")
 
def updatecounter():
    global clickCounter, displayClicks
    displayClicks .set("Currunt Score" +"\n"+str(clickCounter))
    
def highscoreUpdate(highscore):
    global highScoreString
    highScoreString.set(highscore)

class Buttons:
    def __init__(self, text, x, y):
        self.entervalue = text
        self.txtIntake = StringVar()
        self.txtIntake.set(text)
        self.x = x
        self.y = y
        self.btnNumber = Button(ButtonFrame,textvariable = self.txtIntake, font=('arial', 80),bd = 5, borderwidth = 4 ,relief = "solid", command = lambda i = self.x, j=self.y : emptySpotChecker(i,j))
        self.btnNumber.place(x=self.x*168, y=self.y*152, width=170, height=160)
        
def shuffle():
    global btnCheckers, clickCounter
    num = []
    for x in range(12):
        x += 1
        if x == 12:
            num.append("")
        else:
            num.append(str(x))
    
    for y in range(len(btnCheckers)):
        for x in range(len(btnCheckers[y])):
            num = random.choice(num)
            btnCheckers[y][x].txtIntake.set(num)
            num.remove(num)
    
    clickCounter = 0
    updatecounter()
    highscoreUpdate("")
    
def Exit():
    Exit = tkinter.messagebox.askyesno("Number Puzzle","Confirm If you want to exit")
    if Exit >0:
        root.destroy()
        return
    
lblPlayerName = Label(NameFrame, textvariable=NameVariable, borderwidth=4, relief="solid",font=('arial',15)).place(x=0,y=3, width=500,height=70 )
  
lblCountClicks = Label(ScoreFrame, textvariable=displayClicks, borderwidth=4, relief="solid",font=('arial',20)).place(x=0, y=3, width=249,height=90) 

lblHighScore = Label(ScoreFrame, textvariable=highScoreString, borderwidth=4, relief="solid",font=('arial',20)).place(x=250, y=3, width=249,height=90) 

btnNewGame = tkinter.Button(ActionFrame, text="New Game", font=('arial',20,"bold"),bd=5, borderwidth = 4, relief ="solid", command = shuffle).place(x=0,y=3, width=249,height=100 )

btnSaveGame = tkinter.Button(ActionFrame, text="Save Game", font=('arial',20,"bold"),bd=5, borderwidth = 4, relief ="solid", command = "").place(x=250,y=3, width=250,height=100 )

btnSaveGame = tkinter.Button(ActionFrame, text="Logout", font=('arial',20,"bold"),bd=5, borderwidth = 4, relief ="solid", command = Exit).place(x=0,y=104, width=500,height=100 )


btnCheckers = []
name = 0

for y in range(3):
    btnChecker = []
    for x in range(4):
        name += 1
        if name == 12:
            name = ""
        btnChecker.append(Buttons(str(name), x,y))
    btnCheckers.append(btnChecker)

def emptyspotChecker (y, x) :
    global btnCheckers, clickCounter
    if not btnCheckers [x] [y].txtIntake.get () == "":
        for i in range (-1,2):
            newX = x + i
            if not (newX < 0 or len (btnCheckers)-1 < newX or i == 0):
                if btnCheckers [newX] [y].txtIntake.get () =="": 
                    text = btnCheckers [x] [y].txtIntake.get ( )
                    btnCheckers [x] [y].txtIntake.set (btnCheckers [newX] [y] .txtIntake.get () )
                    btnCheckers [newX] [y].txtIntake. set (text)
                    break
        for j in range (-1,2):
            newY = y + j
            if not (newY < 0 or len (btnCheckers [0]) -1 < newY or j == 0) :
                if btnCheckers [x] [newY].txtIntake.get () == "": 
                    text = btnCheckers [x] [y].txtIntake.get ()
                    btnCheckers [x] [y].txtIntake. set (btnCheckers [x] [newY]. txtIntake.get ( ) )
                    btnCheckers [x] [newY].txtIntake.set (text)
                    break
        clickCounter += 1 
        updatecounter()

    
        
root.mainloop()