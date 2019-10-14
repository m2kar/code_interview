import math
def m(a,b,c)->int:
    a,b,c=sorted([a,b,c])
    if c-a<=2*(b-a):
        return a+math.ceil((b-a+c-a)/3)
    else:
        return a+math.floor((c-a)/2)

T=int(input())
for _ in range(T):
    s=input()
    a,b,c=s.split()
    a,b,c=int(a),int(b),int(c)
    print(m(a,b,c))