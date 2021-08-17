class IntegerSequence:
    def __init__(self):
        self.seq={}
        self.seed={
                    "Fibonacci":[0,1],
                    "Ulam":[1,2]
                    }
<<<<<<< HEAD

    def ThueMorse(self):
        seq='0'
        c={'0':'1', '1':'0'}
        while True:
            seq=seq+''.join( map(lambda x: c[x], list(seq)) )
            yield seq

        

=======
>>>>>>> c1d92db1143a39b3d1aa1189fa5cf5b90ff53329
    def Recaman(self):
        count=0
        self.seq['Recaman']=[]
        s=self.seq['Recaman']
        if count==0:
            ans=0
        while True:
            if count>0:
                ans1=s[-1]
                ans=ans1-count
                if ans>0 and (ans not in s):
                    pass
                else:
                    ans=ans1+count
            if ans not in s:
                s.append(ans)
            count=len(s)
            yield ans


    def Fibonacci(self):
        """
        In mathematics, the Fibonacci numbers are the numbers in the following 
        integer sequence: 0, 1, 1, 2, 3, 5, 8, 13, ......
        By definition, the first two Fibonacci numbers are 0 and 1, and each 
        subsequent number is the sum of the previous two.
        In mathematical terms, the sequence Fn of Fibonacci numbers is defined 
        by the recurrence relation
        F(n) = F(n-1) + F(n-2)
        with seed values F(0)=0 and F(1)=1
        
        --Wikipedia
        """    
        e1=0
        e2=1
        yield e1
        yield e2
        while True:
            e3=e1+e2
            yield e3
            e1=e2
            e2=e3

    def Ulam12(self):
        """
        An Ulam number is a member of an integer 
        sequence devised by and named after 
        Stanislaw Ulam, who introduced it in 1964.
        The standard Ulam sequence (the (1, 2)-Ulam 
        sequence) starts with U1 = 1 and U2 = 2. 
        Then for n > 2, U_n is defined to be the 
        smallest integer that is the sum of two 
        distinct earlier terms in exactly one way.
        
        --Wikipedia
        """
        self.seq['Ulam']=self.seed['Ulam']
        yield self.seq['Ulam'][0]
        yield self.seq['Ulam'][1]
        
        s=self.seq['Ulam']
        while True:
            sums=[]
            for i in range(len(s)-1):
                for j in range(i+1,len(s)):
                    sums.append(s[i]+s[j])
            sums.sort()
            while sums.count(sums[0])>1 or (sums[0] in s):
                ndups=sums.count(sums[0])
                sums=sums[ndups:]
            s.append(sums[0])
            yield s[-1]
                
    def Integer(self, start=0):
        """
        The sequence of non-negative integers in base 10.
        """
        count=start
        while True:
            yield count
            count=count+1

    def Baum_Sweet(self):
        """
        In mathematics the Baum-Sweet sequence is an infinite
        automatic sequence of 0s and 1s defined by the rule:
            bn = 1  if the binary representation of n contains 
                    no block of consecutive 0s of odd length;
            bn = 0  otherwise;
        for n >= 0.
        
        --Wikipedia
        """
        count=0
        while True:
            if count==0:
                yield 1
            elif 1 in map(lambda x: len(x)%2, bin(count)[2:].split('1') ):
                yield 0
            else:
                 yield 1
            count=count+1

    def Happy(self):
        """
        A happy number is defined by the following process: 
          Starting with any positive integer, replace the number by the sum of 
        the squares of its digits, and repeat the process until the number 
        equals 1 (where it will stay), or it loops endlessly in a cycle which 
        does not include 1. Those numbers for which this process ends in 1 are 
        happy numbers, while those that do not end in 1 are unhappy numbers 
        (or sad numbers).
        
        --Wikipedia
        """
        count=2
        self.seq["Happy"]=[1]
        s=self.seq["Happy"]
        yield s[-1]
        while True:
            num=count
            while num>s[-1]:
                num=sum(map(lambda x: int(x)**2, list(str(num))))
                if num in [4, 16, 37, 58, 89, 145, 42, 20] or \
                    (num<=s[-1] and num not in s ):
                    break
                elif num==1 or num in s:
                    s.append(count)
                    yield s[-1]
            count=count+1
    def Catalan(self):
        """
        The nth Catalan number is given directly in terms of binomial coefficients by
            $$C_n = \frac{1}{n+1}{2n \choose n} = \frac{(2n)!}{(n+1)! n!} 
            = \prod\limits_{k=2}^{n}\frac{n+k}{k} \qquad\mbox{ for }n\ge 0. $$
            
        --Wikipedia
        """
        count=0
        while True:
            ans=1
            for k in range(count+2, 2*count+1):
                ans=ans*k
            for k in range(2,count+1):
                ans=ans/k
            yield ans
            count=count+1
    def Composite(self):
        """
        A composite number is a positive integer that has at least one positive
        divisor other than one or itself. In other words a composite number is 
        any positive integer greater than one that is not a prime number.
        
        --Wikipedia
        """
        count=0
        ans=4
        while True:
            compositeq=False
            for i in range(2,ans):
                if ans%i==0:
                    compositeq=True
                    break
            if compositeq:
                yield ans
            count=count+1
            ans=ans+1

    def Abundant(self):
<<<<<<< HEAD
        '''
        In number theory, an abundant number or excessive number is a number 
        for which the sum of its proper divisors is greater than the number 
        itself.
        '''
        count=0
        ans=3
        def properdivisors(n):
            ans1=[]
            for i in range(2,n):
                if n%i == 0:
                    ans1.append(i)
            return ans1
        while True:
            if sum ( properdivisors(ans) )>ans:
                yield ans
            ans=ans+1
            count=count+1
    def Triangle(self):
        '''
        Numbers obtained by creating triangles of larger size.
        n T(n)
        - --- 
        1   1        *
        2   3       * *
        3   6      * * *
        4  10     * * * *
        5  15    * * * * *
        6  21   * * * * * *
        7  28  * * * * * * * 
        '''

        n = 1
        while True:
            yield n*(n+1)/2
            n=n+1
=======
    	'''
	In number theory, an abundant number or excessive number is a number 
	for which the sum of its proper divisors is greater than the number 
	itself.
	'''
        count=0
	ans=3
	def properdivisors(n):
	    ans1=[]
	    for i in range(2,n):
	        if n%i == 0:
		    ans1.append(i)
	    return ans1
	while True:
	    if sum ( properdivisors(ans) )>ans:
	        yield ans
	    ans=ans+1
	    count=count+1

>>>>>>> c1d92db1143a39b3d1aa1189fa5cf5b90ff53329
                
if __name__=='__main__':
    seq=IntegerSequence()
    a=[]
    a.append(seq.Integer(0))
    a.append(seq.Recaman())
    a.append(seq.Fibonacci())
    a.append(seq.Ulam12())
    a.append(seq.Baum_Sweet())
    a.append(seq.Happy())
    #a.append(seq.Catalan())
    a.append(seq.Composite())
    a.append(seq.Abundant())
<<<<<<< HEAD
    a.append(seq.Triangle())
=======
>>>>>>> c1d92db1143a39b3d1aa1189fa5cf5b90ff53329

    fs="|"+"%15d |"*len(a)

    fs_title="|"+"%15s |"*len(a)
    title=map(lambda x: x.__name__, a)
    title=(fs_title)%tuple(title)
    print '-'*len(title)
    print title
    print '-'*len(title)

    for i in range(25):
        print (fs)%tuple(map(lambda x:x.next(), a))
    print '-'*len(title)
    
