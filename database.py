import mysql.connector
from datetime import datetime
import loggeduser as loggeduser

db = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd = "navgrewal",
    database = "tiles"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS Users (name varchar(20) NOT NULL, username varchar(20) NOT NULL, password varchar(20) NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT, highscore int DEFAULT 0)")


def createUser(name, username, password):
    mycursor.execute("INSERT INTO Users (name, username,password) VALUES(%s,%s,%s)",(name, username, password))
    db.commit()

def login(username, password):
    user = None
    mycursor.execute("SELECT * FROM Users WHERE username = %s AND password = %s",(username,password))
    for user in mycursor:
        user = user
    if(user):
        loggeduser.loggedUser = {"name": user[0], "username": user[1], "highscore": user[4]}
        return True
    else:
        return False

def updateHighScore(username, highScore):
    mycursor.execute("UPDATE Users Set highscore = %s WHERE username = %s",(highScore, username))
    db.commit()
