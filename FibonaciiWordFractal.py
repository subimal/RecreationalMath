import numpy as np

def FibonacciWord(n):
    assert n>=0, 'n should be non-negative.'
    
    if n==0:
        return '0'
    if n==1:
        return '01'

    if n>1:
        return FibonacciWord(n-1)+FibonacciWord(n-2)

def FibonacciWordFractal(n):
    word = FibonacciWord(n)
    forward=np.array([1,0])
    pos = np.array([0,0])

    right=np.matrix([[0,-1],[1,0]])
    left=np.matrix([[0,1],[-1,0]])

    path=[pos]
    for k in range(len(word)):
        path.append( path[-1]+forward)
        if word[k]=='0':
            if (k+1)%2==0:
                forward = np.array((left*np.matrix(forward).transpose()).transpose())[0]
            else:
                forward = np.array((right*np.matrix(forward).transpose()).transpose())[0]

    X=[]
    Y=[]
    for (x,y) in path:
        X.append(x)
        Y.append(y)
    return (X,Y)

if __name__=='__main__':
    import pylab as pl

    i=int(input("Enter i: "))
    w = FibonacciWord(i) 
    f = FibonacciWordFractal(i) 
    print(w)
    print(f)
    print('-'*10)

    fig=pl.figure()
    ax = fig.add_subplot(111)
    ax.plot(f[0], f[1], '-')
    ax.set_aspect(aspect=1)
    pl.axis('off')
    pl.show()
