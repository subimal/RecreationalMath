def Eratosthenes(n):
    '''
    Generates primes upto `n` using the Eratosthenes sieve.
    '''
    
    # Begin with the assumption that all integers are primes
    ans = (1<<(n+1))-1 
    # The binary representation of ans contains all ones. The idea is that if the i-th bit of ans is 1, then i is a prime number.
    # Now, unset the bits for 0 and 1 (they are not primes).
    ans = ans - (1<<0) - (1<<1)
    
    # We will follow the Eratosthenes sieve algorithm. So we will include the removal of even numbers in the loop. 
    # It could be done while initializing `ans` and I know that will be better, but I want to stick to the algorithm - step for step.
    
    for i in range(2, n+1):
        isprime = ((ans & (1<<i))>0) # is the i-th bit marked prime?
        if isprime:
            yield i
            for j in range(2*i, n+1, i):
                if ((ans & (1<<j))>0):  # if the j-th bit is marked prime (j = 2*i, 3*i, 4*i, ... )
                    ans = (ans - (1<<j)) # unset the j-th bit



def EratosthenesExtended1(n):

    def primebit(seq: int) -> int:
        for i in range(seq.bit_length()):
            if (seq & (1<<i)):
                yield i

    ans = (1<<2) | (1<<3) # 2 and 3 are the first primes

    # probable candidates are of the form 6*k+1 or 6*k-1
    for k in range(1, n//6+1):
        ans = ans | (1<<(6*k-1)) | (1<<(6*k+1))
        
    # remove any excess bits created.
    ans = ans - ((ans>>n)<<n) 
    print(("Prime candidates: %30d")%(len(list(primebit(ans)))), end = "\r")
    # remove any composites
    for i in primebit(ans):
        for j in primebit(ans):
            if (i*j>n):
                break
            if (ans & (1<<(i*j))):
                ans = ans - (1<<(i*j))
                print(("Removing %10d ")%(i*j), end="\r")
    print()
    for i in primebit(ans):
        yield i
        


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


# not working
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
    
    a = [i for i in EratosthenesExtended1(100)]
    print( len(a) )
