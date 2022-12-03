
class Cerchio:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.frazionato = ''

    def __str__(self):
        return 'r:   ' + str(self.r) + '  x:   ' + str(self.x) + '  y:   ' + str(self.y) + ('    // 'if self.frazionato else '   ') +self.frazionato

    def simile(self, cer):
        return  abs(self.x-cer.x) < 0.001 and \
                abs(self.y-cer.y) < 0.001 and \
                abs(self.r - cer.r) < 0.001

    def float(self):
        #raggio convertito sempre a positivo
        return Cerchio(convert(self.x),convert(self.y),abs(convert(self.r)))

class Sfera:

    def __init__(self, x, y,z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

    def __str__(self):
        return '\nr :  ' + str(self.r) + '\nx : ' + str(self.x) + '\ny : ' + str(self.y) + '\nz : ' + str(self.z)

    def simile(self, cer):
        return abs(self.x - cer.x) < 0.001 and \
               abs(self.y - cer.y) < 0.001 and \
               abs(self.z - cer.z) < 0.001 and \
               abs(self.r - cer.r) < 0.001

    def float(self):
        return Sfera(convert(self.x),convert(self.y),convert(self.z),convert(self.r))

def finestra(elementi,size =3):
    #trova spazio che contiene tutte le forme della lista (2=cerchio, tre uguale sfera)
    minx = maxx=miny=maxy=minz=maxz=1
    MAX =  15
    MIN = -MAX
    for c in elementi:
        x1 = c.x -c.r
        x2 = c.x  + c.r
        if x1 < minx:
            minx = x1
        if x2 > maxx:
            maxx = x2
        y1 = c.y-c.r
        y2 = c.y + c.r
        if y1 < miny:
            miny = y1
        if y2 > maxy:
            maxy = y2
        if size == 3:
            z1 = c.z- c.r
            z2 = c.z + c.r
            if z1 < minz:
                minz = z1
            if z2 > maxz:
                maxz = z2
    if size == 2:
        return (float(max(MIN,minx)) ,float(min(MAX,maxx)), float(max(MIN,miny)) ,float(min(MAX,maxy)) )
    else:
        return (float(max(MIN,minx)) ,float(min(MAX,maxx)), float(max(MIN,miny)) ,float(min(MAX,maxy)), float(max(MIN,minz)), float(min(MAX,maxz)))


def convert(n):
    if type(n) == int:
        return float(n)
    elif type(n) == float:
        return n
    else:
        return float(n.evalf())

