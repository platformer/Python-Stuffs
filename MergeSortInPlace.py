def mergesort(arr):
    mergesortimp(arr, 0, len(arr))

def mergesortimp(arr, beg, end):
    size = end - beg
    if size <= 1:
        return
    e1 = s2 = beg + size//2
    mergesortimp(arr, beg, e1)
    mergesortimp(arr, s2, end)
    merge(arr, beg, e1, s2, end)

def merge(arr, s1, e1, s2, e2):
    i = s1;
    j = mid = s2;
    while (i < mid and j < e2):
        if arr[i] <= arr[j]:
            i+=1
        else:
            temp = arr[j]
            for x in range(j, i, -1):
                arr[x] = arr[x-1]
            arr[i] = temp
            i+=1
            mid+=1
            j+=1

if __name__ == "__main__":
    import random as rand
    from Vector import *

    def checksort(arr1, arr2):
        v1=vector(defval=0, isUnbounded=True)
        v2=vector(defval=0, isUnbounded=True)
        for x in arr1:
            v1[x] += 1
        for x in arr2:
            v2[x] += 1
        return v1==v2

    """
    arr = [5,4,3,2,1]
    mergesort(arr)
    print(arr)
    arr = [8,3,5,6,1,7,2,10,4,9]
    mergesort(arr)
    print(arr)
    arr = []
    mergesort(arr)
    print(arr)
    arr = []
    for x in range(100):
        arr.append(rand.randint(0, 100))
    testarr = arr.copy()
    print(arr)
    mergesort(arr)
    print(arr)
    print(checksort(arr, testarr))
    """

    d = {1:"one", 2:"two"}
    print(d)
    d[3]="three"
    print(d)
    d={}