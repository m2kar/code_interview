"""
题目描述：
A同学十分喜欢看连载漫画，由于漫画章节之间有很强的关联性，所以他只会选择一些连续的章节来看。由于情节跌宕起伏，并不是每一章漫画都会令他开心。
已知这本漫画共有N章，每一章漫画都有一个开心值A[i],A同学打算至少看M章连续的小说章节，他希望这些漫画带给他的平均开心值最大。
输入
输入文件的第一行有两个正整数N,M，含义同题面。(M<=N<=100000 ,|A[i]|<=10000)
下面一行N个整数，第i个整数，表示第i章漫画的开心值。
输出
一个实数，保留3位小数（四舍五入），表示最大的平均愉悦值。
样例输入
10 6
6 4 2 10 3 8 5 9 4 1
样例输出
6.500
"""

# -1 5 2 -9

N,M=input().split()
M=int(M)
N=int(N)
A=[int(v) for v in input().split()]
K=N-M
s=sum(A[:M])
ma=s
for x1,x2 in zip(A[:K],A[N-K:]):
    s+=x2-x1
    if s>ma:
        ma=s
print("%.3f" % round(ma/M,3))
