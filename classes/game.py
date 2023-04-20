import tkinter
import random

class Game:
    WINNING_MATRIX = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,None]]
    matrix = [[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]

    def __init__(self, root):
        self.root = root
        self.generateRandomMatrix()
        self.matrix_frame = tkinter.Frame(self.root)
        self.winning_frame = tkinter.Frame(self.root)
        self.displayFrame()
        
    def generateRandomMatrix(self):
        matrix = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,None]
        random.shuffle(matrix)
        for row in range(4):
            for col in range(4):
                self.matrix[row][col] = matrix[(row*4)+col]


    def checkIfWon(self):
        isWon = True
        for row in range(4):
            for col in range(4):
                if(self.matrix[row][col]!= self.WINNING_MATRIX[row][col]):
                    isWon = False
                    break
        return isWon

    def displayFrame(self):
        if(self.checkIfWon()):
            text = tkinter.Text(self.winning_frame)
            text.insert('end',"won")
            text.pack()
            self.winning_frame.pack()
            self.matrix_frame.destroy()
            self.winning_frame.tkraise()
        else:
            for row in range(4):
                for col in range(4):
                    tile = tkinter.Button(self.matrix_frame, text=self.matrix[row][col],
                        borderwidth=10 ,command=lambda r=row,c=col:self.clickEvent(r,c))
                    tile.grid(row=row,column=col)
            self.matrix_frame.pack()
            self.matrix_frame.tkraise()

    def clickEvent(self,row, col):
        if(row-1 >= 0 and row-1<=3 and self.matrix[row-1][col]==None):
            self.matrix[row-1][col] = self.matrix[row][col]
            self.matrix[row][col] = None
        elif(row+1 >= 0 and row+1<=3 and self.matrix[row+1][col]==None):
            self.matrix[row+1][col] = self.matrix[row][col]
            self.matrix[row][col] = None
        elif(col-1 >= 0 and col-1<=3 and self.matrix[row][col-1]==None):
            self.matrix[row][col-1] = self.matrix[row][col]
            self.matrix[row][col] = None
        elif(col+1 >= 0 and col+1<=3 and self.matrix[row][col+1]==None):
            self.matrix[row][col+1] = self.matrix[row][col]
            self.matrix[row][col] = None         
        self.displayFrame()

