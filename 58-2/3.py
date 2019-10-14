def way(n):
    if n<=2:
        return n
    a=1
    b=2
    i=3
    while i<=n:
        a,b=b,a+b
    return b 
    

m=int(input())

print(way(m))