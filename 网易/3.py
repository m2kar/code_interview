class Q():
    def __init__(self,k,h):
        self.k=k
        self.h=h
        self.d={}
        for i,v in enumerate(self.h):
            self.d[i]=[]
            for j in range(max(i-k,0),min(i+k+1,len(h))):
                if i==j:
                    continue
                if self.h[j]<=v:
                    self.d[i].append(j)
            self.d[i]=self.d[i][::-1]

    def solve(self):
        self.state={}
        for i,_ in enumerate(self.h):
            self.state[i]=False
        return self.jmp(0,True)
    
    def jmp(self,dst,superpower):
        if self.state[dst]==True:
            return False
        self.state[dst]=True

        if dst==n-1:
            return True
        for dst2 in self.d[dst]:
            if self.jmp(dst2,superpower):
                return True
        if superpower:
            for j in range(min(dst+self.k+1,len(h))-1,max(dst-self.k,0)-1,-1):
                if self.jmp(j,False):
                    return True
        self.state[dst]=False
        return False


T=int(input())
for _ in range(T):
    s=input()
    n,k=s.split()
    n,k=int(n),int(k)
    h=[int(v) for v in input().split()]
    qu=Q(k,h)
    if qu.solve():
        print("YES")
    else:
        print("NO")
