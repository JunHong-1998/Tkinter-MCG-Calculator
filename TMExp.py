import numpy as np
import math
class Transformation:

    def __init__(self, Mat, Tsf1, Tsf2, Tsf3, Value1, Value2, Value3):
        self.xy = Mat
        self.T1 = Tsf1
        self.T2 = Tsf2
        self.T3 = Tsf3
        self.V1 = Value1
        self.V2 = Value2
        self.V3 = Value3
        np.set_printoptions(precision=3)

    def __del__(self):
        class_name=self.__class__.__name__

    def XY(self):
        return np.array(self.xy).reshape(3,1)

    def Tsl1(self, a, b):
        return np.array([1, 0, a, 0, 1, b, 0, 0, 1]).reshape(3,3)
    def Rtt2(self, b):
        cal = np.array([math.cos(math.radians(b)), math.sin(math.radians(b)), 0, math.sin(math.radians(-b)),math.cos(math.radians(b)), 0, 0, 0, 1]).reshape(3, 3)
        return cal
    def Rtt3(self, b):
        cal = np.array([math.cos(math.radians(b)), math.sin(math.radians(-b)), 0, math.sin(math.radians(b)), math.cos(math.radians(b)), 0, 0, 0, 1]).reshape(3,3)
        return cal
    def Rfl4(self):
        cal = np.array([1, 0, 0, 0, -1, 0, 0, 0, 1]).reshape(3, 3)
        return cal   
    def Rfl5(self):
        cal = np.array([-1, 0, 0, 0, 1, 0, 0, 0, 1]).reshape(3, 3)
        return cal  
    def Rfl6(self):
        cal = np.array([-1, 0, 0, 0, -1, 0, 0, 0, 1]).reshape(3, 3)
        return cal
    def Scl7(self, a, b):
        cal = np.array([a, 0, 0, 0, b, 0, 0, 0, 1]).reshape(3, 3)
        return cal
    def Shr8(self, b):
        cal = np.array([1, math.tan(math.radians(b)), 0, 0, 1, 0, 0, 0, 1]).reshape(3, 3)
        return cal 
    def Shr9(self, b):
        cal = np.array([1, 0, 0, math.tan(math.radians(b)), 1, 0, 0, 0, 1]).reshape(3, 3)
        return cal
    def TSF1(self):
        if self.T1==1:
            cal = self.Tsl1(self.V1[0], self.V1[1])
        elif self.T1==2:
            cal = self.Rtt2(self.V1)
        elif self.T1==3:
            cal = self.Rtt3(self.V1)
        elif self.T1==4:
            cal = self.Rfl4()
        elif self.T1==5:
            cal = self.Rfl5()
        elif self.T1==6:
            cal = self.Rfl6()
        elif self.T1==7:
            cal = self.Scl7(self.V1[0], self.V1[1])
        elif self.T1==8:
            cal = self.Shr8(self.V1)
        elif self.T1==9:
            cal = self.Shr9(self.V1)
        else:
            cal = 0
        return cal
    def TSF2(self):
        if self.T2==1:
            cal = self.Tsl1(self.V2[0], self.V2[1])
        elif self.T2==2:
            cal = self.Rtt2(self.V2)
        elif self.T2==3:
            cal = self.Rtt3(self.V2)
        elif self.T2==4:
            cal = self.Rfl4()
        elif self.T2==5:
            cal = self.Rfl5()
        elif self.T2==6:
            cal = self.Rfl6()
        elif self.T2==7:
            cal = self.Scl7(self.V2[0], self.V2[1])
        elif self.T2==8:
            cal = self.Shr8(self.V2)
        elif self.T2==9:
            cal = self.Shr9(self.V2)
        else:
            cal = 0
        return cal
    def TSF3(self):
        if self.T3==1:
            cal = self.Tsl1(self.V3[0], self.V3[1])
        elif self.T3==2:
            cal = self.Rtt3(self.V3)
        elif self.T3==3:
            cal = self.Rtt3(self.V3)
        elif self.T3==4:
            cal = self.Rfl4()
        elif self.T3==5:
            cal = self.Rfl5()
        elif self.T3==6:
            cal = self.Rfl6()
        elif self.T3==7:
            cal = self.Scl7(self.V3[0], self.V3[1])
        elif self.T3==8:
            cal = self.Shr8(self.V3)
        elif self.T3==9:
            cal = self.Shr9(self.V3)
        else:
            cal = 0
        return cal
    def CT1(self):
        try:
            cal = np.dot(self.TSF1(),self.XY())
            return self.MatBrk(np.round(cal,2))
        except:
            return "E\nR\nR\nO\nR"
    def CT2(self):
        try:
            cal = np.dot(np.dot(self.TSF1(), self.TSF2()), self.XY())
            return self.MatBrk(np.round(cal, 2))
        except:
            return "E\nR\nR\nO\nR"
    def CT3(self):
        try:
            cal = np.dot(np.dot(np.dot(self.TSF1(), self.TSF2()), self.TSF3()), self.XY())
            return self.MatBrk(np.round(cal, 2))
        except:
            return "E\nR\nR\nO\nR"
    def MatBrk(self, arr):
        return str(arr).replace('[[', '').replace(']]', '').replace('[', '').replace(']', '')
            
            

