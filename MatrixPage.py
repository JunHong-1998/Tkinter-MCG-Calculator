from tkinter import *
import pygame
import time

class MatrixPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        pygame.mixer.init()
        SM = PhotoImage(file="Mouse-1.png")
        SMBtn = Button(self, image=SM, bd=0, bg='black', command=lambda: SMAct())
        SMBtn.image = SM
        SMBtn.place(x=-2, y=-2)
        DM = PhotoImage(file="Frozen-1.png")
        DMBtn = Button(self, image=DM, bd=0, bg='black', command=lambda: DMAct())
        DMBtn.image = DM
        DMBtn.place(x=417, y=-2)
        TM = PhotoImage(file="Toy0.png")
        TMBtn = Button(self, image=TM, bd=0, bg='black', command=lambda: TMAct())
        TMBtn.image = TM
        TMBtn.place(x=836, y=-2)
        image_files1 = [('Mouse%s.png' % frame) for frame in range (-1, 12)]
        SMOpen = Label(self)
        SMOpen.place(x=-2, y=-2)
        image_files2 = [('Frozen%s.png' % frame) for frame in range(-1, 12)]
        DMOpen = Label(self)
        DMOpen.place(x=417, y=-2)
        image_files3 = [('Toy%s.png' % frame) for frame in range(0, 10)]
        TMOpen = Label(self)
        TMOpen.place(x=836, y=-2)
        back = PhotoImage(file="SmallBackMat.png")
        BackBtn = Button(self, image=back, command=lambda: BackAct(), bd=0, bg='#262223')
        BackBtn.image=back
        BackBtn.place(x=0, y=0)
        def SMAct():
            SMBtn.lower()
            BackBtn.lower()
            delay = 0.05
            for image in image_files1:
                image_object = PhotoImage(file=image)
                SMOpen.config(image=image_object)
                SMOpen.update()
                time.sleep(delay)
            controller.show_frame("SMPage")
            pygame.mixer.music.load("MickeyMouse.ogg")
            pygame.mixer.music.play(-1)
            SMBtn.lift()
            BackBtn.lift()
        def DMAct():
            DMBtn.lower()
            BackBtn.lower()
            delay = 0.05
            for image in image_files2:
                image_object = PhotoImage(file=image)
                DMOpen.config(image=image_object)
                DMOpen.update()
                time.sleep(delay)
            controller.show_frame("DMPage")
            pygame.mixer.music.load("FrozenBackground.ogg")
            pygame.mixer.music.play(-1)
            DMBtn.lift()
            BackBtn.lift()
        def TMAct():
            TMBtn.lower()
            BackBtn.lower()
            delay = 0.05
            for image in image_files3:
                image_object = PhotoImage(file=image)
                TMOpen.config(image=image_object)
                TMOpen.update()
                time.sleep(delay)
            controller.show_frame("TMPage")
            pygame.mixer.music.load("ToyBackground.ogg")
            pygame.mixer.music.play(-1)
            TMBtn.lift()
            BackBtn.lift()
        def BackAct():
            controller.show_frame("MenuPage")

