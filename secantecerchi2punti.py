import sympy as sp
import sys
from datetime import datetime

from matplotlib.collections import PatchCollection
import numpy as np


import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def dise(cerchi, drawx=[],drawy=[]):

    fig, ax = plt.subplots()
    fig.set_size_inches(8, 8)
    ax.set_aspect('equal')
    colors = ['r','g','b','y']
    patches = []
    for c,col in zip(cerchi,colors):


        cc= Circle((c.x,c.y), c.r,color=col)
        patches.append(cc)

    plt.xlim(-12, 12)
    plt.ylim(-12, 12)

    if drawx:
        plt.plot(drawx,drawy)
    colors = 100 * np.random.rand(len(patches))
  #  p = PatchCollection(patches, alpha=0.4)

    p = PatchCollection(patches)
    p.set_array(colors)
    ax.add_collection(p)
  #  fig.colorbar(p, ax=ax)
    plt.show()

def tempo(old,msg=''):
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    if old:
        print(msg,str(ts - old))
    return ts

class Cerchio:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return 'r:'+str(self.r)+' x:'+str(self.x)+'y:'+str(self.y)


x = sp.symbols('x')
y = sp.symbols('y')
r = sp.symbols('r')
x_1 = sp.symbols('x_1')
x_2 = sp.symbols('x_2')
x_3 = sp.symbols('x_3')
x_4 = sp.symbols('x_4')
y_1 = sp.symbols('y_1')
y_2 = sp.symbols('y_2')
y_3 = sp.symbols('y_3')
y_4 = sp.symbols('y_4')
r_1 = sp.symbols('r_1')
r_2 = sp.symbols('r_2')
r_3 = sp.symbols('r_3')
r_4 = sp.symbols('r_4')





class Soluzione:

    def fafa(self,c1,c2,c3):
        eqq = sp.sqrt((-r_1**2 + 2*r_1*r_2 - r_2**2 + x_1**2 - 2*x_1*x_2 + x_2**2 + y_1**2 - 2*y_1*y_2 + y_2**2)*(r_1**2 + 2*r_1*r_2 + r_2**2 - x_1**2 + 2*x_1*x_2 - x_2**2 - y_1**2 + 2*y_1*y_2 - y_2**2))*(-y_1 + y_2)/(x_1**2 - 2*x_1*x_2 + x_2**2 + y_1**2 - 2*y_1*y_2 + y_2**2)
        print(self.sosti(eqq,c1,c2,c3).evalf())

    def __init__(self,c1,c2,c3):
        self.fafa(c1,c2,c3)
        print('creo soluzione')
        t1 = tempo(None)
        self.expr1 = sp.expand((x - x_1) ** 2 + (y - y_1) ** 2 - r_1 ** 2)
        self.expr2 = sp.expand((x - x_2) ** 2 + (y - y_2) ** 2 - r_2 ** 2)
        self.expr3 = sp.expand((x - x_3) ** 2 + (y - y_3) ** 2 - r_3 ** 2)
        self.expr4 = sp.expand((x - x_4) ** 2 + (y - y_4) ** 2 - r_4  ** 2)
        self.expr5 = sp.expand((x - x_4) ** 2 + (y - y_4) ** 2 - (r - r_2) ** 2)
        self.expr6 = sp.expand((x - x_4) ** 2 + (y - y_4) ** 2 - (r - r_3) ** 2)
       # t1 = self.sosti((self.expr1-self.expr2).simplify(),c1,c2,c3)
        t1 = (self.expr1 - self.expr2).simplify()
      #  print(t1)
        sol = sp.solve((t1), ( y),set =True)
     #   t2 = tempo(t1, 'fatte eq')
        print('soluzy:',sol)

        valori = {}

        for el in sol[1]:
            for ind,el1 in enumerate(el):
                miasol = self.sosti(el1,c1,c2,c3)
                valori[sol[0][ind]]=miasol
            #    print(sol[0][ind],' : ',self.sosti(el1,c1,c2,c3))#sp.factor(el1),'\n')
            #break
        print(valori)

        ee = self.expr1.subs('y',el1)
        sol = sp.solve(ee,t1, (x), set=True)
        print('soluzx:', sol)

        ind = 0
        for el in sol[1]:
                if ind == 0:
                    solx1 = el[0]
                    ind = 1
                else:
                    solx2 = el[0]

        nuova1 = (solx1-solx2).simplify()

        print('nuova1:',nuova1)
        nuova1 = sp.Eq(nuova1,0)
        sol32 = sp.solve(nuova1,t1, (x_2,y_2), set=True)
        print('sol32:',sol32)






        valori = {}
        lisa=[]
        drawx =[]
        drawy =[]
        for el in sol[1]:
            for ind,el2 in enumerate(el):

                tm =  self.sosti(el2,c1,c2,c3).evalf()
                drawx.append(tm)
                valori[sol[0][ind]] = tm
                lisa.append(tm)
                print(tm)
            #    print(sol[0][ind],' : ',self.sosti(el1,c1,c2,c3))#sp.factor(el1),'\n')
            #break
        #print(valori)
        for vv in lisa:
            tm = miasol.subs('x',vv).evalf()
            if tm.has(sp.I):
                print('immagianrio')
                continue

            drawy.append(tm)
            print(tm)
        if drawy:
            dise([c1,c2],drawx,drawy)
        else:
            dise([c1,c2])


    #    dise([Cerchio(0, 0, 4), Cerchio(10, 0, 4), Cerchio(0, 10, 1),Cerchio(valori[x].evalf(),valori[y].evalf(),raggio)])

    def sosti(self,esp,c1,c2,c3):
        return  esp.subs(r_1, c1.r).subs(r_2, c2.r).subs(r_3, c3.r).subs(x_1, c1.x).subs(y_1, c1.y).subs(x_2,c2.x).subs(
                     y_2, c2.y).subs(x_3, c3.x).subs(y_3, c3.y)

soluzione = Soluzione(Cerchio(0, 0, 10), Cerchio(10,10,8), Cerchio(0, 10, 1))
#soluzione = Soluzione(Cerchio(0, 0, 2), Cerchio(5, 0, 2), Cerchio(sp.Rational(5/2),sp.Rational(5/2),sp.Rational(3/2)))
