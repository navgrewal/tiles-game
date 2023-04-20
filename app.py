import tkinter
from classes.game import Game


def startNewGame():
    game = Game(root)

root = tkinter.Tk(  )
startNewGame()
root.mainloop()