import numpy as np
class SingleMatrix:

    def __init__(self, Mat, Dim):
        self.m = Mat
        self.d = Dim
        np.set_printoptions(precision=3)

    def __del__(self):
        class_name=self.__class__.__name__

    def BrcktF(self, ar):
        return str(ar).replace('[[', '⎾ ').replace(']]', '\n').replace('[', '⎸ ').replace(']', '')
    def BrcktI(self, ar):
        return str(ar).replace('[[', ' ⎸ ').replace(']]', ' ⏌\n').replace('[', '⎸ ').replace(']', ' ⎹')
    def Mat2D(self, arr):
        return str(arr).replace('[[', '  ⎾ ').replace(']]', '⏌').replace('[', ' ⎿ ').replace(']', '⏋')
    def Mat3D(self, arr):
        return str(arr).replace('[[', ' ⎾ ').replace(']]', ' ⏌').replace('[', '⎹  ').replace(']', ' ⎹')
    def MatDtm(self, arr):
        return str(arr).replace('[[', ' | ').replace(']]', '   |').replace('[', '      | ').replace(']', '   |')

    def Determinant(self):
        if self.d==2:
            cal = round(self.m[0]*self.m[3]-self.m[2]*self.m[1],2)
            exp2D = np.array(self.m).reshape(self.d, self.d)
            exp = "D ="+self.MatDtm(exp2D)+"\n\n\n D = "+str(self.m[0])+"•"+str(np.round(self.m[3],3))+" - "+str(np.round(self.m[2],3))+"•"+str(np.round(self.m[1],3))+"\n\n\n D = "+str(cal)
        elif self.d==3:
            cal = round(self.m[0]*(self.m[4]*self.m[8]-self.m[7]*self.m[5])-self.m[1]*(self.m[3]*self.m[8]-self.m[6]*self.m[5])+self.m[2]*(self.m[3]*self.m[7]-self.m[6]*self.m[4]),2)
            exp3D = np.array(self.m).reshape(self.d, self.d)
            exp = "D ="+self.MatDtm(exp3D)+\
                  "\n\n D = "+str(self.m[0])+"("+str(np.round(self.m[4],3))+"•"+str(np.round(self.m[8],3))+"-"+str(np.round(self.m[7],3))+"•"+str(np.round(self.m[5],3))+") \n    - "+str(np.round(self.m[1],3))+"("+str(np.round(self.m[3],3))+\
                  "•"+str(np.round(self.m[8],3))+"-"+str(np.round(self.m[6],3))+"•"+str(np.round(self.m[5],3))+") \n    + "+str(np.round(self.m[2],3))+"("+str(np.round(self.m[3],3))+"•"+str(np.round(self.m[7],3))+"-"+str(np.round(self.m[6],3))+"•"+str(np.round(self.m[4],3))+")\n\n D = "+str(cal)
        elif self.d==4:
            cal = round(self.m[0]*self.m[5]*self.m[10]*self.m[15]-self.m[0]*self.m[5]*self.m[11]*self.m[14]-self.m[0]*self.m[6]*self.m[9]*self.m[15]+self.m[0]*self.m[6]*self.m[11]*self.m[13]+self.m[0]*self.m[7]*self.m[9]*self.m[14]-self.m[0]*self.m[7]*self.m[10]*self.m[13]\
                -self.m[1]*self.m[4]*self.m[10]*self.m[15]+self.m[1]*self.m[4]*self.m[11]*self.m[14]+self.m[1]*self.m[6]*self.m[8]*self.m[15]-self.m[1]*self.m[6]*self.m[11]*self.m[12]-self.m[1]*self.m[7]*self.m[8]*self.m[14]+self.m[1]*self.m[7]*self.m[10]*self.m[12]\
                +self.m[2]*self.m[4]*self.m[9]*self.m[15]-self.m[2]*self.m[4]*self.m[11]*self.m[13]-self.m[2]*self.m[5]*self.m[8]*self.m[15]+self.m[2]*self.m[5]*self.m[11]*self.m[12]+self.m[2]*self.m[7]*self.m[8]*self.m[13]-self.m[2]*self.m[7]*self.m[9]*self.m[12]\
                -self.m[3]*self.m[4]*self.m[9]*self.m[14]+self.m[3]*self.m[4]*self.m[10]*self.m[13]+self.m[3]*self.m[5]*self.m[8]*self.m[14]-self.m[3]*self.m[5]*self.m[10]*self.m[12]-self.m[3]*self.m[6]*self.m[8]*self.m[13]+self.m[3]*self.m[6]*self.m[9]*self.m[12],2)
            exp4D = np.array(self.m).reshape(self.d, self.d)
            exp = "D ="+self.MatDtm(exp4D)+\
                  "\n\n D = "+str(np.round(self.m[0],3))+"•"+str(np.round(self.m[5],3))+"•"+str(np.round(self.m[10],3))+"•"+str(np.round(self.m[15],3))+\
                  "-"+str(np.round(self.m[0],3))+"•"+str(np.round(self.m[5],3))+"•"+str(np.round(self.m[11],3))+"•"+str(np.round(self.m[14],3))+\
                  "\n    -"+str(np.round(self.m[0],3))+"•"+str(np.round(self.m[6],3))+"•"+str(np.round(self.m[9],3))+"•"+str(np.round(self.m[15],3))+\
                  "+"+str(np.round(self.m[0],3))+"•"+str(np.round(self.m[6],3))+"•"+str(np.round(self.m[11],3))+"•"+str(np.round(self.m[13],3))+\
                  "\n    +"+str(np.round(self.m[0],3))+"•"+str(np.round(self.m[7],3))+"•"+str(np.round(self.m[9],3))+"•"+str(np.round(self.m[14],3))+\
                  "-"+str(np.round(self.m[0],3))+"•"+str(np.round(self.m[7],3))+"•"+str(np.round(self.m[10],3))+"•"+str(np.round(self.m[13],3))+\
                  "\n\n    -"+str(np.round(self.m[1],3))+"•"+str(np.round(self.m[4],3))+"•"+str(np.round(self.m[10],3))+"•"+str(np.round(self.m[15],3))+\
                  "+"+str(np.round(self.m[1],3))+"•"+str(np.round(self.m[4],3))+"•"+str(np.round(self.m[11],3))+"•"+str(np.round(self.m[14],3))+\
                  "\n    +"+str(np.round(self.m[1],3))+"•"+str(np.round(self.m[6],3))+"•"+str(np.round(self.m[8],3))+"•"+str(np.round(self.m[15],3))+\
                  "-"+str(np.round(self.m[1],3))+"•"+str(np.round(self.m[6],3))+"•"+str(np.round(self.m[11],3))+"•"+str(np.round(self.m[12],3))+\
                  "\n    -"+str(np.round(self.m[1],3))+"•"+str(np.round(self.m[7],3))+"•"+str(np.round(self.m[8],3))+"•"+str(np.round(self.m[14],3))+\
                  "+"+str(np.round(self.m[1],3))+"•"+str(np.round(self.m[7],3))+"•"+str(np.round(self.m[10],3))+"•"+str(np.round(self.m[12],3))+\
                  "\n\n    +"+str(np.round(self.m[2],3))+"•"+str(np.round(self.m[4],3))+"•"+str(np.round(self.m[9],3))+"•"+str(np.round(self.m[15],3))+\
                  "-"+str(np.round(self.m[2],3))+"•"+str(np.round(self.m[4],3))+"•"+str(np.round(self.m[11],3))+"•"+str(np.round(self.m[13],3))+\
                  "\n    -"+str(np.round(self.m[2],3))+"•"+str(np.round(self.m[5],3))+"•"+str(np.round(self.m[8],3))+"•"+str(np.round(self.m[15],3))+\
                  "+"+str(np.round(self.m[2],3))+"•"+str(np.round(self.m[5],3))+"•"+str(np.round(self.m[11],3))+"•"+str(np.round(self.m[12],3))+\
                  "\n    +"+str(np.round(self.m[2],3))+"•"+str(np.round(self.m[7],3))+"•"+str(np.round(self.m[8],3))+"•"+str(np.round(self.m[13],3))+\
                  "-"+str(np.round(self.m[2],3))+"•"+str(np.round(self.m[7],3))+"•"+str(np.round(self.m[9],3))+"•"+str(np.round(self.m[12],3))+\
                  "\n\n    -"+str(np.round(self.m[3],3))+"•"+str(np.round(self.m[4],3))+"•"+str(np.round(self.m[9],3))+"•"+str(np.round(self.m[14],3))+\
                  "+"+str(np.round(self.m[3],3))+"•"+str(np.round(self.m[4],3))+"•"+str(np.round(self.m[10],3))+"•"+str(np.round(self.m[13],3))+\
                  "\n    +"+str(np.round(self.m[3],3))+"•"+str(np.round(self.m[5],3))+"•"+str(np.round(self.m[8],3))+"•"+str(np.round(self.m[14],3))+\
                  "-"+str(np.round(self.m[3],3))+"•"+str(np.round(self.m[5],3))+"•"+str(np.round(self.m[10],3))+"•"+str(np.round(self.m[2],3))+\
                  "\n    -"+str(np.round(self.m[3],3))+"•"+str(np.round(self.m[6],3))+"•"+str(np.round(self.m[8],3))+"•"+str(np.round(self.m[13],3))+\
                  "+"+str(np.round(self.m[3],3))+"•"+str(np.round(self.m[6],3))+"•"+str(np.round(self.m[9],3))+"•"+str(np.round(self.m[12],3))+\
                  "\n\n D = "+str(cal)
        else:
            exp = "Please choose a \ndimension before compute"
        return exp

    def Inverse(self):
        if self.d == 2:
            dtm = round(self.m[0] * self.m[3] - self.m[2] * self.m[1], 2)
            if dtm!=0:
                exp2D = np.array(self.m).reshape(self.d, self.d)
                cal = round(1/(self.m[0]*self.m[3]-self.m[1]*self.m[2]),3)
                Eq0 = np.array([self.m[3], self.m[1]*-1, self.m[2]*-1, self.m[0]]).reshape(self.d, self.d)
                Eq1 = Eq0 * cal
                exp= "(A) = \n\n\nA⁻¹ =\n"+ "(1 / (" + str(np.round(self.m[0],3)) + "•" + str(np.round(self.m[3],3)) + " - " + str(np.round(self.m[1],3)) + "•" + str(np.round(self.m[2],3)) + "))  x\n\nA⁻¹ = \n" + str(cal)+ " x\n\n\nA⁻¹ = "
            else:
                exp="The determinant is 0,"
        elif self.d == 3:
            dtm = round(self.m[0]*(self.m[4]*self.m[8]-self.m[7]*self.m[5])-self.m[1]*(self.m[3]*self.m[8]-self.m[6]*self.m[5])+self.m[2]*(self.m[3]*self.m[7]-self.m[6]*self.m[4]),2)
            if dtm!=0:
                Eq0 = np.array(self.m).reshape(self.d, self.d)
                if Eq0[0,0]==0 and Eq0[1,0]!=0:
                    Eq1 = np.array([Eq0[1], Eq0[0], Eq0[2]])
                elif Eq0[0,0]==0 and Eq0[2,0]!=0:
                    Eq1 = np.array([Eq0[2], Eq0[1], Eq0[0]])
                else:
                    Eq1 = np.array([Eq0[0], Eq0[1] - Eq0[0] * Eq0[1, 0] / Eq0[0, 0], Eq0[2]])
                if Eq1[2,0]==0:
                    Eq2 = Eq1
                else:
                    Eq2 = np.array([Eq1[0], Eq1[1], Eq1[2] - Eq1[0] * Eq1[2, 0] / Eq1[0, 0]])
                if Eq2[1,1]==0:
                    Eq3 = np.array([Eq2[0], Eq2[2], Eq2[1]])
                elif Eq2[2,1]==0:
                    Eq3 = Eq2
                else:
                    Eq3 = np.array([Eq2[0], Eq2[1], Eq2[2]-Eq2[1]*Eq2[2,1]/Eq2[1,1]])
                if Eq3[0,2]==0:
                    Eq4 = Eq3
                else:
                    Eq4 = np.array([Eq3[0] - Eq3[2] * Eq3[0, 2] / Eq3[2, 2], Eq3[1], Eq3[2]])
                if Eq4[1,2]==0:
                    Eq5 = Eq4
                else:
                    Eq5 = np.array([Eq4[0], Eq4[1]-Eq4[2]*Eq4[1,2]/Eq4[2,2], Eq4[2]])
                if Eq5[0,1]==0:
                    Eq6 = Eq5
                else:
                    Eq6 = np.array([Eq5[0] - Eq5[1] * Eq5[0, 1] / Eq5[1, 1], Eq5[1], Eq5[2]])
                Eq7 = np.array([Eq6[0]/Eq6[0,0], Eq6[1]/Eq6[1,1], Eq6[2]/Eq6[2,2]])
                exp = "(A|I) = "+self.BrcktF(Eq0)+"\nR₂ - R₁(R₂[2,1]/R₁[1,1])\nR₃ - R₁(R₃[3,1]/R₁[1,1])\n"+self.BrcktF(np.round(Eq2,3))+"\nR₃ - R₂(R₃[3,2]/R₂[2,2]\n"+self.BrcktF(np.round(Eq3,3))+\
                      "\nR₁ - R₃(R₁[1,3]/R₃[3,3])\nR₂ - R₃(R₂[2,3]/R₃[3,3])\n"+self.BrcktF(np.round(Eq5,3))+"\nR₁ - R₂(R₁[1,2]/R₂[2,2])\n"+self.BrcktF(np.round(Eq6,3))+"\nR₁/R₁[1,1];\nR₂/R₂[2,2];\nR₃/R₃[3,3]\n"+self.BrcktF(np.round(Eq7,3))
            else:
                exp="The determinant is 0,\nmatrix is not invertible !"
        elif self.d == 4:
            dtm = round(self.m[0]*self.m[5]*self.m[10]*self.m[15]-self.m[0]*self.m[5]*self.m[11]*self.m[14]-self.m[0]*self.m[6]*self.m[9]*self.m[15]+self.m[0]*self.m[6]*self.m[11]*self.m[13]+self.m[0]*self.m[7]*self.m[9]*self.m[14]-self.m[0]*self.m[7]*self.m[10]*self.m[13]\
                -self.m[1]*self.m[4]*self.m[10]*self.m[15]+self.m[1]*self.m[4]*self.m[11]*self.m[14]+self.m[1]*self.m[6]*self.m[8]*self.m[15]-self.m[1]*self.m[6]*self.m[11]*self.m[12]-self.m[1]*self.m[7]*self.m[8]*self.m[14]+self.m[1]*self.m[7]*self.m[10]*self.m[12]\
                +self.m[2]*self.m[4]*self.m[9]*self.m[15]-self.m[2]*self.m[4]*self.m[11]*self.m[13]-self.m[2]*self.m[5]*self.m[8]*self.m[15]+self.m[2]*self.m[5]*self.m[11]*self.m[12]+self.m[2]*self.m[7]*self.m[8]*self.m[13]-self.m[2]*self.m[7]*self.m[9]*self.m[12]\
                -self.m[3]*self.m[4]*self.m[9]*self.m[14]+self.m[3]*self.m[4]*self.m[10]*self.m[13]+self.m[3]*self.m[5]*self.m[8]*self.m[14]-self.m[3]*self.m[5]*self.m[10]*self.m[12]-self.m[3]*self.m[6]*self.m[8]*self.m[13]+self.m[3]*self.m[6]*self.m[9]*self.m[12],2)
            if dtm!=0:
                Eq0 = np.array(self.m).reshape(self.d, self.d)
                if Eq0[0,0]==0 and Eq0[1,0]!=0:
                    Eq1 = np.array([Eq0[1], Eq0[0], Eq0[2], Eq0[3]])
                elif Eq0[0,0]==0 and Eq0[2,0]!=0:
                    Eq1 = np.array([Eq0[2], Eq0[1], Eq0[0], Eq0[3]])
                elif Eq0[0,0]==0 and Eq0[3,0]!=0:
                    Eq1 = np.array([Eq0[3], Eq0[1], Eq0[2], Eq0[0]])
                elif Eq0[1,0]==0:
                    Eq1 = Eq0
                else:
                    Eq1 = np.array([Eq0[0], Eq0[1] - Eq0[0] * Eq0[1, 0] / Eq0[0, 0], Eq0[2], Eq0[3]])
                if Eq1[2,0]==0:
                    Eq2 = Eq1
                else:
                    Eq2 = np.array([Eq1[0], Eq1[1], Eq1[2] - Eq1[0] * Eq1[2, 0] / Eq1[0, 0], Eq0[3]])
                if Eq2[3,0]==0:
                    Eq3 = Eq2
                else:
                    Eq3 = np.array([Eq2[0], Eq2[1], Eq2[2], Eq2[3] - Eq2[0] * Eq2[3, 0] / Eq2[0, 0]])
                if Eq3[1,1]==0 and Eq3[3,1]!=0:
                    Eq4 = np.array([Eq3[0], Eq3[3], Eq3[2], Eq3[1]])
                elif Eq3[3, 1] == 0:
                    Eq4 = Eq3
                else:
                    Eq4 = np.array([Eq3[0], Eq3[1], Eq3[2], Eq3[3] - Eq3[1] * Eq3[3, 1] / Eq3[1, 1]])
                if Eq4[1,1]==0 and Eq4[2,1]!=0:
                    Eq5 = np.array([Eq4[0], Eq4[2], Eq4[1], Eq4[3]])
                elif Eq4[2,1]==0:
                    Eq5 = Eq4
                else:
                    Eq5 = np.array([Eq4[0], Eq4[1], Eq4[2] - Eq4[1] * Eq4[2, 1] / Eq4[1, 1], Eq4[3]])
                if Eq5[2,2]==0:
                    Eq6 = np.array([Eq5[0], Eq5[1], Eq5[3], Eq5[2]])
                elif Eq5[3,2]==0:
                    Eq6 = Eq5
                else:
                    Eq6 = np.array([Eq5[0], Eq5[1], Eq5[2], Eq5[3] - Eq5[2] * Eq5[3, 2] / Eq5[2, 2]])
                if Eq6[2,3]==0:
                    Eq7 = Eq6
                else:
                    Eq7 = np.array([Eq6[0], Eq6[1], Eq6[2]-Eq6[3]*Eq6[2, 3]/Eq6[3, 3], Eq6[3]])
                if Eq7[1,3]==0:
                    Eq8 = Eq7
                else:
                    Eq8 = np.array([Eq7[0], Eq7[1] - Eq7[3] * Eq7[1, 3] / Eq7[3, 3], Eq7[2], Eq7[3]])
                if Eq8[0,3]==0:
                    Eq9 = Eq8
                else:
                    Eq9 = np.array([Eq8[0] - Eq8[3] * Eq8[0, 3] / Eq8[3, 3], Eq8[1], Eq8[2], Eq8[3]])
                if Eq9[1,2]==0:
                    Eq10 = Eq9
                else:
                    Eq10 = np.array([Eq9[0], Eq9[1] - Eq9[2] * Eq9[1, 2] / Eq9[2, 2], Eq9[2], Eq9[3]])
                if Eq10[0,2]==0:
                    Eq11 = Eq10
                else:
                    Eq11 = np.array([Eq10[0] - Eq10[2] * Eq10[0, 2] / Eq10[2, 2], Eq10[1], Eq10[2], Eq10[3]])
                if Eq11[0,1]==0:
                    Eq12 = Eq11
                else:
                    Eq12 = np.array([Eq11[0] - Eq11[1] * Eq11[0, 1] / Eq11[1, 1], Eq11[1], Eq11[2], Eq11[3]])
                Eq13 = np.array([Eq12[0]/Eq12[0,0], Eq12[1]/Eq12[1,1], Eq12[2]/Eq12[2,2], Eq12[3]/Eq12[3,3]])
                exp = "(A|I) = "+self.BrcktF(np.round(Eq0,3))+"\nR₂ - R₁(R₂[2,1]/R₁[1,1])\nR₃ - R₁(R₃[3,1]/R₁[1,1])\n"+self.BrcktF(np.round(Eq3,3))+"\n\nR₃ - R₂(R₃[3,2]/R₂[2,2]" \
                "\n"+self.BrcktF(np.round(Eq5,3))+"\n\nR₄ - R₂(R₄[4,3]/R₂[2,3])\n"+self.BrcktF(np.round(Eq6,3))+"\n\nR₁ - R₄(R₁[1,4]/R₄[4,4])\nR₂ - R₄(R₂[2,4]/R₄[4,4])\n"+\
                self.BrcktF(np.round(Eq9,3))+"\n\nR₁ - R₃(R₁[1,3]/R₃[3,3])\n"+self.BrcktF(np.round(Eq11,3))+"\n\nR₁ - R₂(R₁[1,2]/R₂[2,2])\n"+self.BrcktF(np.round(Eq12,3))+\
                "\n\nR₁/R₁[1,1];R₂/R₂[2,2]\n"+ self.BrcktF(np.round(Eq13,3))
            else:
                exp="The determinant is 0,\nmatrix is not invertible !"
        else:
            exp = "Please choose\nbefore"
        return exp

    def InverseRight(self):
        if self.d == 2:
            dtm = round(self.m[0] * self.m[3] - self.m[2] * self.m[1], 2)
            if dtm != 0:
                exp2D = np.array(self.m).reshape(self.d, self.d)
                cal = 1 / (self.m[0] * self.m[3] - self.m[1] * self.m[2])
                Eq0 = np.array([self.m[3], self.m[1] * -1, self.m[2] * -1, self.m[0]]).reshape(self.d, self.d)
                Eq1 = Eq0 * cal
                exp = "" + self.Mat2D(exp2D) + "\n\n" + self.Mat2D(Eq0) + "\n\n\n"+ self.Mat2D(Eq0) +"\n\n\n" + self.Mat2D(np.round(Eq1,3))
            else:
                exp = "Matrix is not invertible ! "

        elif self.d == 3:
            dtm = round(self.m[0] * (self.m[4] * self.m[8] - self.m[7] * self.m[5]) - self.m[1] * (self.m[3] * self.m[8] - self.m[6] * self.m[5]) + self.m[2] * (self.m[3] * self.m[7] - self.m[6] * self.m[4]), 2)
            if dtm != 0:
                Eq0 = np.array(self.m).reshape(self.d, self.d)
                EqI0 = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1]).reshape(self.d, self.d)
                if Eq0[0, 0] == 0 and Eq0[1, 0] != 0:
                    Eq1 = np.array([Eq0[1], Eq0[0], Eq0[2]])
                    EqI1 = np.array([EqI0[1], EqI0[0], EqI0[2]])
                elif Eq0[0, 0] == 0 and Eq0[2, 0] != 0:
                    Eq1 = np.array([Eq0[2], Eq0[1], Eq0[0]])
                    EqI1 = np.array([EqI0[2], EqI0[1], EqI0[0]])
                else:
                    Eq1 = np.array([Eq0[0], Eq0[1] - Eq0[0] * Eq0[1, 0] / Eq0[0, 0], Eq0[2]])
                    EqI1 = np.array([EqI0[0], EqI0[1] - EqI0[0] * Eq0[1, 0] / Eq0[0, 0], EqI0[2]])
                if Eq1[2, 0] == 0:
                    Eq2 = Eq1
                    EqI2 = EqI1
                else:
                    Eq2 = np.array([Eq1[0], Eq1[1], Eq1[2] - Eq1[0] * Eq1[2, 0] / Eq1[0, 0]])
                    EqI2 = np.array([EqI1[0], EqI1[1], EqI1[2] - EqI1[0] * Eq1[2, 0] / Eq1[0, 0]])
                if Eq2[1, 1] == 0:
                    Eq3 = np.array([Eq2[0], Eq2[2], Eq2[1]])
                    EqI3 = np.array([EqI2[0], EqI2[2], EqI2[1]])
                elif Eq2[2, 1] == 0:
                    Eq3 = Eq2
                    EqI3 = EqI2
                else:
                    Eq3 = np.array([Eq2[0], Eq2[1], Eq2[2] - Eq2[1] * Eq2[2, 1] / Eq2[1, 1]])
                    EqI3 = np.array([EqI2[0], EqI2[1], EqI2[2] - EqI2[1] * Eq2[2, 1] / Eq2[1, 1]])
                if Eq3[0, 2] == 0:
                    Eq4 = Eq3
                    EqI4 = EqI3
                else:
                    Eq4 = np.array([Eq3[0] - Eq3[2] * Eq3[0, 2] / Eq3[2, 2], Eq3[1], Eq3[2]])
                    EqI4 = np.array([EqI3[0] - EqI3[2] * Eq3[0, 2] / Eq3[2, 2], EqI3[1], EqI3[2]])
                if Eq4[1, 2] == 0:
                    Eq5 = Eq4
                    EqI5 = EqI4
                else:
                    Eq5 = np.array([Eq4[0], Eq4[1] - Eq4[2] * Eq4[1, 2] / Eq4[2, 2], Eq4[2]])
                    EqI5 = np.array([EqI4[0], EqI4[1] - EqI4[2] * Eq4[1, 2] / Eq4[2, 2], EqI4[2]])
                if Eq5[0, 1] == 0:
                    Eq6 = Eq5
                    EqI6 = EqI5
                else:
                    Eq6 = np.array([Eq5[0] - Eq5[1] * Eq5[0, 1] / Eq5[1, 1], Eq5[1], Eq5[2]])
                    EqI6 = np.array([EqI5[0] - EqI5[1] * Eq5[0, 1] / Eq5[1, 1], EqI5[1], EqI5[2]])
                EqI7 = np.array([EqI6[0] / Eq6[0, 0], EqI6[1] / Eq6[1, 1], EqI6[2] / Eq6[2, 2]])
                exp = self.BrcktI(EqI0) +"\n\n\n"+ self.BrcktI(np.round(EqI2,3)) +"\n\n"+ self.BrcktI(np.round(EqI3,3)) +"\n\n\n"+ self.BrcktI(np.round(EqI5,3)) +"\n\n"+ self.BrcktI(np.round(EqI6,3)) +"\n\n\n\n"+self.BrcktI(np.round(EqI7,3))
            else:
                exp=""
        elif self.d == 4:
            dtm = round(self.m[0] * self.m[5] * self.m[10] * self.m[15] - self.m[0] * self.m[5] * self.m[11] * self.m[14] -self.m[0] * self.m[6] * self.m[9] * self.m[15] + self.m[0] * self.m[6] * self.m[11] * self.m[13] +
                self.m[0] * self.m[7] * self.m[9] * self.m[14] - self.m[0] * self.m[7] * self.m[10] * self.m[13] - self.m[1] * self.m[4] * self.m[10] * self.m[15] + self.m[1] * self.m[4] * self.m[11] * self.m[14] +
                self.m[1] * self.m[6] * self.m[8] * self.m[15] - self.m[1] * self.m[6] * self.m[11] * self.m[12] -self.m[1] * self.m[7] * self.m[8] * self.m[14] + self.m[1] * self.m[7] * self.m[10] * self.m[12]
                + self.m[2] * self.m[4] * self.m[9] * self.m[15] - self.m[2] * self.m[4] * self.m[11] * self.m[13] -self.m[2] * self.m[5] * self.m[8] * self.m[15] + self.m[2] * self.m[5] * self.m[11] * self.m[12] +
                self.m[2] * self.m[7] * self.m[8] * self.m[13] - self.m[2] * self.m[7] * self.m[9] * self.m[12] - self.m[3] * self.m[4] * self.m[9] * self.m[14] + self.m[3] * self.m[4] * self.m[10] * self.m[13] +
                self.m[3] * self.m[5] * self.m[8] * self.m[14] - self.m[3] * self.m[5] * self.m[10] * self.m[12] - self.m[3] * self.m[6] * self.m[8] * self.m[13] + self.m[3] * self.m[6] * self.m[9] * self.m[12], 2)
            if dtm != 0:
                Eq0 = np.array(self.m).reshape(self.d, self.d)
                EqI0 = np.array([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]).reshape(self.d, self.d)
                if Eq0[0, 0] == 0 and Eq0[1, 0] != 0:
                    Eq1 = np.array([Eq0[1], Eq0[0], Eq0[2], Eq0[3]])
                    EqI1 = np.array([EqI0[1], EqI0[0], EqI0[2], EqI0[3]])
                elif Eq0[0, 0] == 0 and Eq0[2, 0] != 0:
                    Eq1 = np.array([Eq0[2], Eq0[1], Eq0[0], Eq0[3]])
                    EqI1 = np.array([EqI0[2], EqI0[1], EqI0[0], EqI0[3]])
                elif Eq0[0, 0] == 0 and Eq0[3, 0] != 0:
                    Eq1 = np.array([Eq0[3], Eq0[1], Eq0[2], Eq0[0]])
                    EqI1 = np.array([EqI0[2], EqI0[1], EqI0[0], EqI0[3]])
                elif Eq0[1, 0] == 0:
                    Eq1 = Eq0
                    EqI1 = EqI0
                else:
                    Eq1 = np.array([Eq0[0], Eq0[1] - Eq0[0] * Eq0[1, 0] / Eq0[0, 0], Eq0[2], Eq0[3]])
                    EqI1 = np.array([EqI0[0], EqI0[1] - EqI0[0] * Eq0[1, 0] / Eq0[0, 0], EqI0[2], EqI0[3]])
                if Eq1[2, 0] == 0:
                    Eq2 = Eq1
                    EqI2 = EqI1
                else:
                    Eq2 = np.array([Eq1[0], Eq1[1], Eq1[2] - Eq1[0] * Eq1[2, 0] / Eq1[0, 0], Eq0[3]])
                    EqI2 = np.array([EqI1[0], EqI1[1], EqI1[2] - EqI1[0] * Eq1[2, 0] / Eq1[0, 0], EqI1[3]])
                if Eq2[3, 0] == 0:
                    Eq3 = Eq2
                    EqI3 = EqI2
                else:
                    Eq3 = np.array([Eq2[0], Eq2[1], Eq2[2], Eq2[3] - Eq2[0] * Eq2[3, 0] / Eq2[0, 0]])
                    EqI3 = np.array([EqI2[0], EqI2[1], EqI2[2], EqI2[3] - EqI2[0] * Eq2[3, 0] / Eq2[0, 0]])
                if Eq3[1, 1] == 0 and Eq3[3, 1] != 0:
                    Eq4 = np.array([Eq3[0], Eq3[3], Eq3[2], Eq3[1]])
                    EqI4 = np.array([EqI3[0], EqI3[3], EqI3[2], EqI3[1]])
                elif Eq3[3, 1] == 0:
                    Eq4 = Eq3
                    EqI4 = EqI3
                else:
                    Eq4 = np.array([Eq3[0], Eq3[1], Eq3[2], Eq3[3] - Eq3[1] * Eq3[3, 1] / Eq3[1, 1]])
                    EqI4 = np.array([EqI3[0], EqI3[1], EqI3[2], EqI3[3] - EqI3[1] * Eq3[3, 1] / Eq3[1, 1]])
                if Eq4[1, 1] == 0 and Eq4[2, 1] != 0:
                    Eq5 = np.array([Eq4[0], Eq4[2], Eq4[1], Eq4[3]])
                    EqI5 = np.array([EqI4[0], EqI4[2], EqI4[1], EqI4[3]])
                elif Eq4[2, 1] == 0:
                    Eq5 = Eq4
                    EqI5 = EqI4
                else:
                    Eq5 = np.array([Eq4[0], Eq4[1], Eq4[2] - Eq4[1] * Eq4[2, 1] / Eq4[1, 1], Eq4[3]])
                    EqI5 = np.array([EqI4[0], EqI4[1], EqI4[2] - EqI4[1] * Eq4[2, 1] / Eq4[1, 1], EqI4[3]])
                if Eq5[2, 2] == 0:
                    Eq6 = np.array([Eq5[0], Eq5[1], Eq5[3], Eq5[2]])
                    EqI6 = np.array([EqI5[0], EqI5[1], EqI5[3], EqI5[2]])
                elif Eq5[3, 2] == 0:
                    Eq6 = Eq5
                    EqI6 = EqI5
                else:
                    Eq6 = np.array([Eq5[0], Eq5[1], Eq5[2], Eq5[3] - Eq5[2] * Eq5[3, 2] / Eq5[2, 2]])
                    EqI6 = np.array([EqI5[0], EqI5[1], EqI5[2], EqI5[3] - EqI5[2] * Eq5[3, 2] / Eq5[2, 2]])
                if Eq6[2, 3] == 0:
                    Eq7 = Eq6
                    EqI7 = EqI6
                else:
                    Eq7 = np.array([Eq6[0], Eq6[1], Eq6[2] - Eq6[3] * Eq6[2, 3] / Eq6[3, 3], Eq6[3]])
                    EqI7 = np.array([EqI6[0], EqI6[1], EqI6[2] - EqI6[3] * Eq6[2, 3] / Eq6[3, 3], EqI6[3]])
                if Eq7[1, 3] == 0:
                    Eq8 = Eq7
                    EqI8 = EqI7
                else:
                    Eq8 = np.array([Eq7[0], Eq7[1] - Eq7[3] * Eq7[1, 3] / Eq7[3, 3], Eq7[2], Eq7[3]])
                    EqI8 = np.array([EqI7[0], EqI7[1] - EqI7[3] * Eq7[1, 3] / Eq7[3, 3], EqI7[2], EqI7[3]])
                if Eq8[0, 3] == 0:
                    Eq9 = Eq8
                    EqI9 = EqI8
                else:
                    Eq9 = np.array([Eq8[0] - Eq8[3] * Eq8[0, 3] / Eq8[3, 3], Eq8[1], Eq8[2], Eq8[3]])
                    EqI9 = np.array([EqI8[0] - EqI8[3] * Eq8[0, 3] / Eq8[3, 3], EqI8[1], EqI8[2], EqI8[3]])
                if Eq9[1, 2] == 0:
                    Eq10 = Eq9
                    EqI10 = EqI9
                else:
                    Eq10 = np.array([Eq9[0], Eq9[1] - Eq9[2] * Eq9[1, 2] / Eq9[2, 2], Eq9[2], Eq9[3]])
                    EqI10 = np.array([EqI9[0], EqI9[1] - EqI9[2] * Eq9[1, 2] / Eq9[2, 2], EqI9[2], EqI9[3]])
                if Eq10[0, 2] == 0:
                    Eq11 = Eq10
                    EqI11 = EqI10
                else:
                    Eq11 = np.array([Eq10[0] - Eq10[2] * Eq10[0, 2] / Eq10[2, 2], Eq10[1], Eq10[2], Eq10[3]])
                    EqI11 = np.array([EqI10[0] - EqI10[2] * Eq10[0, 2] / Eq10[2, 2], EqI10[1], EqI10[2], EqI10[3]])
                if Eq11[0, 1] == 0:
                    Eq12 = Eq11
                    EqI12 = EqI11
                else:
                    Eq12 = np.array([Eq11[0] - Eq11[1] * Eq11[0, 1] / Eq11[1, 1], Eq11[1], Eq11[2], Eq11[3]])
                    EqI12 = np.array([EqI11[0] - EqI11[1] * Eq11[0, 1] / Eq11[1, 1], EqI11[1], EqI11[2], EqI11[3]])
                EqI13 = np.array([EqI12[0] / Eq12[0, 0], EqI12[1] / Eq12[1, 1], EqI12[2] / Eq12[2, 2], EqI12[3] / Eq12[3, 3]])
                exp=self.BrcktI(np.round(EqI0,3))+"\n\nR₄ - R₁(R₄[4,1]/R₁[1,1])\n"+self.BrcktI(np.round(EqI3,3))+"\n\n\n"+self.BrcktI(np.round(EqI5,3))+"\n\nR₄- R₂(R₄[4,2]/R₂[2,2]\n"+self.BrcktI(np.round(EqI6,3))+"\n\n\nR₃ - R₄(R₂[3,4]/R₄[4,4])\n"+\
                self.BrcktI(np.round(EqI9,3))+"\n\nR₂ - R₃(R₁[2,3]/R₃[3,3])\n"+self.BrcktI(np.round(EqI11,3))+"\n\n\n"+self.BrcktI(np.round(EqI12,3))+"    \n\nR₃/R₃[3,3];R₄/R₄[4,4]\n"+self.BrcktI(np.round(EqI13,3))
            else:
                exp=""
        else:
            exp="a dimension\ncompute"
        return exp

    def Transpose(self):
        if self.d == 2:
            exp2D = np.array(self.m).reshape(self.d, self.d)
            cal = exp2D.transpose()
            exp = "[A] =\n"+self.Mat2D(exp2D)+"\n\nTranspose of [A] =\n" +self.Mat2D(cal)
        elif self.d == 3:
            exp3D = np.array(self.m).reshape(self.d, self.d)
            cal = exp3D.transpose()
            exp = "[A] =\n"+self.Mat3D(exp3D) + "\n\nTranspose of [A] =\n" +self.Mat3D(cal)
        elif self.d == 4:
            exp4D = np.array(self.m).reshape(self.d, self.d)
            cal = exp4D.transpose()
            exp = "[A] =\n"+self.Mat3D(exp4D) + "\n\nTranspose of [A] =\n" +self.Mat3D(cal)
        else:
            exp = "Please choose \na dimension\nbefore compute"
        return exp

    def Scalar(self):
        if self.d == 3:
            exp3D = np.array(self.m).reshape(self.d, self.d)
            cal = self.m[0] * self.m[4] * self.m[8] + self.m[1] * self.m[5] * self.m[6] + self.m[2] * self.m[3] *self.m[7] - self.m[2] * self.m[4] * self.m[6] - self.m[1] * self.m[3] * self.m[8] \
                  - self.m[0] * self.m[5] * self.m[7]
            exp = "[A] =\n"+str(exp3D).replace('[[', '  \t| ').replace(']]', '|').replace('[', ' \t| ').replace(']', '|')+"\n\na•(b x c) = \n  " +str(np.round(self.m[0],3))+"•"+str(np.round(np.round(self.m[4],3),3)) \
                +"•"+str(np.round(self.m[8],3))+"+"+str(np.round(self.m[1],3))+"•"+str(np.round(self.m[5],3))+"•"+str(np.round(self.m[6],3))+"\n  +"+str(np.round(self.m[2],3))+"•"+str(np.round(self.m[3],3))+"•"+str(np.round(self.m[7],3))+"-"+str(np.round(self.m[2],3))\
                +"•"+str(np.round(self.m[4],3))+"•"+str(np.round(self.m[6],3))+"\n  -"+str(np.round(self.m[1],3))+"•"+str(np.round(self.m[3],3))+"•"+str(np.round(self.m[8],3))+"-"+str(np.round(self.m[0],3))+"•"+str(np.round(self.m[5],3))+"•"+str(np.round(self.m[7],3))\
                +"\n\n= ("+str(np.round(self.m[0],3) * np.round(self.m[4],3) * np.round(self.m[8],3))+")+("+str(np.round(self.m[1],3) * np.round(self.m[5],3) * np.round(self.m[6],3))+")+("+str(np.round(self.m[2],3) * np.round(self.m[3],3) * np.round(self.m[7],3))+")\n  -("\
                +str(np.round(self.m[2],3) * np.round(self.m[4],3) * np.round(self.m[6],3))+")-("+str(np.round(self.m[1],3) * np.round(self.m[3],3) * np.round(self.m[8],3))+")-("+str(np.round(self.m[0],3) * np.round(self.m[5],3) * np.round(self.m[7],3))+")"+"\n\n="+str(cal)
        else:
            exp = "Please choose \n3x3 dimension \nto compute"
        return exp

    def Triangular(self):
        if self.d == 2:
            Eq0 = np.array(self.m).reshape(self.d, self.d)
            if Eq0[0, 0] == 0:
                Eq1 = np.array([Eq0[1], Eq0[0]])
            elif Eq0[1, 0] == 0:
                Eq1 = Eq0
            else:
                Eq1 = np.array([Eq0[0], Eq0[1] - Eq0[0] * Eq0[1, 0] / Eq0[0, 0]])
            exp = self.Mat2D(Eq0) + "\n\nR₂ - R₁(R₂[2,1]/R₁[1,1])\n" + self.Mat2D(np.round(Eq1,3))
        elif self.d == 3:
            Eq0 = np.array(self.m).reshape(self.d, self.d)
            if Eq0[0, 0] == 0 and Eq0[1, 0] != 0:
                Eq1 = np.array([Eq0[1], Eq0[0], Eq0[2]])
            elif Eq0[0, 0] == 0 and Eq0[2, 0] != 0:
                Eq1 = np.array([Eq0[2], Eq0[1], Eq0[0]])
            else:
                Eq1 = np.array([Eq0[0], Eq0[1] - Eq0[0] * Eq0[1, 0] / Eq0[0, 0], Eq0[2]])
            if Eq1[2, 0] == 0:
                Eq2 = Eq1
            else:
                Eq2 = np.array([Eq1[0], Eq1[1], Eq1[2] - Eq1[0] * Eq1[2, 0] / Eq1[0, 0]])
            if Eq2[1, 1] == 0:
                Eq3 = np.array([Eq2[0], Eq2[2], Eq2[1]])
            elif Eq2[2, 1] == 0:
                Eq3 = Eq2
            else:
                Eq3 = np.array([Eq2[0], Eq2[1], Eq2[2] - Eq2[1] * Eq2[2, 1] / Eq2[1, 1]])
            exp = self.Mat3D(Eq0) + "\n\nR₂ - R₁(R₂[2,1]/R₁[1,1])\nR₃ - R₁(R₃[3,1]/R₁[1,1])\n" + self.Mat3D(
                np.round(Eq2,3)) + "\n\nR₃ - R₂(R₃[3,2]/R₂[2,2]\n" + self.Mat3D(np.round(Eq3,3))
        elif self.d == 4:
            Eq0 = np.array(self.m).reshape(self.d, self.d)
            if Eq0[0, 0] == 0 and Eq0[1, 0] != 0:
                Eq1 = np.array([Eq0[1], Eq0[0], Eq0[2], Eq0[3]])
            elif Eq0[0, 0] == 0 and Eq0[2, 0] != 0:
                Eq1 = np.array([Eq0[2], Eq0[1], Eq0[0], Eq0[3]])
            elif Eq0[0, 0] == 0 and Eq0[3, 0] != 0:
                Eq1 = np.array([Eq0[3], Eq0[1], Eq0[2], Eq0[0]])
            elif Eq0[1, 0] == 0:
                Eq1 = Eq0
            else:
                Eq1 = np.array([Eq0[0], Eq0[1] - Eq0[0] * Eq0[1, 0] / Eq0[0, 0], Eq0[2], Eq0[3]])
            if Eq1[2, 0] == 0:
                Eq2 = Eq1
            else:
                Eq2 = np.array([Eq1[0], Eq1[1], Eq1[2] - Eq1[0] * Eq1[2, 0] / Eq1[0, 0], Eq0[3]])
            if Eq2[3, 0] == 0:
                Eq3 = Eq2
            else:
                Eq3 = np.array([Eq2[0], Eq2[1], Eq2[2], Eq2[3] - Eq2[0] * Eq2[3, 0] / Eq2[0, 0]])
            if Eq3[1, 1] == 0 and Eq3[3, 1] != 0:
                Eq4 = np.array([Eq3[0], Eq3[3], Eq3[2], Eq3[1]])
            elif Eq3[3, 1] == 0:
                Eq4 = Eq3
            else:
                Eq4 = np.array([Eq3[0], Eq3[1], Eq3[2], Eq3[3] - Eq3[1] * Eq3[3, 1] / Eq3[1, 1]])
            if Eq4[1, 1] == 0 and Eq4[2, 1] != 0:
                Eq5 = np.array([Eq4[0], Eq4[2], Eq4[1], Eq4[3]])
            elif Eq4[2, 1] == 0:
                Eq5 = Eq4
            else:
                Eq5 = np.array([Eq4[0], Eq4[1], Eq4[2] - Eq4[1] * Eq4[2, 1] / Eq4[1, 1], Eq4[3]])
            if Eq5[2, 2] == 0:
                Eq6 = np.array([Eq5[0], Eq5[1], Eq5[3], Eq5[2]])
            elif Eq5[3, 2] == 0:
                Eq6 = Eq5
            else:
                Eq6 = np.array([Eq5[0], Eq5[1], Eq5[2], Eq5[3] - Eq5[2] * Eq5[3, 2] / Eq5[2, 2]])
            exp = self.Mat3D(Eq0) + "\n\nR₂ - R₁(R₂[2,1]/R₁[1,1])\nR₃ - R₁(R₃[3,1]/R₁[1,1])\nR₄ - R₁(R₄[4,1]/R₁[1,1])\n" \
                  + self.Mat3D(np.round(Eq3,3)) + "\n\nR₃ - R₂(R₃[3,2]/R₂[2,2])\nR₄ - R₂(R₄[4,2]/R₂[2,2])\n" \
                  + self.Mat3D(np.round(Eq5,3)) + "\n\nR₄ - R₃(R₄[4,3]/R₃[3,3])\n" + self.Mat3D(np.round(Eq6,3))
        else:
            exp = "Please choose a \ndimension before compute"
        return exp

    def Trace(self):
        if self.d == 2:
            exp2D = np.array(self.m).reshape(self.d, self.d)
            cal = round(self.m[0] + self.m[3], 3)
            exp = "Trace =\n" + self.Mat2D(exp2D) + "\n\nTr = " + str(self.m[0]) + " + " + str(np.round(self.m[3],3)) + "\n\nTr = " + str(cal)
        elif self.d == 3:
            exp3D = np.array(self.m).reshape(self.d, self.d)
            cal = round(self.m[0] + self.m[4] + self.m[8], 3)
            exp = "Trace =\n" + self.Mat3D(exp3D) + "\n\nTr = " + str(self.m[0]) + " + " + str(np.round(self.m[4],3)) + " + " + str(
                np.round(self.m[8])) + "\n\nTr = " + str(cal)
        elif self.d == 4:
            exp4D = np.array(self.m).reshape(self.d, self.d)
            cal = round(self.m[0] + self.m[5] + self.m[10] + self.m[15], 3)
            exp = "Trace =\n" + self.Mat3D(exp4D) + "\n\nTr = " + str(self.m[0]) + " + " + str(np.round(self.m[5],3)) + " + " + str(
                np.round(self.m[10],3)) + " + " + str(np.round(self.m[15],3)) + "\n\nTr = " + str(cal)
        else:
            exp = "Please choose \na dimension before \ncompute"
        return exp

    def LUDec(self):
        if self.d == 2:
            Eq0 = np.array(self.m).reshape(self.d, self.d)
            if Eq0[0, 0] == 0:
                Eq1 = np.array([Eq0[1], Eq0[0]])
                L = 0
            else:
                L = Eq0[1, 0] / Eq0[0, 0]
                Eq1 = np.array([Eq0[0], Eq0[1] - Eq0[0] * L])
            EL = np.array([0, 1, L, 0]).reshape(self.d, self.d)
            exp = "[A] =\n"+self.Mat2D(Eq0) + "\n\n[A] = [L][U]\nR₂ - R₁(R₂[2,1]/R₁[1,1])\n\n[U] = \n" + self.Mat2D(
                np.round(Eq1,3)) + "\n\n[L] = \n" + self.Mat2D(np.round(EL,3))

        elif self.d == 3:
            Eq0 = np.array(self.m).reshape(self.d, self.d)
            L1 = 0
            L2 = 0
            L3 = 0
            if Eq0[0, 0] == 0 and Eq0[1, 0] == 0 and Eq0[2, 0] == 0:
                Eq1 = Eq0
            elif Eq0[0, 0] == 0 and Eq0[1, 0] != 0:
                Eq1 = np.array([Eq0[1], Eq0[0], Eq0[2]])
            elif Eq0[0, 0] == 0 and Eq0[2, 0] != 0:
                Eq1 = np.array([Eq0[2], Eq0[1], Eq0[0]])
            else:
                L1 = Eq0[1, 0] / Eq0[0, 0]
                Eq1 = np.array([Eq0[0], Eq0[1] - Eq0[0] * L1, Eq0[2]])
            if Eq1[2, 0] == 0:
                Eq2 = Eq1
            else:
                L2 = Eq1[2, 0] / Eq1[0, 0]
                Eq2 = np.array([Eq1[0], Eq1[1], Eq1[2] - Eq1[0] * L2])
            if Eq2[0, 0] == 0 and Eq2[1, 0] == 0 and Eq2[2, 0] == 0:
                if Eq2[0, 1] == 0 and Eq2[1, 1] != 0:
                    Eq3 = np.array([Eq2[1], Eq2[0], Eq2[2]])
                elif Eq2[0, 1] == 0 and Eq2[2, 1] != 0:
                    Eq3 = np.array([Eq2[2], Eq2[1], Eq2[0]])
                elif Eq2[1, 1] == 0:
                    Eq3 = Eq2
                else:
                    L1 = Eq2[1, 1] / Eq2[0, 1]
                    Eq3 = np.array([Eq2[0], Eq2[1] - Eq2[0] * L1, Eq2[2]])
            elif Eq2[0, 0] != 0 and Eq2[0, 1] == 0 and Eq2[1, 1] == 0 and Eq2[2, 1] == 0:
                if Eq2[1, 2] == 0 and Eq2[2, 2] != 0:
                    Eq3 = np.array([Eq2[0], Eq2[2], Eq2[1]])
                elif Eq2[2, 2] == 0:
                    Eq3 = Eq2
                else:
                    L3 = Eq2[2, 2] / Eq2[1, 2]
                    Eq3 = np.array([Eq2[0], Eq2[1], Eq2[2] - Eq2[1] * L3])
            elif Eq2[1, 1] == 0 and Eq2[2, 1] != 0:
                Eq3 = np.array([Eq2[0], Eq2[2], Eq2[1]])
            elif Eq2[2, 1] == 0:
                Eq3 = Eq2
            else:
                L3 = Eq2[2, 1] / Eq2[1, 1]
                Eq3 = np.array([Eq2[0], Eq2[1], Eq2[2] - Eq2[1] * L3])
            if Eq3[0, 0] == 0 and Eq3[1, 0] == 0 and Eq3[2, 0] == 0 and Eq3[0, 1] == 0 and Eq3[1, 1] == 0 and Eq3[
                2, 1] == 0:
                if Eq3[0, 2] == 0 and Eq3[1, 2] != 0:
                    Eq4 = np.array([Eq3[1], Eq3[0], Eq3[2]])
                elif Eq3[0, 2] == 0 and Eq3[2, 2] != 0:
                    Eq4 = np.array([Eq3[2], Eq3[1], Eq3[0]])
                elif Eq3[0, 2] == 0 and Eq3[1, 2] == 0 and Eq3[2, 2] == 0:
                    Eq4 = Eq3
                else:
                    L1 = Eq3[1, 2] / Eq3[0, 2]
                    Eq4 = np.array([Eq3[0], Eq3[1] - Eq3[0] * L1, Eq3[2]])
            elif Eq3[0, 0] == 0 and Eq3[1, 0] == 0 and Eq3[2, 0] == 0:
                if Eq3[2, 1] == 0:
                    Eq4 = Eq3
                else:
                    L2 = Eq3[2, 1] / Eq3[0, 1]
                    Eq4 = np.array([Eq3[0], Eq3[1], Eq3[2] - Eq3[0] * L2])
            else:
                Eq4 = Eq3
            if Eq4[0, 0] == 0 and Eq4[1, 0] == 0 and Eq4[2, 0] == 0 and Eq4[0, 1] == 0 and Eq4[1, 1] == 0 and Eq4[
                2, 1] == 0:
                if Eq4[2, 2] == 0:
                    Eq5 = Eq4
                else:
                    L2 = Eq4[2, 2] / Eq4[0, 2]
                    Eq5 = np.array([Eq4[0], Eq4[1], Eq4[2] - Eq4[0] * L2])
            elif Eq4[0, 0] != 0 and Eq4[1, 1] == 0 and Eq4[2, 1] == 0:
                if Eq4[1, 2] == 0 and Eq4[2, 2] != 0:
                    Eq5 = np.array([Eq4[0], Eq4[2], Eq4[1]])
                elif Eq4[2, 2] == 0:
                    Eq5 = Eq4
                else:
                    L3 = Eq4[2, 2] / Eq4[1, 2]
                    Eq5 = np.array([Eq4[0], Eq4[1], Eq4[2] - Eq4[1] * L3])
            elif Eq4[0, 0] != 0 and Eq4[1, 1] == 0 and Eq4[1, 2] == 0 and Eq4[2, 2] != 0 or Eq4[0, 0] == 0 and Eq4[
                0, 1] != 0 and Eq4[1, 2] == 0 and Eq4[2, 2] != 0:
                Eq5 = np.array([Eq4[0], Eq4[2], Eq4[1]])
            else:
                Eq5 = Eq4
            EL = np.array([1, 0, 0, L1, 1, 0, L2, L3, 1]).reshape(self.d, self.d)
            exp = "[A] =\n"+self.Mat3D(Eq0) + "\n\n[A] = [L][U]\n\n[U] = \n" + self.Mat3D(np.round(Eq5,3)) + "\n\n[L] = \n" + self.Mat3D(np.round(EL,3))
        elif self.d == 4:
            Eq0 = np.array(self.m).reshape(self.d, self.d)
            L1 = 0
            L2 = 0
            L3 = 0
            L4 = 0
            L5 = 0
            L6 = 0
            if Eq0[0, 0] == 0 and Eq0[1, 0] != 0:
                Eq1 = np.array([Eq0[1], Eq0[0], Eq0[2], Eq0[3]])
            elif Eq0[0, 0] == 0 and Eq0[2, 0] != 0:
                Eq1 = np.array([Eq0[2], Eq0[1], Eq0[0], Eq0[3]])
            elif Eq0[0, 0] == 0 and Eq0[3, 0] != 0:
                Eq1 = np.array([Eq0[3], Eq0[1], Eq0[2], Eq0[0]])
            elif Eq0[1, 0] == 0:
                Eq1 = Eq0
            else:
                L1 = Eq0[1, 0] / Eq0[0, 0]
                Eq1 = np.array([Eq0[0], Eq0[1] - Eq0[0] * L1, Eq0[2], Eq0[3]])
            if Eq1[2, 0] == 0:
                Eq2 = Eq1
            else:
                L2 = Eq1[2, 0] / Eq1[0, 0]
                Eq2 = np.array([Eq1[0], Eq1[1], Eq1[2] - Eq1[0] * L2, Eq0[3]])
            if Eq2[3, 0] == 0:
                Eq3 = Eq2
            else:
                L3 = Eq2[3, 0] / Eq2[0, 0]
                Eq3 = np.array([Eq2[0], Eq2[1], Eq2[2], Eq2[3] - Eq2[0] * L3])
            if Eq3[0, 0] == 0 and Eq3[1, 0] == 0 and Eq3[2, 0] == 0 and Eq3[3, 0] == 0:
                if Eq3[0, 1] == 0 and Eq3[1, 1] != 0:
                    Eq4 = np.array([Eq3[1], Eq3[0], Eq3[2], Eq3[3]])
                elif Eq3[0, 1] == 0 and Eq3[2, 1] != 0:
                    Eq4 = np.array([Eq3[2], Eq3[1], Eq3[0], Eq3[3]])
                elif Eq3[0, 1] == 0 and Eq3[3, 1] != 0:
                    Eq4 = np.array([Eq3[3], Eq3[1], Eq3[2], Eq3[0]])
                elif Eq3[1, 1] == 0:
                    Eq4 = Eq3
                else:
                    L1 = Eq3[1, 1] / Eq3[0, 1]
                    Eq4 = np.array([Eq3[0], Eq3[1] - Eq3[0] * L1, Eq3[2], Eq3[3]])
            elif Eq3[1, 1] == 0 and Eq3[2, 1] != 0:
                Eq4 = np.array([Eq3[0], Eq3[2], Eq3[1], Eq3[3]])
            elif Eq3[1, 1] == 0 and Eq3[3, 1] != 0:
                Eq4 = np.array([Eq3[0], Eq3[3], Eq3[2], Eq3[1]])
            elif Eq3[2, 1] == 0:
                Eq4 = Eq3
            else:
                L4 = Eq3[2, 1] / Eq3[1, 1]
                Eq4 = np.array([Eq3[0], Eq3[1], Eq3[2] - Eq3[1] * L4, Eq3[3]])
            if Eq4[0, 0] == 0 and Eq4[1, 0] == 0 and Eq4[2, 0] == 0 and Eq4[3, 0] == 0:
                if Eq4[2, 1] == 0:
                    Eq5 = Eq4
                else:
                    L2 = Eq4[2, 1] / Eq4[0, 1]
                    Eq5 = np.array([Eq4[0], Eq4[1], Eq4[2] - Eq4[0] * L2, Eq4[3]])
            elif Eq4[3, 1] == 0:
                Eq5 = Eq4
            else:
                L5 = Eq4[3, 1] / Eq4[1, 1]
                Eq5 = np.array([Eq4[0], Eq4[1], Eq4[2], Eq4[3] - Eq4[1] * L5])
            if Eq5[0, 0] == 0 and Eq5[1, 0] == 0 and Eq5[2, 0] == 0 and Eq5[3, 0] == 0 and Eq5[0, 1] == 0 and Eq5[1, 1] == 0 and Eq5[2, 1] == 0 and Eq5[3, 1] == 0:
                if Eq5[0, 2] == 0 and Eq5[1, 2] != 0:
                    Eq6 = np.array([Eq5[1], Eq5[0], Eq5[2], Eq5[3]])
                elif Eq5[0, 2] == 0 and Eq5[2, 2] != 0:
                    Eq6 = np.array([Eq5[2], Eq5[1], Eq5[0], Eq5[3]])
                elif Eq5[0, 2] == 0 and Eq5[3, 2] != 0:
                    Eq6 = np.array([Eq5[3], Eq5[1], Eq5[2], Eq5[0]])
                elif Eq5[1, 2] == 0:
                    Eq6 = Eq5
                else:
                    L1 = Eq5[1, 2] / Eq5[0, 2]
                    Eq6 = np.array([Eq5[0], Eq5[1] - Eq5[0] * L1, Eq5[2], Eq5[3]])
            elif Eq5[0, 1] == 0 and Eq5[1, 1] == 0 and Eq5[2, 1] == 0 and Eq5[3, 1] == 0 and Eq5[0, 2] == 0 and Eq5[1, 2] == 0 and Eq5[2, 2] == 0 and Eq5[3, 2] == 0:
                if Eq5[1, 3] == 0 and Eq5[2, 3] != 0:
                    Eq6 = np.array([Eq5[0], Eq5[2], Eq5[1], Eq5[3]])
                elif Eq5[1, 3] == 0 and Eq5[3, 3] != 0:
                    Eq6 = np.array([Eq5[0], Eq5[3], Eq5[2], Eq5[1]])
                elif Eq5[2, 3] == 0:
                    Eq6 = Eq5
                else:
                    L1 = Eq5[2, 3] / Eq5[1, 3]
                    Eq6 = np.array([Eq5[0], Eq5[1], Eq5[2] - Eq5[1] * L1, Eq5[3]])
            elif Eq5[0, 0] == 0 and Eq5[1, 0] == 0 and Eq5[2, 0] == 0 and Eq5[3, 0] == 0:
                if Eq5[3, 1] == 0:
                    Eq6 = Eq5
                else:
                    L3 = Eq5[3, 1] / Eq5[0, 1]
                    Eq6 = np.array([Eq5[0], Eq5[1], Eq5[2], Eq5[3] - Eq5[0] * L3])
            elif Eq5[0, 1] == 0 and Eq5[1, 1] == 0 and Eq5[2, 1] == 0 and Eq5[3, 1] == 0:
                if Eq5[1, 2] == 0 and Eq5[2, 2] != 0:
                    Eq6 = np.array([Eq5[0], Eq5[2], Eq5[1], Eq5[3]])
                elif Eq5[1, 2] == 0 and Eq5[3, 2] != 0:
                    Eq6 = np.array([Eq5[0], Eq5[3], Eq5[2], Eq5[1]])
                elif Eq5[2, 2] == 0:
                    Eq6 = Eq5
                else:
                    L1 = Eq5[2, 2] / Eq5[1, 2]
                    Eq6 = np.array([Eq5[0], Eq5[1], Eq5[2] - Eq5[1] * L1, Eq5[3]])
            elif Eq5[2, 2] == 0 and Eq5[3, 2] != 0:
                Eq6 = np.array([Eq5[0], Eq5[1], Eq5[3], Eq5[2]])
            elif Eq5[3, 2] == 0:
                Eq6 = Eq5
            else:
                L6 = Eq5[3, 2] / Eq5[2, 2]
                Eq6 = np.array([Eq5[0], Eq5[1], Eq5[2], Eq5[3] - Eq5[2] * L6])
            if Eq6[0, 0] == 0 and Eq6[1, 0] == 0 and Eq6[2, 0] == 0 and Eq6[3, 0] == 0 and Eq6[0, 1] == 0 and Eq6[1, 1] == 0 and Eq6[2, 1] == 0 and Eq6[3, 1] == 0 and Eq6[0, 2] == 0 and Eq6[1, 2] == 0 and Eq6[2, 2] == 0 and Eq6[3, 2] == 0:
                if Eq6[0, 3] == 0 and Eq6[1, 3] != 0:
                    Eq7 = np.array([Eq6[1], Eq6[0], Eq6[2], Eq6[3]])
                elif Eq6[0, 3] == 0 and Eq6[2, 3] != 0:
                    Eq7 = np.array([Eq6[2], Eq6[1], Eq6[0], Eq6[3]])
                elif Eq6[0, 3] == 0 and Eq6[3, 3] != 0:
                    Eq7 = np.array([Eq6[3], Eq6[1], Eq6[2], Eq6[0]])
                elif Eq6[1, 3] == 0:
                    Eq7 = Eq6
                else:
                    L1 = Eq6[1, 3] / Eq6[0, 3]
                    Eq7 = np.array([Eq6[0], Eq6[1] - Eq6[0] * L1, Eq6[2], Eq6[3]])
            elif Eq6[0, 0] == 0 and Eq6[1, 0] == 0 and Eq6[2, 0] == 0 and Eq6[3, 0] == 0 and Eq6[0, 1] == 0 and Eq6[1, 1] == 0 and Eq6[2, 1] == 0 and Eq6[3, 1] == 0:
                if Eq6[2, 2] == 0:
                    Eq7 = Eq6
                else:
                    L2 = Eq6[2, 2] / Eq6[0, 2]
                    Eq7 = np.array([Eq6[0], Eq6[1], Eq6[2] - Eq6[0] * L2, Eq6[3]])
            elif Eq5[0, 1] == 0 and Eq5[1, 1] == 0 and Eq5[2, 1] == 0 and Eq5[3, 1] == 0 and Eq5[0, 2] == 0 and Eq5[1, 2] == 0 and Eq5[2, 2] == 0 and Eq5[3, 2] == 0:
                if Eq6[3, 3] == 0:
                    Eq7 = Eq6
                else:
                    L2 = Eq6[3, 3] / Eq6[1, 3]
                    Eq7 = np.array([Eq6[0], Eq6[1], Eq6[2], Eq6[3] - Eq6[1] * L2])
            elif Eq6[0, 0] == 0 and Eq6[1, 0] == 0 and Eq6[2, 0] == 0 and Eq6[3, 0] == 0:
                if Eq6[1, 2] == 0 and Eq6[2, 2] != 0:
                    Eq7 = np.array([Eq6[0], Eq6[2], Eq6[1], Eq6[3]])
                elif Eq6[1, 2] == 0 and Eq6[3, 2] != 0:
                    Eq7 = np.array([Eq6[0], Eq6[3], Eq6[2], Eq6[1]])
                elif Eq6[2, 2] == 0:
                    Eq7 = Eq6
                else:
                    L4 = Eq6[2, 2] / Eq6[1, 2]
                    Eq7 = np.array([Eq6[0], Eq6[1], Eq6[2] - Eq6[1] * L4, Eq6[3]])
            elif Eq6[0, 1] == 0 and Eq6[1, 1] == 0 and Eq6[2, 1] == 0 and Eq6[3, 1] == 0:
                if Eq6[3, 2] == 0:
                    Eq7 = Eq6
                else:
                    L2 = Eq6[3, 2] / Eq6[1, 2]
                    Eq7 = np.array([Eq6[0], Eq6[1], Eq6[2], Eq6[3] - Eq6[1] * L2])
            elif Eq6[0, 2] == 0 and Eq6[1, 2] == 0 and Eq6[2, 2] == 0 and Eq6[3, 2] == 0:
                if Eq6[2, 3] == 0 and Eq6[3, 3] != 0:
                    Eq7 = np.array([Eq6[0], Eq6[1], Eq6[3], Eq6[2]])
                elif Eq6[3, 3] == 0:
                    Eq7 = Eq6
                else:
                    L6 = Eq6[3, 3] / Eq6[2, 3]
                    Eq7 = np.array([Eq6[0], Eq6[1], Eq6[2], Eq6[3] - Eq6[2] * L6])
            else:
                Eq7 = Eq6
            if Eq7[0, 0] == 0 and Eq7[1, 0] == 0 and Eq7[2, 0] == 0 and Eq7[3, 0] == 0 and Eq7[0, 1] == 0 and Eq7[1, 1] == 0 and Eq7[2, 1] == 0 and Eq7[3, 1] == 0 and Eq7[0, 2] == 0 and Eq7[1, 2] == 0 and Eq7[2, 2] == 0 and Eq7[3, 2] == 0:
                if Eq7[2, 3] == 0:
                    Eq8 = Eq7
                else:
                    L2 = Eq7[2, 3] / Eq7[0, 3]
                    Eq8 = np.array([Eq7[0], Eq7[1], Eq7[2] - Eq7[0] * L2, Eq7[3]])
            elif Eq7[0, 0] == 0 and Eq7[1, 0] == 0 and Eq7[2, 0] == 0 and Eq7[3, 0] == 0 and Eq7[0, 1] == 0 and Eq7[1, 1] == 0 and Eq7[2, 1] == 0 and Eq7[3, 1] == 0:
                if Eq7[3, 2] == 0:
                    Eq8 = Eq7
                else:
                    L3 = Eq7[3, 2] / Eq7[0, 2]
                    Eq8 = np.array([Eq7[0], Eq7[1], Eq7[2], Eq7[3] - Eq7[0] * L3])
            elif Eq7[0, 0] == 0 and Eq7[1, 0] == 0 and Eq7[2, 0] == 0 and Eq7[3, 0] == 0:
                if Eq7[3, 2] == 0:
                    Eq8 = Eq7
                else:
                    L5 = Eq7[3, 2] / Eq7[1, 2]
                    Eq8 = np.array([Eq7[0], Eq7[1], Eq7[2], Eq7[3] - Eq7[1] * L5])
            elif Eq7[0, 1] == 0 and Eq7[1, 1] == 0 and Eq7[2, 1] == 0 and Eq7[3, 1] == 0:
                if Eq7[2, 3] == 0 and Eq7[3, 3] != 0:
                    Eq8 = np.array([Eq7[0], Eq7[1], Eq7[3], Eq7[2]])
                elif Eq7[3, 3] == 0:
                    Eq8 = Eq7
                else:
                    L3 = Eq7[3, 3] / Eq7[2, 3]
                    Eq8 = np.array([Eq7[0], Eq7[1], Eq7[2], Eq7[3] - Eq7[2] * L3])
            else:
                Eq8 = Eq7
            if Eq8[0, 0] == 0 and Eq8[1, 0] == 0 and Eq8[2, 0] == 0 and Eq8[3, 0] == 0 and Eq8[0, 1] == 0 and Eq8[1, 1] == 0 and Eq8[2, 1] == 0 and Eq8[3, 1] == 0 and Eq8[0, 2] == 0 and Eq8[1, 2] == 0 and Eq8[2, 2] == 0 and Eq8[3, 2] == 0:
                if Eq8[3, 3] == 0:
                    Eq9 = Eq8
                else:
                    L3 = Eq8[3, 3] / Eq8[0, 3]
                    Eq9 = np.array([Eq8[0], Eq8[1], Eq8[2], Eq8[3] - Eq8[0] * L3])
            elif Eq8[0, 0] == 0 and Eq8[1, 0] == 0 and Eq8[2, 0] == 0 and Eq8[3, 0] == 0 and Eq8[0, 1] == 0 and Eq8[1, 1] == 0 and Eq8[2, 1] == 0 and Eq8[3, 1] == 0:
                if Eq8[1, 3] == 0 and Eq8[2, 3] != 0:
                    Eq9 = np.array([Eq8[0], Eq8[2], Eq8[1], Eq8[3]])
                elif Eq8[1, 3] == 0 and Eq8[3, 3] != 0:
                    Eq9 = np.array([Eq8[0], Eq8[3], Eq8[2], Eq8[1]])
                elif Eq8[2, 3] == 0:
                    Eq9 = Eq8
                else:
                    L4 = Eq8[2, 3] / Eq8[1, 3]
                    Eq9 = np.array([Eq8[0], Eq8[1], Eq8[2] - Eq8[1] * L4, Eq8[3]])
            elif Eq8[0, 0] == 0 and Eq8[1, 0] == 0 and Eq8[2, 0] == 0 and Eq8[3, 0] == 0:
                if Eq8[2, 3] == 0 and Eq8[3, 3] != 0:
                    Eq9 = np.array([Eq8[0], Eq8[1], Eq8[3], Eq8[2]])
                elif Eq8[3, 3] == 0:
                    Eq9 = Eq8
                else:
                    L6 = Eq8[3, 3] / Eq8[2, 3]
                    Eq9 = np.array([Eq8[0], Eq8[1], Eq8[2], Eq8[3] - Eq8[2] * L6])
            else:
                Eq9 = Eq8
            if Eq9[0, 0] == 0 and Eq9[1, 0] == 0 and Eq9[2, 0] == 0 and Eq9[3, 0] == 0 and Eq9[0, 1] == 0 and Eq9[1, 1] == 0 and Eq9[2, 1] == 0 and Eq9[3, 1] == 0:
                if Eq9[3, 3] == 0:
                    Eq10 = Eq9
                else:
                    L5 = Eq9[3, 3] / Eq9[1, 3]
                    Eq10 = np.array([Eq9[0], Eq9[1], Eq9[2], Eq9[3] - Eq9[1] * L5])
            else:
                Eq10 = Eq9
            EL = np.array([1, 0, 0, 0, L1, 1, 0, 0, L2, L3, 1, 0, L4, L5, L6, 1]).reshape(self.d, self.d)
            exp = "[A] =\n" +self.Mat3D(np.round(Eq0,3)) + "\n\n[A] = [L][U]\n\n[U] = \n" + self.Mat3D(np.round(Eq10,3)) + "\n\n[L] = \n" + self.Mat3D(np.round(EL,3))
        else:
            exp = "Please choose a dimension \nbefore compute"
        return exp


    def Rank(self):
        if self.d == 2:
            Eq0 = np.array(self.m).reshape(self.d, self.d)
            if Eq0[0,0]==0 and Eq0[1,0]!=0:
                Eq1 = np.array([Eq0[1], Eq0[0]])
            elif Eq0[1,0]==0:
                Eq1=Eq0
            else:
                Eq1 = np.array([Eq0[0], Eq0[1]-Eq0[0]*Eq0[1,0]/Eq0[0,0]])
            if Eq1[0,0] == 0 and Eq1[0,1]==0:
                Eq2 = np.array([Eq1[1], Eq1[0]])
            else:
                Eq2 = Eq1
            if Eq2[0,0]!=0:
                if Eq2[1,1]!=0:
                    r = 2
                elif Eq2[1,1]==0:
                   r = 1
                else:
                    r = 0
            else:
                if Eq2[0,1]!=0:
                    r = 1
                else:
                    r = 0
            exp = "[A] =\n"+self.Mat2D(Eq0)+"\n\nRank =\n"+self.Mat2D(np.round(Eq2,3))+"\n\nRank : "+str(r)
        elif self.d == 3:
            Eq0 = np.array(self.m).reshape(self.d, self.d)
            if Eq0[0, 0] == 0 and Eq0[1, 0] == 0 and Eq0[2, 0] == 0:
                Eq1 = Eq0
            elif Eq0[0, 0] == 0 and Eq0[1, 0] != 0:
                Eq1 = np.array([Eq0[1], Eq0[0], Eq0[2]])
            elif Eq0[0, 0] == 0 and Eq0[2, 0] != 0:
                Eq1 = np.array([Eq0[2], Eq0[1], Eq0[0]])
            else:
                Eq1 = np.array([Eq0[0], Eq0[1] - Eq0[0] * Eq0[1, 0] / Eq0[0, 0], Eq0[2]])
            if Eq1[2, 0] == 0:
                Eq2 = Eq1
            else:
                Eq2 = np.array([Eq1[0], Eq1[1], Eq1[2] - Eq1[0] * Eq1[2, 0] / Eq1[0, 0]])
            if Eq2[0,0]==0 and Eq2[1,0]==0 and Eq2[2,0]==0:
                if Eq2[0,1]==0 and Eq2[1,1]!=0:
                    Eq3 = np.array([Eq2[1], Eq2[0], Eq2[2]])
                elif Eq2[0,1]==0 and Eq2[2,1]!=0:
                    Eq3 = np.array([Eq2[2], Eq2[1], Eq2[0]])
                elif Eq2[1,1]==0:
                    Eq3 = Eq2
                else:
                    Eq3 = np.array([Eq2[0], Eq2[1]-Eq2[0]*Eq2[1,1]/Eq2[0,1], Eq2[2]])
            elif Eq2[0,0]!=0 and Eq2[0,1]==0 and Eq2[1,1]==0 and Eq2[2,1]==0:
                if Eq2[1,2]==0 and Eq2[2,2]!=0:
                    Eq3 = np.array([Eq2[0], Eq2[2], Eq2[1]])
                elif Eq2[2,2]==0:
                    Eq3 = Eq2
                else:
                    Eq3 = np.array([Eq2[0], Eq2[1], Eq2[2]-Eq2[1]*Eq2[2,2]/Eq2[1,2]])
            elif Eq2[1, 1] == 0 and Eq2[2,1]!=0:
                Eq3 = np.array([Eq2[0], Eq2[2], Eq2[1]])
            elif Eq2[2, 1] == 0:
                Eq3 = Eq2
            else:
                Eq3 = np.array([Eq2[0], Eq2[1], Eq2[2] - Eq2[1] * Eq2[2, 1] / Eq2[1, 1]])
            if Eq3[0,0]==0 and Eq3[1,0]==0 and Eq3[2,0]==0 and Eq3[0,1]==0 and Eq3[1,1]==0 and Eq3[2,1]==0:
                if Eq3[0,2]==0 and Eq3[1,2]!=0:
                    Eq4 = np.array([Eq3[1], Eq3[0], Eq3[2]])
                elif Eq3[0,2]==0 and Eq3[2,2]!=0:
                    Eq4 = np.array([Eq3[2], Eq3[1], Eq3[0]])
                elif Eq3[0,2]==0 and Eq3[1,2]==0 and Eq3[2,2]==0:
                    Eq4 = Eq3
                else:
                    Eq4 = np.array([Eq3[0], Eq3[1]-Eq3[0]*Eq3[1,2]/Eq3[0,2], Eq3[2]])
            elif Eq3[0,0]==0 and Eq3[1,0]==0 and Eq3[2,0]==0:
                if Eq3[2,1]==0:
                    Eq4 = Eq3
                else:
                    Eq4 = np.array([Eq3[0], Eq3[1], Eq3[2]-Eq3[0]*Eq3[2,1]/Eq3[0,1]])
            else:
                Eq4 = Eq3
            if Eq4[0, 0] == 0 and Eq4[1, 0] == 0 and Eq4[2, 0] == 0 and Eq4[0, 1] == 0 and Eq4[1, 1] == 0 and Eq4[2, 1] == 0:
                if Eq4[2,2]==0:
                    Eq5 = Eq4
                else:
                    Eq5 = np.array([Eq4[0], Eq4[1], Eq4[2]-Eq4[0]*Eq4[2,2]/Eq4[0,2]])
            elif Eq4[0,0]!=0 and Eq4[1,1]==0 and Eq4[2,1]==0:
                if Eq4[1,2]==0 and Eq4[2,2]!=0:
                    Eq5 = np.array([Eq4[0], Eq4[2], Eq4[1]])
                elif Eq4[2,2]==0:
                    Eq5=Eq4
                else:
                    Eq5 = np.array([Eq4[0], Eq4[1], Eq4[2]-Eq4[1]*Eq4[2,2]/Eq4[1,2]])
            elif Eq4[0,0]!=0 and Eq4[1,1]==0 and Eq4[1,2]==0 and Eq4[2,2]!=0 or Eq4[0,0]==0 and Eq4[0,1]!=0 and Eq4[1,2]==0 and Eq4[2,2]!=0:
                Eq5 = np.array([Eq4[0], Eq4[2], Eq4[1]])
            else:
                Eq5 = Eq4
            if Eq5[0,0]!=0:
                if Eq5[1,1]!=0 and Eq5[2,2]!=0:
                    r = 3
                elif Eq5[1,1]!=0 and Eq5[2,2]==0 or Eq5[1,1]==0 and Eq5[1,2]!=0:
                    r = 2
                else:
                    r = 1
            elif Eq5[0,1]!=0:
                if Eq5[1,2]!=0:
                    r = 2
                else:
                    r = 1
            elif Eq5[0,2]!=0:
                r = 1
            elif np.count_nonzero(Eq5==0) == 9:
                r = 0
            else:
                r = 1
            exp="[A] =\n"+self.Mat3D(Eq0)+"\n\nRank = \n"+self.Mat3D(np.round(Eq5,3))+"\n\nRank : "+str(r)
        elif self.d == 4:
            Eq0 = np.array(self.m).reshape(self.d, self.d)
            if Eq0[0, 0] == 0 and Eq0[1, 0] != 0:
                Eq1 = np.array([Eq0[1], Eq0[0], Eq0[2], Eq0[3]])
            elif Eq0[0, 0] == 0 and Eq0[2, 0] != 0:
                Eq1 = np.array([Eq0[2], Eq0[1], Eq0[0], Eq0[3]])
            elif Eq0[0, 0] == 0 and Eq0[3, 0] != 0:
                Eq1 = np.array([Eq0[3], Eq0[1], Eq0[2], Eq0[0]])
            elif Eq0[1, 0] == 0:
                Eq1 = Eq0
            else:
                Eq1 = np.array([Eq0[0], Eq0[1] - Eq0[0] * Eq0[1, 0] / Eq0[0, 0], Eq0[2], Eq0[3]])
            if Eq1[2, 0] == 0:
                Eq2 = Eq1
            else:
                Eq2 = np.array([Eq1[0], Eq1[1], Eq1[2] - Eq1[0] * Eq1[2, 0] / Eq1[0, 0], Eq0[3]])
            if Eq2[3, 0] == 0:
                Eq3 = Eq2
            else:
                Eq3 = np.array([Eq2[0], Eq2[1], Eq2[2], Eq2[3] - Eq2[0] * Eq2[3, 0] / Eq2[0, 0]])
            if Eq3[0,0]==0 and Eq3[1,0]==0 and Eq3[2,0]==0 and Eq3[3,0]==0:
                if Eq3[0,1]==0 and Eq3[1,1]!=0:
                    Eq4 = np.array([Eq3[1], Eq3[0], Eq3[2], Eq3[3]])
                elif Eq3[0,1]==0 and Eq3[2,1]!=0:
                    Eq4 = np.array([Eq3[2], Eq3[1], Eq3[0], Eq3[3]])
                elif Eq3[0,1]==0 and Eq3[3,1]!=0:
                    Eq4 = np.array([Eq3[3], Eq3[1], Eq3[2], Eq3[0]])
                elif Eq3[1,1]==0:
                    Eq4 = Eq3
                else:
                    Eq4 = np.array([Eq3[0], Eq3[1]-Eq3[0]*Eq3[1,1]/Eq3[0,1], Eq3[2], Eq3[3]])
            elif Eq3[1,1]==0 and Eq3[2,1]!=0:
                Eq4 = np.array([Eq3[0], Eq3[2], Eq3[1], Eq3[3]])
            elif Eq3[1,1]==0 and Eq3[3,1]!=0:
                Eq4 = np.array([Eq3[0], Eq3[3], Eq3[2], Eq3[1]])
            elif Eq3[2,1]==0:
                Eq4 = Eq3
            else:
                Eq4 = np.array([Eq3[0], Eq3[1], Eq3[2]-Eq3[1]*Eq3[2,1]/Eq3[1,1], Eq3[3]])
            if Eq4[0,0]==0 and Eq4[1,0]==0 and Eq4[2,0]==0 and Eq4[3,0]==0:
                if Eq4[2,1]==0:
                    Eq5 = Eq4
                else:
                    Eq5 = np.array([Eq4[0], Eq4[1], Eq4[2]-Eq4[0]*Eq4[2,1]/Eq4[0,1], Eq4[3]])
            elif Eq4[3,1]==0:
                Eq5 = Eq4
            else:
                Eq5 = np.array([Eq4[0], Eq4[1], Eq4[2], Eq4[3]-Eq4[1]*Eq4[3,1]/Eq4[1,1]])
            if Eq5[0,0]==0 and Eq5[1,0]==0 and Eq5[2,0]==0 and Eq5[3,0]==0 and Eq5[0,1]==0 and Eq5[1,1]==0 and Eq5[2,1]==0 and Eq5[3,1]==0:
                if Eq5[0,2]==0 and Eq5[1,2]!=0:
                    Eq6 = np.array([Eq5[1], Eq5[0], Eq5[2], Eq5[3]])
                elif Eq5[0,2]==0 and Eq5[2,2]!=0:
                    Eq6 = np.array([Eq5[2], Eq5[1], Eq5[0], Eq5[3]])
                elif Eq5[0,2]==0 and Eq5[3,2]!=0:
                    Eq6 = np.array([Eq5[3], Eq5[1], Eq5[2], Eq5[0]])
                elif Eq5[1,2]==0:
                    Eq6 = Eq5
                else:
                    Eq6 = np.array([Eq5[0], Eq5[1]-Eq5[0]*Eq5[1,2]/Eq5[0,2], Eq5[2], Eq5[3]])
            elif Eq5[0,1]==0 and Eq5[1,1]==0 and Eq5[2,1]==0 and Eq5[3,1]==0 and Eq5[0,2]==0 and Eq5[1,2]==0 and Eq5[2,2]==0 and Eq5[3,2]==0:
                if Eq5[1,3]==0 and Eq5[2,3]!=0:
                    Eq6 = np.array([Eq5[0], Eq5[2], Eq5[1], Eq5[3]])
                elif Eq5[1,3]==0 and Eq5[3,3]!=0:
                    Eq6 = np.array([Eq5[0], Eq5[3], Eq5[2], Eq5[1]])
                elif Eq5[2,3]==0:
                    Eq6 = Eq5
                else:
                    Eq6 = np.array([Eq5[0], Eq5[1], Eq5[2]-Eq5[1]*Eq5[2,3]/Eq5[1,3], Eq5[3]])
            elif Eq5[0,0]==0 and Eq5[1,0]==0 and Eq5[2,0]==0 and Eq5[3,0]==0:
                if Eq5[3,1]==0:
                    Eq6 = Eq5
                else:
                    Eq6 = np.array([Eq5[0], Eq5[1], Eq5[2], Eq5[3]-Eq5[0]*Eq5[3,1]/Eq5[0,1]])
            elif Eq5[0,1]==0 and Eq5[1,1]==0 and Eq5[2,1]==0 and Eq5[3,1]==0:
                if Eq5[1,2]==0 and Eq5[2,2]!=0:
                    Eq6 = np.array([Eq5[0], Eq5[2], Eq5[1], Eq5[3]])
                elif Eq5[1,2]==0 and Eq5[3,2]!=0:
                    Eq6 = np.array([Eq5[0], Eq5[3], Eq5[2], Eq5[1]])
                elif Eq5[2,2]==0:
                    Eq6 = Eq5
                else: Eq6 = np.array([Eq5[0], Eq5[1], Eq5[2]-Eq5[1]*Eq5[2,2]/Eq5[1,2], Eq5[3]])
            elif Eq5[2,2]==0 and Eq5[3,2]!=0:
                Eq6 = np.array([Eq5[0], Eq5[1], Eq5[3], Eq5[2]])
            elif Eq5[3,2]==0:
                Eq6 = Eq5
            else:
                Eq6 = np.array([Eq5[0], Eq5[1], Eq5[2], Eq5[3]-Eq5[2]*Eq5[3,2]/Eq5[2,2]])
            if Eq6[0,0]==0 and Eq6[1,0]==0 and Eq6[2,0]==0 and Eq6[3,0]==0 and Eq6[0,1]==0 and Eq6[1,1]==0 and Eq6[2,1]==0 and Eq6[3,1]==0 and Eq6[0,2]==0 and Eq6[1,2]==0 and Eq6[2,2]==0 and Eq6[3,2]==0:
                if Eq6[0,3]==0 and Eq6[1,3]!=0:
                    Eq7 = np.array([Eq6[1], Eq6[0], Eq6[2], Eq6[3]])
                elif Eq6[0,3]==0 and Eq6[2,3]!=0:
                    Eq7 = np.array([Eq6[2], Eq6[1], Eq6[0], Eq6[3]])
                elif Eq6[0,3]==0 and Eq6[3,3]!=0:
                    Eq7 = np.array([Eq6[3], Eq6[1], Eq6[2], Eq6[0]])
                elif Eq6[1,3]==0:
                    Eq7 = Eq6
                else:
                    Eq7 = np.array([Eq6[0], Eq6[1]-Eq6[0]*Eq6[1,3]/Eq6[0,3], Eq6[2], Eq6[3]])
            elif Eq6[0,0]==0 and Eq6[1,0]==0 and Eq6[2,0]==0 and Eq6[3,0]==0 and Eq6[0,1]==0 and Eq6[1,1]==0 and Eq6[2,1]==0 and Eq6[3,1]==0:
                if Eq6[2,2]==0:
                    Eq7 = Eq6
                else:
                    Eq7 = np.array([Eq6[0], Eq6[1], Eq6[2]-Eq6[0]*Eq6[2,2]/Eq6[0,2], Eq6[3]])
            elif Eq5[0, 1] == 0 and Eq5[1, 1] == 0 and Eq5[2, 1] == 0 and Eq5[3, 1] == 0 and Eq5[0, 2] == 0 and Eq5[1, 2] == 0 and Eq5[2, 2] == 0 and Eq5[3, 2] == 0:
                if Eq6[3,3]==0:
                    Eq7 = Eq6
                else:
                    Eq7 = np.array([Eq6[0], Eq6[1], Eq6[2], Eq6[3]-Eq6[1]*Eq6[3,3]/Eq6[1,3]])
            elif Eq6[0,0]==0 and Eq6[1,0]==0 and Eq6[2,0]==0 and Eq6[3,0]==0:
                if Eq6[1,2]==0 and Eq6[2,2]!=0:
                    Eq7 = np.array([Eq6[0], Eq6[2], Eq6[1], Eq6[3]])
                elif Eq6[1,2]==0 and Eq6[3,2]!=0:
                    Eq7 = np.array([Eq6[0], Eq6[3], Eq6[2], Eq6[1]])
                elif Eq6[2,2]==0:
                    Eq7 = Eq6
                else:
                    Eq7 = np.array([Eq6[0], Eq6[1], Eq6[2]-Eq6[1]*Eq6[2,2]/Eq6[1,2], Eq6[3]])
            elif Eq6[0,1]==0 and Eq6[1,1]==0 and Eq6[2,1]==0 and Eq6[3,1]==0:
                if Eq6[3,2]==0:
                    Eq7 = Eq6
                else:
                    Eq7 = np.array([Eq6[0], Eq6[1], Eq6[2], Eq6[3]-Eq6[1]*Eq6[3,2]/Eq6[1,2]])
            elif Eq6[0,2]==0 and Eq6[1,2]==0 and Eq6[2,2]==0 and Eq6[3,2]==0:
                if Eq6[2,3]==0 and Eq6[3,3]!=0:
                    Eq7 = np.array([Eq6[0], Eq6[1], Eq6[3], Eq6[2]])
                elif Eq6[3,3]==0:
                    Eq7 = Eq6
                else:
                    Eq7 = np.array([Eq6[0], Eq6[1], Eq6[2], Eq6[3]-Eq6[2]*Eq6[3,3]/Eq6[2,3]])
            else:
                Eq7 = Eq6
            if Eq7[0,0]==0 and Eq7[1,0]==0 and Eq7[2,0]==0 and Eq7[3,0]==0 and Eq7[0,1]==0 and Eq7[1,1]==0 and Eq7[2,1]==0 and Eq7[3,1]==0 and Eq7[0,2]==0 and Eq7[1,2]==0 and Eq7[2,2]==0 and Eq7[3,2]==0:
                if Eq7[2,3]==0:
                    Eq8 = Eq7
                else:
                    Eq8 = np.array([Eq7[0], Eq7[1], Eq7[2]-Eq7[0]*Eq7[2,3]/Eq7[0,3], Eq7[3]])
            elif Eq7[0,0]==0 and Eq7[1,0]==0 and Eq7[2,0]==0 and Eq7[3,0]==0 and Eq7[0,1]==0 and Eq7[1,1]==0 and Eq7[2,1]==0 and Eq7[3,1]==0:
                if Eq7[3,2]==0:
                    Eq8 = Eq7
                else:
                    Eq8 = np.array([Eq7[0], Eq7[1], Eq7[2], Eq7[3]-Eq7[0]*Eq7[3,2]/Eq7[0,2]])
            elif Eq7[0,0]==0 and Eq7[1,0]==0 and Eq7[2,0]==0 and Eq7[3,0]==0:
                if Eq7[3,2]==0:
                    Eq8 = Eq7
                else:
                    Eq8 = np.array([Eq7[0], Eq7[1], Eq7[2], Eq7[3]-Eq7[1]*Eq7[3,2]/Eq7[1,2]])
            elif Eq7[0,1]==0 and Eq7[1,1]==0 and Eq7[2,1]==0 and Eq7[3,1]==0:
                if Eq7[2,3]==0 and Eq7[3,3]!=0:
                    Eq8 = np.array([Eq7[0], Eq7[1], Eq7[3], Eq7[2]])
                elif  Eq7[3,3]==0:
                    Eq8 = Eq7
                else:
                    Eq8 = np.array([Eq7[0], Eq7[1], Eq7[2], Eq7[3]-Eq7[2]*Eq7[3,3]/Eq7[2,3]])
            else:
                Eq8 = Eq7
            if Eq8[0,0]==0 and Eq8[1,0]==0 and Eq8[2,0]==0 and Eq8[3,0]==0 and Eq8[0,1]==0 and Eq8[1,1]==0 and Eq8[2,1]==0 and Eq8[3,1]==0 and Eq8[0,2]==0 and Eq8[1,2]==0 and Eq8[2,2]==0 and Eq8[3,2]==0:
                if Eq8[3,3]==0:
                    Eq9 = Eq8
                else:
                    Eq9 = np.array([Eq8[0], Eq8[1], Eq8[2], Eq8[3]-Eq8[0]*Eq8[3,3]/Eq8[0,3]])
            elif Eq8[0,0]==0 and Eq8[1,0]==0 and Eq8[2,0]==0 and Eq8[3,0]==0 and Eq8[0,1]==0 and Eq8[1,1]==0 and Eq8[2,1]==0 and Eq8[3,1]==0:
                if Eq8[1,3]==0 and Eq8[2,3]!=0:
                    Eq9 = np.array([Eq8[0], Eq8[2], Eq8[1], Eq8[3]])
                elif Eq8[1,3]==0 and Eq8[3,3]!=0:
                    Eq9 = np.array([Eq8[0], Eq8[3], Eq8[2], Eq8[1]])
                elif Eq8[2,3]==0:
                    Eq9 = Eq8
                else:
                    Eq9 = np.array([Eq8[0], Eq8[1], Eq8[2]-Eq8[1]*Eq8[2,3]/Eq8[1,3], Eq8[3]])
            elif Eq8[0,0]==0 and Eq8[1,0]==0 and Eq8[2,0]==0 and Eq8[3,0]==0:
                if Eq8[2,3]==0 and Eq8[3,3]!=0:
                    Eq9 = np.array([Eq8[0], Eq8[1], Eq8[3], Eq8[2]])
                elif Eq8[3,3]==0:
                    Eq9 = Eq8
                else:
                    Eq9 = np.array([Eq8[0], Eq8[1], Eq8[2], Eq8[3]-Eq8[2]*Eq8[3,3]/Eq8[2,3]])
            else:
                Eq9 = Eq8
            if Eq9[0,0]==0 and Eq9[1,0]==0 and Eq9[2,0]==0 and Eq9[3,0]==0 and Eq9[0,1]==0 and Eq9[1,1]==0 and Eq9[2,1]==0 and Eq9[3,1]==0:
                if Eq9[3,3]==0:
                    Eq10 = Eq9
                else:
                    Eq10 = np.array([Eq9[0], Eq9[1], Eq9[2], Eq9[3]-Eq9[1]*Eq9[3,3]/Eq9[1,3]])
            else:
                Eq10 = Eq9
            if Eq10[0,0]!=0:
                if Eq10[1,1]!=0 and Eq10[2,2]!=0 and Eq10[3,3]!=0:
                    r = 4
                elif Eq10[1,1]!=0 and Eq10[2,2]!=0 and Eq10[3,3]==0 or Eq10[1,1]!=0 and Eq10[2,2]==0 and Eq10[2,3]!=0 or Eq10[1,1]==0 and Eq10[1,2]!=0 and Eq10[2,3]!=0:
                    r = 3
                elif Eq10[1,1]!=0 and Eq10[2,2]==0 and Eq10[2,3]==0 or Eq10[1,1]==0 and Eq10[1,2]!=0 and Eq10[2,3]==0 or Eq10[1,1]==0 and Eq10[1,2]==0 and Eq10[1,3]!=0:
                    r = 2
                else:
                    r = 1
            elif Eq10[0,1]!=0:
                if Eq10[1,2]!=0 and Eq10[2,3]!=0:
                    r = 3
                elif Eq10[1,2]!=0 and Eq10[2,3]==0 or Eq10[1,2]==0 and Eq10[1,3]!=0:
                    r = 2
                else:
                    r = 1
            elif Eq10[0,2]!=0:
                if Eq10[1,3]!=0:
                    r = 2
                else:
                    r = 1
            elif Eq10[0,3]!=0:
                r = 1
            elif np.count_nonzero(Eq10==0) == 16:
                r = 0
            else:
                r = 1

            exp="[A] =\n"+self.Mat3D(np.round(Eq0,3))+"\n\nRank = \n"+self.Mat3D(np.round(Eq10,3))+"\n\n\tRank : "+str(r)
        else:
            exp = "Please choose \na dimension \nbefore compute"
        return exp