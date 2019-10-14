import math
def qselect(arr,k):
    if len(arr)<k:return arr
    pivot = arr[-1]
    right = [pivot] + [x for x in arr[:-1] if x>=pivot]
    rlen = len(right)
    if rlen==k:
        return right
    if rlen>k:
        return qselect(right, k)
    else:
        left = [x for x in arr[:-1] if x<pivot]
        return qselect(left, k-rlen) + right
    
def fun(arr,r)->list:
    k=math.ceil(r/100*len(arr))
    # arr.sort(reverse=True)
    # ret=qselect(arr,k)
    arr.sort(reverse=True)
    ret=arr[:k]
    # ret.sort(reverse=True)
    # print(ret)
    if ret:
        last=ret[-1]
        ret.extend([v for v in arr if v == last ][1:])
    return ret

sl=[v for v in input().split(",")]
r=float(sl[0])
arr=[ int(v) for v in  sl[1:]]
print(",".join([str(v) for v in  fun(arr,r)]))