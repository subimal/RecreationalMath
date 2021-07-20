import IntegerSequences as ISeq
import numpy as np
import pylab as pl

#tmp='''
seq=ISeq.IntegerSequence().ThueMorse()

for i in range(6):
    s=seq.next()
    s=seq.next()
    n=np.array( map(lambda x: int(x), list(s)) )
    pl.figure(1)
    pl.subplot(121)
    ar=n.reshape((np.sqrt(len(n)), np.sqrt(len(n))))
    pl.imshow(ar, interpolation="none")
    pl.subplot(122)
    pl.imshow(np.abs(np.fft.fftshift(np.fft.fft2(ar)))**.0625, cmap='hot')
    pl.show()
#'''

tmp='''

def SierpinskiCarpet(i):
    A=np.array([[0]])
    B=np.array([[1]])
    for i in range(i):

        A=np.concatenate((np.concatenate((A,A,A), axis=0),
          np.concatenate((A,B,A), axis=0),
          np.concatenate((A,A,A), axis=0)), axis=1)

        B=A*0+1
    pl.figure(1)
    pl.subplot(121)
    pl.imshow(A, interpolation='none')
    pl.subplot(122)
    pl.imshow(np.abs(np.fft.fftshift(np.fft.fft2(A)))**.0625, cmap='hot')
    pl.show()
    

#'''
SierpinskiCarpet(5)