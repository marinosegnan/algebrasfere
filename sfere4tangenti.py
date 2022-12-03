import sympy as sp
from figure import Sfera, finestra
from disegno import plt_sphere
from simboli import *


class Soluzione:

    def crea_eq(self, x_i, y_i, z_i, r_i):
        expr = sp.expand((x - x_i) ** 2 + (y - y_i) ** 2 + (z - z_i) ** 2 - r_i ** 2)
        posx = x_i + r_i * ((x_5 - x_i) / (r_5 + r_i))
        posy = y_i + r_i * ((y_5 - y_i) / (r_5 + r_i))
        posz = z_i + r_i * ((z_5 - z_i) / (r_5 + r_i))
        val = expr.subs(x, posx).subs(y, posy).subs(z, posz)
        return val.expand().simplify()

    def estrai_sol(self,variabili, sol):
        nuovi = []
        solgiuste = len(sol[0]) == len(variabili)
        if not solgiuste:
            print('mancano soluzioni:',variabili,sol[0])
        if len(sol[1]) == 0:
            print('NO SOLUTION')
        else:
            for el in sol[1]:
                valori = {}
                for ind, el1 in enumerate(el):
                    # manteniamo soluzione simbolica  se no: vv = el1.evalf()
                    valori[sol[0][ind]] = el1
                if solgiuste:
                    nuovi.append(Sfera(valori[variabili[0]], valori[variabili[1]], valori[variabili[2]], valori[variabili[3]]))
                print('soluzione:', nuovi[-1])
        return nuovi

    def __init__(self):
        # print('creo soluzione')
        t1 = tempo(None)

        # 4 equazioni di circonferenza

        self.finale1 = self.crea_eq(x_1, y_1, z_1, r_1)
        self.finale2 = self.crea_eq(x_2, y_2, z_2, r_2)
        self.finale3 = self.crea_eq(x_3, y_3, z_3, r_3)
        self.finale4 = self.crea_eq(x_4, y_4, z_4, r_4)

        tempo(t1, 'tempo soluzione equazioni di base')

    def trova(self, c1, c2, c3, c4) -> object:

        t1 = tempo(None)

        # se non si sostituiscono le costanti del caso,
        # risolvere simbolicamente richiede tempo ignoto!!!!!!
        # percio' si ripete per ogni invocazione anziche'
        # risolverlo simbolicamente una volta per tutte

        qua1 = sp.Eq(self.sosti(self.finale1, c1, c2, c3, c4), 0)
        qua2 = sp.Eq(self.sosti(self.finale2, c1, c2, c3, c4), 0)
        qua3 = sp.Eq(self.sosti(self.finale3, c1, c2, c3, c4), 0)
        qua4 = sp.Eq(self.sosti(self.finale4, c1, c2, c3, c4), 0)

        variabili= (x_5, y_5, z_5, r_5)
        sol = sp.solve((qua1, qua2, qua3, qua4), variabili, set=True)
        tempo(t1, 'tempo per soluzione')
        return self.estrai_sol(variabili,sol)

    def sosti(self, esp, c1, c2, c3, c4):
        # togli tutti i coefficienti noti
        return esp.subs(r_1, c1.r).subs(r_2, c2.r).subs(r_3, c3.r).subs(r_4, c4.r) \
            .subs(x_1, c1.x).subs(y_1, c1.y).subs(z_1, c1.z) \
            .subs(x_2, c2.x).subs(y_2, c2.y).subs(z_2, c2.z) \
            .subs(x_3, c3.x).subs(y_3, c3.y).subs(z_3, c3.z) \
            .subs(x_4, c4.x).subs(y_4, c4.y).subs(z_4, c4.z)


# coords = [(0,0,0,1),(10,5,0,2),(5,8,0,2),(15,15,0,1)]
# coords = [(0,0,0,1),(0,5,0,1),(5,0,0,1),(5,5,5,1)]
# coords = [(0,0,0,1),(10,0,0,1),(0,10,0,1),(0,0,10,1)]
# coords = [(0,0,0,1),(10,5,0,1),(5,10,0,1),(10,10,10,1)]
# coords = [(0,0,0,1),(10,5,5,1),(5,10,0,1),(10,10,10,1)]
# coords = [(0,0,0,1),(3,5,0,1),(5,3,0,1),(10,10,0,1)]
# coords = [(0,0,10,1),(3,5,10,1),(5,3,10,1),(10,10,10,1)]

speciale = 2 * sp.sqrt(6) / 3  # tetraedro



def unaprova(coords):
    sfere = [Sfera(c[0], c[1], c[2], c[3]) for c in coords]
    ris = soluzione.trova(*sfere)
    sfere.extend(ris)
    sferefloat = [c.float() for c in sfere]
    plt_sphere(sferefloat)

if __name__ == '__main__':
    soluzione = Soluzione()
    coords = [(0, 0, 0, 1), (2, 0, 0, 1), (1, sp.sqrt(3) / 2, 0, 1), (1, sp.sqrt(3) / 3, speciale, 1)]
    unaprova(coords)
    unaprova([(0, 0, 10, 1), (3, 5, 10, 1), (5, 3, 10, 1), (10, 10, 10, 1)])
    unaprova([(0,0,0,1),(10,5,5,1),(5,10,0,1),(10,10,10,1)])
