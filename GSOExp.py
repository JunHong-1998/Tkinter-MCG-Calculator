import numpy as np
class GSOExp:
    exp1=""
    exp2=""
    exp3=""
    exp4=""
    exp5=""
    e1 = ""
    e2 = ""
    e3 = ""
    e4 = ""
    e5 = ""

    def __init__(self, Vec, Dim, Vec1, Vec2, Vec3, Vec4, Vec5):
        self.Vsize = Vec
        self.DIM = Dim
        self.V1 = Vec1
        self.V2 = Vec2
        self.V3 = Vec3
        self.V4 = Vec4
        self.V5 = Vec5
        np.set_printoptions(precision=3)

    def __del__(self):
        class_name=self.__class__.__name__

    def MatBrkt(self, arr):
        return str(np.round(arr,3)).replace('[[', '[').replace(']]', ']')
    

    def GSOcalc(self):
        u1 = np.array(self.V1).reshape(1, self.DIM)
        GSOExp.e1 = u1 / np.linalg.norm(u1)
        GSOExp.exp1 = "V1 = "+self.MatBrkt(u1)+"\tu1 = "+self.MatBrkt(u1)
        exp = GSOExp.exp1
        if self.Vsize>=2:
            V2 = np.array(self.V2).reshape(1, self.DIM)
            V2e1 = np.sum(V2*GSOExp.e1)
            u2 = V2 - V2e1*GSOExp.e1
            GSOExp.e2 = u2 / np.linalg.norm(u2)
            GSOExp.exp2 = "V2 = "+self.MatBrkt(V2)+"\t<V2,e1> = "+str(round(V2e1,3))+"\nu2 = V2 - <V2,e1>e1 \nu2 = "+self.MatBrkt(u2)
            exp = GSOExp.exp2
        if self.Vsize>=3:
            V3 = np.array(self.V3).reshape(1, self.DIM)
            V3e1 = np.sum(V3*GSOExp.e1)
            V3e2 = np.sum(V3*GSOExp.e2)
            u3 = V3 - V3e2*GSOExp.e2 - V3e1*GSOExp.e1
            GSOExp.e3 = u3 / np.linalg.norm(u3)
            GSOExp.exp3 = "V3 = "+self.MatBrkt(V3)+"\n<V3,e2> = "+str(round(V3e2,3))+"\t\t<V3,e1> = "+str(round(V3e1,3))+"\nu3 = V3 - <V3,e2>e2 - <V3,e1>e1\nu3 = " +self.MatBrkt(u3)
            exp = GSOExp.exp3
        if self.Vsize>=4:
            V4 = np.array(self.V4).reshape(1, self.DIM)
            V4e1 = np.sum(V4*GSOExp.e1)
            V4e2 = np.sum(V4*GSOExp.e2)
            V4e3 = np.sum(V4*GSOExp.e3)
            u4 = V4 - V4e3*GSOExp.e3 - V4e2*GSOExp.e2 - V4e1*GSOExp.e1
            GSOExp.e4 = u4 / np.linalg.norm(u4)
            GSOExp.exp4 = "V4 = "+self.MatBrkt(V4)+"\t<V4,e3> = "+str(round(V4e3,3))+"\n<V4,e2> = "+str(round(V4e2,3))+"\t\t<V4e1> = "+str(round(V4e1,3))+"\nu4 = V4 - <V4,e3>e3 - <V4,e2>e2 - <V4,e1>e1\nu4 = "+self.MatBrkt(u4)
            exp = GSOExp.exp4
        if self.Vsize == 5:
            V5 = np.array(self.V5).reshape(1, self.DIM)
            V5e1 = np.sum(V5*GSOExp.e1)
            V5e2 = np.sum(V5*GSOExp.e2)
            V5e3 = np.sum(V5*GSOExp.e3)
            V5e4 = np.sum(V5*GSOExp.e4)
            u5 = V5 - V5e4*GSOExp.e4 - V5e3*GSOExp.e3 - V5e2*GSOExp.e2 - V5e1*GSOExp.e1
            GSOExp.e5 = u5 / np.linalg.norm(u5)
            GSOExp.exp5 = "V5 = "+self.MatBrkt(V5)+"\n<V5,e4> = "+str(round(V5e4,3))+"\t\t<V5e3> = "+str(round(V5e3,3))+"\n<V5e2> = "+str(round(V5e2,3))+"\t\t<V5e1> = "+str(round(V5e1,3))+"\nu5 = V5 - <V5,e4>e4 - <V5,e3>e3 - \n         <V5,e2>e2 - <V5,e1>e1\nu5 = "+self.MatBrkt(u5)
            exp = GSOExp.exp5
    
    def U1(self):
        self.GSOcalc()
        return GSOExp.exp1
    def U2(self):
        self.GSOcalc()
        return GSOExp.exp2
    def U3(self):
        self.GSOcalc()
        return GSOExp.exp3
    def U4(self):
        self.GSOcalc()
        return GSOExp.exp4
    def U5(self):
        self.GSOcalc()
        return GSOExp.exp5
    
    def E1(self):
        self.GSOcalc()
        return "e1 = "+self.MatBrkt(GSOExp.e1)
    def E2(self):
        self.GSOcalc()
        return "e2 = "+self.MatBrkt(GSOExp.e2)
    def E3(self):
        self.GSOcalc()
        return "e3 = "+self.MatBrkt(GSOExp.e3)
    def E4(self):
        self.GSOcalc()
        return "e4 = "+self.MatBrkt(GSOExp.e4)
    def E5(self):
        self.GSOcalc()
        return "e5 = "+self.MatBrkt(GSOExp.e5)
    
    