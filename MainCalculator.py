from tkinter import *
from tkinter import messagebox

import time
import pygame
from GSOPage import*
from EMPage import*
from MatrixPage import*
from SMPage import*
from DMPage import*
from TMPage import*
from VectorPage import*
from TwoDPage import*
from ThreeDPage import*

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (StartPage, MenuPage, GSOPage, EMPage, MatrixPage, SMPage, DMPage, TMPage, VectorPage, TwoDPage, ThreeDPage):
            context = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[context] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")
    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Wp = PhotoImage(file="Start81.png")
        Wallpaper = Button(self, image=Wp, bd=0, bg='black', command=lambda : StartAct())
        Wallpaper.image = Wp
        Wallpaper.place(x=-2, y=-2)
        Start_file = [('Start%s.png' % frame) for frame in range(1, 82)]
        WpOpen = Label(self)
        WpOpen.place(x=-2, y=-2)
        def StartAct():
            delay = 0.013
            for image in Start_file:
                image_object = PhotoImage(file=image)
                WpOpen.config(image=image_object)
                WpOpen.update()
                time.sleep(delay)
            controller.show_frame("MenuPage")

class MenuPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        pygame.mixer.init()
        pygame.mixer.music.load("MenuBG.ogg")
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.play(-1)
        GSO = PhotoImage(file='GSOMenu.png')
        GSOM = Button(self, image=GSO, bd=0, bg='black', command=lambda: GSOAct())
        GSOM.image = GSO
        GSOM.place(x=-2,y=-2)
        MT = PhotoImage(file='MTMenu.png')
        MTM = Button(self, image=MT, bd=0, bg='black', command=lambda: MTAct())
        MTM.image = MT
        MTM.place(x=624, y=-2)
        VT = PhotoImage(file='VTMenu.png')
        VTM = Button(self, image=VT, bd=0, bg='black', command=lambda: VTAct())
        VTM.image = VT
        VTM.place(x=-2, y=374)
        EM = PhotoImage(file='EMMenu.png')
        EMM = Button(self, image=EM, bd=0, bg='black', command=lambda: EMAct())
        EMM.image = EM
        EMM.place(x=624, y=374)
        Disney_file = [('Disney%s.png' % frame) for frame in range(0, 23)]
        Disney = Label(self)
        Disney.place(x=-2, y=-2)
        Zombie_file = [('Zombie%s.png' % frame) for frame in range(0, 19)]
        Zombie = Label(self)
        Zombie.place(x=-2, y=-2)
        def GSOAct():
            StartS = pygame.mixer.Sound("GSOStart.wav")
            pygame.mixer.Sound.set_volume(StartS, 0.5)
            StartS.play()
            controller.show_frame("GSOPage")
            pygame.mixer.music.load("GSOBg.ogg")
            pygame.mixer.music.play(-1)
        def EMAct():
            StartS = pygame.mixer.Sound("EUStart.wav")
            StartS.play()
            controller.show_frame("EMPage")
            pygame.mixer.music.load("EUBg.ogg")
            pygame.mixer.music.play(-1)
        def MTAct():
            Disney.lift()
            delay = 0.025
            for image in Disney_file:
                image_object = PhotoImage(file=image)
                Disney.config(image=image_object)
                Disney.update()
                time.sleep(delay)
            controller.show_frame("MatrixPage")
            Disney.lower()
        def VTAct():
            Zombie.lift()
            delay = 0.025
            for image in Zombie_file:
                image_object = PhotoImage(file=image)
                Zombie.config(image=image_object)
                Zombie.update()
                time.sleep(delay)
            controller.show_frame("VectorPage")
            Zombie.lower()

def DestroyApp():
    if messagebox.askyesno("Quit", "Are you sure you want to leave us?"):
        app.destroy()

app = App()
app.title("The MCG CALCULATOR - credit by Low Jun Hong/Leong Yau Wah <2019>")
app.geometry("1250x750")
app.protocol("WM_DELETE_WINDOW", DestroyApp)
app.mainloop()