import tkinter as tk
import pyrebase

#Non-authenticated access    
config = {
    "apiKey": #enter firebase api key,
    "authDomain" : #firebase project id + ".firebaseapp.com",
    "databaseURL": #database url,
    "storageBucket" : #firebase project id + ".appspot.com",
    }

firebase = pyrebase.initialize_app(config)

db = firebase.database()

rootWindow = tk.Tk()
rootWindow.title = "Ticket Registration"

    
tk.Label(rootWindow, text = "Name", width = 30).grid(row = 0)
nameEntry = tk.Entry(rootWindow)
nameEntry.grid(row = 0, column = 1)

tk.Label(rootWindow, text = "Age", width = 30).grid(row = 1)
ageEntry = tk.Entry(rootWindow)
ageEntry.grid(row = 1, column = 1)

tk.Label(rootWindow, text = "Email", width = 30).grid(row = 2)
emailEntry = tk.Entry(rootWindow)
emailEntry.grid(row = 2, column = 1)

tk.Label(rootWindow, text = "Ticket #",width = 30).grid(row = 3)
ticketNumEntry = tk.Entry(rootWindow)
ticketNumEntry.grid(row = 3, column = 1)

tk.Label(rootWindow, text = "Student Id",width = 30).grid(row = 4)
sidEntry = tk.Entry(rootWindow)
sidEntry.grid(row = 4, column = 1)

tk.Label(rootWindow, text = "Class Standing",width = 30).grid(row = 5)
classEntry = tk.Entry(rootWindow)
classEntry.grid(row = 5, column = 1)

def dataEntry():
    name = "" + nameEntry.get()
    dataSet = {
        "Age" : "" + ageEntry.get(),
        "Email" : "" + emailEntry.get(),
        "TicketNum" : "" + ticketNumEntry.get(),
        "Sid" : "" + sidEntry.get(),
        "ClassStanding" : "" + classEntry.get(),
    }
    for key,value in dataSet.items():
        newData = {key:value}
        db.child(name).push(newData)

def clearEntries():
    nameEntry.delete(0,'end')
    ageEntry.delete(0,'end')
    emailEntry.delete(0,'end')
    ticketNumEntry.delete(0,'end')
    sidEntry.delete(0,'end')
    classEntry.delete(0,'end')

submitButton = tk.Button(rootWindow, text = "Submit", width = 20, command = dataEntry)
submitButton.grid(row = 5,column = 2)

clearButton = tk.Button(rootWindow, text = "Clear Data", width = 20, command = clearEntries)
clearButton.grid(row = 5, column = 3)

rootWindow.mainloop()



