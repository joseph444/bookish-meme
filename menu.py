from tkinter import *
import snake as s


rt = None


def Exit(rt):

    menu(rt)



def Ser(rt,can):
    can.destroy()
    sn =s.Game(rt)
    rt.bind("<Key>",sn.move)
    pass


def menu(rt):
    can=Canvas(rt,bg="yellow")
    l1=Label(can,text="Start",font="rockwell 20",anchor="center")
    l1.pack()
    l1.bind("<Button-1>",lambda e: Ser(rt,can))
    l2 = Label(can,text="Exit", font="rockwell 20", anchor="center" )
    l2.pack()
    l2.bind("<Button-1>",lambda e:exit(0))
    can.pack(fill="both", expand="true")

    pass


def main():
    rt=Tk()
    rt.resizable(True,True)
    rt.title("SNAKE GAME")
    menu(rt)
    mainloop()
    pass


if __name__ == '__main__':
    main()
