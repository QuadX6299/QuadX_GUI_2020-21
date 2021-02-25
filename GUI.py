import gspread 
from oauth2client.service_account import ServiceAccountCredentials
from tkinter import *
from PIL import ImageTk, Image
import csv
from numpy import double

# You'll need to install the module called Pillow and numpy
# do "pip install Pillow"
# then "pip install numpy"

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("QuadX GUI").sheet1

root = Tk()
highGoal = ["High Goal Makes:"]
midGoal = ['Mid Goal Makes:']
lowGoal = ['Low Goal Makes:']
miss = ['Miss:']

def key(event):
    print("pressed", repr(event.char))


def callback(event):
    if 68 < event.x < 320 and 175 < event.y < 250:
        print("High Goal Makes: (%s, %s)" % (event.x, event.y))
        highGoal.append("(%s, %s)" % (event.x, event.y))
        make = Label(canvas, text="", fg="green", bg="green", image=ImageTk.PhotoImage(Image.open("dot.jpg"))).place(
            x=event.x, y=event.y)
    elif 40 < event.x < 340 and 265 < event.y < 420:
        print("Mid Goal Makes : (%s, %s)" % (event.x, event.y))
        midGoal.append("(%s, %s)" % (event.x, event.y))
        make = Label(canvas, text="", fg="green", bg="green", image=ImageTk.PhotoImage(Image.open("dot.jpg"))).place(
            x=event.x, y=event.y)
    elif 40 < event.x < 340 and 460 < event.y < 565:
        print("Low Goal Makes: (%s, %s)" % (event.x, event.y))
        lowGoal.append("(%s, %s)" % (event.x, event.y))
        make = Label(canvas, text="", fg="green", bg="green", image=ImageTk.PhotoImage(Image.open("dot.jpg"))).place(
            x=event.x, y=event.y)
    else:
        print("Miss: (%s, %s)" % (event.x, event.y))
        miss.append("(%s, %s)" % (event.x, event.y))
        redmiss = Label(canvas, text="", fg="red", bg="red", image=ImageTk.PhotoImage(Image.open("dot.jpg"))).place(
            x=event.x, y=event.y)

    with open('Score.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(highGoal)
        writer.writerow(midGoal)
        writer.writerow(lowGoal)
        writer.writerow(miss)
        sheet.insert_row(highGoal, 1)
        sheet.insert_row(midGoal, 2)
        sheet.insert_row(lowGoal, 3)
        sheet.insert_row(miss, 4)


photo = "Goal.png"
goal = ImageTk.PhotoImage(Image.open(photo))
root.title('QuadX GUI')

canvas = Canvas(root, width=392, height=787)
canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
canvas.pack()
canvas.create_image(0, 0, image=goal, anchor=NW)

root.mainloop()
totalMakes = len(highGoal) + len(midGoal) + len(lowGoal)
totalShots = len(miss) + totalMakes
shootingAccuracy = (double) (totalMakes/(totalShots))

print("Shooting Accuracy: " + "{:.2%}".format(shootingAccuracy))
