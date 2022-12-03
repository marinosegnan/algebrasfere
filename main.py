import sympy as sp
from circonftangenti import  Soluzione
from disegno import dise
from simboli import limita,tempo
from figure import Cerchio


def giaqui(cer,dove):
    for el in dove:
        if cer.simile(el):
            return True
    return False

def toglidup(lista):
    ret = [lista[0]]
    for cer in lista[1:]:
        if not giaqui(cer, ret):
            ret.append(cer)
    return ret


def filtra (lis,listadiliste):
    # elimina cerchi gia' trovati
    ret = []
    for cer in lis:
        if (cer.r < 0.000000001): #cerchio troppo piccolo (raggio == 0)
            continue
        for list1 in listadiliste:
            if giaqui(cer,list1):
                break
        else:
            ret.append(cer)
    return ret

def fraziona(els):
    # se espressione simbolica troppo grande, rimpiccioliscila
    for el in els:
        limita(el)

#tutti =[[Cerchio(sp.Integer(0), sp.Integer(0), sp.Integer(2)), Cerchio(sp.Integer(5), sp.Integer(0), sp.Integer(2)), Cerchio(sp.Rational(5/2),sp.Rational(5/2),sp.Rational(3/2))]]

tutti = [[Cerchio(sp.Integer(0), sp.Integer(0), sp.Integer(1)), Cerchio(sp.Integer(2), sp.Integer(0), sp.Integer(1)), Cerchio(sp.Integer(1),sp.sqrt(3),sp.Integer(1))]]
limit = 30
index = 0
soluzione = Soluzione()
# dati tre cerchi tangenti, disegna poco a poco tutti quelli tangenti internamente, sempre piu' piccoli
#fermati a 10

# rifare da 0 la struttura!!!

tt = tempo()
while index < limit and index < len(tutti):
    c1, c2, c3 = tutti[index]
  #  dise(tutti[index], finestra())
    parziale = soluzione.trova(c1, c2, c3)
    # se raggio < 0 invertine il segno
    for c in parziale:
        print(c)
        c.r = abs(c.r)
    #   print('ris=',c4)
    c4 = filtra(parziale,tutti)

    fraziona(c4)
    tutti[index].extend(c4)
#    dise(tutti[index])
    for cer in c4:
        tutti.append([c1, c2, cer])
        tutti.append([c1, c3, cer])
        tutti.append([c2, c3, cer])
    index += 1
    print('index=',index)

tt('fineprogramma:')
listacerchi = toglidup([inner for outer in tutti for inner in outer])
altra = []
for el in listacerchi:
    altra.append(el.float())
dise(listacerchi)
print('lista cerchi')
for cer in altra:
    print(cer)
