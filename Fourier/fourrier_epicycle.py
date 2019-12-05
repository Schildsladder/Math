# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:17:10 2019

@author: i
"""

#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
#from matplotlib import style
#import numpy as np
#import random
#
#style.use('fivethirtyeight')
#fig = plt.figure()
#ax1 = fig.add_subplot(111)
#x=np.linspace(0,30,300)
#
#def animate(i):
#
##    global k
#
#    ax1.clear()
#    ax1.plot(x,np.sin(x+(i/3.0)))
#    print (i)
##    ax1.axis([-110*scale, 50*scale, -13*scale, 13*scale])
#
#ani = animation.FuncAnimation(fig, animate, interval=100)
#plt.show()


import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np




a=np.array([9.88033+4.4584j, 9.88033+4.4584j, 6.5966000000000005+1.8406800000000003j, 3.8003100000000005+3.92164j])
b=np.array([3.8003100000000005+3.92164j, 1.0040200000000006+6.0026j, 2.2716500000000006+9.953479999999999j, 3.9948700000000006+12.61972j])
c=([3.9948700000000006+12.61972j, 5.71809+15.28596j, 9.88033+17.85458j, 9.88033+17.85458j])

aa=np.append([a],[b],axis=0)
aa=np.append(aa,[c],axis=0)
t=np.linspace(0,1,500)
ti=1-t

def bezz(curve):
    cur=np.empty(0)
    for a in curve:
        x=a[1]-a[0]
        y=a[2]-a[1]
        z=a[3]-a[2]
        d=x*t
        e=y*t
        f=z*t
        g=(((e+x)-d)*t)+d
        h=(((f+y+x)-(e+x))*t)+(e+x)
        i=((h-g)*t)+g+a[0]
        
        cur=np.append(cur,i)
    return cur
love=bezz(aa*np.exp((0+1j)*np.pi))
loveb=np.conj(love*np.exp((0+1j)*np.pi))
loveb=loveb-(np.real(loveb[0])*2)


love=np.append(loveb,np.flip(love))

love=love-(np.sum(love)/love.shape[0])



t=np.linspace(0,1,500)
ti=1-t

def bezz(curve):
    cur=np.empty(0)
    for a in curve:
        x=a[1]-a[0]
        y=a[2]-a[1]
        z=a[3]-a[2]
        d=x*t
        e=y*t
        f=z*t
        g=(((e+x)-d)*t)+d
        h=(((f+y+x)-(e+x))*t)+(e+x)
        i=((h-g)*t)+g+a[0]
        
        cur=np.append(cur,i)
    return cur


A=np.array([[1.43068+18.327j,1.43068+18.327j,2.9645799999999998+12.316600000000001j,4.78022+11.064440000000001j],
      [4.78022+11.064440000000001j, 6.59587+9.812270000000002j, 7.50369+17.23135j, 7.50369+17.544400000000003j],
      [7.50369+17.544400000000003j,7.50369+17.857440000000004j, 8.1631+13.462390000000003j, 7.50369+13.631380000000004j],
      [7.50369+13.631380000000004j, 6.84427+13.800370000000004j,1.4619799999999996+14.946150000000003j, 1.4619799999999996+14.946150000000003j]])
A=bezz(A)
A=np.conj(A)

C=np.array([[11.9489+10.1566j, 11.9489+10.1566j, 8.411529999999999+12.88006j, 8.72457+15.290479999999999j],
    [8.72457+15.290479999999999j, 9.03761+17.700899999999997j, 11.72977+16.667859999999997j, 12.888020000000001+16.511339999999997j]])
C=bezz(C)
C=np.conj(C)


P=np.array([[14.0816+17.1185j, 14.0816+17.1185j, 14.17551+9.82463j, 16.80506+9.07333j],
     [16.80506+9.07333j, 19.43461+8.32203j, 19.84157+10.54463j, 18.74592+11.358540000000001j],
     [18.74592+11.358540000000001j, 17.650270000000003+12.172450000000001j, 13.98769+13.174180000000002j, 13.98769+13.174180000000002j]])
P=bezz(P)
P=np.conj(P)

A=np.append(A,C)
A=np.append(A,P)
A=A-(np.sum(A)/A.shape[0])





s=A
NN=A.shape[0]
x=np.linspace(0,1,NN)
P=1
i=0+1j
pi=np.pi

sss=np.zeros(9000)
C=np.empty(0)
for n in np.arange(-500,500):
    cn=np.sum((1/P)*(s*(np.exp(-i*2*pi*n*x/P)))*(P/NN))
    C=np.append(C,cn)
#    ss=cn*np.exp(i*2*pi*n*(np.linspace(-0.8,0.8,9000))/P)
#    sss=sss+ss
#print (C)
#plt.plot(np.real(sss),np.imag(sss))




def axis():
    ax=np.array([[-9,0,0],[9,0,0]])
    glBegin(GL_LINES)
    glVertex3fv(ax[0])
    glVertex3fv(ax[1])
    glEnd()

    

def line(location):
    glBegin(GL_LINES)
    for loc in location:
        glVertex2fv(loc)
    glEnd()
    
def lineb(location):
    glBegin(GL_LINES)
    for loc in range(location.shape[0]-1):
        glVertex2fv(location[loc])
        glVertex2fv(location[loc+1])
        glColor3fv((0,1,0))
    glEnd()
    
def circle(center, radius):
    glBegin(GL_LINES)
    q=(np.linspace(0,2*np.pi,24))
    x=(radius*np.sin(q))+center[0]
    y=(radius*np.cos(q))+center[1]
    for n in range(23):
        glVertex2fv([x[n],y[n]])
        glVertex2fv([x[n+1],y[n+1]])
        glColor3fv((0,1,1))
#    glVertex3fv(ax[0])
#    glVertex3fv(ax[1])
    glEnd();    


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -30)
    
    
    k=0
#    theta=np.pi/50
    n=np.arange(-500,500)
    while True:

        k=k+1
        theta=(k)/500
        posa=0
        
#        for n in np.arange(-40,40):
#            posc=C[n+40]*np.exp(i*2*pi*n*(theta)/P)
#            posa=posa+posc
#
        posc=C*np.exp(i*2*pi*n*(theta)/P)
        posca=C*np.exp(i*2*pi*n*(theta)/P)
        for q in range(posc.shape[0]):
            posca[q]=np.sum(posc[:q])
            if q==0:
                posca[q]=0+0j

        posca=(np.array([np.real(posca),np.imag(posca)]).T)

        posa=np.sum(posc)

#        print(posd.shape)

            
        posa=posa
        posb=np.array([[0,0],[np.real(posa),np.imag(posa)]])
        



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
#        axis()
#        circle([0,0],0.99)
#        circle([0.,0.99],0.4)
#        line(np.array([[0,0],[0.9,0.5],[0,0.7],[0.4,0.9]]))
        
        
#        lineb(posb)
        for poscb in (np.arange(-6,6)):
            circle(posca[poscb+500],np.abs(posc[poscb+500]))
        
        lineb(posca)
        
        if k==1:
            posd=np.array([np.real(posa),np.imag(posa)])
        if k==2:
            ad=np.array([np.real(posa),np.imag(posa)])
            posd=np.append([posd],[ad],axis=0)
        if k >2:
            ad=np.array([np.real(posa),np.imag(posa)])
            posd=np.append(posd,[ad],axis=0)
            lineb(posd)
        if k>500:
            posd=posd[-499:]
        
        pygame.display.flip()
        pygame.time.wait(10)


main()