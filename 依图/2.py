def shape(A):
    return len(A),len(A[0])

def Mut(A,B):
    A_row, A_col = shape(A)
    B_row, B_col = shape(B)
    if(A_col != B_row):
        raise ValueError
    result = []
    BT = [list(row) for row in zip(*B)] 
    for A_index in range(A_row):
        rowItem = []
        for B_index in range(len(BT)):  
            num = 0     
            for Br in range(len(BT[B_index])):  
                num +=  A[A_index][Br] * BT[B_index][Br]
            rowItem.append(num)  
        result.append(rowItem)  
    return result


def T(A)->list:

    l=[[] for _ in range(len(A[0]))]
    for i,l0 in enumerate(A):
        for j,d in enumerate(l0):
            l[j].append(d)
    return l

def Pe(A):
    for l in A:
        print(" ".join([str(v) for v in l]))

# n,m=[int(v) for v in input().split()]
s=input()
# print(s)
n,m=s.split()
n,m=int(n),int(m)
A=[]
for i in range(n):
    A.append([int(v) for v in input().split()])
B=[]
for i in range(n):
    B.append([int(v) for v in input().split()])
C=T(Mut(Mut(T(A),B),T(B)))
nc,mc=shape(C)
print("%s %s"%(nc,mc))
for i in range(nc):
    for j in range(mc):
        C[i][j]=C[i][j]%1009
Pe(C)

# python3 2.py < input2.txt