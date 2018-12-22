import tkinter as tk

rootWindow = tk.Tk()
rootWindow.title = "Ticket Registration"

tk.Label(rootWindow, text = "Name", width = 30).grid(row = 0)
nameEntry = tk.Entry(rootWindow).grid(row = 0, column = 1)

tk.Label(rootWindow, text = "Age", width = 30).grid(row = 1)
ageEntry = tk.Entry(rootWindow).grid(row = 1, column = 1)

tk.Label(rootWindow, text = "Email", width = 30).grid(row = 2)
emailEntry = tk.Entry(rootWindow).grid(row = 2, column = 1)

tk.Label(rootWindow, text = "Ticket #",width = 30).grid(row = 3)
ticketNumEntry = tk.Entry(rootWindow).grid(row = 3, column = 1)

tk.Label(rootWindow, text = "Student Id",width = 30).grid(row = 4)
sidEntry = tk.Entry(rootWindow).grid(row = 4, column = 1)

tk.Label(rootWindow, text = "Class Standing",width = 30).grid(row = 5)
classEntry = tk.Entry(rootWindow).grid(row = 5, column = 1)

submitButton = tk.Button(rootWindow, text = "Submit", width = 20, command = rootWindow.destroy)
submitButton.grid(column = 2)
rootWindow.mainloop()
