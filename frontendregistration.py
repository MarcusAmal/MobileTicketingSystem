import tkinter as tk
import pyrebase

#Allows Non-authenticated access IF access rules of database are approriately adjusted    
config = {
    #"apiKey": "apikey",
    #"authDomain" : "projectid.firebaseapp.com",
    #"databaseURL": "project url",
    #"storageBucket" :  "projectid.appspot.com"
    }

firebase = pyrebase.initialize_app(config)

#if database rules are set to "auth !== null" for both read and write, authentication is implemented.
#create new user in authentication section of firebase console (allow users with email and password)
#, then fill in following sections with appropriate
#information for authentication implementation.

authentication = firebase.auth()
#newUser = authentication.sign_in_with_email_and_password("valid registered email","valid registered password")
newUser = authentication.refresh(newUser['refreshToken'])


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

tk.Label(rootWindow, text = "Student Status", width = 30).grid(row = 6)
uwStudentEntry = tk.Entry(rootWindow)
uwStudentEntry.grid(row = 6, column = 1)

def dataEntry():
    ticketNum = ticketNumEntry.get()
    dataSet = {
        "Name" : "" + nameEntry.get(),
        "Age" : "" + ageEntry.get(),
        "Email" : "" + emailEntry.get(),
        "Sid" : "" + sidEntry.get(),
        "ClassStanding" : "" + classEntry.get(),
        "Student Status" : "" + uwStudentEntry.get(),
        #"Checked In" : "No"
    }
    for key,value in dataSet.items():
        newData = {key:value}
        db.child(ticketNum).push(newData, newUser['idToken'])
        #if running without authentication, get rid of second parameter in push call

def clearEntries():
    nameEntry.delete(0,'end')
    ageEntry.delete(0,'end')
    emailEntry.delete(0,'end')
    ticketNumEntry.delete(0,'end')
    sidEntry.delete(0,'end')
    classEntry.delete(0,'end')
    uwStudentEntry.delete(0, 'end')

submitButton = tk.Button(rootWindow, text = "Submit", width = 20, command = dataEntry)
submitButton.grid(row = 6,column = 2)

clearButton = tk.Button(rootWindow, text = "Clear Data", width = 20, command = clearEntries)
clearButton.grid(row = 6, column = 3)

rootWindow.mainloop()



