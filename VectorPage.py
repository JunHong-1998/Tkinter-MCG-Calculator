from tkinter import *
import pygame
import time

class VectorPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        pygame.mixer.init()
        TwoD = PhotoImage(file="2DLight0.png")
        TwoDBtn = Button(self, image=TwoD, bd=0, command=lambda: TwoDAct())
        TwoDBtn.image = TwoD
        TwoDBtn.place(x=-2, y=-2)
        ThreeD = PhotoImage(file="3DLight0.png")
        ThreeDBtn = Button(self, image=ThreeD, bd=0, command=lambda: ThreeDAct())
        ThreeDBtn.image = ThreeD
        ThreeDBtn.place(x=623, y=-2)
        image_files1 = [('2DLight%s.png' % frame) for frame in range(0, 16)]
        TwoDOpen = Label(self)
        TwoDOpen.place(x=-2, y=-2)
        image_files2 = [('3DLight%s.png' % frame) for frame in range(0, 14)]
        ThreeDOpen = Label(self)
        ThreeDOpen.place(x=623, y=-2)
        back = PhotoImage(file="SmallBackVec.png")
        BackBtn = Button(self, image=back, command=lambda: BackAct(), bd=0, bg='#142c12')
        BackBtn.image = back
        BackBtn.place(x=0, y=0)
        def TwoDAct():
            TwoDBtn.lower()
            BackBtn.lower()
            delay = 0.05
            for image in image_files1:
                image_object = PhotoImage(file=image)
                TwoDOpen.config(image=image_object)
                TwoDOpen.update()
                time.sleep(delay)
            controller.show_frame("TwoDPage")
            pygame.mixer.music.load("BackgroundMusic.ogg")
            pygame.mixer.music.play(-1)
            TwoDBtn.lift()
            BackBtn.lift()
        def ThreeDAct():
            ThreeDBtn.lower()
            BackBtn.lower()
            delay = 0.05
            for image in image_files2:
                image_object = PhotoImage(file=image)
                ThreeDOpen.config(image=image_object)
                ThreeDOpen.update()
                time.sleep(delay)
            controller.show_frame("ThreeDPage")
            pygame.mixer.music.load("BackgroundMusic.ogg")
            pygame.mixer.music.play(-1)
            ThreeDBtn.lift()
            BackBtn.lift()
        def BackAct():
            controller.show_frame("MenuPage")
