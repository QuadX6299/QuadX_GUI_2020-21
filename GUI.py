from tkinter import *
from PIL import ImageTk, Image

# You'll need to install the module PIl also called Pillow
# Do "pip install Pillow" to install it

def main():
    root = Tk()
    root.title('QuadX GUI')
    make1 = []
    make2 = []
    make3 = []
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
            vars()["%s" % name] = Button(root, text="     ", image=self.photo, command=lambda: self.turnX())
            vars()["%s" % name].grid(row=x, column=y)

        def turnX(self):
            vars()["%s" % self.name] = Label(text="  X  ")
            vars()["%s" % self.name].grid(row=self.y, column=self.x)
            self.confi = Tk()
            self.confi.title('Confirm')
            confirm = Button(self.confi, text="Confirm", command=lambda: self.conf())
            confirm.pack(side=LEFT)
            reset1 = Button(self.confi, text="Reset", command=lambda: self.reset())
            reset1.pack(side=RIGHT)

        def conf(self):
            vars()["%s" % self.name] = Button(root, text="     ", image=self.photo, command=lambda: self.turnX())
            vars()["%s" % self.name].grid(row=self.y, column=self.x)
            self.confi.destroy()
            if 1 < self.x < 8 and self.y == 5:
                print("Make: (%s, %s)" %(self.x, self.y))
                make1.append("(%s, %s)" % (self.x, self.y))
            elif 0 < self.x < 9 and 6 < self.y < 11:
                print("Make 2: (%s, %s)" % (self.x, self.y))
                make2.append("(%s, %s)" % (self.x, self.y))
            elif 0 < self.x < 9 and 11 < self.y < 15:
                print("Make 3: (%s, %s)" % (self.x, self.y))
                make3.append("(%s, %s)" % (self.x, self.y))
            else:
                print("Miss: (%s, %s)" % (self.x, self.y))
                miss.append("(%s, %s)" % (self.x, self.y))


        def reset(self):
            vars()["%s" % self.name] = Button(root, text="     ", image=self.photo, command=lambda: self.turnX())
            vars()["%s" % self.name].grid(row=self.y, column=self.x)
            self.confi.destroy()
            print(make1)
            print(make2)
            print(make3)
            print(miss)

    for x in range(17):
        for y in range(10):
            name2 = "butt_%s_%s" % (x, y)
            vars()["butt_%s_%s" % (x, y)] = Position(name2, x, y)

    root.mainloop()


if __name__ == '__main__':
    main()
