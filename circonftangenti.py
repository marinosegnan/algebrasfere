
from disegno import dise
from figure import Cerchio
from simboli import *
import sympy as sp



timer = tempo()
class Soluzione:

    def crea_eq(self, x_i, y_i, r_i):
        expr = sp.expand((x - x_i) ** 2 + (y - y_i) ** 2  - r_i ** 2)
        posx = x_i + r_i * ((x_4 - x_i) / (r_4 + r_i))
        posy = y_i + r_i * ((y_4 - y_i) / (r_4 + r_i))
        val = expr.subs(x, posx).subs(y, posy)
        return val.expand().simplify()

    def __init__(self):
       # print('creo soluzione')



        # retta1 = sp.Eq((y - y_4) / (y_1 - y_4), (x - x_4) / (x_1 - x_4))
        # retta2 = sp.Eq((y - y_4) / (y_2 - y_4), (x - x_4) / (x_2 - x_4))
        # retta3 = sp.Eq((y - y_4) / (y_3 - y_4), (x - x_4) / (x_3 - x_4))

        # pos* sono coordinate di intersezione tra rette e 3 circonferenze
        # introdotte per eliminare la coppia di variabili (x,y) generica
        # nelle tre equazioni, cosi' x della prima e' sostiuitta da psox1 etc
        # nel seguito expand() e simplify() migliorano parecchio la velocita

        self.finale1 = self.crea_eq(x_1, y_1, r_1)
        self.finale2 = self.crea_eq(x_2, y_2, r_2)
        self.finale3 = self.crea_eq(x_3, y_3, r_3)

        # stampa quanti simboli e numeri ci sono nell'equazione
        timer( 'tempo soluzione equazioni di base')
        s,n = pre(self.finale1)
        print('syms:', s ,'nums:',n)


    def trova(self, c1, c2, c3, diseg = False) -> object:
        t1 = tempo()

        # se non si sostituiscono le costanti del caso,
        # risolvere simbolicamente richiede tempo ignoto!!!!!!
        # percio' si ripete per ogni invocazione anziche'
        # risolverlo simbolicamente una volta per tutte
        # print(self.finale1)
        # print(self.finale2)
        # print(self.finale3)
        qua1 = sp.Eq(self.sosti(self.finale1, c1, c2, c3), 0)
        qua2 = sp.Eq(self.sosti(self.finale2, c1, c2, c3), 0)
        qua3 = sp.Eq(self.sosti(self.finale3, c1, c2, c3), 0)

        # print('operatori:',qua1.count_ops(),self.finale1.count_ops())
        # print('operatori:', qua2.count_ops(), self.finale2.count_ops())
        # print('operatori:', qua3.count_ops(), self.finale3.count_ops())

        # print(qua1)
        # print(qua2)
        # print(qua3)
        sol = sp.solve((qua1,qua2,qua3),(x_4,y_4,r_4),set=True)

        t1('tempo per soluzione')

        print(sol)

        nuovi = []
        for el in sol[1]:
            valori = {}
            for ind, el1 in enumerate(el):
               # manteniamo soluzione simbolica  se no: vv = el1.evalf()
                valori[sol[0][ind]] = el1
            # x_4 y_4 e r_4 sono hardcoded
         #   nuovi.append( Cerchio(valori[x_4], valori[y_4], valori[r_4]))
            nuovi.append(Cerchio(valori[x_4], valori[y_4], valori[r_4]))
        if diseg:
            cerchifloat = [c.float() for c in [c1,c2,c3]+nuovi]
            dise(cerchifloat)
        return nuovi

    def sosti(self, esp, c1, c2, c3):
        # togli tutti i coefficienti noti
        return esp.subs(r_1, c1.r).subs(r_2, c2.r).subs(r_3, c3.r) \
                    .subs(x_1, c1.x).subs(y_1, c1.y).subs(x_2, c2.x) \
                    .subs(y_2, c2.y).subs(x_3, c3.x).subs(y_3, c3.y)

if __name__== '__main__':
    soluzione = Soluzione()
    c4 = soluzione.trova(Cerchio(sp.Rational(2), sp.Rational(22, 10), sp.Rational(17, 8)),
                        Cerchio(sp.Rational(50, 49), sp.Rational(49, 50), sp.Rational(19, 8)),
                        Cerchio(sp.Rational(121, 10), sp.sqrt(3), sp.Rational(15, 8)), diseg=True)

    c4 = soluzione.trova(Cerchio(sp.Rational(2), sp.Rational(2), sp.Rational(2)),
                         Cerchio(sp.Rational(5), sp.Rational(5), sp.Rational(2)),
                         Cerchio(sp.Rational(12), sp.sqrt(3), sp.Rational(2)), diseg=True)

    c4 = soluzione.trova(Cerchio(sp.Integer(0), sp.Integer(0), sp.Integer(1)),
                         Cerchio(sp.Integer(2), sp.Integer(0), sp.Integer(1)),
                         Cerchio(1, sp.sqrt(3), 1), diseg=True)


    c4 = soluzione.trova(Cerchio(sp.Integer(0), sp.Integer(0), sp.Integer(1)), Cerchio(sp.Integer(2), sp.Integer(0), sp.Integer(1)), Cerchio(sp.Integer(1),sp.sqrt(3),sp.Integer(1)), diseg=True)
    c4 = soluzione.trova(Cerchio(sp.Integer(0), sp.Integer(0), sp.Integer(2)), Cerchio(sp.Integer(5), sp.Integer(0), sp.Integer(2)), Cerchio(sp.Rational(5/2),sp.Rational(5/2),sp.Rational(3/2)), diseg=True)

