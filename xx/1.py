def pool(n,m,a,b):
    A=[[(i%10*j%10) for j in range(1,m+1)] for i in range(1,n+1)]
    # B=[]
    s=0

    for i in range(n-2):
        # B.append([])
        for j in range(m-2):
            v=max([A[ii][jj] for jj in range(j,j+b) for ii in range(i,i+a)])
            # B[-1].append()
            s+=v
    return s

l=input().split()
n,m,a,b=[int(v)for v in l]
print(pool(n,m,a,b))