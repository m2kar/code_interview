def fun(m,h):

    for i,v in enumerate(h):
        m+=(v-i)
        if m<0:
            return False
    return True

T=int(input())
for _ in range(T):
    s=input()
    n,m=s.split()
    n,m=int(n),int(m)
    h=[int(v) for v in input().split()]
    if fun(m,h):
        print("YES")
    else:
        print("NO")
