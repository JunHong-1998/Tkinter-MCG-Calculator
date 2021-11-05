from tkinter import *
from EMExp import *
import time
import pygame

class EMPage(Frame):
    MUTE = False
    INFO = False
    CHECK = False
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        pygame.mixer.init()
        BackS = pygame.mixer.Sound("EUBack.wav")
        ClearS = pygame.mixer.Sound("EUClear.wav")
        CalcS = pygame.mixer.Sound("EUCalc.wav")
        InfoS = pygame.mixer.Sound("EUInfo.wav")
        RandomS = pygame.mixer.Sound("EURandom.wav")
        GraphS = pygame.mixer.Sound("EUGraph.wav")
        EuBG = PhotoImage(file="EuBackground.png")
        EuLabel = Label(self, image=EuBG)
        EuLabel.image = EuBG
        EuLabel.place(x=-2, y=-2)
        info = PhotoImage(file='EuInfoPop.png')
        InfoPop = Label(self, image=info)
        InfoPop.image = info
        InfoPop.place(x=-2, y=-2)
        InfoPop.lower()

        Back = PhotoImage(file="EuBack.png")
        BackBtn = Button(self, image=Back, bd=0, bg='#c7e8d5', command=lambda: BackAct())
        BackBtn.image = Back
        BackBtn.place(x=-2, y=-2)
        Info = PhotoImage(file="EuInfo.png")
        InfoBtn = Button(self, image=Info, bd=0, bg='#c7e8d5', command=lambda: InfoAct())
        InfoBtn.image = Info
        InfoBtn.place(x=48, y=-2)
        Sound = PhotoImage(file="EuSoundOn.png")
        SoundBtn = Button(self, image=Sound, bd=0, bg='#c7e8d5', command=lambda: MuteAct())
        SoundBtn.image = Sound
        SoundBtn.place(x=98, y=-2)
        SoundOff = PhotoImage(file="EuSoundOff.png")
        MuteBtn = Button(self, image=SoundOff, bd=0, bg='#c7e8d5', command=lambda: MuteAct())
        MuteBtn.image = SoundOff
        MuteBtn.place(x=98, y=-2)
        MuteBtn.lower()
        Clear = PhotoImage(file="EuClear.png")
        ClrBtn = Button(self, image=Clear, bd=0, bg="#c7e8d5", command=lambda: ClrAct())
        ClrBtn.image = Clear
        ClrBtn.place(x=198, y=-2)
        Random = PhotoImage(file="EuRandom.png")
        RandBtn = Button(self, image=Random, bd=0, bg="#c7e8d5", command=lambda: RandAct())
        RandBtn.image = Random
        RandBtn.place(x=148, y=-2)
        Calc = PhotoImage(file="EuCalc.png")
        CalcBtn = Button(self, image=Calc, bd=0, bg="#141809", command=lambda: CalcAct())
        CalcBtn.image = Calc
        CalcBtn.place(x=108, y=598)
        Graph = PhotoImage(file="EuGraph.png")
        GraphBtn = Button(self, image=Graph, bd=0, bg="#141809", command=lambda: GraphAct())
        GraphBtn.image = Graph
        GraphBtn.place(x=380, y=598)
        Check = PhotoImage(file="EuCheck.png")
        CheckBtn = Button(self, image=Check, bd=0, bg='black', command=lambda: CheckAct())
        CheckBtn.image = Check
        CheckBtn.place(x=371, y=276)
        EuYesMsg = PhotoImage(file="EuYes.png")
        YesMsg = Label(self, image=EuYesMsg, bg='black')
        YesMsg.image = EuYesMsg
        YesMsg.place(x=491, y=209)
        EuNoMsg = PhotoImage(file="EuNo.png")
        NoMsg = Label(self, image=EuNoMsg, bg='black')
        NoMsg.image = EuNoMsg
        NoMsg.place(x=491, y=209)

        xlabel = Label(self, bg='#f7e5b7', anchor='e', justify="right")
        xlabel.place(x=938, y=59, width=93, height=640)
        fxlabel = Label(self, bg='#f7e5b7', anchor='e', justify="right")
        fxlabel.place(x=1035, y=59, width=162, height=640)

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
        def validateFunc(string):
            regex = re.compile(r"[\+\-\(\)\^\/\*abcegilnoqrstxy0-9.]*$")
            result = regex.match(string)
            return (string == ""
                    or (result is not None
                        and result.group(0) != ""))
        def on_validateFunc(P):
            return validateFunc(P)
        FuncEnt = Entry(self, background="#fdc689", font="-family {Arial} -size 20", justify="center", validate="key")
        FuncEnt.config(validatecommand=(FuncEnt.register(on_validateFunc), '%P'))
        FuncEnt.place(x=232, y=211, width=250, height=50)
        HEnt = Entry(self, background="#fdc689", font="-family {Arial} -size 20", justify="center", validate="key")
        HEnt.config(validatecommand=(HEnt.register(on_validate), '%P'))
        HEnt.place(x=232, y=303, width=100, height=50)
        x0Ent = Entry(self, background="#fdc689", font="-family {Arial} -size 20", justify="center", validate="key")
        x0Ent.config(validatecommand=(x0Ent.register(on_validate), '%P'))
        x0Ent.place(x=93, y=395, width=75, height=50)
        y0Ent = Entry(self, background="#fdc689", font="-family {Arial} -size 20", justify="center", validate="key")
        y0Ent.config(validatecommand=(y0Ent.register(on_validate), '%P'))
        y0Ent.place(x=232, y=395, width=75, height=50)
        xfEnt = Entry(self, background="#fdc689", font="-family {Arial} -size 20", justify="center", validate="key")
        xfEnt.config(validatecommand=(xfEnt.register(on_validate), '%P'))
        xfEnt.place(x=232, y=487, width=75, height=50)
        def InfoLower():
            I = (CheckBtn, YesMsg, NoMsg)
            for i in range(len(I)):
                I[i].lower()
        InfoLower()
        def FTest(x):
            return x.lstrip('-').lstrip('+').replace('.', '', 1).isdigit()
        def em():
            if FuncEnt.get()=="" or not FTest(HEnt.get()) or not FTest(x0Ent.get()) or not FTest(y0Ent.get()) or not FTest(xfEnt.get()):
                Func = FuncEnt.get()
                if not EMPage.CHECK:
                    Func = "error"
                H = 0
                x0 = 0
                y0 = 0
                xf = 0
            else:
                Func = FuncEnt.get()
                H = float(HEnt.get())
                x0 = float(x0Ent.get())  # nt necessary float
                y0 = float(y0Ent.get())  # nt necessary float
                xf = float(xfEnt.get())
            em = EM(Func, H, x0, y0, xf)

            return em
        def CalcAct():
            if em().Error():
                xlabel.config(font=("PragmataPro", 13), anchor='ne', text="")
                fxlabel.config(font=("PragmataPro", 14), anchor='c', justify='c', text="Invalid Input\n\nPlz refer to \n\nINSTRUCTION\n\nMath ERROR")
                xlabel.update()
                fxlabel.update()
            else:
                if EMPage.MUTE == False:
                    CalcS.play()
                xlabel.config(font=("PragmataPro", 13), anchor='ne', text=em().xValue())
                fxlabel.config(font=("PragmataPro", 13), anchor='ne', text=em().yValue())
                xlabel.update()
                fxlabel.update()
        def GraphAct():
            if not em().Error():
                if EMPage.MUTE == False:
                    GraphS.play()
                    time.sleep(1.5)
                em().Graph()
        def BackAct():
            BackS.play()
            pygame.mixer.music.load("MenuBG.ogg")
            pygame.mixer.music.play(-1)
            em().CloseGraph()
            controller.show_frame("MenuPage")
        def RandAct():
            if EMPage.MUTE == False:
                RandomS.play()
            time.sleep(1)
            FuncEnt.delete(0, END)
            FuncEnt.insert(1, "sin(x)-y")
            HEnt.delete(0, END)
            HEnt.insert(1, "0.1")
            x0Ent.delete(0, END)
            x0Ent.insert(1, "0")
            y0Ent.delete(0, END)
            y0Ent.insert(1, "2")
            xfEnt.delete(0, END)
            xfEnt.insert(1, "10")
        def MuteAct():
            if EMPage.MUTE == True:
                EMPage.MUTE = False
                pygame.mixer.music.load("EUBg.ogg")
                pygame.mixer.music.play(-1)
                MuteBtn.lower()
            else:
                EMPage.MUTE = True
                pygame.mixer.music.stop()
                MuteBtn.lift()
        def ClrAct():
            if EMPage.MUTE == False:
                ClearS.play()
            time.sleep(1)
            Ent = (FuncEnt, HEnt, x0Ent, y0Ent, xfEnt)
            for i in range(len(Ent)):
                Ent[i].delete(0, END)
        def InfoAct():
            if EMPage.INFO == False:
                EMPage.INFO = True
                if EMPage.MUTE == False:
                    InfoS.play()
                InfoPop.lift()
                InfoBtn.lift()
                FuncEnt.lift()
                CheckBtn.lift()
            else:
                EMPage.INFO = False
                InfoPop.lower()
                InfoLower()
        def CheckAct():
            EMPage.CHECK = True
            if em().FuncError():
                YesMsg.lower()
                NoMsg.lift()
            else:
                NoMsg.lower()
                YesMsg.lift()
            EMPage.CHECK = False