import random as r
import tkinter as t
from tkinter import messagebox as m
import time


def _Exit(rt):
    pass

class Game:

    ingame=False
    _Width = 700
    _Height = 500
    _X = 0
    _Y = 5
    inGAME=True
    IsFOOD=False
    bd_cdtop = [0, 0, 700, 10]
    bd_cdbottom = [0, 490, 700, 500]
    bd_cdright = [690, 0, 700, 500]
    bd_cdleft = [0, 0, 10, 500]
    _body=[]
    coord=[]
    score=0

    def __init__(self, rt):
        self.rt = rt
        self.can = t.Canvas(rt, width=self._Width, height=self._Height, bg="yellow")
        self.bd1 = self.can.create_rectangle(self.bd_cdtop, fill="black")
        self.bd2 = self.can.create_rectangle(self.bd_cdbottom, fill="black")
        self.bd3 = self.can.create_rectangle(self.bd_cdright, fill="black")
        self.bd4 = self.can.create_rectangle(self.bd_cdleft, fill="black")


        self.snake()
        self.can.pack()
        pass



    def snake(self):
        shx = 340
        shy = 240
        self.head = self.can.create_rectangle(shx, shy, shx+10, shy+10, fill="white", tag="snake")

        self._body.append(self.head)
        self.movement()

    def movement(self):
        self.sr = t.Label(self.can, text="SCORE:" + str(self.score), font="rockwell 10", fg="black", bg="white")
        self.sr.place(relwidth=0.31, relx=0.7, relheight=0.02, )
        self.sr.update()
        if not self.IsFOOD:
            self.food()
            pass
        else:
            self.eaten()
        pass

        self.overlap()
        if self.inGAME:

            body = self.can.find_withtag("body")
            head= self.can.find_withtag(self.head)
            fbody=body+head
            z=0
            while z<len(fbody)-1:
                a=self.can.coords(fbody[z])
                b=self.can.coords(fbody[z+1])
                self.can.move(fbody[z],b[0]-a[0],(b[1]-a[1]))
                z+=1
                pass
            self.can.move(self.head, self._X, self._Y)

            self.can.after(100, self.movement)
            pass
        else:
            self.rt.unbind_all("<Key>")
            self.can.delete(self.snake)
            self.can.destroy()
            m.showinfo(title="game over", message="GAME OVER!!")
            time.sleep(1)
            from menu import Exit
            Exit(self.rt)


            pass

        pass

    def move(self, event):

        if event.keysym == "Up":
            self._Y = -5
            self._X = 0
            pass
        elif event.keysym == "Down":
            self._Y = 5
            self._X = 0
            pass
        elif event.keysym == "Right":
            self._Y = 0
            self._X = 5
            pass
        elif event.keysym == "Left":
            self._Y = 0
            self._X = -5
            pass

        pass

    def overlap(self):
        tag1 = self.can.find_withtag(self.bd1)
        tag2 = self.can.find_withtag(self.bd2)
        tag3 = self.can.find_withtag(self.bd3)
        tag4 = self.can.find_withtag(self.bd4)
        tag5 = self.can.find_withtag("body")
        a, b, c, d = self.can.bbox(self.head)
        overlap = self.can.find_overlapping(a, b, c, d)

        for ovr in overlap:
            if tag1[0] == ovr:
                self.inGAME=False
                self.IsFOOD = False
                pass
            elif tag2[0] == ovr:
                self.inGAME=False
                self.IsFOOD = False
                pass
            elif tag3[0] == ovr:
                self.inGAME=False
                self.IsFOOD = False
                pass
            elif tag4[0] == ovr:
                self.inGAME=False
                self.IsFOOD=False
                pass
            else:
                if len(tag5)>6:
                    l=0
                    while l<len(tag5)-5:
                        if tag5[l] == ovr:
                            self.inGAME = False
                            self.IsFOOD = False
                            pass
                        l+=1
                        pass
                    pass
                pass

            pass
        pass

    def food(self):
        t = time.time()
        x = r.Random(t)
        FOODX = x.randint(10,660)
        FOODY = x.randint(10,460)
        self.Food = self.can.create_rectangle(FOODX, FOODY, FOODX+10, FOODY+10, fill="RED",tag="food")

        if not self.IsFOOD:
            self.IsFOOD = True
        pass

    def eaten(self):
        food=self.can.find_withtag(self.Food)
        a, b, c, d = self.can.bbox(self.head)
        overlap = self.can.find_overlapping(a, b, c, d)
        for x in overlap:
            if food[0] == x:
                self.can.delete(self.Food)
                self.food()
                self.can.create_rectangle(self.can.coords(self.Food), fill="white", tag="body")

                self.score += 1
                pass
            pass
        pass

    pass

def main():
    rt = t.Tk()

    g = Game(rt)
    rt.bind("<Key>", g.move)
    rt.mainloop()
    pass

if __name__ == '__main__':
    main()