from tkinter import *
from V3DExp import*
import pygame
import time
import random

class ThreeDPage(Frame):
	MUTE = False
	INFO = False
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		Wallpaper3D = PhotoImage(file="3DComplete.png")
		Background3D = Label(self, image=Wallpaper3D)
		Background3D.image = Wallpaper3D
		Background3D.place(width=1250, height=750)
		InfoPOP = PhotoImage(file="InfoPoP2.png")
		InfoPanel = Label(self, image=InfoPOP)
		InfoPanel.image = InfoPOP
		InfoPanel.place(x=-2, y=-2)
		InfoPanel.lower()
		MuteS = PhotoImage(file="Soundoff.png")
		MuteOff = Button(self, image=MuteS, bd=0, bg="white", command=lambda: MuteAct())
		MuteOff.image = MuteS
		MuteOff.place(x=790, y=120)
		MuteOff.lower()
		Random = PhotoImage(file="RandomButton.png")
		RandBtn = Button(self, image=Random, bd=0, bg="white", command=lambda: RandAct())
		RandBtn.image = Random
		RandBtn.place(x=790, y=180)
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
		V1aEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
		V1aEnt.config(validatecommand=(V1aEnt.register(on_validate), '%P'))
		V1aEnt.place(x=350, y=97, width=60, height=50)
		V1bEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
		V1bEnt.config(validatecommand=(V1bEnt.register(on_validate), '%P'))
		V1bEnt.place(x=453, y=97, width=60, height=50)
		V1cEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
		V1cEnt.config(validatecommand=(V1cEnt.register(on_validate), '%P'))
		V1cEnt.place(x=558, y=97, width=60, height=50)
		V2aEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
		V2aEnt.config(validatecommand=(V2aEnt.register(on_validate), '%P'))
		V2aEnt.place(x=350, y=181, width=60, height=50)
		V2bEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
		V2bEnt.config(validatecommand=(V2bEnt.register(on_validate), '%P'))
		V2bEnt.place(x=453, y=181, width=60, height=50)
		V2cEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
		V2cEnt.config(validatecommand=(V2cEnt.register(on_validate), '%P'))
		V2cEnt.place(x=558, y=181, width=60, height=50)
		V3aEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
		V3aEnt.config(validatecommand=(V3aEnt.register(on_validate), '%P'))
		V3aEnt.place(x=350, y=268, width=60, height=50)
		V3bEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
		V3bEnt.config(validatecommand=(V3bEnt.register(on_validate), '%P'))
		V3bEnt.place(x=453, y=268, width=60, height=50)
		V3cEnt = Entry(self, background="white", font="-family {Segoe Print} -size 16", justify="center", validate="key")
		V3cEnt.config(validatecommand=(V3cEnt.register(on_validate), '%P'))
		V3cEnt.place(x=558, y=268, width=60, height=50)
		Result = Label(self, bg="#363943", justify=LEFT, fg="Spring Green")
		Result.place(x=190, y=467, width=490, height=250)
		Back = PhotoImage(file="Backbutton.png")
		BackBtn = Button(self, image=Back, bd=0, command=lambda: BackAct())
		BackBtn.image = Back
		BackBtn.place(x=0, y=0)
		Info = PhotoImage(file="Infobutton.png")
		InfoBtn = Button(self, image=Info, bd=0, bg="white", command=lambda: InfoAct())
		InfoBtn.image = Info
		InfoBtn.place(x=790, y=0)
		Reset = PhotoImage(file="Resetbutton.png")
		ResetBtn = Button(self, image=Reset, bd=0, bg="white", command=lambda: ResetAct())
		ResetBtn.image = Reset
		ResetBtn.place(x=790, y=60)
		Mute = PhotoImage(file="SoundOn.png")
		MuteBtn = Button(self, image=Mute, bd=0, bg="white", command=lambda: MuteAct())
		MuteBtn.image = Mute
		MuteBtn.place(x=790, y=120)
		Add = PhotoImage(file="3DPlanksZero.png")
		AddBtn = Button(self, image=Add, bd=0, command=lambda:AddAct())
		AddBtn.image = Add
		AddBtn.place(x=908, y=33)
		Diff = PhotoImage(file="3DPlanksOne.png")
		DiffBtn = Button(self, image=Diff, bd=0, command=lambda:DiffAct())
		DiffBtn.image = Diff
		DiffBtn.place(x=1051, y=35)
		Scal = PhotoImage(file="3DPlanksTwo.png")
		ScalBtn = Button(self, image=Scal, bd=0, command=lambda:ScalAct())
		ScalBtn.image = Scal
		ScalBtn.place(x=906, y=116)
		Cross = PhotoImage(file="3DPlanksThree.png")
		CrossBtn = Button(self, image=Cross, bd=0, command=lambda:CrossAct())
		CrossBtn.image = Cross
		CrossBtn.place(x=902, y=197)
		Ang = PhotoImage(file="3DPlanksFour.png")
		AngBtn = Button(self, image=Ang, bd=0, command=lambda:AngAct())
		AngBtn.image = Ang
		AngBtn.place(x=903, y=270)
		Mag = PhotoImage(file="3DPlanksFive.png")
		MagBtn = Button(self, image=Mag, bd=0, command=lambda:MagAct())
		MagBtn.image = Mag
		MagBtn.place(x=909, y=356)
		UnitV = PhotoImage(file="3DPlanksSix.png")
		UnitVBtn = Button(self, image=UnitV, bd=0, command=lambda:UnitVAct())
		UnitVBtn.image = UnitV
		UnitVBtn.place(x=914, y=435)
		Indp = PhotoImage(file="3DPlanksSeven.png")
		IndpBtn = Button(self, image=Indp, bd=0, command=lambda:IndpAct())
		IndpBtn.image = Indp
		IndpBtn.place(x=901, y=510)
		Orth = PhotoImage(file="3DPlanksEight.png")
		OrthBtn = Button(self, image=Orth, bd=0, command=lambda:OrthAct())
		OrthBtn.image = Orth
		OrthBtn.place(x=914, y=594)
		Para = PhotoImage(file="3DPlanksNine.png")
		ParaBtn = Button(self, image=Para, bd=0, command=lambda:ParaAct())
		ParaBtn.image = Para
		ParaBtn.place(x=913, y=671)
		def BackAct():
			BackS = pygame.mixer.Sound("BackSound.wav")
			BackS.play()
			pygame.mixer.music.load("MenuBG.ogg")
			pygame.mixer.music.play(-1)
			controller.show_frame("VectorPage")
		def RandAct():
			if ThreeDPage.MUTE == False:
				RandomS = pygame.mixer.Sound("RandomSound.wav")
				RandomS.play()
			runRandAct()
		def runRandAct():
			V1aEnt.delete(0, END)
			V1bEnt.delete(0, END)
			V1cEnt.delete(0, END)
			V2aEnt.delete(0, END)
			V2bEnt.delete(0, END)
			V2cEnt.delete(0, END)
			V3aEnt.delete(0, END)
			V3bEnt.delete(0, END)
			V3cEnt.delete(0, END)
			time.sleep(3.5)
			V1aEnt.insert(1, random.randrange(-33, 33))
			V1bEnt.insert(1, random.randrange(-33, 33))
			V1cEnt.insert(1, random.randrange(-33, 33))
			V2aEnt.insert(1, random.randrange(-33, 33))
			V2bEnt.insert(1, random.randrange(-33, 33))
			V2cEnt.insert(1, random.randrange(-33, 33))
			V3aEnt.insert(1, random.randrange(-33, 33))
			V3bEnt.insert(1, random.randrange(-33, 33))
			V3cEnt.insert(1, random.randrange(-33, 33))
		def SoundEffect():
			if ThreeDPage.MUTE == False:
				SES = pygame.mixer.Sound("Eat.wav")
				SES.play()
				time.sleep(0.75)
		def SetNoneV2():
			V2aEnt.delete(0, END)
			V2aEnt.insert(1, "X")
			V2bEnt.delete(0, END)
			V2bEnt.insert(1, "X")
			V2cEnt.delete(0, END)
			V2cEnt.insert(1, "X")
		def SetNoneV3():
			V3aEnt.delete(0,END)
			V3aEnt.insert(1,"X")
			V3bEnt.delete(0, END)
			V3bEnt.insert(1, "X")
			V3cEnt.delete(0, END)
			V3cEnt.insert(1, "X")
		def FTest(x):
			return x.lstrip('-').lstrip('+').replace('.', '', 1).isdigit()
		def Check3():
			if not FTest(V1aEnt.get()) or not FTest(V1bEnt.get()) or not FTest(V1cEnt.get()) or not FTest(V2aEnt.get()) or not FTest(V2bEnt.get()) or not FTest(V2cEnt.get()) or not FTest(V3aEnt.get()) or not FTest(V3bEnt.get()) or not FTest(V3cEnt.get()):
				return True
		def Check2():
			if not FTest(V1aEnt.get()) or not FTest(V1bEnt.get()) or not FTest(V1cEnt.get()) or not FTest(V2aEnt.get()) or not FTest(V2bEnt.get()) or not FTest(V2cEnt.get()):
				return True
		def Check1():
			if not FTest(V1aEnt.get()) or not FTest(V1bEnt.get()) or not FTest(V1cEnt.get()):
				return True
		def AddAct():
			SoundEffect()
			if Check2():
				Result.configure(font=("Segoe Print", 20), anchor='c', text="Incomplete Input\nPlease Try Again")
			else:
				v1 = (float(V1aEnt.get()), float(V1bEnt.get()), float(V1cEnt.get()))
				v2 = (float(V2aEnt.get()), float(V2bEnt.get()), float(V2cEnt.get()))
				v3 = (0,0,0)
				SetNoneV3()
				VEC3DEXP = ThreeDExpl(v1, v2, v3)
				Result.configure(font=("Segoe Print", 14), anchor='w', text=VEC3DEXP.Addition())
			Result.update()
		def DiffAct():
			SoundEffect()
			if Check2():
				Result.configure(font=("Segoe Print", 20), anchor='c', text="Incomplete Input\nPlease Try Again")
			else:
				v1 = (float(V1aEnt.get()), float(V1bEnt.get()), float(V1cEnt.get()))
				v2 = (float(V2aEnt.get()), float(V2bEnt.get()), float(V2cEnt.get()))
				v3 = (0, 0, 0)
				SetNoneV3()
				VEC3DEXP = ThreeDExpl(v1, v2, v3)
				Result.configure(font=("Segoe Print", 14), anchor='w', text=VEC3DEXP.Difference())
			Result.update()
		def ScalAct():
			SoundEffect()
			if Check2():
				Result.configure(font=("Segoe Print", 20), anchor='c', text="Incomplete Input\nPlease Try Again")
			else:
				v1 = (float(V1aEnt.get()), float(V1bEnt.get()), float(V1cEnt.get()))
				v2 = (float(V2aEnt.get()), float(V2bEnt.get()), float(V2cEnt.get()))
				v3 = (0, 0, 0)
				SetNoneV3()
				VEC3DEXP = ThreeDExpl(v1, v2, v3)
				Result.configure(font=("Segoe Print", 14), anchor='w', text=VEC3DEXP.Scalar())
			Result.update()
		def CrossAct():
			SoundEffect()
			if Check2():
				Result.configure(font=("Segoe Print", 20), anchor='c', text="Incomplete Input\nPlease Try Again")
			else:
				v1 = (float(V1aEnt.get()), float(V1bEnt.get()), float(V1cEnt.get()))
				v2 = (float(V2aEnt.get()), float(V2bEnt.get()), float(V2cEnt.get()))
				v3 = (0, 0, 0)
				SetNoneV3()
				VEC3DEXP = ThreeDExpl(v1, v2, v3)
				Result.configure(font=("Segoe Print", 12), anchor='w', text=VEC3DEXP.Cross())
			Result.update()
		def AngAct():
			SoundEffect()
			if Check2():
				Result.configure(font=("Segoe Print", 20), anchor='c', text="Incomplete Input\nPlease Try Again")
			else:
				v1 = (float(V1aEnt.get()), float(V1bEnt.get()), float(V1cEnt.get()))
				v2 = (float(V2aEnt.get()), float(V2bEnt.get()), float(V2cEnt.get()))
				v3 = (0, 0, 0)
				SetNoneV3()
				VEC3DEXP = ThreeDExpl(v1, v2, v3)
				Result.configure(font=("Segoe Print", 12), anchor='w', text=VEC3DEXP.Angle()+"??")
			Result.update()
		def MagAct():
			SoundEffect()
			if Check1():
				Result.configure(font=("Segoe Print", 20), anchor='c', text="Incomplete Input\nPlease Try Again")
			else:
				v1 = (float(V1aEnt.get()), float(V1bEnt.get()), float(V1cEnt.get()))
				v2 = (0, 0, 0)
				v3 = (0, 0, 0)
				SetNoneV2()
				SetNoneV3()
				VEC3DEXP = ThreeDExpl(v1, v2, v3)
				Result.configure(font=("Segoe Print", 16), anchor='w', text=VEC3DEXP.Magnitude())
			Result.update()
		def UnitVAct():
			SoundEffect()
			if Check1():
				Result.configure(font=("Segoe Print", 20), anchor='c', text="Incomplete Input\nPlease Try Again")
			else:
				v1 = (float(V1aEnt.get()), float(V1bEnt.get()), float(V1cEnt.get()))
				v2 = (0, 0, 0)
				v3 = (0, 0, 0)
				SetNoneV2()
				SetNoneV3()
				VEC3DEXP = ThreeDExpl(v1, v2, v3)
				Result.configure(font=("Segoe Print", 12), anchor='w', text=VEC3DEXP.UnitVector())
			Result.update()
		def IndpAct():
			SoundEffect()
			if Check3():
				Result.configure(font=("Segoe Print", 20), anchor='c', text="Incomplete Input\nPlease Try Again")
			else:
				v1 = (float(V1aEnt.get()), float(V1bEnt.get()), float(V1cEnt.get()))
				v2 = (float(V2aEnt.get()), float(V2bEnt.get()), float(V2cEnt.get()))
				v3 = (float(V3aEnt.get()), float(V3bEnt.get()), float(V3cEnt.get()))
				VEC3DEXP = ThreeDExpl(v1, v2, v3)
				Result.configure(font=("Segoe Print", 10), anchor='w', text=VEC3DEXP.Independency())
			Result.update()
		def OrthAct():
			SoundEffect()
			if Check2():
				Result.configure(font=("Segoe Print", 20), anchor='c', text="Incomplete Input\nPlease Try Again")
			else:
				v1 = (float(V1aEnt.get()), float(V1bEnt.get()), float(V1cEnt.get()))
				v2 = (float(V2aEnt.get()), float(V2bEnt.get()), float(V2cEnt.get()))
				v3 = (0, 0, 0)
				SetNoneV3()
				VEC3DEXP = ThreeDExpl(v1, v2, v3)
				Result.configure(font=("Segoe Print", 11), anchor='w', text=VEC3DEXP.Orthogonality())
			Result.update()
		def ParaAct():
			SoundEffect()
			if Check2():
				Result.configure(font=("Segoe Print", 20), anchor='c', text="Incomplete Input\nPlease Try Again")
			else:
				v1 = (float(V1aEnt.get()), float(V1bEnt.get()), float(V1cEnt.get()))
				v2 = (float(V2aEnt.get()), float(V2bEnt.get()), float(V2cEnt.get()))
				v3 = (0, 0, 0)
				SetNoneV3()
				VEC3DEXP = ThreeDExpl(v1, v2, v3)
				Result.configure(font=("Segoe Print", 11), anchor='w', text=VEC3DEXP.Parallelism())
			Result.update()
		def InfoAct():
			if ThreeDPage.INFO == False:
				ThreeDPage.INFO = True
				if ThreeDPage.MUTE == False:
					InfoS = pygame.mixer.Sound("InfoSound.wav")
					InfoS.play()
				InfoPanel.lift()
				InfoBtn.lift()
			else:
				ThreeDPage.INFO = False
				InfoPanel.lower()
		def ResetAct():
			if ThreeDPage.MUTE == False:
				ClearS = pygame.mixer.Sound("ResetSound.wav")
				ClearS.play()
			time.sleep(1.5)
			V1aEnt.delete(0, END)
			V1bEnt.delete(0, END)
			V1cEnt.delete(0, END)
			V2aEnt.delete(0, END)
			V2bEnt.delete(0, END)
			V2cEnt.delete(0, END)
			V3aEnt.delete(0, END)
			V3bEnt.delete(0, END)
			V3cEnt.delete(0, END)
			Result.configure(font=("Segoe Print", 12), anchor='w', text="")
			Result.update()
		def MuteAct():
			if ThreeDPage.MUTE == True:
				ThreeDPage.MUTE = False
				pygame.mixer.music.load("BackgroundMusic.ogg")
				pygame.mixer.music.play(-1)
				MuteOff.lower()
			else:
				ThreeDPage.MUTE = True
				pygame.mixer.music.stop()
				MuteOff.lift()
