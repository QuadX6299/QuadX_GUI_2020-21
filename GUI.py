from tkinter import *
from PIL import ImageTk, Image


def main():
    root = Tk()
    root.title('QuadX GUI')

    class Position:
        def __init__(self, name, x1, y2):
            self.name = name
            self.x = x1
            self.y = y2
            self.y1 = y2 + 1 + (10 * self.x)
            # Goal
            if self.y1 < 10:
                self.image = "Goal/image_part_00%s.jpg" % self.y1
            elif 10 <= self.y1 < 100:
                self.image = "Goal/image_part_0%s.jpg" % self.y1
            elif 100 <= self.y1 < 150:
                self.image = "Goal/image_part_%s.jpg" % self.y1
            else:
                self.image = "Goal/image_part_150.jpg"

            self.photo = ImageTk.PhotoImage(Image.open(self.image))
            vars()["%s" % name] = Button(root, text="     ", image=self.photo, command=lambda: self.turnX())
            vars()["%s" % name].grid(row=x, column=y)

        def turnX(self):
            vars()["%s" % self.name] = Label(text="  X  ")
            vars()["%s" % self.name].grid(row=self.x, column=self.y)
            self.confi = Tk()
            self.confi.title('Confirm')
            confirm = Button(self.confi, text="Confirm", command=lambda: self.conf())
            confirm.pack(side=LEFT)
            reset1 = Button(self.confi, text="Reset", command=lambda: self.reset())
            reset1.pack(side=RIGHT)

        def conf(self):
            vars()["%s" % self.name] = Button(root, text="     ", image=self.photo, command=lambda: self.turnX())
            vars()["%s" % self.name].grid(row=self.x, column=self.y)
            self.confi.destroy()

        def reset(self):
            vars()["%s" % self.name] = Button(root, text="     ", image=self.photo, command=lambda: self.turnX())
            vars()["%s" % self.name].grid(row=self.x, column=self.y)
            self.confi.destroy()

    for x in range(15):
        for y in range(10):
            name2 = "butt_%s_%s" % (x, y)
            vars()["butt_%s_%s" % (x, y)] = Position(name2, x, y)

    root.mainloop()


if __name__ == '__main__':
    main()
