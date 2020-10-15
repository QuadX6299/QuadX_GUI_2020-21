from tkinter import *
import csv
from PIL import ImageTk, Image

# You'll need to install the module PIl also called Pillow
# Do "pip install Pillow" to install it

def main():
    root = Tk()
    root.title('QuadX GUI')
    highGoal = []
    midGoal = []
    lowGoal = []
    miss = []

    class Position:
        def __init__(self, name, x1, y2):
            self.name = name
            self.x = y2
            self.y = x1
            self.y1 = y2 + 1 + (10 * x1)
            # Goal
            if self.y1 < 10:
                self.image = "Goal/image_part_00%s.jpg" % self.y1
            elif 10 <= self.y1 < 100:
                self.image = "Goal/image_part_0%s.jpg" % self.y1
            elif 100 <= self.y1 < 151:
                self.image = "Goal/image_part_%s.jpg" % self.y1
            else:
                self.image = "Goal/image_part_026.jpg"

            self.photo = ImageTk.PhotoImage(Image.open(self.image))
            vars()["%s" % name] = Button(root, text="     ", image=self.photo, borderwidth=0, command=lambda: self.turnX())
            vars()["%s" % name].grid(row=x, column=y)

        def turnX(self):
            vars()["%s" % self.name] = Label(text="  X  ")
            vars()["%s" % self.name].grid(row=self.y, column=self.x)
            self.confi = Tk()
            self.confi.title('Confirm')
            confirm = Button(self.confi, text="Confirm", command=lambda: self.conf())
            confirm.pack(side=TOP)
            reset1 = Button(self.confi, text="Reset", command=lambda: self.reset())
            reset1.pack(side=TOP)
            finish = Button(self.confi, text="Confirm and Finish", fg="red", command=lambda: self.finish())
            finish.pack(side=BOTTOM)

        def conf(self):
            vars()["%s" % self.name] = Button(root, text="     ", image=self.photo, borderwidth=0, command=lambda: self.turnX())
            vars()["%s" % self.name].grid(row=self.y, column=self.x)
            self.confi.destroy()
            if 1 < self.x < 8 and self.y == 5:
                print("High Goal Makes: (%s, %s)" %(self.x, self.y))
                highGoal.append("(%s, %s)" % (self.x, self.y))
            elif 0 < self.x < 9 and 6 < self.y < 11:
                print("Mid Goal Makes : (%s, %s)" % (self.x, self.y))
                midGoal.append("(%s, %s)" % (self.x, self.y))
            elif 0 < self.x < 9 and 11 < self.y < 15:
                print("Low Goal Makes: (%s, %s)" % (self.x, self.y))
                lowGoal.append("(%s, %s)" % (self.x, self.y))
            else:
                print("Miss: (%s, %s)" % (self.x, self.y))
                miss.append("(%s, %s)" % (self.x, self.y))


        def reset(self):
            vars()["%s" % self.name] = Button(root, text="     ", image=self.photo, borderwidth=0, command=lambda: self.turnX())
            vars()["%s" % self.name].grid(row=self.y, column=self.x)
            self.confi.destroy()
            print(highGoal)
            print(midGoal)
            print(lowGoal)
            print(miss)

        def finish(self):
            self.conf()
            with open('Score.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['High Goal Makes:'] + highGoal)
                writer.writerow(['Mid Goal Makes:'] + midGoal)
                writer.writerow(['Low Goal Makes:'] + lowGoal)
                writer.writerow(['Miss:'] + miss)

            root.destroy()


    for x in range(17):
        for y in range(10):
            name2 = "butt_%s_%s" % (x, y)
            vars()["butt_%s_%s" % (x, y)] = Position(name2, x, y)

    root.mainloop()


if __name__ == '__main__':
    main()
