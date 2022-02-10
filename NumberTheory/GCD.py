def Euclid(l):
    '''
    Returns the greatest common divisor (GCD) of the list of numbers in the list l.
    
    Uses Euclid's algorithm.
    '''
    # check if all elements in l are ints
    try:
        assert list(set(map(type, l)))==[type(1)]
    except AssertionError:
        print('All elements are not integers.')

    if len(l)==2:
        while l[1]!=0:
            l[0], l[1] = l[1], (l[0]%l[1])
        return l[0]
    else:
        return Euclid( l[:-2]+[Euclid(l[-2:])] )


def Binary(l):
    '''
    Returns the greatest common divisor (GCD) of the list of numbers in the list l.
    
    Uses binary GCD algorithm (also known as Stein's algorithm or the binary Euclidean algorithm).
    '''
    if len(l)==2:
        # do this
        if l==[0,0]:
            return 0

        # gcd(0,v)=v
        if l[0]==0 and l[1]!=0:
            return l[1]
        
        # gcd(u,0)=u
        if l[0]!=0 and l[1]==0:
            return l[0]

        if l[0]%2==0 and l[1]%2==0:
            return 2*Binary([l[0]//2, l[1]//2])

        if l[0]%2==0 and l[1]%2!=0:
            return Binary([l[0]//2, l[1]])

        if l[0]%2!=0 and l[1]%2==0:
            return Binary([l[0], l[1]//2])

        if l[0]%2!=0 and l[1]%2!=0:
            return Binary([ abs(l[0]-l[1]), min(l)])


    else:
        return Binary(l[:-2]+[Binary(l[-2:])])

Stein = Binary
BinaryEuclid = Binary


if __name__=='__main__':
    l=[54,24, 18]
    print (l, Euclid(l), Binary(l))
