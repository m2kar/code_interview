def fun(n,x):
    # a=[0,1,2,3,4,5,6,7,8,9,'!','@','@','D','E','F']
    a='0123456789`!@#$%^&*(){}\<>?'
    b=[]
    while True:
        s=n//x
        y=n%x
        b=b+[y]
        if s==0:
            break
        n=s
    b.reverse()
    return "".join([a[i] for i in b])

print(fun(int(input()),27))
# fun(26,16)
