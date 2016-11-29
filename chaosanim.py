import numpy as np
import pylab as plt
from math import *
import time
import random

def midpt(x1, y1, x2, y2):
    return( (x1+x2)/2., (y1+y2)/2. )

x = np.array([.5])
y = np.array([.5])

line1x = np.array([0,1])
line1y = np.array([.5,.5])

line2x = np.array([.5,.5])
line2y = np.array([0,1])

midx = .5
midy = .5

ptAx = 0
ptAy = 0

ptCx = 0
ptCy = 1

ptGx = 1
ptGy = 0

ptTx = 1
ptTy = 1


data = open("seqs.txt", "r").read()
lines = [data[i:i+16] for i in range(0, len(data), 1)]

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def A(midx, midy):
    midx, midy = midpt(midx, midy, 0, 0)
    return( midx, midy )

def C(midx, midy):
    midx, midy = midpt(midx, midy, 0, 1)
    return( midx, midy )

def G(midx, midy):
    midx, midy = midpt(midx, midy, 1, 0)
    return( midx, midy )

def T(midx, midy):
    midx, midy = midpt(midx, midy, 1, 1)
    return( midx, midy )

def R(midx, midy):
    choice = random.choice('AG')
    if choice == 'A':
        midx, midy = A(midx, midy)
    else:
        midx, midy = G(midx, midy)

    return( midx, midy )

def Y(midx, midy):
    choice = random.choice('CT')
    if choice == 'C':
        midx, midy = C(midx, midy)
    else:
        midx, midy = T(midx, midy)

    return( midx, midy )

def K(midx, midy):
    choice = random.choice('GT')
    if choice == 'G':
        midx, midy = G(midx, midy)
    else:
        midx, midy = T(midx, midy)

    return( midx, midy )


def M(midx, midy):
    choice = random.choice('AC')
    if choice == 'A':
        midx, midy = A(midx, midy)
    else:
        midx, midy = C(midx, midy)

    return( midx, midy )

def S(midx, midy):
    choice = random.choice('CG')
    if choice == 'C':
        midx, midy = C(midx, midy)
    else:
        midx, midy = G(midx, midy)

    return( midx, midy )

def W(midx, midy):
    choice = random.choice('AT')
    if choice == 'A':
        midx, midy = A(midx, midy)
    else:
        midx, midy = T(midx, midy)

    return( midx, midy )

def B(midx, midy):
    choice = random.choice('CGT')
    if choice == 'C':
        midx, midy = C(midx, midy)
    elif choice == 'G':
        midx, midy = G(midx, midy)
    else:
        midx, midy = T(midx, midy)

    return( midx, midy )

def D(midx, midy):
    choice = random.choice('AGT')
    if choice == 'A':
        midx, midy = A(midx, midy)
    elif choice == 'G':
        midx, midy = G(midx, midy)
    else:
        midx, midy = T(midx, midy)

    return( midx, midy )

def H(midx, midy):
    choice = random.choice('ACT')
    if choice == 'A':
        midx, midy = A(midx, midy)
    elif choice == 'C':
        midx, midy = C(midx, midy)
    else:
        midx, midy = T(midx, midy)

    return( midx, midy )


def V(midx, midy):
    choice = random.choice('ACG')
    if choice == 'A':
        midx, midy = A(midx, midy)
    elif choice == 'C':
        midx, midy = C(midx, midy)
    else:
        midx, midy = G(midx, midy)

    return( midx, midy )

plt.ion()
fig = plt.figure()
ax = plt.subplot(111)
ax.set_xlim([0,1])
ax.set_ylim([0,1])
for SEQUENCE in lines:
    midx = .5
    midy = .5
    for amino in SEQUENCE:
        if amino == 'A':
            midx, midy = A(midx, midy)
        if amino == 'C':
            midx, midy = C(midx, midy)
        if amino == 'G':
            midx, midy = G(midx, midy)
        if amino == 'T':
            midx, midy = T(midx, midy)
        if amino == 'R':
            midx, midy = R(midx, midy)
        if amino == 'Y':
            midx, midy = Y(midx, midy)
        if amino == 'K':
            midx, midy = K(midx, midy)
        if amino == 'M':
            midx, midy = M(midx, midy)
        if amino == 'S':
            midx, midy = S(midx, midy)
        if amino == 'W':
            midx, midy = W(midx, midy)
        if amino == 'B':
            midx, midy = B(midx, midy)
        if amino == 'D':
            midx, midy = D(midx, midy)
        if amino == 'H':
            midx, midy = H(midx, midy)
        if amino == 'V':
            midx, midy = V(midx, midy)


    ax.scatter(midx, midy)
    fig.canvas.draw()
    #x = np.append(x, midx)
    #y = np.append(y, midy)


#plt.plot(x,y, 'g.', line1x, line1y, 'b-', line2x, line2y, 'b-')
#plt.show()
