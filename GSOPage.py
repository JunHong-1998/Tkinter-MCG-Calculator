from tkinter import*
from GSOExp import*
import random
import time
import pygame

class GSOPage(Frame):
    EntV1 = False
    EntV2 = False
    EntV3 = False
    EntV4 = False
    EntV5 = False
    DIM = 0
    MUTE = False
    INFO = False
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        pygame.mixer.init()
        BackS = pygame.mixer.Sound("GSOBack.wav")
        pygame.mixer.Sound.set_volume(BackS, 0.5)
        ClearS = pygame.mixer.Sound("GSOClear.wav")
        pygame.mixer.Sound.set_volume(ClearS, 0.7)
        ErrorS = pygame.mixer.Sound("GSOError.wav")
        InfoS = pygame.mixer.Sound("GSOInfo.wav")
        pygame.mixer.Sound.set_volume(InfoS, 0.7)
        RandomS = pygame.mixer.Sound("GSORandom.wav")
        pygame.mixer.Sound.set_volume(RandomS, 0.7)
        GSOV1S = pygame.mixer.Sound("GSOV1.wav")
        pygame.mixer.Sound.set_volume(GSOV1S, 0.85)
        GSOV2S = pygame.mixer.Sound("GSOV2.wav")
        pygame.mixer.Sound.set_volume(GSOV2S, 0.5)
        GSOV3S = pygame.mixer.Sound("GSOV3.wav")
        pygame.mixer.Sound.set_volume(GSOV3S, 0.5)
        GSOV4S = pygame.mixer.Sound("GSOV4.wav")
        pygame.mixer.Sound.set_volume(GSOV4S, 0.5)
        GSOV5S = pygame.mixer.Sound("GSOV5.wav")
        pygame.mixer.Sound.set_volume(GSOV5S, 0.5)
        GramBG = PhotoImage(file="GramBG.png")
        D2Label = Label(self, image=GramBG)
        D2Label.image = GramBG
        D2Label.place(x=-2, y=-2)
        info = PhotoImage(file='GSOInfoPop.png')
        InfoPop = Label(self, image=info)
        InfoPop.image = info
        InfoPop.place(x=-2, y=-2)
        InfoPop.lower()
        Back = PhotoImage(file="GSOBack.png")
        BackBtn = Button(self, image=Back, bd=0, bg='black', command=lambda: BackAct())
        BackBtn.image = Back
        BackBtn.place(x=0, y=0)
        Info = PhotoImage(file="GSOInfo.png")
        InfoBtn = Button(self, image=Info, bd=0, bg='black', command=lambda: InfoAct())
        InfoBtn.image = Info
        InfoBtn.place(x=50, y=0)
        Sound = PhotoImage(file="GSOSoundOn.png")
        SoundBtn = Button(self, image=Sound, bd=0, bg='black', command=lambda: MuteAct())
        SoundBtn.image = Sound
        SoundBtn.place(x=100, y=0)
        SoundOff = PhotoImage(file="GSOSoundOff.png")
        MuteBtn = Button(self, image=SoundOff, bd=0, bg='black', command=lambda: MuteAct())
        MuteBtn.image = SoundOff
        MuteBtn.place(x=100, y=0)
        MuteBtn.lower()
        Clear = PhotoImage(file="GSOClear.png")
        ClrBtn = Button(self, image=Clear, bd=0, bg="black", command=lambda: ClrAct())
        ClrBtn.image = Clear
        ClrBtn.place(x=150, y=0)
        Random = PhotoImage(file="GSORandom.png")
        RandBtn = Button(self, image=Random, bd=0, bg="black", command=lambda: RandAct())
        RandBtn.image = Random
        RandBtn.place(x=200, y=0)
        V1 = PhotoImage(file="Vector1Button.png")
        V1Btn = Button(self, image=V1, bd=0, bg='green', command=lambda: V1Act())
        V1Btn.image = V1
        V1Btn.place(x=20, y=185)
        V2 = PhotoImage(file="Vector2Button.png")
        V2Btn = Button(self, image=V2, bd=0, bg='green', command=lambda: V2Act())
        V2Btn.image = V2
        V2Btn.place(x=20, y=253)
        V3 = PhotoImage(file="Vector3Button.png")
        V3Btn = Button(self, image=V3, bd=0, bg='green', command=lambda: V3Act())
        V3Btn.image = V3
        V3Btn.place(x=20, y=321)
        V4 = PhotoImage(file="Vector4Button.png")
        V4Btn = Button(self, image=V4, bd=0, bg='green', command=lambda: V4Act())
        V4Btn.image = V4
        V4Btn.place(x=20, y=389)
        V5 = PhotoImage(file="Vector5Button.png")
        V5Btn = Button(self, image=V5, bd=0, bg='green', command=lambda: V5Act())
        V5Btn.image = V5
        V5Btn.place(x=20, y=457)
        Calc = PhotoImage(file="GSOCalculate.png")
        CalcBtn = Button(self, image=Calc, bd=0, bg="#727676", command=lambda: CalcAct())
        CalcBtn.image = Calc
        CalcBtn.place(x=737, y=9)

        ErrorMsg = PhotoImage(file="ErrorMessage.png")
        ErMsg = Label(self, image=ErrorMsg, bg='green')
        ErMsg.image = ErrorMsg
        ErMsg.place(x=46, y=552)
        u1 = Label(self, bg='#252630', anchor='w', justify="left")
        u1.place(x=738, y=62, width=500, height=28)
        e1 = Label(self, bg='#252630', anchor='w', justify="left")
        e1.place(x=738, y=92, width=500, height=28)
        u2 = Label(self, bg='#252630', anchor='w', justify="left")
        u2.place(x=738, y=122, width=500, height=73)
        e2 = Label(self, bg='#252630', anchor='w', justify="left")
        e2.place(x=738, y=197, width=500, height=28)
        u3 = Label(self, bg='#252630', anchor='w', justify="left")
        u3.place(x=738, y=227, width=500, height=98)
        e3 = Label(self, bg='#252630', anchor='w', justify="left")
        e3.place(x=738, y=327, width=500, height=28)
        u4 = Label(self, bg='#252630', anchor='w', justify="left")
        u4.place(x=738, y=357, width=500, height=98)
        e4 = Label(self, bg='#252630', anchor='w', justify="left")
        e4.place(x=738, y=457, width=500, height=28)
        u5 = Label(self, bg='#252630', anchor='w', justify="left")
        u5.place(x=738, y=487, width=500, height=141)
        e5 = Label(self, bg='#252630', anchor='w', justify="left")
        e5.place(x=738, y=630, width=500, height=28)
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
        V1U1Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V1U1Ent.config(validatecommand=(V1U1Ent.register(on_validate), '%P'))
        V1U1Ent.place(x=154, y=185, width=50, height=50)
        V1U2Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V1U2Ent.config(validatecommand=(V1U2Ent.register(on_validate), '%P'))
        V1U2Ent.place(x=221, y=185, width=50, height=50)
        V1U3Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V1U3Ent.config(validatecommand=(V1U3Ent.register(on_validate), '%P'))
        V1U3Ent.place(x=288, y=185, width=50, height=50)
        V1U4Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V1U4Ent.config(validatecommand=(V1U4Ent.register(on_validate), '%P'))
        V1U4Ent.place(x=355, y=185, width=50, height=50)
        V1U5Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V1U5Ent.config(validatecommand=(V1U5Ent.register(on_validate), '%P'))
        V1U5Ent.place(x=422, y=185, width=50, height=50)
        V2U1Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V2U1Ent.config(validatecommand=(V2U1Ent.register(on_validate), '%P'))
        V2U1Ent.place(x=154, y=253, width=50, height=50)
        V2U2Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V2U2Ent.config(validatecommand=(V2U2Ent.register(on_validate), '%P'))
        V2U2Ent.place(x=221, y=253, width=50, height=50)
        V2U3Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V2U3Ent.config(validatecommand=(V2U3Ent.register(on_validate), '%P'))
        V2U3Ent.place(x=288, y=253, width=50, height=50)
        V2U4Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V2U4Ent.config(validatecommand=(V2U4Ent.register(on_validate), '%P'))
        V2U4Ent.place(x=355, y=253, width=50, height=50)
        V2U5Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V2U5Ent.config(validatecommand=(V2U5Ent.register(on_validate), '%P'))
        V2U5Ent.place(x=422, y=253, width=50, height=50)
        V3U1Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V3U1Ent.config(validatecommand=(V3U1Ent.register(on_validate), '%P'))
        V3U1Ent.place(x=154, y=321, width=50, height=50)
        V3U2Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V3U2Ent.config(validatecommand=(V3U2Ent.register(on_validate), '%P'))
        V3U2Ent.place(x=221, y=321, width=50, height=50)
        V3U3Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V3U3Ent.config(validatecommand=(V3U3Ent.register(on_validate), '%P'))
        V3U3Ent.place(x=288, y=321, width=50, height=50)
        V3U4Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V3U4Ent.config(validatecommand=(V3U4Ent.register(on_validate), '%P'))
        V3U4Ent.place(x=355, y=321, width=50, height=50)
        V3U5Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V3U5Ent.config(validatecommand=(V3U5Ent.register(on_validate), '%P'))
        V3U5Ent.place(x=422, y=321, width=50, height=50)
        V4U1Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V4U1Ent.config(validatecommand=(V4U1Ent.register(on_validate), '%P'))
        V4U1Ent.place(x=154, y=389, width=50, height=50)
        V4U2Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V4U2Ent.config(validatecommand=(V4U2Ent.register(on_validate), '%P'))
        V4U2Ent.place(x=221, y=389, width=50, height=50)
        V4U3Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V4U3Ent.config(validatecommand=(V4U3Ent.register(on_validate), '%P'))
        V4U3Ent.place(x=288, y=389, width=50, height=50)
        V4U4Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V4U4Ent.config(validatecommand=(V4U4Ent.register(on_validate), '%P'))
        V4U4Ent.place(x=355, y=389, width=50, height=50)
        V4U5Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V4U5Ent.config(validatecommand=(V4U5Ent.register(on_validate), '%P'))
        V4U5Ent.place(x=422, y=389, width=50, height=50)
        V5U1Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V5U1Ent.config(validatecommand=(V5U1Ent.register(on_validate), '%P'))
        V5U1Ent.place(x=154, y=457, width=50, height=50)
        V5U2Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V5U2Ent.config(validatecommand=(V5U2Ent.register(on_validate), '%P'))
        V5U2Ent.place(x=221, y=457, width=50, height=50)
        V5U3Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V5U3Ent.config(validatecommand=(V5U3Ent.register(on_validate), '%P'))
        V5U3Ent.place(x=288, y=457, width=50, height=50)
        V5U4Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V5U4Ent.config(validatecommand=(V5U4Ent.register(on_validate), '%P'))
        V5U4Ent.place(x=355, y=457, width=50, height=50)
        V5U5Ent = Entry(self, background="#c8ffd5", font="-family {Arial} -size 20", justify="center", validate="key")
        V5U5Ent.config(validatecommand=(V5U5Ent.register(on_validate), '%P'))
        V5U5Ent.place(x=422, y=457, width=50, height=50)
        V1 = (V1U1Ent, V1U2Ent, V1U3Ent, V1U4Ent, V1U5Ent)
        V2 = (V2U1Ent, V2U2Ent, V2U3Ent, V2U4Ent, V2U5Ent)
        V3 = (V3U1Ent, V3U2Ent, V3U3Ent, V3U4Ent, V3U5Ent)
        V4 = (V4U1Ent, V4U2Ent, V4U3Ent, V4U4Ent, V4U5Ent)
        V5 = (V5U1Ent, V5U2Ent, V5U3Ent, V5U4Ent, V5U5Ent)
        def LIFTtool(L, n):
            for i in range(n):
                L[i].lift()
        def LOWERtool(L, n):
            for i in range(n):
                L[i].lower()
        def APPENDtool(A, n):
            B = []
            for i in range(n):
                B.append(float(A[i].get()))
            check = sum(B)
            if check==0:
                B = 0
            return B
        def LOWER():
            L = (ErMsg, V1U1Ent, V1U2Ent, V1U3Ent, V1U4Ent, V1U5Ent, V2U1Ent, V2U2Ent, V2U3Ent, V2U4Ent, V2U5Ent, V3U1Ent, V3U2Ent, V3U3Ent, V3U4Ent, V3U5Ent, V4U1Ent, V4U2Ent, V4U3Ent, V4U4Ent, V4U5Ent,
                 V5U1Ent, V5U2Ent, V5U3Ent, V5U4Ent, V5U5Ent, u1, e1, u2, e2, u3, e3, u4, e4, u5, e5)
            LOWERtool(L,len(L))
        LOWER()

        def V1Act():
            if not GSOPage.EntV1:
                GSOV1S.play()
                LIFTtool(V1,len(V1))
                GSOPage.EntV1 = True
            elif not GSOPage.EntV2 and not GSOPage.EntV3 and not GSOPage.EntV4 and not GSOPage.EntV5:
                LOWERtool(V1,len(V1))
                GSOPage.EntV1 = False
        def V2Act():
            if GSOPage.EntV1 and not GSOPage.EntV2:
                GSOV2S.play()
                LIFTtool(V2,len(V2))
                GSOPage.EntV2 = True
            elif not GSOPage.EntV3 and not GSOPage.EntV4 and not GSOPage.EntV5:
                LOWERtool(V2,len(V2))
                GSOPage.EntV2 = False
        def V3Act():
            if GSOPage.EntV1 and GSOPage.EntV2 and not GSOPage.EntV3:
                GSOV3S.play()
                LIFTtool(V3,len(V3))
                GSOPage.EntV3 = True
            elif not GSOPage.EntV4 and not GSOPage.EntV5:
                LOWERtool(V3,len(V3))
                GSOPage.EntV3 = False
        def V4Act():
            if GSOPage.EntV1 and GSOPage.EntV2 and GSOPage.EntV3 and not GSOPage.EntV4:
                GSOV4S.play()
                LIFTtool(V4,len(V4))
                GSOPage.EntV4 = True
            elif not GSOPage.EntV5:
                LOWERtool(V4,len(V4))
                GSOPage.EntV4 = False
        def V5Act():
            if GSOPage.EntV1 and GSOPage.EntV2 and GSOPage.EntV3 and GSOPage.EntV4 and not GSOPage.EntV5:
                GSOV5S.play()
                LIFTtool(V5,len(V5))
                GSOPage.EntV5 = True
            elif GSOPage.EntV1 and GSOPage.EntV2 and GSOPage.EntV3 and GSOPage.EntV4 and GSOPage.EntV5:
                LOWERtool(V5,len(V5))
                GSOPage.EntV5 = False
        def FTest(x):
            return x.lstrip('-').lstrip('+').replace('.', '', 1).isdigit()
        def DimError():
            error = False
            if GSOPage.EntV1:
                if GSOPage.EntV1 and FTest(V1U1Ent.get()) and FTest(V1U2Ent.get()) and FTest(V1U3Ent.get()) and FTest(V1U4Ent.get()) and FTest(V1U5Ent.get()):
                    GSOPage.DIM = 5
                    if GSOPage.EntV2:
                        if not FTest(V2U1Ent.get()) or not FTest(V2U2Ent.get()) or not FTest(V2U3Ent.get()) or not FTest(V2U4Ent.get()) or not FTest(V2U5Ent.get()):
                            error = True
                    if GSOPage.EntV3:
                        if not FTest(V3U1Ent.get()) or not FTest(V3U2Ent.get()) or not FTest(V3U3Ent.get()) or not FTest(V3U4Ent.get()) or not FTest(V3U5Ent.get()):
                            error = True
                    if GSOPage.EntV4:
                        if not FTest(V4U1Ent.get()) or not FTest(V4U2Ent.get()) or not FTest(V4U3Ent.get()) or not FTest(V4U4Ent.get()) or not FTest(V4U5Ent.get()):
                            error = True
                    if GSOPage.EntV5:
                        if not FTest(V5U1Ent.get()) or not FTest(V5U2Ent.get()) or not FTest(V5U3Ent.get()) or not FTest(V5U4Ent.get()) or not FTest(V5U5Ent.get()):
                            error = True
                elif GSOPage.EntV1 and FTest(V1U1Ent.get()) and FTest(V1U2Ent.get()) and FTest(V1U3Ent.get()) and FTest(V1U4Ent.get()):
                    GSOPage.DIM = 4
                    if GSOPage.EntV2:
                        if not FTest(V2U1Ent.get()) or not FTest(V2U2Ent.get()) or not FTest(V2U3Ent.get()) or not FTest(V2U4Ent.get()) or FTest(V2U5Ent.get()):
                            error = True
                    if GSOPage.EntV3:
                        if not FTest(V2U1Ent.get()) or not FTest(V2U2Ent.get()) or not FTest(V2U3Ent.get()) or not FTest(V2U4Ent.get()) or FTest(V3U5Ent.get()):
                            error = True
                    if GSOPage.EntV4:
                        if not FTest(V4U1Ent.get()) or not FTest(V4U2Ent.get()) or not FTest(V4U3Ent.get()) or not FTest(V4U4Ent.get()) or FTest(V4U5Ent.get()):
                            error = True
                    if GSOPage.EntV5:
                        if not FTest(V5U1Ent.get()) or not FTest(V5U2Ent.get()) or not FTest(V5U3Ent.get()) or not FTest(V5U4Ent.get()) or FTest(V5U5Ent.get()):
                            error = True
                elif GSOPage.EntV1 and FTest(V1U1Ent.get()) and FTest(V1U2Ent.get()) and FTest(V1U3Ent.get()):
                    GSOPage.DIM = 3
                    if GSOPage.EntV2:
                        if not FTest(V2U1Ent.get()) or not FTest(V2U2Ent.get()) or not FTest(V2U3Ent.get()) or FTest(V2U4Ent.get()) or FTest(V2U5Ent.get()):
                            error = True
                    if GSOPage.EntV3:
                        if not FTest(V3U1Ent.get()) or not FTest(V3U2Ent.get()) or not FTest(V3U3Ent.get()) or FTest(V3U4Ent.get()) or FTest(V3U5Ent.get()):
                            error = True
                    if GSOPage.EntV4:
                        if not FTest(V4U1Ent.get()) or not FTest(V4U2Ent.get()) or not FTest(V4U3Ent.get()) or FTest(V4U4Ent.get()) or FTest(V4U5Ent.get()):
                            error = True
                    if GSOPage.EntV5:
                        if not FTest(V5U1Ent.get()) or not FTest(V5U2Ent.get()) or not FTest(V5U3Ent.get()) or FTest(V5U4Ent.get()) or FTest(V5U5Ent.get()):
                            error = True
                elif GSOPage.EntV1 and FTest(V1U1Ent.get()) and FTest(V1U2Ent.get()):
                    GSOPage.DIM = 2
                    if GSOPage.EntV2:
                        if not FTest(V2U1Ent.get()) or not FTest(V2U2Ent.get()) or FTest(V2U3Ent.get()) or FTest(V2U4Ent.get()) or FTest(V2U5Ent.get()):
                            error = True
                    if GSOPage.EntV3:
                        if not FTest(V3U1Ent.get()) or not FTest(V3U2Ent.get()) or FTest(V3U3Ent.get()) or FTest(V3U4Ent.get()) or FTest(V3U5Ent.get()):
                            error = True
                    if GSOPage.EntV4:
                        if not FTest(V4U1Ent.get()) or not FTest(V4U2Ent.get()) or FTest(V4U3Ent.get()) or FTest(V4U4Ent.get()) or FTest(V4U5Ent.get()):
                            error = True
                    if GSOPage.EntV5:
                        if not FTest(V5U1Ent.get()) or not FTest(V5U2Ent.get()) or FTest(V5U3Ent.get()) or FTest(V5U4Ent.get()) or FTest(V5U5Ent.get()):
                            error = True
                else:
                    error = True
            else:
                error = True
            return error
        def CalcAct():
            Vec1 = 0
            Vec2 = 0
            Vec3 = 0
            Vec4 = 0
            Vec5 = 0
            VSize = 0
            AL = (u1, e1, u2, e2, u3, e3, u4, e4, u5, e5)
            LOWERtool(AL, len(AL))
            if DimError():
                ErrorS.play()
                time.sleep(1)
                ErMsg.lift()
            else:
                ErMsg.lower()
                if GSOPage.EntV1:
                    VSize = 1
                    if GSOPage.DIM == 5:
                        Vec1 = APPENDtool(V1, len(V1))
                    elif GSOPage.DIM == 4:
                        Vec1 = APPENDtool(V1, GSOPage.DIM)
                    elif GSOPage.DIM == 3:
                        Vec1 = APPENDtool(V1, GSOPage.DIM)
                    elif GSOPage.DIM == 2:
                        Vec1 = APPENDtool(V1, GSOPage.DIM)
                if GSOPage.EntV2:
                    VSize = 2
                    if GSOPage.DIM == 5:
                        Vec2 = APPENDtool(V2, len(V2))
                    elif GSOPage.DIM == 4:
                        Vec2 = APPENDtool(V2, GSOPage.DIM)
                    elif GSOPage.DIM == 3:
                        Vec2 = APPENDtool(V2, GSOPage.DIM)
                    elif GSOPage.DIM == 2:
                        Vec2 = APPENDtool(V2, GSOPage.DIM)
                if GSOPage.EntV3:
                    VSize = 3
                    if GSOPage.DIM == 5:
                        Vec3 = APPENDtool(V3, len(V3))
                    elif GSOPage.DIM == 4:
                        Vec3 = APPENDtool(V3, GSOPage.DIM)
                    elif GSOPage.DIM == 3:
                        Vec3 = APPENDtool(V3, GSOPage.DIM)
                    elif GSOPage.DIM == 2:
                        Vec3 = APPENDtool(V3, GSOPage.DIM)
                if GSOPage.EntV4:
                    VSize = 4
                    if GSOPage.DIM == 5:
                        Vec4 = APPENDtool(V4, len(V4))
                    elif GSOPage.DIM == 4:
                        Vec4 = APPENDtool(V4, GSOPage.DIM)
                    elif GSOPage.DIM == 3:
                        Vec4 = APPENDtool(V4, GSOPage.DIM)
                    elif GSOPage.DIM == 2:
                        Vec4 = APPENDtool(V4, GSOPage.DIM)
                if GSOPage.EntV5:
                    VSize = 5
                    if GSOPage.DIM==5:
                        Vec5 = APPENDtool(V5, len(V5))
                    elif GSOPage.DIM==4:
                        Vec5 = APPENDtool(V5, GSOPage.DIM)
                    elif GSOPage.DIM==3:
                        Vec5 = APPENDtool(V5, GSOPage.DIM)
                    elif GSOPage.DIM==2:
                        Vec5 = APPENDtool(V5, GSOPage.DIM)
                if GSOPage.EntV1 and Vec1==0 or GSOPage.EntV2 and Vec2==0 or GSOPage.EntV3 and Vec3==0 or GSOPage.EntV4 and Vec4==0 or GSOPage.EntV5 and Vec5==0:
                    ErrorS.play()
                    time.sleep(1)
                    ErMsg.lift()
                else:
                    GSO = GSOExp(VSize, GSOPage.DIM, Vec1, Vec2, Vec3, Vec4, Vec5)
                    delay = 0.1
                    if VSize >= 1:
                        u1.config(font=("Arial", 14), fg='white', anchor='nw', text=GSO.U1())
                        e1.config(font=("Arial", 14), fg='SpringGreen', anchor='nw', text=GSO.E1())
                        u1.update()
                        e1.update()
                        u1.lift()
                        e1.lift()
                        time.sleep(delay)
                    if VSize >= 2:
                        u2.config(font=("Arial", 14), fg='white', anchor='nw', text=GSO.U2())
                        e2.config(font=("Arial", 14), fg='SpringGreen', anchor='nw', text=GSO.E2())
                        u2.update()
                        e2.update()
                        u2.lift()
                        e2.lift()
                        time.sleep(delay)
                    if VSize >= 3:
                        u3.config(font=("Arial", 14), fg='white', anchor='nw', text=GSO.U3())
                        e3.config(font=("Arial", 14), fg='SpringGreen', anchor='nw', text=GSO.E3())
                        u3.update()
                        e3.update()
                        u3.lift()
                        e3.lift()
                        time.sleep(delay)
                    if VSize >= 4:
                        u4.config(font=("Arial", 14), fg='white', anchor='nw', text=GSO.U4())
                        e4.config(font=("Arial", 14), fg='SpringGreen', anchor='nw', text=GSO.E4())
                        u4.update()
                        e4.update()
                        u4.lift()
                        e4.lift()
                        time.sleep(delay)
                    if VSize == 5:
                        u5.config(font=("Arial", 14), fg='white', anchor='nw', text=GSO.U5())
                        e5.config(font=("Arial", 14), fg='SpringGreen', anchor='nw', text=GSO.E5())
                        u5.update()
                        e5.update()
                        u5.lift()
                        e5.lift()
                        time.sleep(delay)
        def RANDOMtool(E, n):
            for i in range(n):
                E[i].delete(0, END)
                E[i].insert(1, random.randrange(-9, 10))
        def runRandAct():
            time.sleep(1)
            if GSOPage.EntV1:
                RANDOMtool(V1,len(V1))
            if GSOPage.EntV2:
                RANDOMtool(V2, len(V2))
            if GSOPage.EntV3:
                RANDOMtool(V3,len(V3))
            if GSOPage.EntV4:
                RANDOMtool(V4,len(V4))
            if GSOPage.EntV5:
                RANDOMtool(V5,len(V5))
        def BackAct():
            BackS.play()
            pygame.mixer.music.load("MenuBG.ogg")
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1)
            controller.show_frame("MenuPage")
        def RandAct():
            if GSOPage.MUTE == False:
                RandomS.play()
            runRandAct()
        def MuteAct():
            if GSOPage.MUTE == True:
                GSOPage.MUTE = False
                pygame.mixer.music.load("GSOBg.ogg")
                pygame.mixer.music.play(-1)
                MuteBtn.lower()
            else:
                GSOPage.MUTE = True
                pygame.mixer.music.stop()
                MuteBtn.lift()
        def ClrAct():
            if GSOPage.MUTE == False:
                ClearS.play()
            time.sleep(1)
            for i in range(len(V1)):
                V1[i].delete(0, END)
            for i in range(len(V2)):
                V2[i].delete(0, END)
            for i in range(len(V3)):
                V3[i].delete(0, END)
            for i in range(len(V4)):
                V4[i].delete(0, END)
            for i in range(len(V5)):
                V5[i].delete(0, END)
        def InfoAct():
            if GSOPage.INFO == False:
                GSOPage.INFO = True
                if GSOPage.MUTE == False:
                    InfoS.play()
                InfoPop.lift()
                InfoBtn.lift()
            else:
                GSOPage.INFO = False
                InfoPop.lower()

            





