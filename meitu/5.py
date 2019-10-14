# 输出连续序列
def cs(s):
    # write code here
    ll = []
    lo,hi = 1,2
    while lo<hi:
        ccs = (lo+hi)*(hi-lo+1)/2
        if ccs == s:
            l =[]
            for i in range(lo,hi+1):
                l.append(i)
            ll.append(l)
            lo += 1 
        elif ccs<s:
            hi+= 1
        else:
            lo += 1
    return ll
for l in cs(int(input())):
    print(" ".join([str(v) for v in l]))