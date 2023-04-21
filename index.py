from tkinter import*
import random
import tkinter.messagebox


root = Tk()
root.geometry("1350x760+0+0")
root.title("Number Puzzle Game")
root.configure(bg = 'Lightgray')


# def startNewGame():
#     game = Game(root)

# class Game:
#     WINNING_MATRIX = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,None]]
#     matrix = [[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]

#     def __init__(self, root):
#         self.root = root
#         self.generateRandomMatrix()
#         self.matrix_frame = tkinter.Frame(self.root)
#         self.winning_frame = tkinter.Frame(self.root)
#         self.displayFrame()
        
#     def generateRandomMatrix(self):
#         # matrix = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,None]
#         # random.shuffle(matrix)
#         # for row in range(4):
#         #     for col in range(4):
#         #         self.matrix[row][col] = matrix[(row*4)+col]
#         self.matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,None]]


#     def checkIfWon(self):
#         isWon = True
#         for row in range(4):
#             for col in range(4):
#                 if(self.matrix[row][col]!= self.WINNING_MATRIX[row][col]):
#                     isWon = False
#                     break
#         return isWon

#     def displayFrame(self):
#         if(self.checkIfWon()):
#             text = tkinter.Text(self.winning_frame)
#             text.insert('end',"won")
#             text.pack()
#             self.winning_frame.pack()
#             self.matrix_frame.destroy()
#             self.winning_frame.tkraise()
#         else:
#             for row in range(4):
#                 for col in range(4):
#                     tile = tkinter.Button(self.matrix_frame, text=self.matrix[row][col],
#                         borderwidth=10 ,command=lambda r=row,c=col:self.clickEvent(r,c))
#                     tile.grid(row=row,column=col)
#             self.matrix_frame.pack()
#             self.matrix_frame.tkraise()

#     def clickEvent(self,row, col):
#         if(row-1 >= 0 and row-1<=3 and self.matrix[row-1][col]==None):
#             self.matrix[row-1][col] = self.matrix[row][col]
#             self.matrix[row][col] = None
#         elif(row+1 >= 0 and row+1<=3 and self.matrix[row+1][col]==None):
#             self.matrix[row+1][col] = self.matrix[row][col]
#             self.matrix[row][col] = None
#         elif(col-1 >= 0 and col-1<=3 and self.matrix[row][col-1]==None):
#             self.matrix[row][col-1] = self.matrix[row][col]
#             self.matrix[row][col] = None
#         elif(col+1 >= 0 and col+1<=3 and self.matrix[row][col+1]==None):
#             self.matrix[row][col+1] = self.matrix[row][col]
#             self.matrix[row][col] = None         
#         self.displayFrame()
        
    
rootFrame = Frame(root, bg='Lightgray', pady =2, padx = 40, width=1350, height=100, relief= "solid" )
rootFrame.grid(row=0,column = 0)

lblTitle = Label(rootFrame,font=('arial',80,'bold'), text="Number Puzzle Game", bd = 10, bg="Cadet Blue", fg='dimgray',justify=CENTER,borderwidth=12,relief="solid",width=19)
lblTitle.grid(row=4,column = 0)

MainFrame = Frame(root, bg='Cadet Blue', bd =10, width=1350, height=600, relief= "solid" )
MainFrame.grid(row=1,column = 0,padx=30)

matrix_frame = LabelFrame(MainFrame,text="Number Puzzle",font=('arial',12,'bold'),fg='cornsilk',bg='cadet blue',bd=10,width=700,height=500, relief=RAISED)
matrix_frame.pack(side=LEFT)

ScoreButtonFrame = Frame(MainFrame ,bg='cadet blue',bd=10,padx=1,width=540,height=500, relief=RAISED)
ScoreButtonFrame.pack(side=RIGHT)

name_frame = LabelFrame(ScoreButtonFrame,text="Result",font=('arial',12,'bold'),fg='black',bd=10,width=540,height=110, relief=RAISED,padx=10,pady=2 )
name_frame.grid(row=0,column = 0)

