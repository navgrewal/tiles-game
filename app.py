import tkinter
root = tkinter.Tk(  )

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,None,15]]
winning_matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,None]]

matrix_frame = tkinter.Frame(root)
winning_frame = tkinter.Frame(root)

def clickEvent(row, col):
   for i in range(4):
       for j in range(4):
           if(matrix[i][j]==None):
                matrix[i][j] = matrix[row][col]
                matrix[row][col] = None
                print(matrix,row,col)
   displayGrid()

def checkIfWon():
    isWon = True
    for row in range(4):
        for col in range(4):
            if(matrix[row][col]!=winning_matrix[row][col]):
                isWon = False
                break
    return isWon

def displayGrid():
    if(checkIfWon()):
        print("won")
        text = tkinter.Text(root)
        text.insert('end',"won")
        text.grid(row=0,col=0)
        
    else:
        for row in range(4):
            for col in range(4):
                tile = tkinter.Button(matrix_frame, text=matrix[row][col],
                    borderwidth=10 ,command=lambda r=row,c=col:clickEvent(r,c))
                tile.grid(row=row,column=col)
        matrix_frame.pack()
        matrix_frame.tkraise()

displayGrid()
root.mainloop(  )