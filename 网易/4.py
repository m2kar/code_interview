import time
import copy
def InversePairs( array):
    if not array:
        return 0
    arrCopy = copy.deepcopy(array)
    return InverseRecur(array, arrCopy, 0, len(array)-1)

def InverseRecur( array, arrCopy, start, end):
    if start == end:
        return 0
    mid = (start + end) // 2
    left = InverseRecur(array, arrCopy, start, mid)
    right = InverseRecur(array, arrCopy, mid+1, end)
    count = 0
    i = mid
    j = end
    locCopy = end
    while i>=start and j > mid:
        if array[i] > array[j]:
            count += j - mid
            arrCopy[locCopy] = array[i]
            locCopy -= 1
            i -= 1
        else:
            arrCopy[locCopy] = array[i]
            locCopy -= 1
            i -= 1

    while i >= start:
        arrCopy[locCopy] = array[i]
        locCopy -= 1
        i -= 1
    while j > mid:
        arrCopy[locCopy] = array[j]
        locCopy -= 1
        j -= 1
    s = start
    while s <= end:
        array[s] = arrCopy[s]
        s += 1
    return left + right + count


def sumr():

n=int(input())
a=[int(v) for v in input().split()]
