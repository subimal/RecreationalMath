def Euclidean_algorithm(l):
    '''
    Returns the greatest common divisor (GCD) of the list of numbers in the list l.
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
        return Euclidean_algorithm( l[:-2]+[Euclidean_algorithm(l[-2:])] )


l=[54,24, 18]
print l, Euclidean_algorithm(l)
