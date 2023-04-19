import tkinter
root = tkinter.Tk(  )

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,None,15]]
winning_matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,None]]

matrix_frame = tkinter.Frame(root)
winning_frame = tkinter.Frame(root)

def clickEvent(row, col):
    if(row-1 >= 0 and row-1<=3 and matrix[row-1][col]==None):
        matrix[row-1][col] = matrix[row][col]
        matrix[row][col] = None
    elif(row+1 >= 0 and row+1<=3 and matrix[row+1][col]==None):
        matrix[row+1][col] = matrix[row][col]
        matrix[row][col] = None
    elif(col-1 >= 0 and col-1<=3 and matrix[row][col-1]==None):
        matrix[row][col-1] = matrix[row][col]
        matrix[row][col] = None
    elif(col+1 >= 0 and col+1<=3 and matrix[row][col+1]==None):
        matrix[row][col+1] = matrix[row][col]
        matrix[row][col] = None         
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
        text = tkinter.Text(winning_frame)
        text.insert('end',"won")
        text.pack()
        winning_frame.pack()
        matrix_frame.destroy()
        winning_frame.tkraise()
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