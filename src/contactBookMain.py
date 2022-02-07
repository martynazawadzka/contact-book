import sqlite3

conn = sqlite3.connect('users.db')

c = conn.cursor()

#def readSQLFile(filePath):
#	dbCreate = open(filePath, 'r')
#	sqlFile = dbCreate.read()
#	dbCreate.close()
#
#	sqlCommands = sqlFile.split(';')
#
#	for command in sqlCommands:
#	    try:
#	        c.execute(command)
#	    except(OperationalError, msg):
#	        print("Command skipped: ", msg)

def printSQL(task):
	c.execute(task)
	#print(c.fetchall())
	return(c.fetchall())

#readSQLFile('db/createUsersTable.sql')
#c.execute("DROP TABLE users")
#c.execute("CREATE TABLE users (UserId INTEGER PRIMARY KEY AUTOINCREMENT, FirstName text, LastName text, Adres text, PhoneNumber varchar(12), EmailAdress text);")
#c.execute("INSERT INTO Users (FirstName, LastName, Adres, PhoneNumber, EmailAdress) VALUES ('Adam', 'Pawlak', 'Moon', 123123123, 'kox123@essa.pl');")
#c.execute("DELETE FROM users WHERE FirstName = 'Adam';")
columnNamesList = printSQL("PRAGMA table_info(users);")
usersList = printSQL("SELECT * FROM users")

conn.commit()
conn.close()