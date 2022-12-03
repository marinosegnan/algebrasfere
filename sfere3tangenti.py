import sympy as sp

from disegno import plt_sphere
from figure import Sfera
from simboli import *

class Soluzione:

    def crea_eq(self, x_i, y_i, z_i, r_i):
        expr = sp.expand((x - x_i) ** 2 + (y - y_i) ** 2 + (z - z_i) ** 2 - r_i ** 2)
        posx = x_i + r_i * ((x_5 - x_i) / (r_5 + r_i))
        posy = y_i + r_i * ((y_5 - y_i) / (r_5 + r_i))
        posz = z_i + r_i * ((z_5 - z_i) / (r_5 + r_i))
        val = expr.subs(x, posx).subs(y, posy).subs(z, posz)
        return val.expand().simplify()

    def __init__(self):
        # print('creo soluzione')
        t1 = tempo()

        # 3 equazioni di circonferenza
        self.finale1 = self.crea_eq(x_1, y_1, z_1, r_1)
        self.finale2 = self.crea_eq(x_2, y_2, z_2, r_2)
        self.finale3 = self.crea_eq(x_3, y_3, z_3, r_3)
        t1('tempo soluzione equazioni di base')
        #
        # troppo lento!!!!!, occorre sostituire i coefficienti numerici
        # qua1 = sp.Eq( self.finale1 , 0)
        # qua2 = sp.Eq( self.finale2 , 0)
        # qua3 = sp.Eq( self.finale3,  0)
        # qua4 = sp.Eq( self.finale4,   0)
        #
        # sol = sp.solve((qua1, qua2, qua3, qua4), (x_5, y_5, z_5, r_5), set=True)
        # print(sol)



    def trova(self, c1, c2, c3,c4) -> object:
        t1 = tempo()
        # la sfera c4 e' usata per imporre la soluzione con raggio noto,
        # le coordinate del suo centro non sono usate
        # altrimenti date 3 circonferenze, in molti casi le soluzioni sono infinite.
        # imporre il raggio limita le soluzioni a 2
        # se non si sostituiscono le costanti del caso,
        # risolvere simbolicamente richiede tempo ignoto!!!!!!
        # percio' si ripete per ogni invocazione anziche'
        # risolverlo simbolicamente una volta per tutte

        qua1 = sp.Eq(self.sosti(self.finale1, c1, c2, c3, c4), 0)
        qua2 = sp.Eq(self.sosti(self.finale2, c1, c2, c3, c4), 0)
        qua3 = sp.Eq(self.sosti(self.finale3, c1, c2, c3, c4), 0)

        sol = sp.solve((qua1, qua2, qua3), (x_5, y_5, z_5), set=True)
        t1( 'tempo per soluzione')
        # print(sol)
        nuovi = []
        for el in sol[1]:
            valori = {}
            for ind, el1 in enumerate(el):
                # manteniamo soluzione simbolica  se no: vv = el1.evalf()
                valori[sol[0][ind]] = el1
            # x_5 .... sono hardcoded
            nuovi.append(Sfera(valori[x_5], valori[y_5],  valori[z_5], c4.r))
            print('soluzione:',nuovi[-1])
        return nuovi

    def sosti(self, esp, c1, c2, c3, c4):
        # togli tutti i coefficienti noti
        # la quarta circonferenze e' usata solo per il raggio
        return esp.subs(r_1, c1.r).subs(r_2, c2.r).subs(r_3, c3.r) \
            .subs(x_1, c1.x).subs(y_1, c1.y).subs(z_1, c1.z) \
            .subs(x_2, c2.x).subs(y_2, c2.y).subs(z_2, c2.z) \
            .subs(x_3, c3.x).subs(y_3, c3.y).subs(z_3, c3.z) \
            .subs(r_5, c4.r)

coords = [(0,0,0,1),(0,5,0,1),(5,0,0,1),(5,5,0,5)]
speciale = 2*sp.sqrt(6)/3

coords = [(0,0,0,1),(2,0,0,1),(1,sp.sqrt(3),0,1),(5,5,0,1)]

#sfere = [Sfera(sp.Rational(c[0]),sp.Rational(c[1]),sp.Rational(c[2]),sp.Rational(c[3])) for c in coords]
#sfere = [Sfera(sp.Rational(c[0]),c[1],sp.Rational(c[2]),sp.Rational(c[3])) for c in coords]
sfere = [Sfera(c[0],c[1],c[2],c[3]) for c in coords]


# 2 radice 6 / 3

if __name__ == '__main__':
    soluzione = Soluzione()
    ris = soluzione.trova(*sfere)
    del sfere[-1] # quarta sfera dummy, ci serve solo per il raggio
    sfere.extend(ris)
    sferefloat = [s.float() for s in sfere]
    plt_sphere(sferefloat,3)