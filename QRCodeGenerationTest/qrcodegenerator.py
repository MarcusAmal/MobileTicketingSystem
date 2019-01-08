import qrcode
import string
import random
import pyrebase

def random_generator(size = 25, chars=string.ascii_letters + string.digits): 
    return ''.join(random.choice(chars) for x in range(size))




config = {
  "apiKey": "AIzaSyCzzEgVtFxG-HvQ1PYVdlI65n6aoiz_0P8",
  "authDomain": "ticketmanagement-a1903.firebaseapp.com",
  "databaseURL": "https://ticketmanagement-a1903.firebaseio.com",
  "storageBucket": "ticketmanagement-a1903.appspot.com"
}

ticket_data = {
    "name" : None,
    "email" : None,
    "UW-Student" : None,
    "Paid" : False
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

db.child("Ticket-IDs").child(random_generator()).set(ticket_data);

tempdata = db.child("lsoslsosdf").get();
print(tempdata.val())

print(random_generator())

img = qrcode.make('Marcus Amalachandran');
img.save("test.png", "PNG")
print("done")