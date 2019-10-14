"""
题目描述：
现在有n个长度为m的字符串，编号为从1到n，每个字符串由m个大写字母组成。现在你可以完成以下操作，请你任选第 i 个字符串和第 j 个字符串，并交换长度为 k 的前缀。你可以在变换后的基础上进行任意次这样的操作。

例如：ABCD 和 EFGH，令k=2则变为 EFCD 和 ABGH。

此时对于新的字符串 EFCD 和 ABGH 令k=1则变为 AFCD 和 EBGH。

显然变化后的字符串是不同的。

现在请问你可以生成多少个不同的字符串。包含原串本身。

输入
输入第一行包含两个正整数n，m，(1<=n,m<=100)表示n个长度为m的字符串。

接下来n行，每行有一个长度为m的字符串，仅包含大写字母。

输出
输出仅包含一个正整数，表示不同的字符串数量，由于数量可能很大，所以请输出答案对1000000007取模的结果。


样例输入
2 3
ABC
DEF
样例输出
8
"""
from functools import reduce
n,m=input().split()
n,m=int(n),int(m)
M=[set() for _ in range(m)]
for i in range(n):
    for j,v in enumerate(input()):
        M[j].add(v)

# S=reduce(lambda x,y:x*y,[len(v) for v in M ])
S=1
for v in M:
    S*=len(v)

print(S%1000000007)


# Exception has occurred: ValueError
# need more than 1 value to unpack
#   File "/root/exam/Baidu/1.py", line 30, in <module>
#     n,m=input().split()