ScoreFrame = LabelFrame(ScoreButtonFrame,text="Score",font=('arial',12,'bold'),fg='black',bd=10,width=540,height=130, relief=RAISED,padx=10,pady=2 )
ScoreFrame.grid(row=1,column = 0)


ActionFrame = Frame(ScoreButtonFrame,bd=10,width=540,height=230, relief=RAISED,padx=10,pady=2 )
ActionFrame.grid(row=2,column = 0)


NameVariable = StringVar()
NameVariable.set("")

clickCounter = 0
highscore = 0
winnermsg = StringVar()
displayClicks = StringVar()
displayClicks .set("Currunt Score" +"\n"+"0")

highScoreString = StringVar()
highScoreString.set("High Score" +"\n"+ str(highscore))

def winner():
    global winnermsg
    winnermsg .set("You Won")
def updatecounter():
    global clickCounter, displayClicks
    displayClicks .set("Current Score" +"\n"+str(clickCounter))
    
def highscoreUpdate():
    global highScoreString, highscore
    highScoreString.set("High Score" +"\n"+str(highscore))

class Buttons:
    def __init__(self, text, x, y):
        self.entervalue = text
        self.txtIntake = StringVar()
        self.txtIntake.set(text)
        self.x = x
        self.y = y
        self.btnNumber = Button(matrix_frame,textvariable = self.txtIntake, font=('arial', 80),bd = 5, borderwidth = 4 ,relief = "solid", command = lambda i = self.x, j=self.y : emptyspotChecker(i,j))
        self.btnNumber.place(x=self.x*168, y=self.y*152, width=170, height=160)
        
def shuffle():
    global btnCheckers, clickCounter
    nums = []
    for x in range(12):
        x += 1
        if x == 12:
            nums.append("")
        else:
            nums.append(str(x))
    
    for y in range(len(btnCheckers)):
        for x in range(len(btnCheckers[y])):
            num = random.choice(nums)
            btnCheckers[y][x].txtIntake.set(num)
            nums.remove(num)
    
    clickCounter = 0
    updatecounter()
    
    
def Exit():
    Exit = tkinter.messagebox.askyesno("Number Puzzle","Confirm If you want to exit")
    if Exit >0:
        root.destroy()
        return
    
lblPlayerName = Label(name_frame, textvariable=winnermsg, borderwidth=4, relief="solid",font=('arial',15)).place(x=0,y=3, width=500,height=70 )
  
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
shuffle()
def emptyspotChecker(y, x) :
    global btnCheckers, clickCounter
    if not btnCheckers [x] [y].txtIntake.get() == "":
        for i in range (-1,2):
            newX = x + i
            if not (newX < 0 or len (btnCheckers)-1 < newX or i == 0):
                if btnCheckers [newX] [y].txtIntake.get () =="": 
                    text = btnCheckers [x] [y].txtIntake.get ( )
                    btnCheckers[x][y].txtIntake.set(btnCheckers[newX][y].txtIntake.get())
                    btnCheckers [newX] [y].txtIntake.set(text)
                    checkwinner()
                    break
            
        for j in range (-1,2):
            newY = y + j
            if not (newY < 0 or len (btnCheckers [0]) -1 < newY or j == 0) :
                if btnCheckers[x][newY].txtIntake.get () == "": 
                    text = btnCheckers[x][y].txtIntake.get()
                    btnCheckers [x][y].txtIntake.set(btnCheckers[x][newY].txtIntake.get())
                    btnCheckers [x][newY].txtIntake.set(text)
                    checkwinner()
                    break
        clickCounter += 1 
        updatecounter()

def checkwinner():
    lost = False
    for y in range(len(btnCheckers)):
        for x in range(len(btnCheckers[y])):
            if btnCheckers[y][x].entervalue != btnCheckers[y][x].txtIntake.get():
                lost = True
                break
    if not lost:
        winner()
    
        
root.mainloop()