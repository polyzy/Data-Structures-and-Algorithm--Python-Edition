#--coding: utf8 --
def mergeSort(seq):
    if len(seq)<=1:
        return seq
    mid = int(len(seq)/2)
    lo = mergeSort(seq[:mid])
    hi = mergeSort(seq[mid:])
    return merge(lo,hi)

def merge(lo,hi):
    result = []
    i,j = 0,0
    while i<len(lo) and j<len(hi):
        if lo[i] <= hi[j]:
            result.append(lo[i])
            i += 1
        else:
            result.append(hi[j])
            j += 1
    result += lo[i:]  #如果有没有剩下的没有归并的，直接复制到后面
    result += hi[j:]
    return result

