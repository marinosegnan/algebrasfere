import sympy as sp

##esempio: x ,y ,x_1,y_1,r_1,x_2,y_2,r_2,x_3,y_3,r_3,x_4,y_4,r_4 = sp.symbols('x  y  x_1 y_1 r_1 x_2 y_2 r_2 x_3 y_3 r_3 x_4 y_4 r_4')
x = sp.symbols('x')
y = sp.symbols('y')
z = sp.symbols('z')
x_1 = sp.symbols('x_1')
x_2 = sp.symbols('x_2')
x_3 = sp.symbols('x_3')
x_4 = sp.symbols('x_4')
x_5 = sp.symbols('x_5')
y_1 = sp.symbols('y_1')
y_2 = sp.symbols('y_2')
y_3 = sp.symbols('y_3')
y_4 = sp.symbols('y_4')
y_5 = sp.symbols('y_5')
z_1 = sp.symbols('z_1')
z_2 = sp.symbols('z_2')
z_3 = sp.symbols('z_3')
z_4 = sp.symbols('z_4')
z_5 = sp.symbols('z_5')
r_1 = sp.symbols('r_1')
r_2 = sp.symbols('r_2')
r_3 = sp.symbols('r_3')
r_4 = sp.symbols('r_4')
r_5 = sp.symbols('r_5')
sym = sp.symbols('sym')
R1 = sp.symbols('R1')
R2 = sp.symbols('R2')
R3 = sp.symbols('R3')
S1 = sp.symbols('S1')
S2 = sp.symbols('S2')
S3 = sp.symbols('S3')

from datetime import datetime


class tempo:

    def __init__(self):
        self.time = datetime.timestamp(datetime.now())

    def __call__(self, msg=None):
        ts = datetime.timestamp(datetime.now())
        if msg:
            print(msg, str(ts - self.time))
        self.time = ts


def timer():  # versione con closure
    prev = datetime.timestamp(datetime.now())

    def miot(msg=None):
        t1 = datetime.timestamp(datetime.now())
        nonlocal prev
        if msg:
            print(msg, t1 - prev)
        prev = t1

    return miot


from fractions import Fraction

def nuovoval(espr,lim):
    temp = Fraction.from_float(float(espr.evalf())).limit_denominator(lim)
    return sp.Rational(temp.numerator, temp.denominator)

def limita(cerchio):
    # se espressione troppo lunga, semplificala con una frazione convertita in sp.Rational
    if contiene(cerchio.x):
        cerchio.x = nuovoval(cerchio.x,100000)
    s,n = pre(cerchio.x)
    if (s+n) > 4:
        cerchio.x = nuovoval(cerchio.x,1000)
        cerchio.frazionato += '(X)'
    if contiene(cerchio.y):
        cerchio.y = nuovoval(cerchio.y, 100000)
    s, n = pre(cerchio.y)
    if (s + n) > 4:
        cerchio.y = nuovoval(cerchio.y, 1000)
        cerchio.frazionato += '(Y)'
    if contiene(cerchio.r):
        cerchio.r = nuovoval(cerchio.r, 100000)
    s, n = pre(cerchio.r)
    if (s + n) > 4:
        cerchio.r = nuovoval(cerchio.r, 1000)
        cerchio.frazionato += '(R)'

def limitaOld(cerchio):
    # se espressione troppo lunga, semplificala con una frazione convertita in Rational
    if len(cerchio.x.expr_free_symbols) > 4:
        temp = Fraction.from_float(float(cerchio.x.evalf())).limit_denominator(1000)
        cerchio.x = sp.Rational(temp.numerator, temp.denominator)
        cerchio.frazionato += '(X)'
    if len(cerchio.y.expr_free_symbols) > 4:
        temp = Fraction.from_float(float(cerchio.y.evalf())).limit_denominator(1000)
        cerchio.y = sp.Rational(temp.numerator, temp.denominator)
        cerchio.frazionato += '(Y)'
    if len(cerchio.r.expr_free_symbols) > 4:
        temp = Fraction.from_float(float(cerchio.r.evalf())).limit_denominator(1000)
        cerchio.r = sp.Rational(temp.numerator, temp.denominator)
        cerchio.frazionato += '(R)'

def pre(expr, syms=0, nums=0):
    # print(expr)
    for a in expr.args:
        if type(a) == sp.core.Symbol:
            syms += 1
        if issubclass(type(a), sp.core.Number):
            nums += 1
    for arg in expr.args:
        s, n = pre(arg)
        syms += s
        nums += n
    return syms, nums

def contiene(expr):
    # se expr contiene un numero troppo grande
    # segnalalo in modo che la espressione sara' convertita a float
    # print(expr)
    if issubclass(type(expr), sp.core.Integer):
        if abs(expr) > 10**15:
            return True
    if issubclass(type(expr), sp.core.Rational):
        if abs(expr.numerator) > 10**15:
            return True
    for a in expr.args:
        if contiene(a):
            return True
    return False

def contieneErroreapprossimazione(expr):
    # print(expr)
    if issubclass(type(expr), sp.core.Integer):
        if abs(expr) > 10**15:
            return 2
    if issubclass(type(expr), sp.core.Rational):
        if abs(expr.numerator) > 10**15:
            return 2
    for a in expr.args:
        nuova = contiene(a)
        if nuova == 2:
            newval = sp.Float(a.evalf())
            expr = expr.subs(a, newval)
        else:
            print('nuova=',nuova)
            print('NUOVA=', nuova.evalf())
            expr = expr.subs(a, nuova)
    return expr
