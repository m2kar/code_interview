import itertools
cache={}
def gcd(a,b):
    b,a=max(a,b),min(a,b)
    if (a,b) in cache:
        return cache[(a,b)]
    a, b = (a, b) if a >=b else (b, a)
    if a%b == 0:  
        v=b
        cache[(a,b)]=v
        return v 
    else :  
        v=gcd(b,a%b)
        cache[(a,b)]=v
        return v

def sol(N):
    s=0
    if N==2:
        return 2
    for i in range(1,N+1):
        s+=i
    for a,b in itertools.combinations(list(range(2,N+1)), 2):
        if not gcd(a,b)==1:
            s+=a*b
    t1=gcd(s,N)
    return "%d/%d" % (s//t1,N//t1)

T=int(input())
for _ in range(T):
    N=int(input())
    print(sol(N))
