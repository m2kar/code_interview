def fun(a0,M)->list:
    m=len(M)
    L=[l for l,r in M]
    R=[r for l,r in M]
    L.sort()
    R.sort()
    # a=a0.copy()
    a=[a0[0]]
    for aa in a0:
        while aa!=a[-1]:
            a.append(aa)
    a.sort()
    li,ri=0,0
    da={}
    h=0
    for aa in a:
        while li<m and L[li]<=aa:
            li+=1
            h+=1
        while ri<m and R[ri]<aa:
            ri+=1
            h-=1
        da[aa]=h
        while ri<m and R[ri]==aa:
            ri+=1
            h-=1
    
    return [da[aa] for aa in a0]

T=int(input())
for caseid in range(T):
    s=input()
    n,m=s.split()
    n,m=int(n),int(m)

    a=[int(v) for v in input().split()]
    M=[]
    for i in range(m):
        s=input()
        l,r=s.split()
        l,r=int(l),int(r)
        # l,r=input().split()
        # print(l,b)
        M.append((int(l),int(r)),)
    print("Case #%d:" % (caseid+1) )
    for v in fun(a,M):
        print(v)

