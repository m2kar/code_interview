import bisect
l=[int(_) for _ in input().split()]
n=l[0]
m=l[1]
l=l[2:]
# l=[-x for x in l]
l.sort()
for i in range(m):
    v=l.pop(0)+l.pop(0)
    bisect.insort(l,v)
print(l[0])
