from tkinter import *
from PIL import ImageTk, Image
import csv

# You'll need to install the module called Pillow
# do "pip install Pillow"
from numpy import double
root = Tk()
highGoal = []
midGoal = []
lowGoal = []
miss = []

def key(event):
    print("pressed", repr(event.char))


def callback(event):
    lbl = Label(canvas, image=ImageTk.PhotoImage(Image.open("dot.jpg"))).place(x=event.x, y=event.y)
    if 68 < event.x < 320 and 175 < event.y < 250:
        print("High Goal Makes: (%s, %s)" % (event.x, event.y))
        highGoal.append("(%s, %s)" % (event.x, event.y))
    elif 40 < event.x < 340 and 265 < event.y < 420:
        print("Mid Goal Makes : (%s, %s)" % (event.x, event.y))
        midGoal.append("(%s, %s)" % (event.x, event.y))
    elif 40 < event.x < 340 and 460 < event.y < 565:
        print("Low Goal Makes: (%s, %s)" % (event.x, event.y))
        lowGoal.append("(%s, %s)" % (event.x, event.y))
    else:
        print("Miss: (%s, %s)" % (event.x, event.y))
        miss.append("(%s, %s)" % (event.x, event.y))

    with open('Score.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['High Goal Makes:'] + highGoal)
        writer.writerow(['Mid Goal Makes:'] + midGoal)
        writer.writerow(['Low Goal Makes:'] + lowGoal)
        writer.writerow(['Miss:'] + miss)


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