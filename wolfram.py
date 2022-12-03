from disegno import dise
from figure import Cerchio
from simboli import *

# esempio che trae dal sito wolfram sfruttando le loro equazioni
# https://mathworld.wolfram.com/ApolloniusProblem.html
a, a1, b, b1, c, c1, d, d1, r, e1 = sp.symbols('a b c d a1 b1 c1 d1 r e1')


class Soluzione:

    def __init__(self):
        t1 = tempo()
        solx = (b1 * d - b * d1 - b1 * c * r + b * c1 * r) / (a * b1 - b * a1)
        soly = (-a1 * d + a * d1 + a1 * c * r - a * c1 * r) / (a * b1 - a1 * b)
        e1 = (x-x_1)**2 +(y-y_1)**2 -(r+r_1)**2 # rciodare il meno! -
        efin = e1.subs(x,solx).subs(y,soly)
        # ci mette 7 secondi
        print('operatori:',efin.count_ops())
        sol = sp.solve((efin), (r))
        #ognuna delle due soluzioni ha 150 termini circa
        t1( 'tempo per soluzione')
        s1 = sol[1]
        print(s1)
        print('operatori sol:', s1.count_ops())
        # e ognuno dei parametri a sua volta (a a1 b b1... quando sostituito diventa ancor piu' grande
        va = 2*(x_1-x_2)
        vb = 2 * (y_1 - y_2)
        vc = 2*(r_1+r_2)   #segno per r1 e r2
        vd = (x_1**2 +y_1**2-r_1**2)-(x_2**2 +y_2**2-r_2**2)
        va1 = 2 * (x_1 - x_3)
        vb1 = 2 * (y_1 - y_3)
        vc1 = 2 * (r_1 + r_3)  # segno per r1 e r2
        vd1 = (x_1 ** 2 + y_1 ** 2 - r_1 ** 2) - (x_3 ** 2 + y_3 ** 2 - r_3 ** 2)
        self.finale = s1.subs(a,va).subs(b,vb).subs(c,vc).subs(d,vd).subs(a1,va1).subs(b1,vb1).subs(c1,vc1).subs(d1,vd1)
        print(self.finale)




    def trova(self, c1, c2, c3, diseg=False) -> object:
        finale1 = self.sosti(self.finale,c1,c2,c3)
        # da' valore giusto del raggio usando il mio altro metodo,
        # ma approssimazione differente: 7.37 contro 7.32 del mio!!!
        ff = finale1.evalf()
        print(ff)

    def sosti(self, esp, c1, c2, c3):
        # togli tutti i coefficienti noti
        return esp.subs(r_1, c1.r).subs(r_2, c2.r).subs(r_3, c3.r) \
            .subs(x_1, c1.x).subs(y_1, c1.y).subs(x_2, c2.x) \
            .subs(y_2, c2.y).subs(x_3, c3.x).subs(y_3, c3.y)


if __name__ == '__main__':
    soluzione = Soluzione()

    c4 = soluzione.trova(Cerchio(sp.Rational(2), sp.Rational(2), sp.Rational(2)),
                         Cerchio(sp.Rational(5), sp.Rational(5), sp.Rational(2)),
                         Cerchio(sp.Rational(12), sp.sqrt(3), sp.Rational(2)), diseg=True)
