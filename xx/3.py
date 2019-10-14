def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n*factorial(n-1))

n,k,m=input().split()
n=int(n)
k=int(k)
m=int(m)
s1=input()
s2=input()
# c=0
# for c1,c2 in zip(s1,s2):
#     if c1!=c2:
#         c+=1
if k<m:
    print(0)
elif k==m:
    print(factorial(m))
elif (k-m)%2==1:
    print(0)
elif (k-m)%2==0:

    print(factorial(m)*2)
