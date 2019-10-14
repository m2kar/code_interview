mask="MASK"
def func(o):
    p=o.find("@")
    p=p-1
    i=0
    r=""
    while i<p:
        r+=o[i]
        r+=mask[i%4]
        i=i+1
    r+=o[p:]
    return r

o=input()
r=func(o)
print(r)