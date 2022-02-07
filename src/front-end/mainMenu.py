from tkinter import *
import sys
sys.path.append('C:/Users/Marcin/Desktop/pavlackson/contact-book/src/')
from contactBookMain import usersList, columnNamesList

window = Tk()

header = Label(window, text = "Contact Book")
colNumber = 6

if __name__ == "__main__":
	header.grid(row = 0, columnspan = colNumber)
	# column names
	for colId, col in enumerate(columnNamesList):
		colName = Label(window, text = col[1])
		colName.grid(row = 1, column = colId)
	# values 
	for rowId, row in enumerate(usersList):
		for cellId, cell in enumerate(row):
			userRow = Label(window, text = cell)
			userRow.grid(row = rowId + 2, column = cellId)

	window.mainloop()