import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection
import numpy as np
from figure import Sfera,finestra
from matplotlib.colors import colorConverter
import matplotlib

def dise(cerchi):
    spazio = finestra(cerchi,size=2)
    #colors = list(matplotlib.colors.CSS4_COLORS.keys())
    colors = list(matplotlib.colors.TABLEAU_COLORS.keys())*3

    fig, ax = plt.subplots()
    print('disegno cerchi: ', len(cerchi))
    cerchi = sorted(cerchi,key= lambda x: x.r,reverse=True)
    fig.set_size_inches(8, 8)
    ax.set_aspect('equal')
    patches = []
  #  colors = 100 * np.random.rand(len(cerchi))
    for cer ,col in zip(cerchi,colors):
        c =cer.float()
        fc = colorConverter.to_rgba(col, alpha=0.5)
        ec = colorConverter.to_rgba('black')#, alpha=0.5)
        cc = Circle(( c.x, c.y), c.r,facecolor =fc ,edgecolor=ec, linewidth=1 )
        patches.append(cc)
    plt.xlim(spazio[0]-1,spazio[1]+1)
    plt.ylim(spazio[2]-1,spazio[3]+1)
    p = PatchCollection(patches,match_original=True) # se no colore eliminato!!!

    ax.add_collection(p)
    plt.show()


def plt_sphere(sfere,partenza = 4 ):
    spazio = finestra(sfere)
    fig = plt.figure()
    fig.set_size_inches(8, 8)
    ax = fig.add_subplot(projection='3d')
    ax.axes.set_xlim3d(left=spazio[0], right=spazio[1])
    ax.axes.set_ylim3d(bottom=spazio[2], top=spazio[3])
    ax.axes.set_zlim3d(bottom=spazio[4], top=spazio[5])
    for col, s in zip(['y', 'y', 'y', 'y' if partenza == 4 else 'r', 'm', 'g'],sfere):
    # draw sphere
        u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:50j]
        x = s.r*np.cos(u)*np.sin(v)
        y = s.r*np.sin(u)*np.sin(v)
        z = s.r*np.cos(v)

  #      ax.plot_surface(x-c[0], y-c[1], z-c[2], color=np.random.choice(['g','b','y','r','c','m']), alpha=0.5*np.random.random()+0.5)
        ax.plot_surface( s.x - x,  s.y - y, s.z - z, color=col,
                    alpha=0.3)
  #  ax.set_aspect('equal')
    ax.set_xlabel('X')
    ax.set_zlabel('Z')
    ax.set_ylabel('Y')
    plt.axis('equal')
    plt.show()

if __name__ == '__main__':
    plt_sphere([ Sfera(1,2,3,1),Sfera(-4,-5,6,2), Sfera(5,5,6,1)])
