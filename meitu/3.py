# 一个台阶有N级，每次可以走1或2级，输出所有可能走法的数量

def step(n):
    if n in (0,1,2):
        return n
    p,q=1,2
    i=3
    while i<=n:
        p,q=q,p+q
        i=i+1
    return q
print(step(int(input())))
