from tkinter import *
from TMExp import*
import pygame
import time
class TMPage(Frame):
    CT1 = 0
    CT2 = 0
    CT3 = 0
    MUTE = False
    INFO = False
    SLC2 = False
    SLC3 = False
    CHG = 0
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        pygame.mixer.init()
        TmWall = PhotoImage(file="ToyBackGround.png")
        TmWallLabel = Label(self, image=TmWall)
        TmWallLabel.image = TmWall
        TmWallLabel.place(x=-2, y=-2)
        TmWall2 = PhotoImage(file="ToyButtonBG.png")
        TsfWall = Label(self, image=TmWall2)
        TsfWall.image = TmWall2
        TsfWall.place(x=-2, y=-2)
        Back = PhotoImage(file="ToyBack.png")
        BackBtn = Button(self, image=Back, bd=0, bg='white', command=lambda: BackAct())
        BackBtn.image = Back
        BackBtn.place(x=-2, y=-2)
        Info = PhotoImage(file="ToyInfo.png")
        InfoBtn = Button(self, image=Info, bd=0, bg='white', command=lambda: InfoAct())
        InfoBtn.image = Info
        InfoBtn.place(x=48, y=-2)
        Music = PhotoImage(file="ToySoundOn.png")
        MusicBtn = Button(self, image=Music, bd=0, bg='white', command=lambda: MuteAct())
        MusicBtn.image = Music
        MusicBtn.place(x=98, y=-2)
        Mute = PhotoImage(file="ToySoundOff.png")
        MuteOff = Button(self, image=Mute, bd=0, bg='white', command=lambda: MuteAct())
        MuteOff.image = Mute
        MuteOff.place(x=98, y=-2)
        MuteOff.lower()
        Reset = PhotoImage(file="ToyReset.png")
        ResetBtn = Button(self, image=Reset, bd=0, bg='white', command=lambda: ResetAct())
        ResetBtn.image = Reset
        ResetBtn.place(x=148, y=-2)
        oneT = PhotoImage(file="oneTransform.png")
        T1Btn = Button(self, image=oneT, bd=0, bg='white', command=lambda: TsfSLC1())
        T1Btn.image = oneT
        T1Btn.place(x=1021, y=-2)
        twoT = PhotoImage(file="twoTransform.png")
        T2Btn = Button(self, image=twoT, bd=0, bg='white', command=lambda: TsfSLC2())
        T2Btn.image = twoT
        T2Btn.place(x=1097, y=-2)
        threeT = PhotoImage(file="threeTransform.png")
        T3Btn = Button(self, image=threeT, bd=0, bg='white', command=lambda: TsfSLC3())
        T3Btn.image = threeT
        T3Btn.place(x=1173, y=-2)
        Cal = PhotoImage(file="Calculate.png")
        CalBtn = Button(self, image=Cal, bd=0, bg='white', command=lambda: CalAct())
        CalBtn.image = Cal
        CalBtn.place(x=532, y=655)
        Trans = PhotoImage(file="TranslationButton.png")
        TransBtn = Button(self, image=Trans, bd=0, bg='white', command=lambda: TslAct())
        TransBtn.image = Trans
        TransBtn.place(x=163, y=147)
        Rot = PhotoImage(file="RotationButton.png")
        RotBtn = Button(self, image=Rot, bd=0, bg='white', command=lambda: RttAct())
        RotBtn.image = Rot
        RotBtn.place(x=831, y=147)
        Refl = PhotoImage(file="ReflectButton.png")
        ReflBtn = Button(self, image=Refl, bd=0, bg='white', command=lambda: RflAct())
        ReflBtn.image = Refl
        ReflBtn.place(x=163, y=355)
        Scal = PhotoImage(file="ScalingButton.png")
        ScalBtn = Button(self, image=Scal, bd=0, bg='white', command=lambda: SclAct())
        ScalBtn.image = Scal
        ScalBtn.place(x=831, y=355)
        Shear = PhotoImage(file="ShearButton.png")
        ShearBtn = Button(self, image=Shear, bd=0, bg='white', command=lambda: ShrAct())
        ShearBtn.image = Shear
        ShearBtn.place(x=498, y=265)
        Chg = PhotoImage(file="ChangeButton.png")
        ChgBtn = Button(self, image=Chg, bd=0, bg='white', command=lambda: TsfSLC1())
        ChgBtn.image = Chg
        ChgBtn.place(x=201, y=568)
        Chg2aBtn = Button(self, image=Chg, bd=0, bg='white', command=lambda: TsfSLC2a())
        Chg2aBtn.image = Chg
        Chg2aBtn.place(x=81, y=568)
        Chg2bBtn = Button(self, image=Chg, bd=0, bg='white', command=lambda: TsfSLC2b())
        Chg2bBtn.image = Chg
        Chg2bBtn.place(x=427, y=568)
        Chg3aBtn = Button(self, image=Chg, bd=0, bg='white', command=lambda: TsfSLC3a())
        Chg3aBtn.image = Chg
        Chg3aBtn.place(x=46, y=568)
        Chg3bBtn = Button(self, image=Chg, bd=0, bg='white', command=lambda: TsfSLC3b())
        Chg3bBtn.image = Chg
        Chg3bBtn.place(x=317, y=568)
        Chg3cBtn = Button(self, image=Chg, bd=0, bg='white', command=lambda: TsfSLC3c())
        Chg3cBtn.image = Chg
        Chg3cBtn.place(x=588, y=568)
        # <editor-fold desc="Description">
        RotC = PhotoImage(file="ClockwiseButton.png")
        RotCBtn = Button(self, image=RotC, bd=0, bg='white', command=lambda: RotAct())
        RotCBtn.image = RotC
        RotCBtn.place(x=201, y=78)
        RotC2aBtn = Button(self, image=RotC, bd=0, bg='white', command=lambda: Rot2aAct())
        RotC2aBtn.image = RotC
        RotC2aBtn.place(x=81, y=78)
        RotC2bBtn = Button(self, image=RotC, bd=0, bg='white', command=lambda: Rot2bAct())
        RotC2bBtn.image = RotC
        RotC2bBtn.place(x=427, y=78)
        RotC3aBtn = Button(self, image=RotC, bd=0, bg='white', command=lambda:Rot3aAct())
        RotC3aBtn.image = RotC
        RotC3aBtn.place(x=46, y=78)
        RotC3bBtn = Button(self, image=RotC, bd=0, bg='white', command=lambda: Rot3bAct())
        RotC3bBtn.image = RotC
        RotC3bBtn.place(x=317, y=78)
        RotC3cBtn = Button(self, image=RotC, bd=0, bg='white', command=lambda: Rot3cAct())
        RotC3cBtn.image = RotC
        RotC3cBtn.place(x=588, y=78)
        RotA = PhotoImage(file="AntiClockwiseButton.png")
        RotABtn = Button(self, image=RotA, bd=0, bg='white', command=lambda: RotAct())
        RotABtn.image = RotA
        RotABtn.place(x=201, y=78)
        RotA2aBtn = Button(self, image=RotA, bd=0, bg='white', command=lambda: Rot2aAct())
        RotA2aBtn.image = RotA
        RotA2aBtn.place(x=81, y=78)
        RotA2bBtn = Button(self, image=RotA, bd=0, bg='white', command=lambda: Rot2bAct())
        RotA2bBtn.image = RotA
        RotA2bBtn.place(x=427, y=78)
        RotA3aBtn = Button(self, image=RotA, bd=0, bg='white', command=lambda: Rot3aAct())
        RotA3aBtn.image = RotA
        RotA3aBtn.place(x=46, y=78)
        RotA3bBtn = Button(self, image=RotA, bd=0, bg='white', command=lambda: Rot3bAct())
        RotA3bBtn.image = RotA
        RotA3bBtn.place(x=317, y=78)
        RotA3cBtn = Button(self, image=RotA, bd=0, bg='white', command=lambda: Rot3cAct())
        RotA3cBtn.image = RotA
        RotA3cBtn.place(x=588, y=78)
        ReflX = PhotoImage(file="ReflectionXButton.png")
        ReflXBtn = Button(self, image=ReflX, bd=0, bg='white', command=lambda: RefAct())
        ReflXBtn.image = ReflX
        ReflXBtn.place(x=201, y=78)
        ReflX2aBtn = Button(self, image=ReflX, bd=0, bg='white', command=lambda: Ref2aAct())
        ReflX2aBtn.image = ReflX
        ReflX2aBtn.place(x=81, y=78)
        ReflX2bBtn = Button(self, image=ReflX, bd=0, bg='white', command=lambda: Ref2bAct())
        ReflX2bBtn.image = ReflX
        ReflX2bBtn.place(x=427, y=78)
        ReflX3aBtn = Button(self, image=ReflX, bd=0, bg='white', command=lambda: Ref3aAct())
        ReflX3aBtn.image = ReflX
        ReflX3aBtn.place(x=46, y=78)
        ReflX3bBtn = Button(self, image=ReflX, bd=0, bg='white', command=lambda: Ref3bAct())
        ReflX3bBtn.image = ReflX
        ReflX3bBtn.place(x=317, y=78)
        ReflX3cBtn = Button(self, image=ReflX, bd=0, bg='white', command=lambda: Ref3cAct())
        ReflX3cBtn.image = ReflX
        ReflX3cBtn.place(x=588, y=78)
        ReflY = PhotoImage(file="ReflectionYButton.png")
        ReflYBtn = Button(self, image=ReflY, bd=0, bg='white', command=lambda: RefAct())
        ReflYBtn.image = ReflY
        ReflYBtn.place(x=201, y=78)
        ReflY2aBtn = Button(self, image=ReflY, bd=0, bg='white', command=lambda: Ref2aAct())
        ReflY2aBtn.image = ReflY
        ReflY2aBtn.place(x=81, y=78)
        ReflY2bBtn = Button(self, image=ReflY, bd=0, bg='white', command=lambda: Ref2bAct())
        ReflY2bBtn.image = ReflY
        ReflY2bBtn.place(x=427, y=78)
        ReflY3aBtn = Button(self, image=ReflY, bd=0, bg='white', command=lambda: Ref3aAct())
        ReflY3aBtn.image = ReflY
        ReflY3aBtn.place(x=46, y=78)
        ReflY3bBtn = Button(self, image=ReflY, bd=0, bg='white', command=lambda: Ref3bAct())
        ReflY3bBtn.image = ReflY
        ReflY3bBtn.place(x=317, y=78)
        ReflY3cBtn = Button(self, image=ReflY, bd=0, bg='white', command=lambda: Ref3cAct())
        ReflY3cBtn.image = ReflY
        ReflY3cBtn.place(x=588, y=78)
        ReflO = PhotoImage(file="ReflectionOButton.png")
        ReflOBtn = Button(self, image=ReflO, bd=0, bg='white', command=lambda: RefAct())
        ReflOBtn.image = ReflO
        ReflOBtn.place(x=201, y=78)
        ReflO2aBtn = Button(self, image=ReflO, bd=0, bg='white', command=lambda: Ref2aAct())
        ReflO2aBtn.image = ReflO
        ReflO2aBtn.place(x=81, y=78)
        ReflO2bBtn = Button(self, image=ReflO, bd=0, bg='white', command=lambda: Ref2bAct())
        ReflO2bBtn.image = ReflO
        ReflO2bBtn.place(x=427, y=78)
        ReflO3aBtn = Button(self, image=ReflO, bd=0, bg='white', command=lambda: Ref3aAct())
        ReflO3aBtn.image = ReflO
        ReflO3aBtn.place(x=46, y=78)
        ReflO3bBtn = Button(self, image=ReflO, bd=0, bg='white', command=lambda: Ref3bAct())
        ReflO3bBtn.image = ReflO
        ReflO3bBtn.place(x=317, y=78)
        ReflO3cBtn = Button(self, image=ReflO, bd=0, bg='white', command=lambda: Ref3cAct())
        ReflO3cBtn.image = ReflO
        ReflO3cBtn.place(x=588, y=78)
        ShrX = PhotoImage(file="ShearXButton.png")
        ShrXBtn = Button(self, image=ShrX, bd=0, bg='white', command=lambda: SheAct())
        ShrXBtn.image = ShrX
        ShrXBtn.place(x=201, y=78)
        ShrX2aBtn = Button(self, image=ShrX, bd=0, bg='white', command=lambda: She2aAct())
        ShrX2aBtn.image = ShrX
        ShrX2aBtn.place(x=81, y=78)
        ShrX2bBtn = Button(self, image=ShrX, bd=0, bg='white', command=lambda: She2bAct())
        ShrX2bBtn.image = ShrX
        ShrX2bBtn.place(x=427, y=78)
        ShrX3aBtn = Button(self, image=ShrX, bd=0, bg='white', command=lambda: She3aAct())
        ShrX3aBtn.image = ShrX
        ShrX3aBtn.place(x=46, y=78)
        ShrX3bBtn = Button(self, image=ShrX, bd=0, bg='white', command=lambda: She3bAct())
        ShrX3bBtn.image = ShrX
        ShrX3bBtn.place(x=317, y=78)
        ShrX3cBtn = Button(self, image=ShrX, bd=0, bg='white', command=lambda: She3cAct())
        ShrX3cBtn.image = ShrX
        ShrX3cBtn.place(x=588, y=78)
        ShrY = PhotoImage(file="ShearYButton.png")
        ShrYBtn = Button(self, image=ShrY, bd=0, bg='white', command=lambda: SheAct())
        ShrYBtn.image = ShrY
        ShrYBtn.place(x=201, y=78)
        ShrY2aBtn = Button(self, image=ShrY, bd=0, bg='white', command=lambda: She2aAct())
        ShrY2aBtn.image = ShrY
        ShrY2aBtn.place(x=81, y=78)
        ShrY2bBtn = Button(self, image=ShrY, bd=0, bg='white', command=lambda: She2bAct())
        ShrY2bBtn.image = ShrY
        ShrY2bBtn.place(x=427, y=78)
        ShrY3aBtn = Button(self, image=ShrY, bd=0, bg='white', command=lambda: She3aAct())
        ShrY3aBtn.image = ShrY
        ShrY3aBtn.place(x=46, y=78)
        ShrY3bBtn = Button(self, image=ShrY, bd=0, bg='white', command=lambda: She3bAct())
        ShrY3bBtn.image = ShrY
        ShrY3bBtn.place(x=317, y=78)
        ShrY3cBtn = Button(self, image=ShrY, bd=0, bg='white', command=lambda: She3cAct())
        ShrY3cBtn.image = ShrY
        ShrY3cBtn.place(x=588, y=78)
        Next = PhotoImage(file="NextPage.png")
        NextBtn = Button(self, image=Next, bd=0, bg='#2b1b08', command=lambda: NxtAct())
        NextBtn.image = Next
        NextBtn.place(x=1166, y=667)
        Previous = PhotoImage(file="PreviousPage.png")
        PreviousBtn = Button(self, image=Previous, bd=0, bg='#2b1b08', command=lambda: PrvAct())
        PreviousBtn.image = Previous
        PreviousBtn.place(x=0, y=667)
        ToyPop1 = PhotoImage(file="ToyPop1.png")
        InfoPop1 = Label(self, image=ToyPop1)
        InfoPop1.image = ToyPop1
        InfoPop1.place(x=-2, y=-2)
        ToyPop2 = PhotoImage(file="ToyPop2.png")
        InfoPop2 = Label(self, image=ToyPop2)
        InfoPop2.image = ToyPop2
        InfoPop2.place(x=-2, y=-2)
        InfoBG = PhotoImage(file="ToyInfoBG.png")
        InfoPopBtn = Button(self, image=InfoBG, bd=0, bg='#52a6cb', command=lambda: InfoAct())
        InfoPopBtn.image = InfoBG
        InfoPopBtn.place(x=47, y=-2)
        def PoPlower():
            Low = (NextBtn, PreviousBtn, InfoPop1, InfoPop2, InfoPopBtn)
            for i in range(len(Low)):
                Low[i].lower()
        PoPlower()
        Trs = PhotoImage(file="Translation.png")
        Tsl = Label(self, image=Trs)
        Tsl.image = Trs
        Tsl.place(x=201, y=118)
        Tsl2a = Label(self, image=Trs)
        Tsl2a.image = Trs
        Tsl2a.place(x=81, y=118)
        Tsl2b = Label(self, image=Trs)
        Tsl2b.image = Trs
        Tsl2b.place(x=427, y=118)
        Tsl3a = Label(self, image=Trs)
        Tsl3a.image = Trs
        Tsl3a.place(x=46, y=118)
        Tsl3b = Label(self, image=Trs)
        Tsl3b.image = Trs
        Tsl3b.place(x=317, y=118)
        Tsl3c = Label(self, image=Trs)
        Tsl3c.image = Trs
        Tsl3c.place(x=588, y=118)
        RotC = PhotoImage(file="RotationClock.png")
        RttC = Label(self, image=RotC)
        RttC.image = RotC
        RttC.place(x=201, y=118)
        RttC2a = Label(self, image=RotC)
        RttC2a.image = RotC
        RttC2a.place(x=81, y=118)
        RttC2b = Label(self, image=RotC)
        RttC2b.image = RotC
        RttC2b.place(x=427, y=118)
        RttC3a = Label(self, image=RotC)
        RttC3a.image = RotC
        RttC3a.place(x=46, y=118)
        RttC3b = Label(self, image=RotC)
        RttC3b.image = RotC
        RttC3b.place(x=317, y=118)
        RttC3c = Label(self, image=RotC)
        RttC3c.image = Trs
        RttC3c.place(x=588, y=118)
        RotA = PhotoImage(file="RotationAnti.png")
        RttA = Label(self, image=RotA)
        RttA.image = RotA
        RttA.place(x=201, y=118)
        RttA2a = Label(self, image=RotA)
        RttA2a.image = RotA
        RttA2a.place(x=81, y=118)
        RttA2b = Label(self, image=RotA)
        RttA2b.image = RotA
        RttA2b.place(x=427, y=118)
        RttA3a = Label(self, image=RotA)
        RttA3a.image = RotA
        RttA3a.place(x=46, y=118)
        RttA3b = Label(self, image=RotA)
        RttA3b.image = RotA
        RttA3b.place(x=317, y=118)
        RttA3c = Label(self, image=RotA)
        RttA3c.image = RotA
        RttA3c.place(x=588, y=118)
        RefX = PhotoImage(file="ReflectionX.png")
        RflX = Label(self, image=RefX)
        RflX.image = RefX
        RflX.place(x=201, y=118)
        RflX2a = Label(self, image=RefX)
        RflX2a.image = RefX
        RflX2a.place(x=81, y=118)
        RflX2b = Label(self, image=RefX)
        RflX2b.image = RefX
        RflX2b.place(x=427, y=118)
        RflX3a = Label(self, image=RefX)
        RflX3a.image = RefX
        RflX3a.place(x=46, y=118)
        RflX3b = Label(self, image=RefX)
        RflX3b.image = RefX
        RflX3b.place(x=317, y=118)
        RflX3c = Label(self, image=RefX)
        RflX3c.image = RefX
        RflX3c.place(x=588, y=118)
        RefY = PhotoImage(file="ReflectionY.png")
        RflY = Label(self, image=RefY)
        RflY.image = RefY
        RflY.place(x=201, y=118)
        RflY2a = Label(self, image=RefY)
        RflY2a.image = RefY
        RflY2a.place(x=81, y=118)
        RflY2b = Label(self, image=RefY)
        RflY2b.image = RefY
        RflY2b.place(x=427, y=118)
        RflY3a = Label(self, image=RefY)
        RflY3a.image = RefY
        RflY3a.place(x=46, y=118)
        RflY3b = Label(self, image=RefY)
        RflY3b.image = RefY
        RflY3b.place(x=317, y=118)
        RflY3c = Label(self, image=RefY)
        RflY3c.image = RefY
        RflY3c.place(x=588, y=118)
        RefO = PhotoImage(file="ReflectionO.png")
        RffO = Label(self, image=RefO)
        RffO.image = RefO
        RffO.place(x=201, y=118)
        RffO2a = Label(self, image=RefO)
        RffO2a.image = RefO
        RffO2a.place(x=81, y=118)
        RffO2b = Label(self, image=RefO)
        RffO2b.image = RefO
        RffO2b.place(x=427, y=118)
        RffO3a = Label(self, image=RefO)
        RffO3a.image = RefO
        RffO3a.place(x=46, y=118)
        RffO3b = Label(self, image=RefO)
        RffO3b.image = RefO
        RffO3b.place(x=317, y=118)
        RffO3c = Label(self, image=RefO)
        RffO3c.image = RefO
        RffO3c.place(x=588, y=118)
        Scal = PhotoImage(file="Scaling.png")
        Scl = Label(self, image=Scal)
        Scl.image = Scal
        Scl.place(x=201, y=118)
        Scl2a = Label(self, image=Scal)
        Scl2a.image = Scal
        Scl2a.place(x=81, y=118)
        Scl2b = Label(self, image=Scal)
        Scl2b.image = Scal
        Scl2b.place(x=427, y=118)
        Scl3a = Label(self, image=Scal)
        Scl3a.image = Scal
        Scl3a.place(x=46, y=118)
        Scl3b = Label(self, image=Scal)
        Scl3b.image = Scal
        Scl3b.place(x=317, y=118)
        Scl3c = Label(self, image=Scal)
        Scl3c.image = Scal
        Scl3c.place(x=588, y=118)
        ShrX = PhotoImage(file="ShearingX.png")
        ShX = Label(self, image=ShrX)
        ShX.image = ShrX
        ShX.place(x=201, y=118)
        ShX2a = Label(self, image=ShrX)
        ShX2a.image = ShrX
        ShX2a.place(x=81, y=118)
        ShX2b = Label(self, image=ShrX)
        ShX2b.image = ShrX
        ShX2b.place(x=427, y=118)
        ShX3a = Label(self, image=ShrX)
        ShX3a.image = ShrX
        ShX3a.place(x=46, y=118)
        ShX3b = Label(self, image=ShrX)
        ShX3b.image = ShrX
        ShX3b.place(x=317, y=118)
        ShX3c = Label(self, image=ShrX)
        ShX3c.image = ShrX
        ShX3c.place(x=588, y=118)
        ShrY = PhotoImage(file="ShearingY.png")
        ShY = Label(self, image=ShrY)
        ShY.image = ShrY
        ShY.place(x=201, y=118)
        ShY2a = Label(self, image=ShrY)
        ShY2a.image = ShrY
        ShY2a.place(x=81, y=118)
        ShY2b = Label(self, image=ShrY)
        ShY2b.image = ShrY
        ShY2b.place(x=427, y=118)
        ShY3a = Label(self, image=ShrY)
        ShY3a.image = ShrY
        ShY3a.place(x=46, y=118)
        ShY3b = Label(self, image=ShrY)
        ShY3b.image = ShrY
        ShY3b.place(x=317, y=118)
        ShY3c = Label(self, image=ShrY)
        ShY3c.image = ShrY
        ShY3c.place(x=588, y=118)
        XY = PhotoImage(file="InputLabel.png")
        Input = Label(self, image=XY)
        Input.image = XY
        Input.place(x=575, y=118)
        Input2 = Label(self, image=XY)
        Input2.image = XY
        Input2.place(x=773, y=118)
        Input3 = Label(self, image=XY)
        Input3.image = XY
        Input3.place(x=859, y=118)
        ANS = PhotoImage(file="ResultImage.png")
        Result = Label(self, image=ANS)
        Result.image = ANS
        Result.place(x=884, y=118)
        Result2 = Label(self, image=ANS)
        Result2.image = ANS
        Result2.place(x=1019, y=118)
        Result3 = Label(self, image=ANS)
        Result3.image = ANS
        Result3.place(x=1055, y=118)
        ans = Label(self, bg='#53a4ca', anchor='c', justify="center")
        ans.place(x=924, y=171, width=74, height=129)
        ans2 = Label(self, bg='#53a4ca', anchor='c', justify="center")
        ans2.place(x=1058, y=171, width=74, height=129)
        ans3 = Label(self, bg='#53a4ca', anchor='c', justify="center")
        ans3.place(x=1095, y=171, width=74, height=129)
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
        XEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        XEnt.config(validatecommand=(XEnt.register(on_validate), '%P'))
        XEnt.place(x=652, y=163, width=50, height=50)
        XEnt2 = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        XEnt2.config(validatecommand=(XEnt2.register(on_validate), '%P'))
        XEnt2.place(x=850, y=163, width=50, height=50)
        XEnt3 = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        XEnt3.config(validatecommand=(XEnt3.register(on_validate), '%P'))
        XEnt3.place(x=936, y=163, width=50, height=50)
        YEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        YEnt.config(validatecommand=(YEnt.register(on_validate), '%P'))
        YEnt.place(x=652, y=260, width=50, height=50)
        YEnt2 = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        YEnt2.config(validatecommand=(YEnt2.register(on_validate), '%P'))
        YEnt2.place(x=850, y=260, width=50, height=50)
        YEnt3 = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        YEnt3.config(validatecommand=(YEnt3.register(on_validate), '%P'))
        YEnt3.place(x=936, y=260, width=50, height=50)
        Ent1a = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        Ent1a.config(validatecommand=(Ent1a.register(on_validate), '%P'))
        Ent1a.place(x=311, y=163, width=75, height=50)
        Ent1b = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        Ent1b.config(validatecommand=(Ent1b.register(on_validate), '%P'))
        Ent1b.place(x=311, y=260, width=75, height=50)
        Ent2a1 = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        Ent2a1.config(validatecommand=(Ent2a1.register(on_validate), '%P'))
        Ent2a1.place(x=191, y=163, width=75, height=50)
        Ent2a2 = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        Ent2a2.config(validatecommand=(Ent2a2.register(on_validate), '%P'))
        Ent2a2.place(x=191, y=260, width=75, height=50)
        Ent2b1 = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        Ent2b1.config(validatecommand=(Ent2b1.register(on_validate), '%P'))
        Ent2b1.place(x=537, y=163, width=75, height=50)
        Ent2b2 = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        Ent2b2.config(validatecommand=(Ent2b2.register(on_validate), '%P'))
        Ent2b2.place(x=537, y=260, width=75, height=50)
        Ent3a1 = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        Ent3a1.config(validatecommand=(Ent3a1.register(on_validate), '%P'))
        Ent3a1.place(x=156, y=163, width=75, height=50)
        Ent3a2 = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        Ent3a2.config(validatecommand=(Ent3a2.register(on_validate), '%P'))
        Ent3a2.place(x=156, y=260, width=75, height=50)
        Ent3b1 = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        Ent3b1.config(validatecommand=(Ent3b1.register(on_validate), '%P'))
        Ent3b1.place(x=427, y=163, width=75, height=50)
        Ent3b2 = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        Ent3b2.config(validatecommand=(Ent3b2.register(on_validate), '%P'))
        Ent3b2.place(x=427, y=260, width=75, height=50)
        Ent3c1 = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        Ent3c1.config(validatecommand=(Ent3c1.register(on_validate), '%P'))
        Ent3c1.place(x=698, y=163, width=75, height=50)
        Ent3c2 = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
        Ent3c2.config(validatecommand=(Ent3c2.register(on_validate), '%P'))
        Ent3c2.place(x=698, y=260, width=75, height=50)
        def Base():
            B = (TsfWall, TransBtn, RotBtn, ReflBtn, ScalBtn, ShearBtn, ChgBtn, Chg2aBtn, Chg2bBtn, Chg3aBtn, Chg3bBtn, Chg3cBtn, RotCBtn, RotC2aBtn, RotC2bBtn, RotC3aBtn, RotC3bBtn, RotC3cBtn,
                 RotABtn, RotA2aBtn, RotA2bBtn, RotA3aBtn, RotA3bBtn, RotA3cBtn, ReflXBtn, ReflX2aBtn, ReflX2bBtn, ReflX3aBtn, ReflX3bBtn, ReflX3cBtn, ReflYBtn, ReflY2aBtn, ReflY2bBtn, ReflY3aBtn,
                 ReflY3bBtn, ReflY3cBtn, ReflOBtn, ReflO2aBtn, ReflO2bBtn, ReflO3aBtn, ReflO3bBtn, ReflO3cBtn, ShrXBtn, ShrX2aBtn, ShrX2bBtn, ShrX3aBtn, ShrX3bBtn, ShrX3cBtn, ShrYBtn, ShrY2aBtn,
                 ShrY2bBtn, ShrY3aBtn, ShrY3bBtn, ShrY3cBtn, Tsl, Tsl2a, Tsl2b, Tsl3a, Tsl3b, Tsl3c, RttC, RttC2a, RttC2b, RttC3a, RttC3b, RttC3c, RttA, RttA2a, RttA2b, RttA3a, RttA3b, RttA3c, RflX,
                 RflX2a, RflX2b, RflX3a, RflX3b, RflX3c, RflY, RflY2a, RflY2b, RflY3a, RflY3b, RflY3c, RffO, RffO2a, RffO2b, RffO3a, RffO3b, RffO3c, Scl, Scl2a, Scl2b, Scl3a, Scl3b, Scl3c, ShX,
                 ShX2a, ShX2b, ShX3a, ShX3b, ShX3c, ShY, ShY2a, ShY2b, ShY3a, ShY3b, ShY3c, Input, Input2, Input3, Result, Result2, Result3, ans, ans2, ans3, XEnt, XEnt2, XEnt3, YEnt, YEnt2,
                 YEnt3, Ent1a, Ent1b, Ent2a1, Ent2a2, Ent2b1, Ent2b2, Ent3a1, Ent3a2, Ent3b1, Ent3b2, Ent3c1, Ent3c2)
            for i in range(len(B)):
                B[i].lower()
        Base()
        def CallTSF():
            Base()
            L = (TsfWall, TransBtn, RotBtn, ReflBtn, ScalBtn, ShearBtn)
            for i in range(len(L)):
                L[i].lift()
        def TsfSLC1():
            TMPage.CHG = 1
            CallTSF()
        def TsfSLC2():
            TMPage.SLC2 = True
            TMPage.CHG = 2
            CallTSF()
        def TsfSLC2a():
            TMPage.CHG = 21
            CallTSF()
        def TsfSLC2b():
            TMPage.CHG = 22
            CallTSF()
        def TsfSLC3():
            TMPage.SLC3 = True
            TMPage.CHG = 3
            CallTSF()
        def TsfSLC3a():
            TMPage.CHG = 31
            CallTSF()
        def TsfSLC3b():
            TMPage.CHG = 32
            CallTSF()
        def TsfSLC3c():
            TMPage.CHG = 33
            CallTSF()
        def TslAct():
            if TMPage.CHG == 1 or TMPage.CHG == 21 or TMPage.CHG == 22 or TMPage.CHG == 31 or TMPage.CHG == 32 or TMPage.CHG == 33:
                if TMPage.CHG == 31:
                    TMPage.CT1 = 31
                elif TMPage.CHG == 32:
                    TMPage.CT2 = 21
                elif TMPage.CT1 > 30 and TMPage.SLC3==True or TMPage.CHG == 33:
                    TMPage.CT3 = 1
                elif TMPage.CHG == 21:
                    TMPage.CT1 = 21
                elif TMPage.CT1 > 20 and TMPage.SLC2==True or TMPage.CHG == 22:
                    TMPage.CT2 = 1
                    TMPage.CT3 = 0
                else:
                    TMPage.CT1 = 1
                    TMPage.CT2 = 0
                    TMPage.CT3 = 0
                TMPage.SLC3 = False
                TMPage.SLC2 = False
                TSF()
            if TMPage.CHG == 2:
                if TMPage.CT1 > 30 and TMPage.SLC3==True:
                    TMPage.CT2 = 21
                else:
                    TMPage.CT1 = 21
                TsfSLC1()
            if TMPage.CHG == 3:
                TMPage.CT1 = 31
                TsfSLC2()
        def RttAct():
            if TMPage.CHG == 1 or TMPage.CHG == 21 or TMPage.CHG == 22 or TMPage.CHG == 31 or TMPage.CHG == 32 or TMPage.CHG == 33:
                if TMPage.CHG == 31:
                    TMPage.CT1 = 32
                elif TMPage.CHG == 32:
                    TMPage.CT2 = 22
                elif TMPage.CT1 > 30 and TMPage.SLC3==True or TMPage.CHG == 33:
                    TMPage.CT3 = 2
                elif TMPage.CHG == 21:
                    TMPage.CT1 = 22
                elif TMPage.CT1 > 20 and TMPage.SLC2==True or TMPage.CHG == 22:
                    TMPage.CT2 = 2
                    TMPage.CT3 = 0
                else:
                    TMPage.CT1 = 2
                    TMPage.CT2 = 0
                    TMPage.CT3 = 0
                TMPage.SLC3 = False
                TMPage.SLC2 = False
                TSF()
            if TMPage.CHG == 2:
                if TMPage.CT1 > 30 and TMPage.SLC3==True:
                    TMPage.CT2 = 22
                else:
                    TMPage.CT1 = 22
                TsfSLC1()
            if TMPage.CHG == 3:
                TMPage.CT1 = 32
                TsfSLC2()
        def RflAct():
            if TMPage.CHG == 1 or TMPage.CHG == 21 or TMPage.CHG == 22 or TMPage.CHG == 31 or TMPage.CHG == 32 or TMPage.CHG == 33:
                if TMPage.CHG == 31:
                    TMPage.CT1 = 34
                elif TMPage.CHG == 32:
                    TMPage.CT2 = 24
                elif TMPage.CT1 > 30 and TMPage.SLC3==True or TMPage.CHG == 33:
                    TMPage.CT3 = 4
                elif TMPage.CHG == 21:
                    TMPage.CT1 = 24
                elif TMPage.CT1 > 20 and TMPage.SLC2==True or TMPage.CHG == 22:
                    TMPage.CT2 = 4
                    TMPage.CT3 = 0
                else:
                    TMPage.CT1 = 4
                    TMPage.CT2 = 0
                    TMPage.CT3 = 0
                TMPage.SLC3 = False
                TMPage.SLC2 = False
                TSF()
            if TMPage.CHG == 2:
                if TMPage.CT1 > 30 and TMPage.SLC3==True:
                    TMPage.CT2 = 24
                else:
                    TMPage.CT1 = 24
                TsfSLC1()
            if TMPage.CHG == 3:
                TMPage.CT1 = 34
                TsfSLC2()
        def SclAct():
            if TMPage.CHG == 1 or TMPage.CHG == 21 or TMPage.CHG == 22 or TMPage.CHG == 31 or TMPage.CHG == 32 or TMPage.CHG == 33:
                if TMPage.CHG == 31:
                    TMPage.CT1 = 37
                elif TMPage.CHG == 32:
                    TMPage.CT2 = 27
                elif TMPage.CT1 > 30 and TMPage.SLC3==True or TMPage.CHG == 33:
                    TMPage.CT3 = 7
                elif TMPage.CHG == 21:
                    TMPage.CT1 = 27
                elif TMPage.CT1 > 20 and TMPage.SLC2==True or TMPage.CHG == 22:
                    TMPage.CT2 = 7
                    TMPage.CT3 = 0
                else:
                    TMPage.CT1 = 7
                    TMPage.CT2 = 0
                    TMPage.CT3 = 0
                TMPage.SLC3 = False
                TMPage.SLC2 = False
                TSF()
            if TMPage.CHG == 2:
                if TMPage.CT1 > 30 and TMPage.SLC3==True:
                    TMPage.CT2 = 27
                else:
                    TMPage.CT1 = 27
                TsfSLC1()
            if TMPage.CHG == 3:
                TMPage.CT1 = 37
                TsfSLC2()
        def ShrAct():
            if TMPage.CHG == 1 or TMPage.CHG == 21 or TMPage.CHG == 22 or TMPage.CHG == 31 or TMPage.CHG == 32 or TMPage.CHG == 33:
                if TMPage.CHG == 31:
                    TMPage.CT1 = 38
                elif TMPage.CHG == 32:
                    TMPage.CT2 = 28
                elif TMPage.CT1 > 30 and TMPage.SLC3==True or TMPage.CHG == 33:
                    TMPage.CT3 = 8
                elif TMPage.CHG == 21:
                    TMPage.CT1 = 28
                elif TMPage.CT1 > 20 and TMPage.SLC2==True or TMPage.CHG == 22:
                    TMPage.CT2 = 8
                    TMPage.CT3 = 0
                else:
                    TMPage.CT1 = 8
                    TMPage.CT2 = 0
                    TMPage.CT3 = 0
                TMPage.SLC3 = False
                TMPage.SLC2 = False
                TSF()
            if TMPage.CHG == 2:
                if TMPage.CT1 > 30 and TMPage.SLC3==True:
                    TMPage.CT2 = 28
                else:
                    TMPage.CT1 = 28
                TsfSLC1()
            if TMPage.CHG == 3:
                TMPage.CT1 = 38
                TsfSLC2()
        def RotAct():
            if TMPage.CT1 == 2:
                TMPage.CT1 = 3
            else:
                TMPage.CT1 = 2
            TSF()
        def Rot2aAct():
            if TMPage.CT1 == 22:
                TMPage.CT1 = 23
            else:
                TMPage.CT1 = 22
            TSF()
        def Rot2bAct():
            if TMPage.CT2 == 2:
                TMPage.CT2 = 3
            else:
                TMPage.CT2 = 2
            TSF()
        def Rot3aAct():
            if TMPage.CT1 == 32:
                TMPage.CT1 = 33
            else:
                TMPage.CT1 = 32
            TSF()
        def Rot3bAct():
            if TMPage.CT2 == 22:
                TMPage.CT2 = 23
            else:
                TMPage.CT2 = 22
            TSF()
        def Rot3cAct():
            if TMPage.CT3 == 2:
                TMPage.CT3 = 3
            else:
                TMPage.CT3 = 2
            TSF()
        def RefAct():
            if TMPage.CT1 == 4:
                TMPage.CT1 = 5
            elif TMPage.CT1 == 5:
                TMPage.CT1 = 6
            else:
                TMPage.CT1 = 4
            TSF()
        def Ref2aAct():
            if TMPage.CT1 == 24:
                TMPage.CT1 = 25
            elif TMPage.CT1 == 25:
                TMPage.CT1 = 26
            else:
                TMPage.CT1 = 24
            TSF()
        def Ref2bAct():
            if TMPage.CT2 == 4:
                TMPage.CT2 = 5
            elif TMPage.CT2 == 5:
                TMPage.CT2 = 6
            else:
                TMPage.CT2 = 4
            TSF()
        def Ref3aAct():
            if TMPage.CT1 == 34:
                TMPage.CT1 = 35
            elif TMPage.CT1 == 35:
                TMPage.CT1 = 36
            else:
                TMPage.CT1 = 34
            TSF()
        def Ref3bAct():
            if TMPage.CT2 == 24:
                TMPage.CT2 = 25
            elif TMPage.CT2 == 25:
                TMPage.CT2 = 26
            else:
                TMPage.CT2 = 24
            TSF()
        def Ref3cAct():
            if TMPage.CT3 == 4:
                TMPage.CT3 = 5
            elif TMPage.CT3 == 5:
                TMPage.CT3 = 6
            else:
                TMPage.CT3 = 4
            TSF()
        def SheAct():
            if TMPage.CT1 == 8:
                TMPage.CT1 = 9
            else:
                TMPage.CT1 = 8
            TSF()
        def She2aAct():
            if TMPage.CT1 == 28:
                TMPage.CT1 = 29
            else:
                TMPage.CT1 = 28
            TSF()
        def She2bAct():
            if TMPage.CT2 == 8:
                TMPage.CT2 = 9
            else:
                TMPage.CT2 = 8
            TSF()
        def She3aAct():
            if TMPage.CT1 == 38:
                TMPage.CT1 = 39
            else:
                TMPage.CT1 = 38
            TSF()
        def She3bAct():
            if TMPage.CT2 == 28:
                TMPage.CT2 = 29
            else:
                TMPage.CT2 = 28
            TSF()
        def She3cAct():
            if TMPage.CT3 == 8:
                TMPage.CT3 = 9
            else:
                TMPage.CT3 = 8
            TSF()
        def TSF():
            Base()
            if TMPage.CT1==1:
                L = (Input, XEnt, YEnt, Tsl, ChgBtn, Ent1a, Ent1b, Result, ans)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==2:
                L = (Input, XEnt, YEnt, RttC, RotCBtn, ChgBtn, Ent1b, Result, ans)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==3:
                L = (Input, XEnt, YEnt, RttA, RotABtn, ChgBtn, Ent1b, Result, ans)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==4:
                L = (Input, XEnt, YEnt, RflX, ReflXBtn, ChgBtn, Result, ans)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==5:
                L = (Input, XEnt, YEnt, RflY, ReflYBtn, ChgBtn, Result, ans)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1 == 6:
                L = (Input, XEnt, YEnt, RffO, ReflOBtn, ChgBtn, Result, ans)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==7:
                L = (Input, XEnt, YEnt, Scl, Ent1a, Ent1b, ChgBtn, Result, ans)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==8:
                L = (Input, XEnt, YEnt, ShX, ShrXBtn, Ent1b, ChgBtn, Result, ans)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==9:
                L = (Input, XEnt, YEnt, ShY, ShrYBtn, Ent1b, ChgBtn, Result, ans)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==21:
                L = (Tsl2a, Ent2a1, Ent2a2, Input2, XEnt2, YEnt2, Result2, ans2, Chg2aBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==22:
                L = (RttC2a, RotC2aBtn, Ent2a2, Input2, XEnt2, YEnt2, Result2, ans2, Chg2aBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==23:
                L = (RttA2a, RotA2aBtn, Ent2a2, Input2, XEnt2, YEnt2, Result2, ans2, Chg2aBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==24:
                L = (RflX2a, ReflX2aBtn, Input2, XEnt2, YEnt2, Result2, ans2, Chg2aBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==25:
                L = (RflY2a, ReflY2aBtn, Input2, XEnt2, YEnt2, Result2, ans2, Chg2aBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==26:
                L = (RffO2a, ReflO2aBtn, Input2, XEnt2, YEnt2, Result2, ans2, Chg2aBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==27:
                L = (Scl2a, Ent2a1, Ent2a2, Input2, XEnt2, YEnt2, Result2, ans2, Chg2aBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==28:
                L = (ShX2a, ShrX2aBtn, Ent2a2, Input2, XEnt2, YEnt2, Result2, ans2, Chg2aBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==29:
                L = (ShY2a, ShrY2aBtn, Ent2a2, Input2, XEnt2, YEnt2, Result2, ans2, Chg2aBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT2==1:
                L = (Tsl2b, Ent2b1, Ent2b2, Chg2bBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT2==2:
                L = (RttC2b, RotC2bBtn, Ent2b2, Chg2bBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT2==3:
                L = (RttA2b, RotA2bBtn, Ent2b2, Chg2bBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT2==4:
                L = (RflX2b, ReflX2bBtn, Chg2bBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT2==5:
                L = (RflY2b, ReflY2bBtn, Chg2bBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT2==6:
                L = (RffO2b, ReflO2bBtn, Chg2bBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT2==7:
                L = (Scl2b, Ent2b1, Ent2b2, Chg2bBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT2==8:
                L = (ShX2b, ShrX2bBtn, Ent2b2, Chg2bBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT2==9:
                L = (ShY2b, ShrY2bBtn, Ent2b2, Chg2bBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==31:
                L = (Tsl3a, Ent3a1, Ent3a2, Input3, XEnt3, YEnt3, Result3, ans3, Chg3aBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==32:
                L = (RttC3a, RotC3aBtn, Ent3a2, Input3, XEnt3, YEnt3, Result3, ans3, Chg3aBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==33:
                L = (RttA3a, RotA3aBtn, Ent3a2, Input3, XEnt3, YEnt3, Result3, ans3, Chg3aBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==34:
                L = (RflX3a, ReflX3aBtn, Input3, XEnt3, YEnt3, Result3, ans3, Chg3aBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==35:
                L = (RflY3a, ReflY3aBtn, Input3, XEnt3, YEnt3, Result3, ans3, Chg3aBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==36:
                L = (RffO3a, ReflO3aBtn, Input3, XEnt3, YEnt3, Result3, ans3, Chg3aBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==37:
                L = (Scl3a, Ent3a1, Ent3a2, Input3, XEnt3, YEnt3, Result3, ans3, Chg3aBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==38:
                L = (ShX3a, ShrX3aBtn, Ent3a2, Input3, XEnt3, YEnt3, Result3, ans3, Chg3aBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT1==39:
                L = (ShY3a, ShrY3aBtn, Ent3a2, Input3, XEnt3, YEnt3, Result3, ans3, Chg3aBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT2==21:
                L = (Tsl3b, Ent3b1, Ent3b2, Chg3bBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT2==22:
                L = (RttC3b, RotC3bBtn, Ent3b2, Chg3bBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT2==23:
                L = (RttA3b, RotA3bBtn, Ent3b2, Chg3bBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT2==24:
                L = (RflX3b, ReflX3bBtn, Chg3bBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT2==25:
                L = (RflY3b, ReflY3bBtn, Chg3bBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT2==26:
                L = (RffO3b, ReflO3bBtn, Chg3bBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT2==27:
                L = (Scl3b, Ent3b1, Ent3b2, Chg3bBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT2==28:
                L = (ShX3b, ShrX3bBtn, Ent3b2, Chg3bBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT2==29:
                L = (ShY3b, ShrY3bBtn, Ent3b2, Chg3bBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT3==1:
                L = (Tsl3c, Ent3c1, Ent3c2, Chg3cBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT3==2:
                L = (RttC3c, RotC3cBtn, Ent3c2, Chg3cBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT3==3:
                L = (RttA3c, RotA3cBtn, Ent3c2, Chg3cBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT3==4:
                L = (RflX3c, ReflX3cBtn, Chg3cBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT3==5:
                L = (RflY3c, ReflY3cBtn, Chg3cBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT3==6:
                L = (RffO3c, ReflO3cBtn, Chg3cBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT3==7:
                L = (Scl3c, Ent3c1, Ent3c2, Chg3cBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT3==8:
                L = (ShX3c, ShrX3cBtn, Ent3c2, Chg3cBtn)
                for i in range(len(L)):
                    L[i].lift()
            if TMPage.CT3==9:
                L = (ShY3c, ShrY3cBtn, Ent3c2, Chg3cBtn)
                for i in range(len(L)):
                    L[i].lift()
            ans3.configure(font=("Segoe Print", 13), anchor='c', text="")
            ans3.update()
            ans2.configure(font=("Segoe Print", 13), anchor='c', text="")
            ans2.update()
            ans.configure(font=("Segoe Print", 13), anchor='c', text="")
            ans.update()
            Ent = ( XEnt, XEnt2, XEnt3, YEnt, YEnt2, YEnt3, Ent1a, Ent1b, Ent2a1, Ent2a2, Ent2b1, Ent2b2, Ent3a1, Ent3a2, Ent3b1, Ent3b2, Ent3c1, Ent3c2)
            for i in range(len(Ent)):
                Ent[i].delete(0, END)
        def CalAct():
            try:
                if TMPage.CT1>30 and TMPage.CT2>20 and TMPage.CT3>0:
                    XY = (float(XEnt3.get()), float(YEnt3.get()), 1)
                    T3 = TMPage.CT3
                    T2 = TMPage.CT2 % 10
                    T1 = TMPage.CT1 % 10
                elif TMPage.CT1>20 and TMPage.CT2<20:
                    XY = (float(XEnt2.get()), float(YEnt2.get()), 1)
                    T3 = 0
                    T2 = TMPage.CT2
                    T1 = TMPage.CT1 % 10
                else:
                    XY = (float(XEnt.get()), float(YEnt.get()), 1)
                    T3 = 0
                    T2 = 0
                    T1 = TMPage.CT1
                if TMPage.CT1 == 1 or TMPage.CT1 == 7:
                    V1 = (float(Ent1a.get()), float(Ent1b.get()))
                elif TMPage.CT1 == 2 or TMPage.CT1 == 3 or TMPage.CT1 == 8 or TMPage.CT1 == 9:
                    V1 = float(Ent1b.get())
                elif TMPage.CT1 == 21 or TMPage.CT1 == 27:
                    V1 = (float(Ent2a1.get()), float(Ent2a2.get()))
                elif TMPage.CT1 == 22 or TMPage.CT1 == 23 or TMPage.CT1 == 28 or TMPage.CT1 == 29:
                    V1 = float(Ent2a2.get())
                elif TMPage.CT1 == 31 or TMPage.CT1 == 37:
                    V1 = (float(Ent3a1.get()), float(Ent3a2.get()))
                elif TMPage.CT1 == 32 or TMPage.CT1 == 33 or TMPage.CT1 == 38 or TMPage.CT1 == 39:
                    V1 = float(Ent3a2.get())
                else:
                    V1 = 0
                if TMPage.CT2 == 1 or TMPage.CT2 == 7:
                    V2 = (float(Ent2b1.get()), float(Ent2b2.get()))
                elif TMPage.CT2 == 2 or TMPage.CT2 == 3 or TMPage.CT2 == 8 or TMPage.CT2 == 9:
                    V2 = float(Ent2b2.get())
                elif TMPage.CT2 == 21 or TMPage.CT2 == 27:
                    V2 = (float(Ent3b1.get()), float(Ent3b2.get()))
                elif TMPage.CT2 == 22 or TMPage.CT2 == 23 or TMPage.CT2 == 28 or TMPage.CT2 == 29:
                    V2 = float(Ent3b2.get())
                else:
                    V2 = 0
                if TMPage.CT3 == 1 or TMPage.CT3 == 7:
                    V3 = (float(Ent3c1.get()), float(Ent3c2.get()))
                elif TMPage.CT3 == 2 or TMPage.CT3 == 3 or TMPage.CT3 == 8 or TMPage.CT3 == 9:
                    V3 = float(Ent3c2.get())
                else:
                    V3 = 0
                T = Transformation(XY, T1, T2, T3, V1, V2, V3)
            except:
                T = Transformation(0, 0, 0, 0, 0, 0, 0)
            if TMPage.CT3>0:
                ans3.configure(font=("Segoe Print", 12), anchor='c', text=T.CT3())
                ans3.update()
            elif TMPage.CT2>0:
                ans2.configure(font=("Segoe Print", 12), anchor='c', text=T.CT2())
                ans2.update()
            else:
                ans.configure(font=("Segoe Print", 12), anchor='c', text=T.CT1())
                ans.update()
        def BackAct():
            BackS = pygame.mixer.Sound("ToyBack.wav")
            BackS.play()
            pygame.mixer.music.load("MenuBG.ogg")
            pygame.mixer.music.play(-1)
            controller.show_frame("MatrixPage")
        def InfoAct():
            if TMPage.INFO == False:
                TMPage.INFO = True
                if TMPage.MUTE == False:
                    InfoS = pygame.mixer.Sound("ToyInfo.wav")
                    InfoS.play()
                InfoPop1.lift()
                NextBtn.lift()
                InfoPopBtn.lift()
            else:
                TMPage.INFO = False
                PoPlower()
        def NxtAct():
            InfoPop2.lift()
            InfoPopBtn.lift()
            PreviousBtn.lift()
        def PrvAct():
            InfoPop1.lift()
            InfoPopBtn.lift()
            NextBtn.lift()
        def ResetAct():
            if TMPage.MUTE == False:
                ClearS = pygame.mixer.Sound("ToyReset.wav")
                ClearS.play()
            time.sleep(2)
            Base()     
        def MuteAct():
            if TMPage.MUTE == True:
                TMPage.MUTE = False
                pygame.mixer.music.load("ToyBackground.ogg")
                pygame.mixer.music.play(-1)
                MuteOff.lower()
            else:
                TMPage.MUTE = True
                pygame.mixer.music.stop()
                MuteOff.lift()