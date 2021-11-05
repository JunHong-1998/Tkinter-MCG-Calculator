import re
import math
import numpy as np
from matplotlib import pyplot as plt


class EM:
    X = []
    Y = []
    F = ""
    def __init__(self, func, size, initialX, initialY, finalX):
        self.f = func
        self.h = size
        self.x0 = initialX
        self.y0 = initialY
        self.xf = finalX

    def __del__(self):
        class_name=self.__class__.__name__

    def Func(self):
        self.f = re.sub("(x)+", "*x", self.f)
        self.f = re.sub("(y)+", "*y", self.f)
        self.f = re.sub("(\()+", "*(", self.f)
        self.f = re.sub("(asin\*)+", "*math.asin", self.f)
        self.f = re.sub("(acos\*)+", "*math.acos", self.f)
        self.f = re.sub("(atan\*)+", "*math.atan", self.f)
        self.f = re.sub("(sin\*)+", "*math.sin", self.f)  # sin(x)
        self.f = re.sub("(cos\*)+", "*math.cos", self.f)
        self.f = re.sub("(tan\*)+", "*math.tan", self.f)
        self.f = re.sub("(cot\*)+", "*1/math.tan", self.f)
        self.f = re.sub("(sec\*)+", "*1/math.cos", self.f)
        self.f = re.sub("(csc\*)+", "*1/math.sin", self.f)
        # self.f = re.sub("(acot\*)+", "*math.acot", self.f)
        # self.f = re.sub("(asec\*)+", "*math.asec", self.f)
        # self.f = re.sub("(acsc\*)+", "*math.acsc", self.f)
        if "e^" not in self.f:
            self.f = re.sub("(e)+", "*math.e", self.f)
        self.f = re.sub("(pi)+", "*math.pi", self.f)
        self.f = re.sub("(log\*)+", "*math.log", self.f)  # log(x, base)
        self.f = re.sub("(e\^\*)+", "*math.exp", self.f)  # e^(x)
        self.f = re.sub("(ln\*)+", "*math.log", self.f)  # ln(x)  #log.e(x)
        self.f = re.sub("(lg\*)+", "*math.log10", self.f)  # log(x) #log.10(x)
        self.f = re.sub("(sqrt\*)+", "*math.sqrt", self.f)
        self.f = re.sub("(\^\*)+", "**", self.f)  # x^()     #if cube root(1/3)
        self.f = re.sub("(abs\*)+", "*math.fabs", self.f)  # abs()    ||
        self.f = re.sub("(/\*)+", "/", self.f)
        self.f = re.sub("(\(\*)+", "(", self.f)
        self.f = re.sub("(\+\*)+", "+", self.f)
        self.f = re.sub("(\-\*)+", "-", self.f)
        if self.f.find("*") == 0:  # remove if 1st is *
            self.f = self.f[1::]
        return self.f

    def Error(self):
        EM.F = self.Func()
        x=1
        y=1
        try:
            eval(EM.F)
            try:
                self.EMcalc()
                return False
            except:
                return True
        except:
            return True
    def FuncError(self):
        EM.F = self.Func()
        x=1
        y=1
        try:
            eval(EM.F)
            return False
        except:
            return True
    def EMcalc(self):
        x = self.x0
        y = self.y0
        n = int((self.xf-self.x0)/self.h)
        EM.X.clear()
        EM.Y.clear()
        EM.X.append(x)
        EM.Y.append(y)
        for i in range(n):
            y = y + self.h * eval(EM.F)
            x = x + self.h
            EM.X.append(round(x, 2))
            EM.Y.append(y)
    def xValue(self):
        return self.MatBrk(np.array([EM.X]).reshape(len(EM.X),1))
    def yValue(self):
        return self.MatBrk(np.array(np.round([EM.Y], decimals=5)).reshape(len(EM.Y), 1))
    def MatBrk(self, arr):
        return str(arr).replace('[[', ' ').replace(']]', '').replace('[', '').replace(']', '')

    def Graph(self):
        plt.close('all')
        plt.rcParams['axes.facecolor'] = 'black'
        fig = plt.figure()
        # fig.patch.set_facecolor('xkcd:black')
        fig.canvas.set_window_title("Euler's Method Graph")
        plt.tick_params(direction='out', length=5, width=1, colors='r', grid_color='r', grid_alpha=0.8, labelcolor='r')
        plt.plot(EM.X, EM.Y, 'bo')
        plt.grid(True,color='red')
        plt.xlabel("X-label")
        plt.ylabel("Y-label")
        plt.title("Approximate Solution with Euler's Method")
        plt.show()
    def CloseGraph(self):
        return plt.close('all')






