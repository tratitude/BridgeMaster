import sqlite3

mydb = sqlite3.connect("C:\\Users\\Jeff\\Documents\\GitHub\\BridgeMaster\\Web\\db.sqlite3")
cursor=mydb.cursor()

cursor.execute("SELECT PlayerID FROM seat")
Tables=cursor.fetchall()
print(Tables)
