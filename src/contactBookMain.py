from tkinter import *
import sqlite3

conn = sqlite3.connect('users.db')

window = Tk()
c = conn.cursor()
#c.execute("""CREATE TABLE users (
#      UserId int PRIMARY KEY,
#      FirstName text,
#      LastName text,
#      Adres text,
#      PhoneNumber varchar(12),
#      EmailAdress text
#   )""")

#c.execute("INSERT INTO Users (FirstName, LastName, Adres, PhoneNumber, EmailAdress) VALUES ('Adam', 'Pawlak', 'Moon', 123123123, 'kox123@essa.pl')");

c.execute("SELECT * FROM users")
firstUser = c.fetchone()
label = Label(window, text = firstUser)
label.pack()
#print(c.fetchone())

window.mainloop()
#conn.execute("SELECT * from Users;")
conn.commit()
conn.close()