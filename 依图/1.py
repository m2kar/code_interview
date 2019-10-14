import queue
def s(n,m,a,b,c)->list:
    d=[[0 for _ in range(m) ] for _ in range(n)]
    q=queue.Queue()
    q.put((a,b,c), )
    while not q.empty():
        a,b,c=q.get()
        if not (0<=a<n and 0<=b<m):
            continue
        if c==0:
            continue
        elif d[a][b]!=0:
            continue
        else:
            d[a][b]=c
            q.put((a-1,b,c-1))
            q.put((a+1,b,c-1))
            q.put((a,b-1,c-1))
            q.put((a,b+1,c-1))
    return d

T=int(input())

for i in range(T):
    n,m,a,b,c=[int(v) for v in input().split()]
    print("Case #%d:" % (i+1) )
    d=s(n,m,a,b,c)
    for l in d:
        print(" ".join([str(v) for v in l]))
    

