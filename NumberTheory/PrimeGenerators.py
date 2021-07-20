def TrialDivision():
    '''
    Generates prime numbers by the brute force technique of trial division.

    Steps

    1. 2 is a prime.
    2. 3 is the next prime
    3. Take the next odd number N.
    4. Check divisibility of N by odd integers from 3 to N/2.
    5. 
    '''
    ans = 2
    yield ans
    ans = 3
    yield ans
    while True:
        ans = ans+2
        PrimeQ = True
        for i in range(3,int(ans/2.0), 2):
            if ans%i == 0:
                PrimeQ = False
                break
        if PrimeQ:
            yield ans



def SieveOfSundaram(n):
    ans = list(range(1,n+1))
    j = range(1, int((n-1)/3.0) )
    for ji in j:
        i = range(1,ji+1)
        for ii in i:
            rt = ii+ji+2*ii*ji
            if (rt <= n) and (rt in ans):
                del ans[ ans.index(rt) ]
            else:
                break

    ans_new = [2]
    for i in ans:
        j = 2*i+1
        if j<=n:
            ans_new.append(j)
        else:
            break
    return ans_new


if __name__ == '__main__':
    p=[]
    p_i = TrialDivision()
    while len(p)<25:
        p.append(next(p_i))
    print(p)
    print('-'*10)
    print(SieveOfSundaram(100))

