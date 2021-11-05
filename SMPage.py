from tkinter import *
from SMExp import*
from DMExp import*
import pygame
import time
import random
class SMPage(Frame):
    MUTE = False
    INFO = False
    DIM = 0
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        pygame.mixer.init()
        SGMWall = PhotoImage(file="TwoDimension.png")
        SGLabel = Label(self, image=SGMWall)
        SGLabel.image = SGMWall
        SGLabel.place(x=-2, y=-2)
        Info = PhotoImage(file="InfoPopOne.png")
        InfoPop = Label(self, image=Info)
        InfoPop.image = Info
        InfoPop.place(x=-2, y=-2)
        InfoPop.lower()
        Back = PhotoImage(file="DisneyBackbutton.png")
        BackBtn = Button(self, image=Back, bd=0, bg='#182b3a', command=lambda: BackAct())
        BackBtn.image = Back
        BackBtn.place(x=-2, y=-2)
        Info = PhotoImage(file="DisneyInfoButton.png")
        InfoBtn = Button(self, image=Info, bd=0, bg='black', command=lambda: InfoAct())
        InfoBtn.image = Info
        InfoBtn.place(x=-2, y=698)
        Music = PhotoImage(file="DisneyMusicOn.png")
        MusicBtn = Button(self, image=Music, bd=0, bg='black', command=lambda: MuteAct())
        MusicBtn.image = Music
        MusicBtn.place(x=48, y=698)
        MusicOff = PhotoImage(file="DisneyMusicOff.png")
        MuteOff = Button(self, image=MusicOff, bd=0, bg='black', command=lambda: MuteAct())
        MuteOff.image = MusicOff
        MuteOff.place(x=48, y=698)
        MuteOff.lower()
        Random = PhotoImage(file="DisneyRandomButton.png")
        RandBtn = Button(self, image=Random, bd=0, bg="black", command=lambda: RandAct())
        RandBtn.image = Random
        RandBtn.place(x=98, y=698)
        Reset = PhotoImage(file="DisneyClearButton.png")
        ResetBtn = Button(self, image=Reset, bd=0, bg="black", command=lambda: ResetAct())
        ResetBtn.image = Reset
        ResetBtn.place(x=148, y=698)
        Dtm = PhotoImage(file="Button1.png")
        DtmBtn = Button(self, image=Dtm, bd=0, command=lambda: DtmAct())
        DtmBtn.image = Dtm
        DtmBtn.place(x=48, y=174)
        Inverse = PhotoImage(file="Button2.png")
        InverseBtn = Button(self, image=Inverse, bd=0, command=lambda: InvAct())
        InverseBtn.image = Inverse
        InverseBtn.place(x=48, y=282)
        Trans = PhotoImage(file="Button3.png")
        TransBtn = Button(self, image=Trans, bd=0, command=lambda: TrpAct())
        TransBtn.image = Trans
        TransBtn.place(x=48, y=390)
        Scal = PhotoImage(file="Button4.png")
        ScalBtn = Button(self, image=Scal, bd=0, command=lambda: ScaAct())
        ScalBtn.image = Scal
        ScalBtn.place(x=48, y=498)
        Multi = PhotoImage(file="Button5.png")
        MultiBtn = Button(self, image=Multi, bd=0, command=lambda: MulAct())
        MultiBtn.image = Multi
        MultiBtn.place(x=48, y=606)
        Triangle = PhotoImage(file="Button6.png")
        TriangleBtn = Button(self, image=Triangle, bd=0, command=lambda: TriAct())
        TriangleBtn.image = Triangle
        TriangleBtn.place(x=281, y=174)
        Trac = PhotoImage(file="Button7.png")
        TraceBtn = Button(self, image=Trac, bd=0, command=lambda: TrcAct())
        TraceBtn.image = Trac
        TraceBtn.place(x=281, y=282)
        LUdec = PhotoImage(file="Button8.png")
        LUdecBtn = Button(self, image=LUdec, bd=0, command=lambda: LUDAct())
        LUdecBtn.image = LUdec
        LUdecBtn.place(x=281, y=390)
        Rank = PhotoImage(file="Button9.png")
        RankBtn = Button(self, image=Rank, bd=0, command=lambda: RanAct())
        RankBtn.image = Rank
        RankBtn.place(x=281, y=498)
        Pwr = PhotoImage(file="Button10.png")
        PwrBtn = Button(self, image=Pwr, bd=0, command=lambda: PowAct())
        PwrBtn.image = Pwr
        PwrBtn.place(x=281, y=606)
        TwoMatrix = PhotoImage(file="twoD.png")
        TwoMatrixBtn = Button(self, image=TwoMatrix, bd=0, command=lambda: EntLIFT2())
        TwoMatrixBtn.image = TwoMatrix
        TwoMatrixBtn.place(x=514, y=403)
        ThreeMatrix = PhotoImage(file="threeD.png")
        ThreeMatrixBtn = Button(self, image=ThreeMatrix, bd=0, command=lambda: EntLIFT3())
        ThreeMatrixBtn.image = ThreeMatrix
        ThreeMatrixBtn.place(x=634, y=403)
        FourMatrix = PhotoImage(file="fourD.png")
        FourMatrixBtn = Button(self, image=FourMatrix, bd=0, command=lambda: EntLIFT4())
        FourMatrixBtn.image = FourMatrix
        FourMatrixBtn.place(x=754, y=403)
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
        M1aEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        M1aEnt.config(validatecommand=(M1aEnt.register(on_validate), '%P'))
        M1aEnt.place(x=529, y=61, width=50, height=50)
        M1bEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        M1bEnt.config(validatecommand=(M1bEnt.register(on_validate), '%P'))
        M1bEnt.place(x=609, y=61, width=50, height=50)
        M1cEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        M1cEnt.config(validatecommand=(M1cEnt.register(on_validate), '%P'))
        M1cEnt.place(x=689, y=61, width=50, height=50)
        M1dEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        M1dEnt.config(validatecommand=(M1dEnt.register(on_validate), '%P'))
        M1dEnt.place(x=769, y=61, width=50, height=50)
        M2aEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        M2aEnt.config(validatecommand=(M2aEnt.register(on_validate), '%P'))
        M2aEnt.place(x=529, y=146, width=50, height=50)
        M2bEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        M2bEnt.config(validatecommand=(M2bEnt.register(on_validate), '%P'))
        M2bEnt.place(x=609, y=146, width=50, height=50)
        M2cEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        M2cEnt.config(validatecommand=(M2cEnt.register(on_validate), '%P'))
        M2cEnt.place(x=689, y=146, width=50, height=50)
        M2dEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        M2dEnt.config(validatecommand=(M2dEnt.register(on_validate), '%P'))
        M2dEnt.place(x=769, y=146, width=50, height=50)
        M3aEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        M3aEnt.config(validatecommand=(M3aEnt.register(on_validate), '%P'))
        M3aEnt.place(x=529, y=231, width=50, height=50)
        M3bEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        M3bEnt.config(validatecommand=(M3bEnt.register(on_validate), '%P'))
        M3bEnt.place(x=609, y=231, width=50, height=50)
        M3cEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        M3cEnt.config(validatecommand=(M3cEnt.register(on_validate), '%P'))
        M3cEnt.place(x=689, y=231, width=50, height=50)
        M3dEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        M3dEnt.config(validatecommand=(M3dEnt.register(on_validate), '%P'))
        M3dEnt.place(x=769, y=231, width=50, height=50)
        M4aEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        M4aEnt.config(validatecommand=(M4aEnt.register(on_validate), '%P'))
        M4aEnt.place(x=529, y=316, width=50, height=50)
        M4bEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        M4bEnt.config(validatecommand=(M4bEnt.register(on_validate), '%P'))
        M4bEnt.place(x=609, y=316, width=50, height=50)
        M4cEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        M4cEnt.config(validatecommand=(M4cEnt.register(on_validate), '%P'))
        M4cEnt.place(x=689, y=316, width=50, height=50)
        M4dEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        M4dEnt.config(validatecommand=(M4dEnt.register(on_validate), '%P'))
        M4dEnt.place(x=769, y=316, width=50, height=50)
        MultiEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        MultiEnt.config(validatecommand=(MultiEnt.register(on_validate), '%P'))
        MultiEnt.place(x=176, y=611, width=50, height=50)
        PowEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center",validate="key")
        PowEnt.config(validatecommand=(PowEnt.register(on_validate), '%P'))
        PowEnt.place(x=411, y=611, width=50, height=50)
        Result = Label(self, bg='#016738', fg='white', anchor='w', justify="left")
        Result.place(x=898, y=50, width=344, height=685)
        Result1 = Label(self, bg='#016738', fg='white', anchor='w', justify="right")
        Result1.place(x=898, y=50, width=172, height=685)
        Result2 = Label(self, bg='#016738', fg='white', anchor='w', justify="left")
        Result2.place(x=1070, y=50, width=172, height=685)
        def EntLOWER():
            Ent = (M1aEnt, M1bEnt, M1cEnt, M1dEnt, M2aEnt, M2bEnt, M2cEnt, M2dEnt, M3aEnt, M3bEnt, M3cEnt, M3dEnt, M4aEnt, M4bEnt, M4cEnt, M4dEnt)
            for i in range (16):
                Ent[i].lower()
        EntLOWER()

        def EntLIFT4():
            SMPage.DIM = 4
            EntLOWER()
            Ent = (M1aEnt, M1bEnt, M1cEnt, M1dEnt, M2aEnt, M2bEnt, M2cEnt, M2dEnt, M3aEnt, M3bEnt, M3cEnt, M3dEnt, M4aEnt,M4bEnt, M4cEnt, M4dEnt)
            for i in range(16):
                Ent[i].lift()
        def EntLIFT3():
            SMPage.DIM = 3
            EntLOWER()
            Ent = (M1aEnt, M1bEnt, M1cEnt, M2aEnt, M2bEnt, M2cEnt, M3aEnt, M3bEnt, M3cEnt)
            for i in range(9):
                Ent[i].lift()
        def EntLIFT2():
            SMPage.DIM = 2
            EntLOWER()
            Ent = (M2bEnt, M2cEnt, M3bEnt, M3cEnt)
            for i in range(4):
                Ent[i].lift()
        def SM():
            if SMPage.DIM==2:
                if not FTest(M2bEnt.get()) or not FTest(M2cEnt.get()) or not FTest(M3bEnt.get()) or not FTest(M3cEnt.get()):
                    SMat = SingleMatrix(0, 0)
                else:
                    Mat2D = (float(M2bEnt.get()),float(M2cEnt.get()),float(M3bEnt.get()), float(M3cEnt.get()))
                    SMat = SingleMatrix(Mat2D, SMPage.DIM)
            elif SMPage.DIM==3:
                if not FTest(M1aEnt.get()) or not FTest(M1bEnt.get()) or not FTest(M1cEnt.get()) or not FTest(M2aEnt.get()) or not FTest(M2bEnt.get()) or not FTest(M2cEnt.get())\
                        or not FTest(M3aEnt.get()) or not FTest(M3bEnt.get()) or not FTest(M3cEnt.get()):
                    SMat = SingleMatrix(0, 0)
                else:
                    Mat3D = (float(M1aEnt.get()), float(M1bEnt.get()), float(M1cEnt.get()), float(M2aEnt.get()), float(M2bEnt.get()),float(M2cEnt.get()), float(M3aEnt.get()), float(M3bEnt.get()), float(M3cEnt.get()))
                    SMat = SingleMatrix(Mat3D, SMPage.DIM)
            elif SMPage.DIM==4:
                if not FTest(M1aEnt.get()) or not FTest(M1bEnt.get()) or not FTest(M1cEnt.get()) or not FTest(M1dEnt.get()) or not FTest(M2aEnt.get()) or not FTest(M2bEnt.get()) or not FTest(M2cEnt.get()) or not FTest(M2dEnt.get())\
                    or not FTest(M3aEnt.get()) or not FTest(M3bEnt.get()) or not FTest(M3cEnt.get()) or not FTest(M3dEnt.get()) or not FTest(M4aEnt.get()) or not FTest(M4bEnt.get()) or not FTest(M4cEnt.get()) or not FTest(M4dEnt.get()):
                    SMat = SingleMatrix(0, 0)
                else:
                    Mat4D = (float(M1aEnt.get()), float(M1bEnt.get()), float(M1cEnt.get()), float(M1dEnt.get()), float(M2aEnt.get()), float(M2bEnt.get()), float(M2cEnt.get()), float(M2dEnt.get()),
                            float(M3aEnt.get()), float(M3bEnt.get()), float(M3cEnt.get()), float(M3dEnt.get()), float(M4aEnt.get()), float(M4bEnt.get()), float(M4cEnt.get()), float(M4dEnt.get()))
                    SMat = SingleMatrix(Mat4D, SMPage.DIM)
            else:
                SMat = SingleMatrix(0, 0)
            return SMat
        def FTest(x):
            return x.lstrip('-').lstrip('+').replace('.', '', 1).isdigit()
        def Avalue():
            if FTest(MultiEnt.get()):
                value = float(MultiEnt.get())
            else:
                value = 1
            return value
        def Bvalue():
            if FTest(PowEnt.get()):
                value = float(PowEnt.get())
            else:
                value = 1
            return value
        def SME():
            if SMPage.DIM==2:
                if not FTest(M2bEnt.get()) or not FTest(M2cEnt.get()) or not FTest(M3bEnt.get()) or not FTest(M3cEnt.get()):
                    SMat = DoubleMatrix(0,0,0,0,0)
                else:
                    Mat2D = (float(M2bEnt.get()),float(M2cEnt.get()),float(M3bEnt.get()), float(M3cEnt.get()))
                    SMat = DoubleMatrix(Mat2D,0,SMPage.DIM,Avalue(),Bvalue())
            elif SMPage.DIM==3:
                if not FTest(M1aEnt.get()) or not FTest(M1bEnt.get()) or not FTest(M1cEnt.get()) or not FTest(M2aEnt.get()) or not FTest(M2bEnt.get()) or not FTest(M2cEnt.get())\
                        or not FTest(M3aEnt.get()) or not FTest(M3bEnt.get()) or not FTest(M3cEnt.get()):
                    SMat = DoubleMatrix(0,0,0,0,0)
                else:
                    Mat3D = (float(M1aEnt.get()), float(M1bEnt.get()), float(M1cEnt.get()), float(M2aEnt.get()), float(M2bEnt.get()),float(M2cEnt.get()), float(M3aEnt.get()), float(M3bEnt.get()), float(M3cEnt.get()))
                    SMat = DoubleMatrix(Mat3D,0,SMPage.DIM,Avalue(),Bvalue())
            elif SMPage.DIM==4:
                if not FTest(M1aEnt.get()) or not FTest(M1bEnt.get()) or not FTest(M1cEnt.get()) or not FTest(M1dEnt.get()) or not FTest(M2aEnt.get()) or not FTest(M2bEnt.get()) or not FTest(M2cEnt.get()) or not FTest(M2dEnt.get())\
                    or not FTest(M3aEnt.get()) or not FTest(M3bEnt.get()) or not FTest(M3cEnt.get()) or not FTest(M3dEnt.get()) or not FTest(M4aEnt.get()) or not FTest(M4bEnt.get()) or not FTest(M4cEnt.get()) or not FTest(M4dEnt.get()):
                    SMat = DoubleMatrix(0,0,0,0,0)
                else:
                    Mat4D = (float(M1aEnt.get()), float(M1bEnt.get()), float(M1cEnt.get()), float(M1dEnt.get()), float(M2aEnt.get()), float(M2bEnt.get()), float(M2cEnt.get()), float(M2dEnt.get()),
                            float(M3aEnt.get()), float(M3bEnt.get()), float(M3cEnt.get()), float(M3dEnt.get()), float(M4aEnt.get()), float(M4bEnt.get()), float(M4cEnt.get()), float(M4dEnt.get()),)
                    SMat = DoubleMatrix(Mat4D,0,SMPage.DIM,Avalue(),Bvalue())
            else:
                SMat = DoubleMatrix(0,0,0,0,0)
            return SMat
        def RESULTlift():
            Result.lift()
            Result.update()
        def DtmAct():
            Result.configure(font=("PragmataPro", 14), anchor='n', text=SM().Determinant())
            RESULTlift()
        def InvAct():
            Result1.lift()
            Result2.lift()
            Result1.configure(font=("Lucida Console", 8), anchor='ne', text=SM().Inverse())
            Result1.update()
            Result2.configure(font=("Lucida Console", 8), anchor='nw', text=SM().InverseRight())
            Result2.update()
        def TrpAct():
            Result.configure(font=("Lucida Console", 20), anchor='n', text=SM().Transpose())
            RESULTlift()
        def ScaAct():
            Result.configure(font=("Menlo", 17), anchor='n', text=SM().Scalar())
            RESULTlift()
        def MulAct():
            Result.configure(font=("PragmataPro", 18), anchor='n', text=SME().MultiplyBy())
            RESULTlift()
        def TriAct():
            Result.configure(font=("Menlo", 15), anchor='n', text=SM().Triangular())
            RESULTlift()
        def TrcAct():
            Result.configure(font=("Lucida Console", 16), anchor='n', text=SM().Trace())
            RESULTlift()
        def LUDAct():
            Result.configure(font=("Menlo", 15), anchor='n', text=SM().LUDec())
            RESULTlift()
        def RanAct():
            Result.configure(font=("PragmataPro", 15), anchor='n', text=SM().Rank())
            RESULTlift()
        def PowAct():
            Result.configure(font=("PragmataPro", 11), anchor='n', text=SME().PowerBy())
            RESULTlift()
        def BackAct():
            BackS = pygame.mixer.Sound("DisneyBack.wav")
            BackS.play()
            pygame.mixer.music.load("MenuBG.ogg")
            pygame.mixer.music.play(-1)
            controller.show_frame("MatrixPage")
        def InfoAct():
            if SMPage.INFO == False:
                SMPage.INFO = True
                if SMPage.MUTE == False:
                    InfoS = pygame.mixer.Sound("DisneyInfoButton.wav")
                    InfoS.play()
                InfoPop.lift()
                InfoBtn.lift()
            else:
                SMPage.INFO = False
                InfoPop.lower()
        
        def ResetAct():
            if SMPage.MUTE == False:
                ClearS = pygame.mixer.Sound("DisneyReset.wav")
                ClearS.play()
            time.sleep(1)
            Ent = (M1aEnt, M1bEnt, M1cEnt, M1dEnt, M2aEnt, M2bEnt, M2cEnt, M2dEnt, M3aEnt, M3bEnt, M3cEnt, M3dEnt, M4aEnt, M4bEnt, M4cEnt, M4dEnt)
            for i in range(16):
                Ent[i].delete(0, END)
                Ent[i].lower()           
        def MuteAct():
            if SMPage.MUTE == True:
                SMPage.MUTE = False
                pygame.mixer.music.load("MickeyMouse.ogg")
                pygame.mixer.music.play(-1)
                MuteOff.lower()
            else:
                SMPage.MUTE = True
                pygame.mixer.music.stop()
                MuteOff.lift()
        def RandAct():
            if SMPage.MUTE == False:
                RandomS = pygame.mixer.Sound("DisneyRandom.wav")
                RandomS.play()
            runRandAct() 
        def runRandAct():
            time.sleep(2)
            Ent = (M1aEnt, M1bEnt, M1cEnt, M1dEnt, M2aEnt, M2bEnt, M2cEnt, M2dEnt, M3aEnt, M3bEnt, M3cEnt, M3dEnt, M4aEnt,M4bEnt, M4cEnt, M4dEnt)
            if SMPage.DIM==2:
                for i in range(5,7):
                    Ent[i].delete(0, END)
                    Ent[i].insert(1, random.randrange(-9, 10))
                for i in range(9, 11):
                    Ent[i].delete(0, END)
                    Ent[i].insert(1, random.randrange(-9, 10))
            elif SMPage.DIM==3:
                for i in range(0,3):
                    Ent[i].delete(0, END)
                    Ent[i].insert(1, random.randrange(-9, 10))
                for i in range(4, 7):
                    Ent[i].delete(0, END)
                    Ent[i].insert(1, random.randrange(-9, 10))
                for i in range(8, 11):
                    Ent[i].delete(0, END)
                    Ent[i].insert(1, random.randrange(-9, 10))
            elif SMPage.DIM==4:
                for i in range(16):
                    Ent[i].delete(0, END)
                    Ent[i].insert(1, random.randrange(-9, 10))
            else:
                SMPage.DIM=0