import math
class TwoDExpl:

    def __init__(self, Vec1, Vec2):
        self.v1 = Vec1
        self.v2 = Vec2

    def __del__(self):
        class_name = self.__class__.__name__

    def Addition(self):
        Cal = (round(self.v1[0]+self.v2[0],2),round(self.v1[1]+self.v2[1],2))
        return "v1 = (a1,a2) \t v2 = (b1,b2) \nv = (a1+b1,a2+b2) \nv = ("+str(self.v1[0])+"+"+str(self.v2[0])+","+str(self.v1[1])+"+"+str(self.v2[1])+") \nv = "+str(Cal)

    def Difference(self):
        Cal = (round(self.v1[0]-self.v2[0],2),round(self.v1[1]-self.v2[1],2))
        return "v1 = (a1,a2) \t v2 = (b1,b2) \nv = (a1-b1,a2-b2) \nv = ("+str(self.v1[0])+"-"+str(self.v2[0])+","+str(self.v1[1])+"-"+str(self.v2[1])+") \nv = "+str(Cal)

    def Scalar(self):
        Cal = round((self.v1[0]*self.v2[0] + self.v1[1]*self.v2[1]),2)
        return "v1 = (a1,a2) \t v2 = (b1,b2) \nv1•v2 = a1•b1+a2•b2 \nv1•v2 = "+str(self.v1[0])+"•"+str(self.v2[0])+"+"+str(self.v1[1])+"•"+str(self.v2[1])+\
            " \nv1•v2 = "+str(round(self.v1[0]*self.v2[0],3))+"+"+str(round(self.v1[1]*self.v2[1],3))+" \nv1•v2 = "+str(Cal)

    def Angle(self):
        Cal = round(math.degrees(math.acos((self.v1[0]*self.v2[0]+self.v1[1]*self.v2[1])/(math.sqrt(self.v1[0]*self.v1[0]+self.v1[1]*self.v1[1])*math.sqrt(self.v2[0]*self.v2[0]+self.v2[1]*self.v2[1])))),2)
        return "v1 = (a1,a2) \t v2 = (b1,b2) \ncos θ = v1•v2/||v1||•||v2|| \nv1•v2 = "+str(self.v1[0])+"•"+str(self.v2[0])+"+"+str(self.v1[1])+"•"+str(self.v2[1])+\
               " \tv1•v2 = "+str(round(self.v1[0]*self.v2[0] + self.v1[1]*self.v2[1],3))+" \n||v1|| = √a1²+a2² \t ||v2|| = √b1²+b2² \n||v1|| = √"+str(round(self.v1[0]*self.v1[0],3))+"+"+\
               str(round(self.v1[1]*self.v1[1],3))+" \t||v2|| = √"+str(round(self.v2[0]*self.v2[0],3))+"+"+str(round(self.v2[1]*self.v2[1],3))+"\ncos θ = "+str(round(self.v1[0]*self.v2[0] + self.v1[1]*self.v2[1],3))+\
               " / "+str(round(math.sqrt(self.v1[0]*self.v1[0] + self.v1[1]*self.v1[1]),3))+" • "+str(round(math.sqrt(self.v2[0]*self.v2[0] +self.v2[1]*self.v2[1]),3))+" \nθ = "+str(Cal)

    def Magnitude(self):
        Cal = round(math.sqrt(self.v1[0]*self.v1[0] + self.v1[1]*self.v1[1]),2)
        return "v1 = (a1,a2) \n||v|| = √a1²+a2² \n||v|| = √"+str(round(self.v1[0]*self.v1[0],3))+"+"+str(round(self.v1[1]*self.v1[1],3))+"\n||v|| = "+str(Cal)

    def UnitVector(self):
        Cal = (round((1/math.sqrt(self.v1[0]*self.v1[0] + self.v1[1]*self.v1[1]))*self.v1[0],2), round((1/math.sqrt(self.v1[0]*self.v1[0] + self.v1[1]*self.v1[1]))*self.v1[1],2))
        return "v1 = (a1,a2) \nv = v/|v| \n|v| = √a1²+a2² \t|v| = √"+str(round(self.v1[0]*self.v1[0],3))+"+"+str(round(self.v1[1]*self.v1[1],3))+" \n|v| = (1/"+str(round(math.sqrt(self.v1[0]*self.v1[0] +\
            self.v1[1]*self.v1[1]),3))+") • ("+str(self.v1[0])+","+str(self.v1[1])+") \nv = "+str(Cal)

    def Independency(self):
        Cal = round(self.v1[0] * self.v2[1] - self.v2[0] * self.v1[1],2)
        if Cal!=0:
            Conclu = "Since D≠0, it can be conclude that \nv1 and v2 are linearly independent."
        else:
            Conclu = "Since D=0, it can be conclude that \nv1 and v2 are linearly dependent."
        return "D = | "+str(self.v1[0])+"\t"+str(self.v1[1])+" | \n      | "+str(self.v2[0])+"\t"+str(self.v2[1])+" | \nD = "+str(self.v1[0])+"•"+str(self.v2[1])+"-"+str(self.v2[0])+"•"+\
            str(self.v1[1])+" \nD = "+str(Cal)+" \n"+Conclu

    def Orthogonality(self):
        Cal = (round(self.v1[0]*self.v2[0] + self.v1[1]*self.v2[1],2), round(math.sqrt(self.v1[0]*self.v1[0] + self.v1[1]*self.v1[1]),2), round(math.sqrt(self.v2[0]*self.v2[0] + self.v2[1]*self.v2[1]),2))
        Sg1 = self.Sign2(Cal[0])
        Sg2 = self.Sign2(Cal[1])
        Sg3 = self.Sign2(Cal[2])
        if Cal[0]==0 and Cal[1]!=0 and Cal[2]!=0:
            Conclu = "Since v1•v2"+str(Sg1)+"0, ||v1||"+str(Sg2)+"0 and ||v2||"+str(Sg3)+"0, \nit can be conclude that v1 and v2 \nare perpendicular to one another."
        else:
            Conclu = "Since v1•v2"+str(Sg1)+"0, ||v1||"+str(Sg2)+"0 and ||v2||"+str(Sg3)+"0, \nit can be conclude that v1 and v2 \nare not perpendicular to one another."
        return "v1 = (a1,a2) \t v2 = (b1,b2) \nv1•v2 = ||v1||||v2||cos θ \tv1•v2 = "+str(Cal[0])+" \n||v1|| = √a1²+a2² \t||v1|| = "+str(Cal[1])+" \n||v2|| = √b1²+b2² \t||v2|| = "+str(Cal[2])+\
            " \n"+Conclu
    def Sign2(self, value):
        if value == 0:
            sg = "="
        else:
            sg = "≠"
        return sg

    def Parallelism(self):
        Cal = (round(self.v1[0]*self.v2[0] + self.v1[1]*self.v2[1],2), round(math.sqrt(self.v1[0]*self.v1[0] + self.v1[1]*self.v1[1])*math.sqrt(self.v2[0]*self.v2[0] + self.v2[1]*self.v2[1]),2))
        if Cal[0]==Cal[1]:
            Conclu = "Since v1•v2=||v1||||v2||, then cos θ = 1, so θ = 0 \nit can be conclude that v1 and v2 \nare parallel to one another."
        else:
            Conclu = "Since v1•v2≠||v1||||v2||, then cos θ ≠ 1, so θ ≠ 0 \nit can be conclude that v1 and v2 \nare not parallel to one another."
        return "v1 = (a1,a2) \t v2 = (b1,b2) \nv1•v2 = ||v1||||v2||cos θ \tv1•v2 = "+str(Cal[0])+" \n||v1||||v2|| = √a1²+a2²•√b1²+b2² \n||v1||||v2|| = "+str(Cal[1])+" \n"+Conclu
