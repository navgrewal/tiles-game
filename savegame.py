import mysql.connector
import loggeduser as loggeduser

savedGame = None

savedb = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd = "navgrewal",
    database = "tiles"
)

savecursor = savedb.cursor(buffered=True)

savecursor.execute("CREATE TABLE IF NOT EXISTS SavedGames (i00 varchar(5),i01 varchar(5),i02 varchar(5),i03 varchar(5),i10 varchar(5),i11 varchar(5),i12 varchar(5),i13 varchar(5),i20 varchar(5),i21 varchar(5),i22 varchar(5),i23 varchar(5))")

def saveGame(num):
    savecursor.execute("INSERT INTO SavedGames VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(num[0][0].txtIntake.get(),num[0][1].txtIntake.get(),num[0][2].txtIntake.get(),num[0][3].txtIntake.get(),num[1][0].txtIntake.get(),num[1][1].txtIntake.get(),num[1][2].txtIntake.get(),num[1][3].txtIntake.get(),num[2][0].txtIntake.get(),num[2][1].txtIntake.get(),num[2][2].txtIntake.get(),num[2][3].txtIntake.get()))
    savedb.commit()

def getSavedGame():
    global savedGame
    savecursor.execute("SELECT * FROM SavedGames")
    for game in savecursor:
        if(game):
            savedGame = [[game[0],game[1],game[2],game[3]],[game[4],game[5],game[6],game[7]],[game[8],game[9],game[10],game[11]]]
            savecursor.execute("TRUNCATE TABLE SavedGames;")
            return True
    else:
        return False