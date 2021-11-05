from tkinter import *
from DMExp import*
import pygame
import time
import random
class DMPage(Frame):
    MUTE = False
    INFO = False
    DIM = 0
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        pygame.mixer.init()
        DBMWall = PhotoImage(file="DoubleMatrix.png")
        DBLabel = Label(self, image=DBMWall)
        DBLabel.image = DBMWall
        DBLabel.place(x=-2, y=-2)
        Info = PhotoImage(file="FrozenPop.png")
        InfoPop = Label(self, image=Info)
        InfoPop.image = Info
        InfoPop.place(x=-2, y=-2)
        InfoPop.lower()
        Back = PhotoImage(file="FrozenBack.png")
        BackBtn = Button(self, image=Back, bd=0, bg='#2357b5', command=lambda: BackAct())
        BackBtn.image = Back
        BackBtn.place(x=-2, y=-2)
        Info = PhotoImage(file="FrozenInfo.png")
        InfoBtn = Button(self, image=Info, bd=0, bg='#2357b5', command=lambda: InfoAct())
        InfoBtn.image = Info
        InfoBtn.place(x=48, y=-2)
        Music = PhotoImage(file="FrozenMusic.png")
        MusicBtn = Button(self, image=Music, bd=0, bg='#2357b5', command=lambda: MuteAct())
        MusicBtn.image = Music
        MusicBtn.place(x=98, y=-2)
        MusicOff = PhotoImage(file="FrozenMusicOff.png")
        MuteOff = Button(self, image=MusicOff, bd=0, bg='#2357b5', command=lambda: MuteAct())
        MuteOff.image = MusicOff
        MuteOff.place(x=98, y=-2)
        MuteOff.lower()
        Random = PhotoImage(file="FrozenRandom.png")
        RandBtn = Button(self, image=Random, bd=0, bg="#2357b5", command=lambda: RandAct())
        RandBtn.image = Random
        RandBtn.place(x=148, y=-2)
        Reset = PhotoImage(file="FrozenClear.png")
        ResetBtn = Button(self, image=Reset, bd=0, bg="#2357b5", command=lambda: ResetAct())
        ResetBtn.image = Reset
        ResetBtn.place(x=198, y=-2)
        Multiply = PhotoImage(file="MultiplyButton.png")
        MultiplyBtn = Button(self, image=Multiply, bd=0, bg="#ff82fe", command=lambda: MultAct())
        MultiplyBtn.image = Multiply
        MultiplyBtn.place(x=572, y=149)
        Plus = PhotoImage(file="PlusButton.png")
        PlusBtn = Button(self, image=Plus, bd=0, bg="#ff82fe", command=lambda: PlusAct())
        PlusBtn.image = Plus
        PlusBtn.place(x=572, y=240)
        Minus = PhotoImage(file="MinusButton.png")
        MinusBtn = Button(self, image=Minus, bd=0, bg="#ff82fe", command=lambda: MinuAct())
        MinusBtn.image = Minus
        MinusBtn.place(x=572, y=331)
        Reverse = PhotoImage(file="ReverseButton.png")
        ReverseBtn = Button(self, image=Reverse, bd=0, bg="#8cb5ea", command=lambda: RevrAct())
        ReverseBtn.image = Reverse
        ReverseBtn.place(x=646, y=59)
        def validate(string):
            regex = re.compile(r"(\+|\-)?[0-9.]*$")
            result = regex.match(string)
            return (string == ""
                    or (string.count('+') <= 1
                        and string.count('-') <= 1
                        and string.count('.') <= 1
                        and result is not None
                        and result.group(0) != ""))
        def on_validate(P):
            return validate(P)
        AEnt = Entry(self, background="#8cb5ea", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        AEnt.config(validatecommand=(AEnt.register(on_validate), '%P'))
        AEnt.place(x=573, y=73, width=50, height=50)
        BEnt = Entry(self, background="#8cb5ea", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        BEnt.config(validatecommand=(AEnt.register(on_validate), '%P'))
        BEnt.place(x=741, y=73, width=50, height=50)
        MA1aEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MA1aEnt.config(validatecommand=(MA1aEnt.register(on_validate), '%P'))
        MA1aEnt.place(x=193, y=116, width=50, height=50)
        MA1bEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MA1bEnt.config(validatecommand=(MA1bEnt.register(on_validate), '%P'))
        MA1bEnt.place(x=273, y=116, width=50, height=50)
        MA1cEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MA1cEnt.config(validatecommand=(MA1cEnt.register(on_validate), '%P'))
        MA1cEnt.place(x=353, y=116, width=50, height=50)
        MA1dEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MA1dEnt.config(validatecommand=(MA1dEnt.register(on_validate), '%P'))
        MA1dEnt.place(x=433, y=116, width=50, height=50)
        MA2aEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MA2aEnt.config(validatecommand=(MA2aEnt.register(on_validate), '%P'))
        MA2aEnt.place(x=193, y=201, width=50, height=50)
        MA2bEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MA2bEnt.config(validatecommand=(MA2aEnt.register(on_validate), '%P'))
        MA2bEnt.place(x=273, y=201, width=50, height=50)
        MA2cEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MA2cEnt.config(validatecommand=(MA2cEnt.register(on_validate), '%P'))
        MA2cEnt.place(x=353, y=201, width=50, height=50)
        MA2dEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MA2dEnt.config(validatecommand=(MA2dEnt.register(on_validate), '%P'))
        MA2dEnt.place(x=433, y=201, width=50, height=50)
        MA3aEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MA3aEnt.config(validatecommand=(MA3aEnt.register(on_validate), '%P'))
        MA3aEnt.place(x=193, y=286, width=50, height=50)
        MA3bEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MA3bEnt.config(validatecommand=(MA3aEnt.register(on_validate), '%P'))
        MA3bEnt.place(x=273, y=286, width=50, height=50)
        MA3cEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MA3cEnt.config(validatecommand=(MA3cEnt.register(on_validate), '%P'))
        MA3cEnt.place(x=353, y=286, width=50, height=50)
        MA3dEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MA3dEnt.config(validatecommand=(MA3dEnt.register(on_validate), '%P'))
        MA3dEnt.place(x=433, y=286, width=50, height=50)
        MA4aEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MA4aEnt.config(validatecommand=(MA4aEnt.register(on_validate), '%P'))
        MA4aEnt.place(x=193, y=371, width=50, height=50)
        MA4bEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MA4bEnt.config(validatecommand=(MA4aEnt.register(on_validate), '%P'))
        MA4bEnt.place(x=273, y=371, width=50, height=50)
        MA4cEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MA4cEnt.config(validatecommand=(MA4cEnt.register(on_validate), '%P'))
        MA4cEnt.place(x=353, y=371, width=50, height=50)
        MA4dEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MA4dEnt.config(validatecommand=(MA4dEnt.register(on_validate), '%P'))
        MA4dEnt.place(x=433, y=371, width=50, height=50)
        MB1aEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MB1aEnt.config(validatecommand=(MB1aEnt.register(on_validate), '%P'))
        MB1aEnt.place(x=884, y=116, width=50, height=50)
        MB1bEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MB1bEnt.config(validatecommand=(MB1bEnt.register(on_validate), '%P'))
        MB1bEnt.place(x=964, y=116, width=50, height=50)
        MB1cEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MB1cEnt.config(validatecommand=(MB1cEnt.register(on_validate), '%P'))
        MB1cEnt.place(x=1044, y=116, width=50, height=50)
        MB1dEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MB1dEnt.config(validatecommand=(MB1dEnt.register(on_validate), '%P'))
        MB1dEnt.place(x=1124, y=116, width=50, height=50)
        MB2aEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MB2aEnt.config(validatecommand=(MB2aEnt.register(on_validate), '%P'))
        MB2aEnt.place(x=884, y=201, width=50, height=50)
        MB2bEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MB2bEnt.config(validatecommand=(MB2aEnt.register(on_validate), '%P'))
        MB2bEnt.place(x=964, y=201, width=50, height=50)
        MB2cEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MB2cEnt.config(validatecommand=(MB2cEnt.register(on_validate), '%P'))
        MB2cEnt.place(x=1044, y=201, width=50, height=50)
        MB2dEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MB2dEnt.config(validatecommand=(MB2dEnt.register(on_validate), '%P'))
        MB2dEnt.place(x=1124, y=201, width=50, height=50)
        MB3aEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MB3aEnt.config(validatecommand=(MB3aEnt.register(on_validate), '%P'))
        MB3aEnt.place(x=884, y=286, width=50, height=50)
        MB3bEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MB3bEnt.config(validatecommand=(MB3aEnt.register(on_validate), '%P'))
        MB3bEnt.place(x=964, y=286, width=50, height=50)
        MB3cEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MB3cEnt.config(validatecommand=(MB3cEnt.register(on_validate), '%P'))
        MB3cEnt.place(x=1044, y=286, width=50, height=50)
        MB3dEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MB3dEnt.config(validatecommand=(MB3dEnt.register(on_validate), '%P'))
        MB3dEnt.place(x=1124, y=286, width=50, height=50)
        MB4aEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MB4aEnt.config(validatecommand=(MB4aEnt.register(on_validate), '%P'))
        MB4aEnt.place(x=884, y=371, width=50, height=50)
        MB4bEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MB4bEnt.config(validatecommand=(MB4aEnt.register(on_validate), '%P'))
        MB4bEnt.place(x=964, y=371, width=50, height=50)
        MB4cEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MB4cEnt.config(validatecommand=(MB4cEnt.register(on_validate), '%P'))
        MB4cEnt.place(x=1044, y=371, width=50, height=50)
        MB4dEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MB4dEnt.config(validatecommand=(MB4dEnt.register(on_validate), '%P'))
        MB4dEnt.place(x=1124, y=371, width=50, height=50)
        Ans1 = Label(self, bg='#79bcc5', anchor='c', justify="center")
        Ans1.place(x=233, y=552, width=154, height=175)
        Ans2 = Label(self, bg='#79bcc5', anchor='c', justify="center")
        Ans2.place(x=438, y=552, width=154, height=175)
        Ans3 = Label(self, bg='#79bcc5', anchor='c', justify="center")
        Ans3.place(x=643, y=552, width=343, height=177)
        Ans4 = Label(self, bg='#79bcc5', anchor='c', justify="center")
        Ans4.place(x=1036, y=552, width=194, height=175)
        AddBox = PhotoImage(file="PlusResult.png")
        PlusR = Label(self, image=AddBox)
        PlusR.image = AddBox
        PlusR.place(x=-2, y=490)
        MinusBox = PhotoImage(file="MinusResult.png")
        MinusR = Label(self, image=MinusBox)
        MinusR.image = MinusBox
        MinusR.place(x=-2, y=490)
        MultiBox = PhotoImage(file="MultiplyResult.png")
        MultiR = Label(self, image=MultiBox)
        MultiR.image = MultiBox
        MultiR.place(x=-2, y=490)
        def ResultLower():
            r = (Ans1, Ans2, Ans3, Ans4, PlusR, MinusR, MultiR)
            for i in range(7):
                r[i].lower()
        ResultLower()
        def RevrAct():
            MatA = (MA1aEnt.get(), MA1bEnt.get(), MA1cEnt.get(), MA1dEnt.get(),MA2aEnt.get(), MA2bEnt.get(), MA2cEnt.get(), MA2dEnt.get(),MA3aEnt.get(), MA3bEnt.get(), MA3cEnt.get(), MA3dEnt.get(),MA4aEnt.get(), MA4bEnt.get(), MA4cEnt.get(), MA4dEnt.get())
            MatB = (MB1aEnt.get(), MB1bEnt.get(), MB1cEnt.get(), MB1dEnt.get(),MB2aEnt.get(), MB2bEnt.get(), MB2cEnt.get(), MB2dEnt.get(),MB3aEnt.get(), MB3bEnt.get(), MB3cEnt.get(), MB3dEnt.get(),MB4aEnt.get(), MB4bEnt.get(), MB4cEnt.get(), MB4dEnt.get())
            EntA = (MA1aEnt, MA1bEnt, MA1cEnt, MA1dEnt, MA2aEnt, MA2bEnt, MA2cEnt, MA2dEnt,MA3aEnt, MA3bEnt, MA3cEnt, MA3dEnt,MA4aEnt, MA4bEnt, MA4cEnt, MA4dEnt)
            EntB = (MB1aEnt, MB1bEnt, MB1cEnt, MB1dEnt, MB2aEnt, MB2bEnt, MB2cEnt, MB2dEnt,MB3aEnt, MB3bEnt, MB3cEnt, MB3dEnt,MB4aEnt, MB4bEnt, MB4cEnt, MB4dEnt)
            value = (AEnt.get(), BEnt.get())
            for i in range (16):
                EntA[i].delete(0, END)
                EntB[i].delete(0, END)
                EntA[i].insert(1, MatB[i])
                EntB[i].insert(1, MatA[i])
            AEnt.delete(0, END)
            BEnt.delete(0, END)
            AEnt.insert(1, value[1])
            BEnt.insert(1, value[0])
        def FTest(x):
            return x.lstrip('-').lstrip('+').replace('.', '', 1).isdigit()
        def Avalue():
            if FTest(AEnt.get()):
                value = float(AEnt.get())
            else:
                value = 1
            return value
        def Bvalue():
            if FTest(BEnt.get()):
                value = float(BEnt.get())
            else:
                value = 1
            return value
        def TM():
            if FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA1cEnt.get()) and FTest(MA1dEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA2bEnt.get()) and FTest(MA2cEnt.get()) and FTest(MA2dEnt.get()) and FTest(MA3aEnt.get()) and FTest(MA3bEnt.get()) and FTest(MA3cEnt.get()) and FTest(MA3dEnt.get()) and FTest(MA4aEnt.get()) and FTest(MA4bEnt.get()) and FTest(MA4cEnt.get()) and FTest(MA4dEnt.get()) and \
                FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB1cEnt.get()) and FTest(MB1dEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB2bEnt.get()) and FTest(MB2cEnt.get()) and FTest(MB2dEnt.get()) and FTest(MB3aEnt.get()) and FTest(MB3bEnt.get()) and FTest(MB3cEnt.get()) and FTest(MB3dEnt.get()) and FTest(MB4aEnt.get()) and FTest(MB4bEnt.get()) and FTest(MB4cEnt.get()) and FTest(MB4dEnt.get()):
                DMPage.DIM = 44
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA1cEnt.get()), float(MA1dEnt.get()), float(MA2aEnt.get()), float(MA2bEnt.get()), float(MA2cEnt.get()), float(MA2dEnt.get()), float(MA3aEnt.get()), float(MA3bEnt.get()),float(MA3cEnt.get()), float(MA3dEnt.get()), float(MA4aEnt.get()), float(MA4bEnt.get()), float(MA4cEnt.get()), float(MA4dEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB1cEnt.get()), float(MB1dEnt.get()), float(MB2aEnt.get()), float(MB2bEnt.get()), float(MB2cEnt.get()), float(MB2dEnt.get()), float(MB3aEnt.get()), float(MB3bEnt.get()), float(MB3cEnt.get()), float(MB3dEnt.get()),float(MB4aEnt.get()), float(MB4bEnt.get()), float(MB4cEnt.get()), float(MB4dEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA1cEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA2bEnt.get()) and FTest(MA2cEnt.get()) and FTest(MA3aEnt.get()) and FTest(MA3bEnt.get()) and FTest(MA3cEnt.get()) and FTest(MA4aEnt.get()) and FTest(MA4bEnt.get()) and FTest(MA4cEnt.get()) and not FTest(MA1dEnt.get()) and not FTest(MA2dEnt.get()) and not FTest(MA3dEnt.get()) and not FTest(MA4dEnt.get()) and\
                FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB1cEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB2bEnt.get()) and FTest(MB2cEnt.get()) and FTest(MB3aEnt.get()) and FTest(MB3bEnt.get()) and FTest(MB3cEnt.get()) and FTest(MB4aEnt.get()) and FTest(MB4bEnt.get()) and FTest(MB4cEnt.get()) and not FTest(MB1dEnt.get()) and not FTest(MB2dEnt.get()) and not FTest(MB3dEnt.get()) and not FTest(MB4dEnt.get()):
                DMPage.DIM = 43
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA1cEnt.get()), float(MA2aEnt.get()), float(MA2bEnt.get()), float(MA2cEnt.get()), float(MA3aEnt.get()), float(MA3bEnt.get()), float(MA3cEnt.get()), float(MA4aEnt.get()), float(MA4bEnt.get()), float(MA4cEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB1cEnt.get()), float(MB2aEnt.get()), float(MB2bEnt.get()), float(MB2cEnt.get()), float(MB3aEnt.get()), float(MB3bEnt.get()), float(MB3cEnt.get()), float(MB4aEnt.get()), float(MB4bEnt.get()), float(MB4cEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA2bEnt.get()) and FTest(MA3aEnt.get()) and FTest(MA3bEnt.get()) and FTest(MA4aEnt.get()) and FTest(MA4bEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB2bEnt.get()) and FTest(MB3aEnt.get()) and FTest(MB3bEnt.get()) and FTest(MB4aEnt.get()) and FTest(MB4bEnt.get()) and not FTest(MA1cEnt.get()) and not FTest(MA2cEnt.get()) and not FTest(MA3cEnt.get()) and not FTest(MA4cEnt.get()) and not FTest(MB1cEnt.get()) and not FTest(MB2cEnt.get()) and not FTest(MB3cEnt.get()) and not FTest(MB4cEnt.get()):
                DMPage.DIM = 42
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA2aEnt.get()), float(MA2bEnt.get()), float(MA3aEnt.get()), float(MA3bEnt.get()), float(MA4aEnt.get()), float(MA4bEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB2aEnt.get()), float(MB2bEnt.get()), float(MB3aEnt.get()), float(MB3bEnt.get()), float(MB4aEnt.get()), float(MB4bEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA3aEnt.get()) and FTest(MA4aEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB3aEnt.get()) and FTest(MB4aEnt.get()) and not FTest(MA1bEnt.get()) and not FTest(MA2bEnt.get()) and not FTest(MA3bEnt.get()) and not FTest(MA4bEnt.get()) and not FTest(MB1bEnt.get()) and not FTest(MB2bEnt.get()) and not FTest(MB3bEnt.get()) and not FTest(MB4bEnt.get()):
                DMPage.DIM = 41
                MatA = (float(MA1aEnt.get()), float(MA2aEnt.get()), float(MA3aEnt.get()), float(MA4aEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB2aEnt.get()), float(MB3aEnt.get()), float(MB4aEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA1cEnt.get()) and FTest(MA1dEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA2bEnt.get()) and FTest(MA2cEnt.get()) and FTest(MA2dEnt.get()) and FTest(MA3aEnt.get()) and FTest(MA3bEnt.get()) and FTest(MA3cEnt.get()) and FTest(MA3dEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB1cEnt.get()) and FTest(MB1dEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB2bEnt.get()) and FTest(MB2cEnt.get()) and FTest(MB2dEnt.get()) and FTest(MB3aEnt.get()) and FTest(MB3bEnt.get()) and FTest(MB3cEnt.get()) and FTest(MB3dEnt.get()) and not FTest(MA4aEnt.get()) and not FTest(MA4bEnt.get()) and not FTest(MA4cEnt.get()) and not FTest(MA4dEnt.get()) and not FTest(MB4aEnt.get()) and not FTest(MB4bEnt.get()) and not FTest(MB4cEnt.get()) and not FTest(MB4dEnt.get()):
                DMPage.DIM = 34
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA1cEnt.get()), float(MA1dEnt.get()), float(MA2aEnt.get()), float(MA2bEnt.get()), float(MA2cEnt.get()), float(MA2dEnt.get()), float(MA3aEnt.get()), float(MA3bEnt.get()), float(MA3cEnt.get()), float(MA3dEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB1cEnt.get()), float(MB1dEnt.get()), float(MB2aEnt.get()), float(MB2bEnt.get()), float(MB2cEnt.get()), float(MB2dEnt.get()), float(MB3aEnt.get()), float(MB3bEnt.get()), float(MB3cEnt.get()), float(MB3dEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA1cEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA2bEnt.get()) and FTest(MA2cEnt.get()) and FTest(MA3aEnt.get()) and FTest(MA3bEnt.get()) and FTest(MA3cEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB1cEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB2bEnt.get()) and FTest(MB2cEnt.get()) and FTest(MB3aEnt.get()) and FTest(MB3bEnt.get()) and FTest(MB3cEnt.get()) and not FTest(MA1dEnt.get()) and not FTest(MA2dEnt.get()) and not FTest(MA3dEnt.get()) and not FTest(MA4aEnt.get()) and not FTest(MA4bEnt.get()) and not FTest(MA4cEnt.get()) and not FTest(MA4dEnt.get()) and not FTest(MB1dEnt.get()) and not FTest(MB2dEnt.get()) and not FTest(MB3dEnt.get()) and not FTest(MB4aEnt.get()) and not FTest(MB4bEnt.get()) and not FTest(MB4cEnt.get()) and not FTest(MB4dEnt.get()):
                DMPage.DIM = 33
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA1cEnt.get()), float(MA2aEnt.get()), float(MA2bEnt.get()), float(MA2cEnt.get()), float(MA3aEnt.get()), float(MA3bEnt.get()), float(MA3cEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB1cEnt.get()), float(MB2aEnt.get()), float(MB2bEnt.get()), float(MB2cEnt.get()), float(MB3aEnt.get()), float(MB3bEnt.get()), float(MB3cEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA2bEnt.get()) and  FTest(MA3aEnt.get()) and FTest(MA3bEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB2bEnt.get()) and FTest(MB3aEnt.get()) and FTest(MB3bEnt.get()) and not FTest(MA1cEnt.get()) and not FTest(MA2cEnt.get()) and not FTest(MA3cEnt.get()) and not FTest(MA4aEnt.get()) and not FTest(MA4bEnt.get()) and not FTest(MB1cEnt.get()) and not FTest(MB2cEnt.get()) and not FTest(MB3cEnt.get()) and not FTest(MB4aEnt.get()) and not FTest(MB4bEnt.get()):
                DMPage.DIM = 32
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA2aEnt.get()), float(MA2bEnt.get()), float(MA3aEnt.get()), float(MA3bEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB2aEnt.get()), float(MB2bEnt.get()), float(MB3aEnt.get()), float(MB3bEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA3aEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB3aEnt.get()) and not FTest(MA1bEnt.get()) and not FTest(MA2bEnt.get()) and not FTest(MA3bEnt.get()) and not FTest(MA4aEnt.get()) and not FTest(MB1bEnt.get()) and not FTest(MB2bEnt.get()) and not FTest(MB3bEnt.get()) and not FTest(MB4aEnt.get()):
                DMPage.DIM = 31
                MatA = (float(MA1aEnt.get()), float(MA2aEnt.get()), float(MA3aEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB2aEnt.get()), float(MB3aEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA1cEnt.get()) and FTest(MA1dEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA2bEnt.get()) and FTest(MA2cEnt.get()) and FTest(MA2dEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB1cEnt.get()) and FTest(MB1dEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB2bEnt.get()) and FTest(MB2cEnt.get()) and FTest(MB2dEnt.get()) and not FTest(MA3aEnt.get()) and not FTest(MA3bEnt.get()) and not FTest(MA3cEnt.get()) and not FTest(MA3dEnt.get()) and not FTest(MB3aEnt.get()) and not FTest(MB3bEnt.get()) and not FTest(MB3cEnt.get()) and not FTest(MB3dEnt.get()):
                DMPage.DIM = 24
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA1cEnt.get()), float(MA1dEnt.get()), float(MA2aEnt.get()), float(MA2bEnt.get()), float(MA2cEnt.get()), float(MA2dEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB1cEnt.get()), float(MB1dEnt.get()), float(MB2aEnt.get()), float(MB2bEnt.get()), float(MB2cEnt.get()), float(MB2dEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA1cEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA2bEnt.get()) and FTest(MA2cEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB1cEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB2bEnt.get()) and FTest(MB2cEnt.get()) and not FTest(MA1dEnt.get()) and not FTest(MA2dEnt.get()) and not FTest(MA3aEnt.get()) and not FTest(MA3bEnt.get()) and not FTest(MA3cEnt.get()) and not FTest(MB1dEnt.get()) and not FTest(MB2dEnt.get()) and not FTest(MB3aEnt.get()) and not FTest(MB3bEnt.get()) and not FTest(MB3cEnt.get()):
                DMPage.DIM = 23
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA1cEnt.get()), float(MA2aEnt.get()), float(MA2bEnt.get()), float(MA2cEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB1cEnt.get()), float(MB2aEnt.get()), float(MB2bEnt.get()), float(MB2cEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA2bEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB2bEnt.get()) and not FTest(MA1cEnt.get()) and not FTest(MA2cEnt.get()) and not FTest(MA3aEnt.get()) and not FTest(MA3bEnt.get()) and not FTest(MB1cEnt.get()) and not FTest(MB2cEnt.get()) and not FTest(MB3aEnt.get()) and not FTest(MB3bEnt.get()):
                DMPage.DIM = 22
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA2aEnt.get()), float(MA2bEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB2aEnt.get()), float(MB2bEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA2aEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB2aEnt.get()) and not FTest(MA1bEnt.get()) and not FTest(MA2bEnt.get()) and not FTest(MB3aEnt.get()) and not FTest(MB1bEnt.get()) and not FTest(MB2bEnt.get()) and not FTest(MB3aEnt.get()):
                DMPage.DIM = 21
                MatA = (float(MA1aEnt.get()), float(MA2aEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB2aEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA1cEnt.get()) and FTest(MA1dEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB1cEnt.get()) and FTest(MB1dEnt.get()) and not FTest(MA2aEnt.get()) and not FTest(MA2bEnt.get()) and not FTest(MA2cEnt.get()) and not FTest(MA2dEnt.get()) and not FTest(MB2aEnt.get()) and not FTest(MB2bEnt.get()) and not FTest(MB2cEnt.get()) and not FTest(MB2dEnt.get()):
                DMPage.DIM = 14
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA1cEnt.get()), float(MA1dEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB1cEnt.get()), float(MB1dEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA1cEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB1cEnt.get()) and not FTest(MA1dEnt.get()) and not FTest(MA2aEnt.get()) and not FTest(MA2bEnt.get()) and not FTest(MA2cEnt.get()) and not FTest(MB1dEnt.get()) and not FTest(MB2aEnt.get()) and not FTest(MB2bEnt.get()) and not FTest(MB2cEnt.get()):
                DMPage.DIM = 13
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA1cEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB1cEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and not FTest(MA1cEnt.get()) and not FTest(MA2aEnt.get()) and not FTest(MA2bEnt.get()) and not FTest(MB1cEnt.get()) and not FTest(MB2aEnt.get()) and not FTest(MB2bEnt.get()):
                DMPage.DIM = 12
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MB1aEnt.get()) and not FTest(MA1bEnt.get()) and not FTest(MA2aEnt.get()):
                DMPage.DIM = 11
                MatA = float(MA1aEnt.get())
                MatB = float(MB1aEnt.get())
            else:
                DMPage.DIM = 0
                MatA = 0
                MatB = 0
            TMat = DoubleMatrix(MatA, MatB, DMPage.DIM, Avalue(), Bvalue())
            return TMat
        def TMM():
            if FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA1cEnt.get()) and FTest(MA1dEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA2bEnt.get()) and FTest(MA2cEnt.get()) and FTest(MA2dEnt.get()) and FTest(MA3aEnt.get()) and FTest(MA3bEnt.get()) and FTest(MA3cEnt.get()) and FTest(MA3dEnt.get()) and FTest(MA4aEnt.get()) and FTest(MA4bEnt.get()) and FTest(MA4cEnt.get()) and FTest(MA4dEnt.get()) and \
                FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB1cEnt.get()) and FTest(MB1dEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB2bEnt.get()) and FTest(MB2cEnt.get()) and FTest(MB2dEnt.get()) and FTest(MB3aEnt.get()) and FTest(MB3bEnt.get()) and FTest(MB3cEnt.get()) and FTest(MB3dEnt.get()) and FTest(MB4aEnt.get()) and FTest(MB4bEnt.get()) and FTest(MB4cEnt.get()) and FTest(MB4dEnt.get()):
                DMPage.DIM = 44
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA1cEnt.get()), float(MA1dEnt.get()), float(MA2aEnt.get()), float(MA2bEnt.get()), float(MA2cEnt.get()), float(MA2dEnt.get()), float(MA3aEnt.get()), float(MA3bEnt.get()),float(MA3cEnt.get()), float(MA3dEnt.get()), float(MA4aEnt.get()), float(MA4bEnt.get()), float(MA4cEnt.get()), float(MA4dEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB1cEnt.get()), float(MB1dEnt.get()), float(MB2aEnt.get()), float(MB2bEnt.get()), float(MB2cEnt.get()), float(MB2dEnt.get()), float(MB3aEnt.get()), float(MB3bEnt.get()), float(MB3cEnt.get()), float(MB3dEnt.get()),float(MB4aEnt.get()), float(MB4bEnt.get()), float(MB4cEnt.get()), float(MB4dEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA1cEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA2bEnt.get()) and FTest(MA2cEnt.get()) and FTest(MA3aEnt.get()) and FTest(MA3bEnt.get()) and FTest(MA3cEnt.get()) and FTest(MA4aEnt.get()) and FTest(MA4bEnt.get()) and FTest(MA4cEnt.get()) and not FTest(MA1dEnt.get()) and not FTest(MA2dEnt.get()) and not FTest(MA3dEnt.get()) and not FTest(MA4dEnt.get()) and\
                FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB1cEnt.get()) and FTest(MB1dEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB2bEnt.get()) and FTest(MB2cEnt.get()) and FTest(MB2dEnt.get()) and FTest(MB3aEnt.get()) and FTest(MB3bEnt.get()) and FTest(MB3cEnt.get()) and FTest(MB3dEnt.get()) and not FTest(MB4aEnt.get()) and not FTest(MB4bEnt.get()) and not FTest(MB4cEnt.get()) and not FTest(MB4dEnt.get()):
                DMPage.DIM = 43
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA1cEnt.get()), float(MA2aEnt.get()), float(MA2bEnt.get()), float(MA2cEnt.get()), float(MA3aEnt.get()), float(MA3bEnt.get()), float(MA3cEnt.get()), float(MA4aEnt.get()), float(MA4bEnt.get()), float(MA4cEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB1cEnt.get()), float(MB1dEnt.get()), float(MB2aEnt.get()), float(MB2bEnt.get()), float(MB2cEnt.get()), float(MB2dEnt.get()), float(MB3aEnt.get()), float(MB3bEnt.get()), float(MB3cEnt.get()), float(MB3dEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA2bEnt.get()) and FTest(MA3aEnt.get()) and FTest(MA3bEnt.get()) and FTest(MA4aEnt.get()) and FTest(MA4bEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB1cEnt.get()) and FTest(MB1dEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB2bEnt.get()) and FTest(MB2cEnt.get()) and FTest(MB2dEnt.get()) and not FTest(MA1cEnt.get()) and not FTest(MA2cEnt.get()) and not FTest(MA3cEnt.get()) and not FTest(MA4cEnt.get()) and not FTest(MB3aEnt.get()) and not FTest(MB3bEnt.get()) and not FTest(MB3cEnt.get()) and not FTest(MB3dEnt.get()):
                DMPage.DIM = 42
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA2aEnt.get()), float(MA2bEnt.get()), float(MA3aEnt.get()), float(MA3bEnt.get()), float(MA4aEnt.get()), float(MA4bEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB1cEnt.get()), float(MB1dEnt.get()), float(MB2aEnt.get()), float(MB2bEnt.get()), float(MB2cEnt.get()), float(MB2dEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA3aEnt.get()) and FTest(MA4aEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB1cEnt.get()) and FTest(MB1dEnt.get()) and not FTest(MA1bEnt.get()) and not FTest(MA2bEnt.get()) and not FTest(MA3bEnt.get()) and not FTest(MA4bEnt.get()) and not FTest(MB2aEnt.get()) and not FTest(MB2bEnt.get()) and not FTest(MB2cEnt.get()) and not FTest(MB2dEnt.get()):
                DMPage.DIM = 41
                MatA = (float(MA1aEnt.get()), float(MA2aEnt.get()), float(MA3aEnt.get()), float(MA4aEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB1cEnt.get()), float(MB1dEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA1cEnt.get()) and FTest(MA1dEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA2bEnt.get()) and FTest(MA2cEnt.get()) and FTest(MA2dEnt.get()) and FTest(MA3aEnt.get()) and FTest(MA3bEnt.get()) and FTest(MA3cEnt.get()) and FTest(MA3dEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB1cEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB2bEnt.get()) and FTest(MB2cEnt.get()) and FTest(MB3aEnt.get()) and FTest(MB3bEnt.get()) and FTest(MB3cEnt.get()) and FTest(MB4aEnt.get()) and FTest(MB4bEnt.get()) and FTest(MB4cEnt.get()) and not FTest(MA4aEnt.get()) and not FTest(MA4bEnt.get()) and not FTest(MA4cEnt.get()) and not FTest(MA4dEnt.get()) and not FTest(MB1dEnt.get()) and not FTest(MB2dEnt.get()) and not FTest(MB3dEnt.get()) and not FTest(MB4dEnt.get()):
                DMPage.DIM = 34
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA1cEnt.get()), float(MA1dEnt.get()), float(MA2aEnt.get()), float(MA2bEnt.get()), float(MA2cEnt.get()), float(MA2dEnt.get()), float(MA3aEnt.get()), float(MA3bEnt.get()), float(MA3cEnt.get()), float(MA3dEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB1cEnt.get()), float(MB2aEnt.get()), float(MB2bEnt.get()), float(MB2cEnt.get()), float(MB3aEnt.get()), float(MB3bEnt.get()), float(MB3cEnt.get()), float(MB4aEnt.get()), float(MB4bEnt.get()), float(MB4cEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA1cEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA2bEnt.get()) and FTest(MA2cEnt.get()) and FTest(MA3aEnt.get()) and FTest(MA3bEnt.get()) and FTest(MA3cEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB1cEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB2bEnt.get()) and FTest(MB2cEnt.get()) and FTest(MB3aEnt.get()) and FTest(MB3bEnt.get()) and FTest(MB3cEnt.get()) and not FTest(MA1dEnt.get()) and not FTest(MA2dEnt.get()) and not FTest(MA3dEnt.get()) and not FTest(MA4aEnt.get()) and not FTest(MA4bEnt.get()) and not FTest(MA4cEnt.get()) and not FTest(MA4dEnt.get()) and not FTest(MB1dEnt.get()) and not FTest(MB2dEnt.get()) and not FTest(MB3dEnt.get()) and not FTest(MB4aEnt.get()) and not FTest(MB4bEnt.get()) and not FTest(MB4cEnt.get()) and not FTest(MB4dEnt.get()):
                DMPage.DIM = 33
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA1cEnt.get()), float(MA2aEnt.get()), float(MA2bEnt.get()), float(MA2cEnt.get()), float(MA3aEnt.get()), float(MA3bEnt.get()), float(MA3cEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB1cEnt.get()), float(MB2aEnt.get()), float(MB2bEnt.get()), float(MB2cEnt.get()), float(MB3aEnt.get()), float(MB3bEnt.get()), float(MB3cEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA2bEnt.get()) and  FTest(MA3aEnt.get()) and FTest(MA3bEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB1cEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB2bEnt.get()) and FTest(MB2cEnt.get()) and not FTest(MA1cEnt.get()) and not FTest(MA2cEnt.get()) and not FTest(MA3cEnt.get()) and not FTest(MA4aEnt.get()) and not FTest(MA4bEnt.get()) and not FTest(MB1dEnt.get()) and not FTest(MB2dEnt.get()) and not FTest(MB3aEnt.get()) and not FTest(MB3bEnt.get()) and not FTest(MB3cEnt.get()):
                DMPage.DIM = 32
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA2aEnt.get()), float(MA2bEnt.get()), float(MA3aEnt.get()), float(MA3bEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB1cEnt.get()), float(MB2aEnt.get()), float(MB2bEnt.get()), float(MB2cEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA3aEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB1cEnt.get()) and not FTest(MA1bEnt.get()) and not FTest(MA2bEnt.get()) and not FTest(MA3bEnt.get()) and not FTest(MA4aEnt.get()) and not FTest(MB1dEnt.get()) and not FTest(MB2aEnt.get()) and not FTest(MB2bEnt.get()) and not FTest(MB2cEnt.get()):
                DMPage.DIM = 31
                MatA = (float(MA1aEnt.get()), float(MA2aEnt.get()), float(MA3aEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB1cEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA1cEnt.get()) and FTest(MA1dEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA2bEnt.get()) and FTest(MA2cEnt.get()) and FTest(MA2dEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB2bEnt.get()) and FTest(MB3aEnt.get()) and FTest(MB3bEnt.get()) and FTest(MB4aEnt.get()) and FTest(MB4bEnt.get()) and not FTest(MA3aEnt.get()) and not FTest(MA3bEnt.get()) and not FTest(MA3cEnt.get()) and not FTest(MA3dEnt.get()) and not FTest(MB1cEnt.get()) and not FTest(MB2cEnt.get()) and not FTest(MB3cEnt.get()) and not FTest(MB4cEnt.get()):
                DMPage.DIM = 24
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA1cEnt.get()), float(MA1dEnt.get()), float(MA2aEnt.get()), float(MA2bEnt.get()), float(MA2cEnt.get()), float(MA2dEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB2aEnt.get()), float(MB2bEnt.get()), float(MB3aEnt.get()), float(MB3bEnt.get()), float(MB4aEnt.get()), float(MB4bEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA1cEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA2bEnt.get()) and FTest(MA2cEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB2bEnt.get()) and FTest(MB3aEnt.get()) and FTest(MB3bEnt.get()) and not FTest(MA1dEnt.get()) and not FTest(MA2dEnt.get()) and not FTest(MA3aEnt.get()) and not FTest(MA3bEnt.get()) and not FTest(MA3cEnt.get()) and not FTest(MB1cEnt.get()) and not FTest(MB2cEnt.get()) and not FTest(MB3cEnt.get()) and not FTest(MB4aEnt.get()) and not FTest(MB4bEnt.get()):
                DMPage.DIM = 23
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA1cEnt.get()), float(MA2aEnt.get()), float(MA2bEnt.get()), float(MA2cEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB2aEnt.get()), float(MB2bEnt.get()), float(MB3aEnt.get()), float(MB3bEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA2aEnt.get()) and FTest(MA2bEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB2bEnt.get()) and not FTest(MA1cEnt.get()) and not FTest(MA2cEnt.get()) and not FTest(MA3aEnt.get()) and not FTest(MA3bEnt.get()) and not FTest(MB1cEnt.get()) and not FTest(MB2cEnt.get()) and not FTest(MB3aEnt.get()) and not FTest(MB3bEnt.get()):
                DMPage.DIM = 22
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA2aEnt.get()), float(MA2bEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()), float(MB2aEnt.get()), float(MB2bEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA2aEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB1bEnt.get()) and not FTest(MA1bEnt.get()) and not FTest(MA2bEnt.get()) and not FTest(MB3aEnt.get()) and not FTest(MB1cEnt.get()) and not FTest(MB2aEnt.get()) and not FTest(MB2bEnt.get()):
                DMPage.DIM = 21
                MatA = (float(MA1aEnt.get()), float(MA2aEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB1bEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA1cEnt.get()) and FTest(MA1dEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB3aEnt.get()) and FTest(MB4aEnt.get()) and not FTest(MA2aEnt.get()) and not FTest(MA2bEnt.get()) and not FTest(MA2cEnt.get()) and not FTest(MA2dEnt.get()) and not FTest(MB1bEnt.get()) and not FTest(MB2bEnt.get()) and not FTest(MB3bEnt.get()) and not FTest(MB4bEnt.get()):
                DMPage.DIM = 14
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA1cEnt.get()), float(MA1dEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB2aEnt.get()), float(MB3aEnt.get()), float(MB4aEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MA1cEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB2aEnt.get()) and FTest(MB3aEnt.get()) and not FTest(MA1dEnt.get()) and not FTest(MA2aEnt.get()) and not FTest(MA2bEnt.get()) and not FTest(MA2cEnt.get()) and not FTest(MB1bEnt.get()) and not FTest(MB2bEnt.get()) and not FTest(MB3bEnt.get()) and not FTest(MB4aEnt.get()):
                DMPage.DIM = 13
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()), float(MA1cEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB2aEnt.get()), float(MB3aEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MA1bEnt.get()) and FTest(MB1aEnt.get()) and FTest(MB2aEnt.get()) and not FTest(MA1cEnt.get()) and not FTest(MA2aEnt.get()) and not FTest(MA2bEnt.get()) and not FTest(MB1bEnt.get()) and not FTest(MB2bEnt.get()) and not FTest(MB3aEnt.get()):
                DMPage.DIM = 12
                MatA = (float(MA1aEnt.get()), float(MA1bEnt.get()))
                MatB = (float(MB1aEnt.get()), float(MB2aEnt.get()))
            elif FTest(MA1aEnt.get()) and FTest(MB1aEnt.get()) and not FTest(MA1bEnt.get()) and not FTest(MA2aEnt.get()):
                DMPage.DIM = 11
                MatA = float(MA1aEnt.get())
                MatB = float(MB1aEnt.get())
            else:
                DMPage.DIM = 0
                MatA = 0
                MatB = 0
            TMat = DoubleMatrix(MatA, MatB, DMPage.DIM, Avalue(), Bvalue())
            return TMat
        def UpdateAns():
            Ans1.update()
            Ans2.update()
            Ans3.update()
            Ans4.update()
        def AnsLift():
            a = (Ans1, Ans2, Ans3, Ans4)
            for i in range(4):
                a[i].lift()
        def PlusAct():
            ResultLower()
            PlusR.lift()
            AnsLift()
            Ans1.configure(font=("Segoe Print", 14), anchor='c', text=TM().MatA())
            Ans2.configure(font=("Segoe Print", 14), anchor='c', text=TM().MatB())
            Ans3.configure(font=("Segoe Print", 10), anchor='c', text=TM().AddEXP())
            Ans4.configure(font=("Segoe Print", 12), anchor='c', text=TM().Add())
            UpdateAns()
        def MinuAct():
            ResultLower()
            MinusR.lift()
            AnsLift()
            Ans1.configure(font=("Segoe Print", 14), anchor='c', text=TM().MatA())
            Ans2.configure(font=("Segoe Print", 14), anchor='c', text=TM().MatB())
            Ans3.configure(font=("Segoe Print", 10), anchor='c', text=TM().MinusEXP())
            Ans4.configure(font=("Segoe Print", 12), anchor='c', text=TM().Minus())
            UpdateAns()
        def MultAct():
            ResultLower()
            MultiR.lift()
            AnsLift()
            Ans1.configure(font=("Segoe Print", 14), anchor='c', text=TMM().MatA())
            Ans2.configure(font=("Segoe Print", 14), anchor='c', text=TMM().MatBM())
            Ans3.configure(font=("Arial Narrow", 7), anchor='c', text=TMM().MultiplyEXP())
            Ans4.configure(font=("Menlo", 10), anchor='c', text=TMM().Multiply())
            UpdateAns()
        def BackAct():
            BackS = pygame.mixer.Sound("FrozenBack.wav")
            BackS.play()
            pygame.mixer.music.load("MenuBG.ogg")
            pygame.mixer.music.play(-1)
            controller.show_frame("MatrixPage")
        def InfoAct():
            if DMPage.INFO == False:
                DMPage.INFO = True
                if DMPage.MUTE == False:
                    InfoS = pygame.mixer.Sound("FrozenInfo.wav")
                    InfoS.play()
                InfoPop.lift()
                InfoBtn.lift()
            else:
                DMPage.INFO = False
                InfoPop.lower()
        def ResetAct():
            if DMPage.MUTE == False:
                ClearS = pygame.mixer.Sound("FrozenReset.wav")
                ClearS.play()
            time.sleep(2)
            EntA = (MA1aEnt, MA1bEnt, MA1cEnt, MA1dEnt, MA2aEnt, MA2bEnt, MA2cEnt, MA2dEnt, MA3aEnt, MA3bEnt, MA3cEnt, MA3dEnt,MA4aEnt, MA4bEnt, MA4cEnt, MA4dEnt)
            EntB = (MB1aEnt, MB1bEnt, MB1cEnt, MB1dEnt, MB2aEnt, MB2bEnt, MB2cEnt, MB2dEnt, MB3aEnt, MB3bEnt, MB3cEnt, MB3dEnt,MB4aEnt, MB4bEnt, MB4cEnt, MB4dEnt)
            for i in range(16):
                EntA[i].delete(0, END)
                EntB[i].delete(0, END)
            AEnt.delete(0, END)
            BEnt.delete(0, END)
        def MuteAct():
            if DMPage.MUTE == True:
                DMPage.MUTE = False
                pygame.mixer.music.load("FrozenBackground.ogg")
                pygame.mixer.music.play(-1)
                MuteOff.lower()
            else:
                DMPage.MUTE = True
                pygame.mixer.music.stop()
                MuteOff.lift()
        def RandAct():
            if DMPage.MUTE == False:
                RandomS = pygame.mixer.Sound("FrozenRandom.wav")
                RandomS.play()
            runRandAct()
        def runRandAct():
            time.sleep(2)
            EntA = (MA1aEnt, MA1bEnt, MA1cEnt, MA1dEnt, MA2aEnt, MA2bEnt, MA2cEnt, MA2dEnt, MA3aEnt, MA3bEnt, MA3cEnt, MA3dEnt,MA4aEnt, MA4bEnt, MA4cEnt, MA4dEnt)
            EntB = (MB1aEnt, MB1bEnt, MB1cEnt, MB1dEnt, MB2aEnt, MB2bEnt, MB2cEnt, MB2dEnt, MB3aEnt, MB3bEnt, MB3cEnt, MB3dEnt,MB4aEnt, MB4bEnt, MB4cEnt, MB4dEnt)
            for i in range(16):
                EntA[i].delete(0, END)
                EntB[i].delete(0, END)
            x = random.randrange(1,4)
            if x==1:
                for i in range(2):
                    EntA[i].insert(1, random.randrange(-9, 10))
                    EntB[i].insert(1, random.randrange(-9, 10))
                for i in range(4,6):
                    EntA[i].insert(1, random.randrange(-9, 10))
                    EntB[i].insert(1, random.randrange(-9, 10))
            elif x==2:
                for i in range(3):
                    EntA[i].insert(1, random.randrange(-9, 10))
                    EntB[i].insert(1, random.randrange(-9, 10))
                for i in range(4,7):
                    EntA[i].insert(1, random.randrange(-9, 10))
                    EntB[i].insert(1, random.randrange(-9, 10))
                for i in range(8,11):
                    EntA[i].insert(1, random.randrange(-9, 10))
                    EntB[i].insert(1, random.randrange(-9, 10))
            else:
                for i in range(16):
                    EntA[i].insert(1, random.randrange(-9, 10))
                    EntB[i].insert(1, random.randrange(-9, 10))