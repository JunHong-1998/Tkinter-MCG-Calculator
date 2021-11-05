import numpy as np
class DoubleMatrix:

    def __init__(self, MatxA, MatxB, Dim, Avalue, Bvalue):
        self.mA = MatxA
        self.mB = MatxB
        self.d = Dim
        self.A = Avalue
        self.B = Bvalue
        np.set_printoptions(precision=3)

    def __del__(self):
        class_name=self.__class__.__name__
    def MatBrk(self, arr):
        return str(arr).replace('[[', '').replace(']]', '').replace('[', '').replace(']', '')
    def MatNum(self):
        if self.d==11:
            n = 1
        elif self.d==12 or self.d==21:
            n = 2
        elif self.d==13 or self.d==31:
            n = 3
        elif self.d==14 or self.d==22 or self.d==41:
            n = 4
        elif self.d==23 or self.d==32:
            n = 6
        elif self.d==24 or self.d==42:
            n = 8
        elif self.d==33:
            n = 9
        elif self.d==34 or self.d==43:
            n = 12
        elif self.d==44:
            n = 16
        else:
            n=0
        return n
    def MA(self):
        if self.d == 11 or self.d == 12 or self.d == 13 or self.d == 14:
            matA = np.array(self.mA).reshape(1, self.d % 10)
        elif self.d == 21 or self.d == 22 or self.d == 23 or self.d == 24:
            matA = np.array(self.mA).reshape(2, self.d % 10)
        elif self.d == 31 or self.d == 32 or self.d == 33 or self.d == 34:
            matA = np.array(self.mA).reshape(3, self.d % 10)
        elif self.d == 41 or self.d == 42 or self.d == 43 or self.d == 44:
            matA = np.array(self.mA).reshape(4, self.d % 10)
        else:
            matA = "Please use same"
        return matA
    def MB(self):
        if self.d == 11 or self.d == 12 or self.d == 13 or self.d == 14:
            matB = np.array(self.mB).reshape(1, self.d % 10)
        elif self.d == 21 or self.d == 22 or self.d == 23 or self.d == 24:
            matB = np.array(self.mB).reshape(2, self.d % 10)
        elif self.d == 31 or self.d == 32 or self.d == 33 or self.d == 34:
            matB = np.array(self.mB).reshape(3, self.d % 10)
        elif self.d == 41 or self.d == 42 or self.d == 43 or self.d == 44:
            matB = np.array(self.mB).reshape(4, self.d % 10)
        else:
            matB = "Matrix Dimension"
        return matB
    def MBM(self):
        if self.d == 11 or self.d == 21 or self.d == 31 or self.d == 41:
            matB = np.array(self.mB).reshape(1, self.d//10**1%10)
        elif self.d == 12 or self.d == 22 or self.d == 32 or self.d == 42:
            matB = np.array(self.mB).reshape(2, self.d//10**1%10)
        elif self.d == 13 or self.d == 23 or self.d == 33 or self.d == 43:
            matB = np.array(self.mB).reshape(3, self.d//10**1%10)
        elif self.d == 14 or self.d == 24 or self.d == 34 or self.d == 44:
            matB = np.array(self.mB).reshape(4, self.d//10**1%10)
        else:
            matB = "Matrix Dimension"
        return matB
    def MatA(self):
        if self.A!=0 and self.B!=0:
            exp = self.MatBrk(self.MA())
        else:
            exp = "Please Try"
        return exp
    def MatB(self):
        if self.A!=0 and self.B!=0:
            exp = self.MatBrk(self.MB())
        else:
            exp = "another number"
        return exp
    def MatBM(self):
        if self.A != 0 and self.B != 0:
            exp = self.MatBrk(self.MBM())
        else:
            exp = "another number"
        return exp

    def MStep(self, arr):
        if self.d == 11 or self.d == 12 or self.d == 13 or self.d == 14:
            mat = np.array(arr).reshape(1, self.d % 10)
        elif self.d == 21 or self.d == 22 or self.d == 23 or self.d == 24:
            mat = np.array(arr).reshape(2, self.d % 10)
        elif self.d == 31 or self.d == 32 or self.d == 33 or self.d == 34:
            mat = np.array(arr).reshape(3, self.d % 10)
        elif self.d == 41 or self.d == 42 or self.d == 43 or self.d == 44:
            mat = np.array(arr).reshape(4, self.d % 10)
        else:
            mat = ""
        return mat
    def MStepM(self, arr):
        if self.d == 11 or self.d == 12 or self.d == 13 or self.d == 14:
            mat = np.array(arr).reshape(1, 1)
        elif self.d == 21 or self.d == 22 or self.d == 23 or self.d == 24:
            mat = np.array(arr).reshape(2, 2)
        elif self.d == 31 or self.d == 32 or self.d == 33 or self.d == 34:
            mat = np.array(arr).reshape(3, 3)
        elif self.d == 41 or self.d == 42 or self.d == 43 or self.d == 44:
            mat = np.array(arr).reshape(4, 4)
        else:
            mat = ""
        return mat
    def Add(self):
        if self.A == 0 or self.B == 0 or self.d==0:
            exp = ""
        else:
            exp = self.MatBrk(self.A*self.MA() + self.B*self.MB())
        return exp

    def AddEXP(self):
        step=[]
        if self.A==1 and self.B==1 and self.mA==0 and self.mB==0:
            mat = "Please try another number"
        elif self.A==1 and self.B==1 and self.mA!=0 and self.mB!=0:
            for i in range(self.MatNum()):
                if self.d == 11:
                    step.append(str(self.mA)+"+"+str(self.mB))
                else:
                    step.append(str(self.mA[i])+"+"+str(self.mB[i]))
            mat = self.MStep(step)
        else:
            for i in range(self.MatNum()):
                if self.d == 11:
                    step.append(str(self.A)+"•"+str(self.mA)+"+"+str(self.B)+"•"+str(self.mB))
                else:
                    step.append(str(self.A)+"•"+str(self.mA[i])+"+"+str(self.B)+"•"+str(self.mB[i]))
            mat = self.MStep(step)
        exp = self.MatBrk(mat)
        return exp

    def Minus(self):
        if self.A == 0 or self.B == 0 or self.d==0:
            exp = ""
        else:
            exp = self.MatBrk(self.A * self.MA() - self.B * self.MB())
        return exp

    def MinusEXP(self):
        step = []
        if self.A == 1 and self.B == 1 and self.mA == 0 and self.mB == 0:
            mat = "Please try another number"
        elif self.A == 1 and self.B == 1 and self.mA != 0 and self.mB != 0:
            for i in range(self.MatNum()):
                if self.d == 11:
                    step.append(str(self.mA) + "-" + str(self.mB))
                else:
                    step.append(str(self.mA[i]) + "-" + str(self.mB[i]))
            mat = self.MStep(step)
        else:
            for i in range(self.MatNum()):
                if self.d == 11:
                    step.append(str(self.A) + "•" + str(self.mA) + "-" + str(self.B) + "•" + str(self.mB))
                else:
                    step.append(str(self.A) + "•" + str(self.mA[i]) + "-" + str(self.B) + "•" + str(self.mB[i]))
            mat = self.MStep(step)
        exp = self.MatBrk(mat)
        return exp

    def Multiply(self):
        if self.A == 0 or self.B == 0 or self.d==0:
            exp = ""
        else:
            exp = np.dot((self.A *self.MA()), (self.B *self.MBM()))
        return self.MatBrk(exp)

    def MultiplyEXP(self):
        if self.A == 1 and self.B == 1 and self.mA == 0 and self.mB == 0:
            mat = "Please try another number"
        elif self.A == 1 and self.B == 1:
            if self.d==11:
                step = (str(self.mA[0])+"x"+str(self.mB[0]))
            elif self.d==12:
                step = (str(self.mA[0])+"x"+str(self.mB[0])+"+"+str(self.mA[1])+"x"+str(self.mB[1]))
            elif self.d==13:
                step = (str(self.mA[0])+"x"+str(self.mB[0])+"+"+str(self.mA[1])+"x"+str(self.mB[1])+"+"+str(self.mA[2])+"x"+str(self.mB[2]))
            elif self.d==14:
                step = (str(self.mA[0])+"x"+str(self.mB[0])+"+"+str(self.mA[1])+"x"+str(self.mB[1])+"+"+str(self.mA[2])+"x"+str(self.mB[2])+"+"+str(self.mA[3])+"x"+str(self.mB[3]))
            elif self.d==21:
                step = (str(self.mA[0]) + "x" + str(self.mB[0]), str(self.mA[0]) + "x" + str(self.mB[1]), str(self.mA[1]) + "x" + str(self.mB[0]), str(self.mA[1]) + "x" + str(self.mB[1]))
            elif self.d==22:
                step = (str(self.mA[0])+"x"+str(self.mB[0])+"+"+str(self.mA[1])+"x"+str(self.mB[2]),  str(self.mA[0])+"x"+str(self.mB[1])+"+"+str(self.mA[1])+"x"+str(self.mB[3]), str(self.mA[2])+"x"+str(self.mB[0])+"+"+str(self.mA[3])+"x"+str(self.mB[2]), str(self.mA[2])+"x"+str(self.mB[1])+"+"+str(self.mA[3])+"x"+str(self.mB[3]))
            elif self.d==23:
                step = (str(self.mA[0])+"x"+str(self.mB[0])+"+"+str(self.mA[1])+"x"+str(self.mB[2])+"+"+str(self.mA[2])+"x"+str(self.mB[4]),  str(self.mA[0])+"x"+str(self.mB[1])+"+"+str(self.mA[1])+"x"+str(self.mB[3])+"+"+str(self.mA[2])+"x"+str(self.mB[5]), str(self.mA[3])+"x"+str(self.mB[0])+"+"+str(self.mA[4])+"x"+str(self.mB[2])+"+"+str(self.mA[5])+"x"+str(self.mB[4]), str(self.mA[3])+"x"+str(self.mB[1])+"+"+str(self.mA[4])+"x"+str(self.mB[3])+"+"+str(self.mA[5])+"x"+str(self.mB[5]))
            elif self.d==24:
                step = (str(self.mA[0])+"x"+str(self.mB[0])+"+"+str(self.mA[1])+"x"+str(self.mB[2])+"+"+str(self.mA[2])+"x"+str(self.mB[4])+"+"+str(self.mA[3])+"x"+str(self.mB[6]),  str(self.mA[0])+"x"+str(self.mB[1])+"+"+str(self.mA[1])+"x"+str(self.mB[3])+"+"+str(self.mA[2])+"x"+str(self.mB[5])+"+"+str(self.mA[3])+"x"+str(self.mB[7]), str(self.mA[4])+"x"+str(self.mB[0])+"+"+str(self.mA[5])+"x"+str(self.mB[2])+"+"+str(self.mA[6])+"x"+str(self.mB[4])+"+"+str(self.mA[7])+"x"+str(self.mB[6]), str(self.mA[4])+"x"+str(self.mB[1])+"+"+str(self.mA[5])+"x"+str(self.mB[3])+"+"+str(self.mA[6])+"x"+str(self.mB[5])+"+"+str(self.mA[7])+"x"+str(self.mB[7]))
            elif self.d==31:
                step = (str(self.mA[0])+"x"+str(self.mB[0]), str(self.mA[0])+"x"+str(self.mB[1]), str(self.mA[0])+"x"+str(self.mB[2]), str(self.mA[1])+"x"+str(self.mB[0]), str(self.mA[1])+"x"+str(self.mB[1]), str(self.mA[1])+"x"+str(self.mB[2]), str(self.mA[2])+"x"+str(self.mB[0]), str(self.mA[2])+"x"+str(self.mB[1]), str(self.mA[2])+"x"+str(self.mB[2]))
            elif self.d==32:
                step = (str(self.mA[0])+"x"+str(self.mB[0])+"+"+str(self.mA[1])+"x"+str(self.mB[3]), str(self.mA[0])+"x"+str(self.mB[1])+"+"+str(self.mA[1])+"x"+str(self.mB[4]), str(self.mA[0])+"x"+str(self.mB[2])+"+"+str(self.mA[1])+"x"+str(self.mB[5]), str(self.mA[2])+"x"+str(self.mB[0])+"+"+str(self.mA[3])+"x"+str(self.mB[3]), str(self.mA[2])+"x"+str(self.mB[1])+"+"+str(self.mA[3])+"x"+str(self.mB[4]), str(self.mA[2])+"x"+str(self.mB[2])+"+"+str(self.mA[3])+"x"+str(self.mB[5]), str(self.mA[2])+"x"+str(self.mB[0])+"+"+str(self.mA[3])+"x"+str(self.mB[3]), str(self.mA[2])+"x"+str(self.mB[1])+"+"+str(self.mA[3])+"x"+str(self.mB[4]), str(self.mA[2])+"x"+str(self.mB[2])+"+"+str(self.mA[3])+"x"+str(self.mB[5]))
            elif self.d==33:
                step = (str(self.mA[0])+"x"+str(self.mB[0])+"+"+str(self.mA[1])+"x"+str(self.mB[3])+"+"+str(self.mA[2])+"x"+str(self.mB[6]), str(self.mA[0])+"x"+str(self.mB[1])+"+"+str(self.mA[1])+"x"+str(self.mB[4])+"+"+str(self.mA[2])+"x"+str(self.mB[7]), str(self.mA[0])+"x"+str(self.mB[2])+"+"+str(self.mA[1])+"x"+str(self.mB[5])+"+"+str(self.mA[2])+"x"+str(self.mB[8]), str(self.mA[3])+"x"+str(self.mB[0])+"+"+str(self.mA[4])+"x"+str(self.mB[3])+"+"+str(self.mA[5])+"x"+str(self.mB[6]), str(self.mA[3])+"x"+str(self.mB[1])+"+"+str(self.mA[4])+"x"+str(self.mB[4])+"+"+str(self.mA[5])+"x"+str(self.mB[7]), str(self.mA[3])+"x"+str(self.mB[2])+"+"+str(self.mA[4])+"x"+str(self.mB[5])+"+"+str(self.mA[5])+"x"+str(self.mB[8]), str(self.mA[6])+"x"+str(self.mB[0])+"+"+str(self.mA[7])+"x"+str(self.mB[3])+"+"+str(self.mA[8])+"x"+str(self.mB[6]), str(self.mA[6])+"x"+str(self.mB[1])+"+"+str(self.mA[7])+"x"+str(self.mB[4])+"+"+str(self.mA[8])+"x"+str(self.mB[7]), str(self.mA[6])+"x"+str(self.mB[2])+"+"+str(self.mA[7])+"x"+str(self.mB[5])+"+"+str(self.mA[8])+"x"+str(self.mB[8]))
            elif self.d==34:
                step = (str(self.mA[0])+"x"+str(self.mB[0])+"+"+str(self.mA[1])+"x"+str(self.mB[3])+"+"+str(self.mA[2])+"x"+str(self.mB[6])+"+"+str(self.mA[3])+"x"+str(self.mB[9]), str(self.mA[0])+"x"+str(self.mB[1])+"+"+str(self.mA[1])+"x"+str(self.mB[4])+"+"+str(self.mA[2])+"x"+str(self.mB[7])+"+"+str(self.mA[3])+"x"+str(self.mB[10]), str(self.mA[0])+"x"+str(self.mB[2])+"+"+str(self.mA[1])+"x"+str(self.mB[5])+"+"+str(self.mA[2])+"x"+str(self.mB[8])+"+"+str(self.mA[3])+"x"+str(self.mB[11]), str(self.mA[4])+"x"+str(self.mB[0])+"+"+str(self.mA[5])+"x"+str(self.mB[3])+"+"+str(self.mA[6])+"x"+str(self.mB[6])+"+"+str(self.mA[7])+"x"+str(self.mB[9]), str(self.mA[4])+"x"+str(self.mB[1])+"+"+str(self.mA[5])+"x"+str(self.mB[4])+"+"+str(self.mA[6])+"x"+str(self.mB[7])+"+"+str(self.mA[7])+"x"+str(self.mB[10]), str(self.mA[4])+"x"+str(self.mB[2])+"+"+str(self.mA[5])+"x"+str(self.mB[5])+"+"+str(self.mA[6])+"x"+str(self.mB[8])+"+"+str(self.mA[7])+"x"+str(self.mB[11]), str(self.mA[8])+"x"+str(self.mB[0])+"+"+str(self.mA[9])+"x"+str(self.mB[3])+"+"+str(self.mA[10])+"x"+str(self.mB[6])+"+"+str(self.mB[11])+"x"+str(self.mB[9]), str(self.mA[8])+"x"+str(self.mB[1])+"+"+str(self.mA[9])+"x"+str(self.mB[4])+"+"+str(self.mA[10])+"x"+str(self.mB[7])+"+"+str(self.mA[11])+"x"+str(self.mB[10]), str(self.mA[8])+"x"+str(self.mB[2])+"+"+str(self.mA[9])+"x"+str(self.mB[5])+"+"+str(self.mA[10])+"x"+str(self.mB[8])+"+"+str(self.mA[11])+"x"+str(self.mB[11]))
            elif self.d==41:
                step = (str(self.mA[0])+"x"+str(self.mB[0]), str(self.mA[0])+"x"+str(self.mB[1]), str(self.mA[0])+"x"+str(self.mB[2]), str(self.mA[0])+"x"+str(self.mB[3]), str(self.mA[1])+"x"+str(self.mB[0]), str(self.mA[1])+"x"+str(self.mB[1]), str(self.mA[1])+"x"+str(self.mB[2]), str(self.mA[1])+"x"+str(self.mB[3]), str(self.mA[2])+"x"+str(self.mB[0]), str(self.mA[2])+"x"+str(self.mB[1]), str(self.mA[2])+"x"+str(self.mB[2]), str(self.mA[2])+"x"+str(self.mB[3]), str(self.mA[3])+"x"+str(self.mB[0]), str(self.mA[3])+"x"+str(self.mB[1]), str(self.mA[3])+"x"+str(self.mB[2]), str(self.mA[3])+"x"+str(self.mB[3]))
            elif self.d==42:
                step = (str(self.mA[0])+"x"+str(self.mB[0])+"+"+str(self.mA[1])+"x"+str(self.mB[4]), str(self.mA[0])+"x"+str(self.mB[1])+"+"+str(self.mA[1])+"x"+str(self.mB[5]), str(self.mA[0])+"x"+str(self.mB[2])+"+"+str(self.mA[1])+"x"+str(self.mB[6]), str(self.mA[0])+"x"+str(self.mB[3])+"+"+str(self.mA[1])+"x"+str(self.mB[7]), str(self.mA[2])+"x"+str(self.mB[0])+"+"+str(self.mA[3])+"x"+str(self.mB[4]), str(self.mA[2])+"x"+str(self.mB[1])+"+"+str(self.mA[3])+"x"+str(self.mB[5]), str(self.mA[2])+"x"+str(self.mB[2])+"+"+str(self.mA[3])+"x"+str(self.mB[6]), str(self.mA[2])+"x"+str(self.mB[3])+"+"+str(self.mA[3])+"x"+str(self.mB[7]), str(self.mA[4])+"x"+str(self.mB[0])+"+"+str(self.mA[5])+"x"+str(self.mB[4]), str(self.mA[4])+"x"+str(self.mB[1])+"+"+str(self.mA[5])+"x"+str(self.mB[5]), str(self.mA[4])+"x"+str(self.mB[2])+"+"+str(self.mA[5])+"x"+str(self.mB[6]), str(self.mA[4])+"x"+str(self.mB[3])+"+"+str(self.mA[5])+"x"+str(self.mB[7]), str(self.mA[6])+"x"+str(self.mB[0])+"+"+str(self.mA[7])+"x"+str(self.mB[4]), str(self.mA[6])+"x"+str(self.mB[1])+"+"+str(self.mA[7])+"x"+str(self.mB[5]), str(self.mA[6])+"x"+str(self.mB[2])+"+"+str(self.mA[7])+"x"+str(self.mB[6]), str(self.mA[6])+"x"+str(self.mB[3])+"+"+str(self.mA[7])+"x"+str(self.mB[7]))
            elif self.d==43:
                step = (str(self.mA[0])+"x"+str(self.mB[0])+"+"+str(self.mA[1])+"x"+str(self.mB[4])+"+"+str(self.mA[2])+"x"+str(self.mB[8]), str(self.mA[0])+"x"+str(self.mB[1])+"+"+str(self.mA[1])+"x"+str(self.mB[5])+"+"+str(self.mA[2])+"x"+str(self.mB[9]), str(self.mA[0])+"x"+str(self.mB[2])+"+"+str(self.mA[1])+"x"+str(self.mB[6])+"+"+str(self.mA[2])+"x"+str(self.mB[10]),  str(self.mA[0])+"x"+str(self.mB[3])+"+"+str(self.mA[1])+"x"+str(self.mB[7])+"+"+str(self.mA[2])+"x"+str(self.mB[11]), str(self.mA[3])+"x"+str(self.mB[0])+"+"+str(self.mA[4])+"x"+str(self.mB[4])+"+"+str(self.mA[5])+"x"+str(self.mB[8]), str(self.mA[3])+"x"+str(self.mB[1])+"+"+str(self.mA[4])+"x"+str(self.mB[5])+"+"+str(self.mA[5])+"x"+str(self.mB[9]), str(self.mA[3])+"x"+str(self.mB[2])+"+"+str(self.mA[4])+"x"+str(self.mB[6])+"+"+str(self.mA[5])+"x"+str(self.mB[10]),  str(self.mA[3])+"x"+str(self.mB[3])+"+"+str(self.mA[4])+"x"+str(self.mB[7])+"+"+str(self.mA[5])+"x"+str(self.mB[11]), str(self.mA[6])+"x"+str(self.mB[0])+"+"+str(self.mA[7])+"x"+str(self.mB[4])+"+"+str(self.mA[8])+"x"+str(self.mB[8]), str(self.mA[6])+"x"+str(self.mB[1])+"+"+str(self.mA[7])+"x"+str(self.mB[5])+"+"+str(self.mA[8])+"x"+str(self.mB[9]), str(self.mA[6])+"x"+str(self.mB[2])+"+"+str(self.mA[7])+"x"+str(self.mB[6])+"+"+str(self.mA[8])+"x"+str(self.mB[10]),  str(self.mA[6])+"x"+str(self.mB[3])+"+"+str(self.mA[7])+"x"+str(self.mB[7])+"+"+str(self.mA[8])+"x"+str(self.mB[11]), str(self.mA[9])+"x"+str(self.mB[0])+"+"+str(self.mA[10])+"x"+str(self.mB[4])+"+"+str(self.mA[11])+"x"+str(self.mB[8]), str(self.mA[9])+"x"+str(self.mB[1])+"+"+str(self.mA[10])+"x"+str(self.mB[5])+"+"+str(self.mA[11])+"x"+str(self.mB[9]), str(self.mA[9])+"x"+str(self.mB[2])+"+"+str(self.mA[10])+"x"+str(self.mB[6])+"+"+str(self.mA[11])+"x"+str(self.mB[10]),  str(self.mA[9])+"x"+str(self.mB[3])+"+"+str(self.mA[10])+"x"+str(self.mB[7])+"+"+str(self.mA[11])+"x"+str(self.mB[11]))
            elif self.d==44:
                step = (str(self.mA[0])+"x"+str(self.mB[0])+"+"+str(self.mA[1])+"x"+str(self.mB[4])+"+"+str(self.mA[2])+"x"+str(self.mB[8])+"+"+str(self.mA[3])+"x"+str(self.mB[12]), str(self.mA[0])+"x"+str(self.mB[1])+"+"+str(self.mA[1])+"x"+str(self.mB[5])+"+"+str(self.mA[2])+"x"+str(self.mB[9])+"+"+str(self.mA[3])+"x"+str(self.mB[13]), str(self.mA[0])+"x"+str(self.mB[2])+"+"+str(self.mA[1])+"x"+str(self.mB[6])+"+"+str(self.mA[2])+"x"+str(self.mB[10])+"+"+str(self.mA[3])+"x"+str(self.mB[14]),  str(self.mA[0])+"x"+str(self.mB[3])+"+"+str(self.mA[1])+"x"+str(self.mB[7])+"+"+str(self.mA[2])+"x"+str(self.mB[11])+"+"+str(self.mA[3])+"x"+str(self.mB[15]), str(self.mA[4])+"x"+str(self.mB[0])+"+"+str(self.mA[5])+"x"+str(self.mB[4])+"+"+str(self.mA[6])+"x"+str(self.mB[8])+"+"+str(self.mA[7])+"x"+str(self.mB[12]), str(self.mA[4])+"x"+str(self.mB[1])+"+"+str(self.mA[5])+"x"+str(self.mB[5])+"+"+str(self.mA[6])+"x"+str(self.mB[9])+"+"+str(self.mA[7])+"x"+str(self.mB[13]), str(self.mA[4])+"x"+str(self.mB[2])+"+"+str(self.mA[5])+"x"+str(self.mB[6])+"+"+str(self.mA[6])+"x"+str(self.mB[10])+"+"+str(self.mA[7])+"x"+str(self.mB[14]), str(self.mA[4])+"x"+str(self.mB[3])+"+"+str(self.mA[5])+"x"+str(self.mB[7])+"+"+str(self.mA[6])+"x"+str(self.mB[11])+"+"+str(self.mA[7])+"x"+str(self.mB[15]),
                        str(self.mA[8])+"x"+str(self.mB[0])+"+"+str(self.mA[9])+"x"+str(self.mB[4])+"+"+str(self.mA[10])+"x"+str(self.mB[8])+"+"+str(self.mA[11])+"x"+str(self.mB[12]), str(self.mA[8])+"x"+str(self.mB[1])+"+"+str(self.mA[9])+"x"+str(self.mB[5])+"+"+str(self.mA[10])+"x"+str(self.mB[9])+"+"+str(self.mA[11])+"x"+str(self.mB[13]), str(self.mA[8])+"x"+str(self.mB[2])+"+"+str(self.mA[9])+"x"+str(self.mB[6])+"+"+str(self.mA[10])+"x"+str(self.mB[10])+"+"+str(self.mA[11])+"x"+str(self.mB[14]),  str(self.mA[8])+"x"+str(self.mB[3])+"+"+str(self.mA[9])+"x"+str(self.mB[7])+"+"+str(self.mA[10])+"x"+str(self.mB[11])+"+"+str(self.mA[11])+"x"+str(self.mB[15]), str(self.mA[12])+"x"+str(self.mB[0])+"+"+str(self.mA[13])+"x"+str(self.mB[4])+"+"+str(self.mA[14])+"x"+str(self.mB[8])+"+"+str(self.mA[15])+"x"+str(self.mB[12]), str(self.mA[12])+"x"+str(self.mB[1])+"+"+str(self.mA[13])+"x"+str(self.mB[5])+"+"+str(self.mA[14])+"x"+str(self.mB[9])+"+"+str(self.mA[15])+"x"+str(self.mB[13]), str(self.mA[12])+"x"+str(self.mB[2])+"+"+str(self.mA[13])+"x"+str(self.mB[6])+"+"+str(self.mA[14])+"x"+str(self.mB[10])+"+"+str(self.mA[15])+"x"+str(self.mB[14]),  str(self.mA[12])+"x"+str(self.mB[3])+"+"+str(self.mA[13])+"x"+str(self.mB[7])+"+"+str(self.mA[14])+"x"+str(self.mB[11])+"+"+str(self.mA[15])+"x"+str(self.mB[15]))
            else:
                step = 0
            mat = self.MStepM(step)
        else:
            if self.d == 11:
                step = (str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[0]))
            elif self.d == 12:
                step = (str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[1]))
            elif self.d == 13:
                step = (str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[2]))
            elif self.d == 14:
                step = (str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[3]))
            elif self.d == 21:
                step = (str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[0]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[1]), str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[0]), str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[1]))
            elif self.d == 22:
                step = (str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[2]),  str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[3]), str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[2]), str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[3]))
            elif self.d == 23:
                step = (str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[4]),  str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[5]), str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[4]), str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[5]))
            elif self.d == 24:
                step = (str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[4])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[6]),  str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[5])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[7]), str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[4])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[6]), str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[5])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[7]))
            elif self.d == 31:
                step = (str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[0]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[1]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[2]), str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[0]), str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[1]), str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[2]), str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[0]), str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[1]), str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[2]))
            elif self.d == 32:
                step = (str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[3]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[4]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[5]), str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[3]), str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[4]), str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[5]), str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[3]), str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[4]), str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[5]))
            elif self.d == 33:
                step = (str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[6]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[4])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[7]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[5])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[8]), str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[6]), str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[4])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[7]), str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[5])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[8]), str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[8])+"x"+str(self.B)+"•"+str(self.mB[6]), str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[4])+"+"+str(self.A)+"•"+str(self.mA[8])+"x"+str(self.B)+"•"+str(self.mB[7]), str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[5])+"+"+str(self.A)+"•"+str(self.mA[8])+"x"+str(self.B)+"•"+str(self.mB[8]))
            elif self.d == 34:
                step = (str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[6])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[9]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[4])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[7])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[10]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[5])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[8])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[11]), str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[6])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[9]), str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[4])+"+"+str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[7])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[10]), str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[5])+"+"+str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[8])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[11]), str(self.A)+"•"+str(self.mA[8])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[9])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[10])+"x"+str(self.B)+"•"+str(self.mB[6])+"+"+str(self.B)+"•"+str(self.mB[11])+"x"+str(self.B)+"•"+str(self.mB[9]), str(self.A)+"•"+str(self.mA[8])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[9])+"x"+str(self.B)+"•"+str(self.mB[4])+"+"+str(self.A)+"•"+str(self.mA[10])+"x"+str(self.B)+"•"+str(self.mB[7])+"+"+str(self.A)+"•"+str(self.mA[11])+"x"+str(self.B)+"•"+str(self.mB[10]), str(self.A)+"•"+str(self.mA[8])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[9])+"x"+str(self.B)+"•"+str(self.mB[5])+"+"+str(self.A)+"•"+str(self.mA[10])+"x"+str(self.B)+"•"+str(self.mB[8])+"+"+str(self.A)+"•"+str(self.mA[11])+"x"+str(self.B)+"•"+str(self.mB[11]))
            elif self.d == 41:
                step = (str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[0]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[1]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[2]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[3]), str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[0]), str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[1]), str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[2]), str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[3]), str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[0]), str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[1]), str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[2]), str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[3]), str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[0]), str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[1]), str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[2]), str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[3]))
            elif self.d == 42:
                step = (str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[4]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[5]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[6]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[7]), str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[4]), str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[5]), str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[6]), str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[7]), str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[4]), str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[5]), str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[6]), str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[7]), str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[4]), str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[5]), str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[6]), str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[7]))
            elif self.d == 43:
                step = (str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[4])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[8]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[5])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[9]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[6])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[10]),  str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[7])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[11]), str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[4])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[8]), str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[5])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[9]), str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[6])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[10]),  str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[7])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[11]), str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[4])+"+"+str(self.A)+"•"+str(self.mA[8])+"x"+str(self.B)+"•"+str(self.mB[8]), str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[5])+"+"+str(self.A)+"•"+str(self.mA[8])+"x"+str(self.B)+"•"+str(self.mB[9]), str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[6])+"+"+str(self.A)+"•"+str(self.mA[8])+"x"+str(self.B)+"•"+str(self.mB[10]),  str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[7])+"+"+str(self.A)+"•"+str(self.mA[8])+"x"+str(self.B)+"•"+str(self.mB[11]), str(self.A)+"•"+str(self.mA[9])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[10])+"x"+str(self.B)+"•"+str(self.mB[4])+"+"+str(self.A)+"•"+str(self.mA[11])+"x"+str(self.B)+"•"+str(self.mB[8]), str(self.A)+"•"+str(self.mA[9])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[10])+"x"+str(self.B)+"•"+str(self.mB[5])+"+"+str(self.A)+"•"+str(self.mA[11])+"x"+str(self.B)+"•"+str(self.mB[9]), str(self.A)+"•"+str(self.mA[9])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[10])+"x"+str(self.B)+"•"+str(self.mB[6])+"+"+str(self.A)+"•"+str(self.mA[11])+"x"+str(self.B)+"•"+str(self.mB[10]),  str(self.A)+"•"+str(self.mA[9])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[10])+"x"+str(self.B)+"•"+str(self.mB[7])+"+"+str(self.A)+"•"+str(self.mA[11])+"x"+str(self.B)+"•"+str(self.mB[11]))
            elif self.d == 44:
                step = (str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[4])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[8])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[12]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[5])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[9])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[13]), str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[6])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[10])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[14]),  str(self.A)+"•"+str(self.mA[0])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[1])+"x"+str(self.B)+"•"+str(self.mB[7])+"+"+str(self.A)+"•"+str(self.mA[2])+"x"+str(self.B)+"•"+str(self.mB[11])+"+"+str(self.A)+"•"+str(self.mA[3])+"x"+str(self.B)+"•"+str(self.mB[15]), str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[4])+"+"+str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[8])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[12]), str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[5])+"+"+str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[9])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[13]), str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[6])+"+"+str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[10])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[14]), str(self.A)+"•"+str(self.mA[4])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[5])+"x"+str(self.B)+"•"+str(self.mB[7])+"+"+str(self.A)+"•"+str(self.mA[6])+"x"+str(self.B)+"•"+str(self.mB[11])+"+"+str(self.A)+"•"+str(self.mA[7])+"x"+str(self.B)+"•"+str(self.mB[15]),
                str(self.A)+"•"+str(self.mA[8])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[9])+"x"+str(self.B)+"•"+str(self.mB[4])+"+"+str(self.A)+"•"+str(self.mA[10])+"x"+str(self.B)+"•"+str(self.mB[8])+"+"+str(self.A)+"•"+str(self.mA[11])+"x"+str(self.B)+"•"+str(self.mB[12]), str(self.A)+"•"+str(self.mA[8])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[9])+"x"+str(self.B)+"•"+str(self.mB[5])+"+"+str(self.A)+"•"+str(self.mA[10])+"x"+str(self.B)+"•"+str(self.mB[9])+"+"+str(self.A)+"•"+str(self.mA[11])+"x"+str(self.B)+"•"+str(self.mB[13]), str(self.A)+"•"+str(self.mA[8])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[9])+"x"+str(self.B)+"•"+str(self.mB[6])+"+"+str(self.A)+"•"+str(self.mA[10])+"x"+str(self.B)+"•"+str(self.mB[10])+"+"+str(self.A)+"•"+str(self.mA[11])+"x"+str(self.B)+"•"+str(self.mB[14]),  str(self.A)+"•"+str(self.mA[8])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[9])+"x"+str(self.B)+"•"+str(self.mB[7])+"+"+str(self.A)+"•"+str(self.mA[10])+"x"+str(self.B)+"•"+str(self.mB[11])+"+"+str(self.A)+"•"+str(self.mA[11])+"x"+str(self.B)+"•"+str(self.mB[15]), str(self.A)+"•"+str(self.mA[12])+"x"+str(self.B)+"•"+str(self.mB[0])+"+"+str(self.A)+"•"+str(self.mA[13])+"x"+str(self.B)+"•"+str(self.mB[4])+"+"+str(self.A)+"•"+str(self.mA[14])+"x"+str(self.B)+"•"+str(self.mB[8])+"+"+str(self.A)+"•"+str(self.mA[15])+"x"+str(self.B)+"•"+str(self.mB[12]), str(self.A)+"•"+str(self.mA[12])+"x"+str(self.B)+"•"+str(self.mB[1])+"+"+str(self.A)+"•"+str(self.mA[13])+"x"+str(self.B)+"•"+str(self.mB[5])+"+"+str(self.A)+"•"+str(self.mA[14])+"x"+str(self.B)+"•"+str(self.mB[9])+"+"+str(self.A)+"•"+str(self.mA[15])+"x"+str(self.B)+"•"+str(self.mB[13]), str(self.A)+"•"+str(self.mA[12])+"x"+str(self.B)+"•"+str(self.mB[2])+"+"+str(self.A)+"•"+str(self.mA[13])+"x"+str(self.B)+"•"+str(self.mB[6])+"+"+str(self.A)+"•"+str(self.mA[14])+"x"+str(self.B)+"•"+str(self.mB[10])+"+"+str(self.A)+"•"+str(self.mA[15])+"x"+str(self.B)+"•"+str(self.mB[14]),  str(self.A)+"•"+str(self.mA[12])+"x"+str(self.B)+"•"+str(self.mB[3])+"+"+str(self.A)+"•"+str(self.mA[13])+"x"+str(self.B)+"•"+str(self.mB[7])+"+"+str(self.A)+"•"+str(self.mA[14])+"x"+str(self.B)+"•"+str(self.mB[11])+"+"+str(self.A)+"•"+str(self.mA[15])+"x"+str(self.B)+"•"+str(self.mB[15]))
            else:
                step = 0
            mat = self.MStepM(step)
        exp = self.MatBrk(mat)
        return exp
    def Mat2D(self, arr):
        return str(arr).replace('[[', '  ⎾ ').replace(']]', '⏌').replace('[', ' ⎿ ').replace(']', '⏋')
    def Mat3D(self, arr):
        return str(arr).replace('[[', ' ⎾ ').replace(']]', ' ⏌').replace('[', '⎹  ').replace(']', ' ⎹')
    def MultiplyBy(self):
        if self.mA!=0 and self.A==0 or self.mA!=0 and self.A==1:
            exp = "Please try another number"
        else:
            if self.d == 2:
                exp2D = np.array(self.mA).reshape(self.d, self.d)
                exp = "[A] = \n"+self.Mat2D(np.round(exp2D,3))+"\n\n"+str(self.A)+" x [A] =\n"+self.Mat2D(np.round(self.A*exp2D,3))
            elif self.d == 3:
                exp3D = np.array(self.mA).reshape(self.d, self.d)
                exp = "[A] = \n"+self.Mat3D(np.round(exp3D,3)) +"\n\n"+str(self.A)+" x [A] =\n"+ self.Mat3D(np.round(self.A *exp3D,3))
            elif self.d == 4:
                exp4D = np.array(self.mA).reshape(self.d, self.d)
                exp = "[A] = \n"+self.Mat3D(np.round(exp4D,3))+"\n\n"+str(self.A)+" x [A] =\n"+self.Mat3D(np.round(self.A*exp4D,3))
            else:
                exp="Please choose a \ndimension before compute"
        return exp
    def PowerBy(self):
        cal = 1
        if self.mA!=0 and self.B==0 or self.mA!=0 and self.B==1:
            exp = "Please try another number"
        else:
            if self.d == 2:
                exp2D = np.array(self.mA).reshape(self.d, self.d)
                for i in range (int(self.B)):
                    cal = np.dot(exp2D,cal)
                exp = "[A] = \n"+self.Mat2D(exp2D)+"\n\n[A]^"+str(self.B)+" = \n"+self.Mat2D(np.round(cal,3))
            elif self.d == 3:
                exp3D = np.array(self.mA).reshape(self.d, self.d)
                for i in range (int(self.B)):
                    cal = np.dot(exp3D,cal)
                exp = "[A] = \n"+self.Mat3D(exp3D)+"\n\n[A]^"+str(self.B)+" = \n"+self.Mat3D(np.round(cal,3))
            elif self.d == 4:
                exp4D = np.array(self.mA).reshape(self.d, self.d)
                for i in range (int(self.B)):
                    cal = np.dot(exp4D,cal)
                exp = "[A] = \n"+self.Mat3D(exp4D)+"\n\n[A]^"+str(self.B)+" = \n"+self.Mat3D(np.round(cal,3))
            else:
                exp="Please choose a \ndimension before compute"
        return exp