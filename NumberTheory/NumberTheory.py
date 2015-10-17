####################################################################################
def __getdigits__(n):
    div=n
    digits=[]
    while div!=0:
        digit=div%10
        div=div/10
        digits.append(digit)
    return digits

def __getdivisors__(n):
    divisors=[]
    for i in range(1,n/2+1):
        if n%i==0:
            divisors.append(i)
    divisors.append(n)
    return divisors
####################################################################################
def IsArmstrong(n, base=10):
    
    if type(n)!=type(1):
        raise ValueError("Argument should be an integer.")
    elif base!=10:
        raise NotImplementedError("Only base 10 implemented.")
    else:
        # correct input type. continue check
        digits=__getdigits__(n)
        if n==sum(map(lambda x: int(x)**len(digits), digits)):
            return True
        else:
            return False
###########################
# aliases
IsNarcissistic=IsArmstrong
############################
####################################################################################
def IsZeroFree(n):
    '''A number is Zero-free or 0-free if its digits do not have a zero.'''
    if not (0 in __getdigits__(n)):
        return True
    else:
        return False
####################################################################################

def DivisorSigma(k,n):
    divisors=__getdivisors__(n)
    return sum(map(lambda x: x**k, divisors))

def ProperDivisors(n):
    return __getdivisors__(n)[:-1]

def RestrictedDivisor(n):
    return sum(ProperDivisors(n))

def IsAbundant(n):
    if DivisorSigma(1,n)>2*n:
        return True
    else:
        return False


def Deficiency(n):
    return 2*n - sum(__getdivisors__(n))

def Abundance(n):
    return sum(__getdivisors__(n)) - 2*n

def IsDeficient(n):
    if Abundance(n)<0:
        return True
    else:
        return False

def IsPerfect(n):
    if Abundance(n)==0:
        return True
    else:
        return False

def IsAbundant(n):
    if Abundance(n)>0:
        return True
    else:
        return False

def IsAlmostPerfect(n):
    if Abundance(n)==-1:
        return True
    else:
        return False

def IsQuasiPerfect(n):
    if Abundance(n)==1:
        return True
    else:
        return False



def IsPrimitiveAbundant(n):
    ProperDivisorsDeficient=map(lambda x: IsDeficeint(x), ProperDivisors(n))
    AllProperDivisorsDeficient= not (False in ProperDivisorsDeficient)
    if IsAbundant(n) and AllProperDivisorsDeficient:
        return True
    else:
        return False

if __name__=="__main__":
    for i in range(32):
        if IsDeficient(i):
            print i
