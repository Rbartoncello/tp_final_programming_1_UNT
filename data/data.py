import sqlite3 as sql


def createDB():
    with sql.connect("./data/ranking.db") as conexition:
        conexition.commit()


def createTable():
    with sql.connect("./data/ranking.db") as conexition:
        try:
            conexition.execute(
                """CREATE TABLE score(
                    id integer primary key autoincrement,
                    name text,
                    score integer
                )"""
            )
        except sql.OperationalError:
            print("La tabla score ya existe")


def insertRow(name, score):
    with sql.connect("./data/ranking.db") as conexition:
        try:
            conexition.execute(
                "insert into score(name,score) values (?,?)", (name, score))
            conexition.commit()
        except:
            print("Error insert row")


def updateRow(name, score):
    with sql.connect("./data/ranking.db") as conexition:
        try:
            conexition.execute(
                "UPDATE score SET score=? WHERE name=? AND score < ?", (score, name, score))
            conexition.commit()
        except:
            print("Error update row")


def checkData(name):
    with sql.connect("./data/ranking.db") as conexition:
            cursor = conexition.cursor()
            instruccion = "SELECT * FROM score WHERE name = '{}'".format(name)
            cursor.execute(instruccion)
            datos = cursor.fetchall()
            conexition.commit()
            return datos
        


def readRows():
    with sql.connect("./data/ranking.db") as conexition:
        try:
            cursor = conexition.cursor()
            instruccion = f"SELECT * FROM score ORDER BY score DESC"
            cursor.execute(instruccion)
            datos = cursor.fetchall()
            conexition.commit()
            return datos
        except:
            print("Error")


def updateInfo(name, score):
    if (checkData(name)):
        updateRow(name, score)
    else:
        insertRow(name, score)

createTable()
