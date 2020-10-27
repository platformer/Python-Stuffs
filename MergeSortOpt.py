def mergesort(arr):
    mergesortimp(arr, [], 0, len(arr))

def mergesortimp(arr, copy, beg, end):
    size = end - beg
    if size <= 1:
        return
    e1 = s2 = beg + size//2
    mergesortimp(arr, copy, beg, e1)
    mergesortimp(arr, copy, s2, end)
    merge(arr, copy, beg, e1, s2, end)

def merge(arr, copy, s1, e1, s2, e2):
    size1 = e1-s1
    size2 = e2-s2
    i = s1;
    j = s2;
    copy = []
    while (len(copy) < size1 + size2):
        if (i >= e1):
            for x in range (j,e2):
                copy.append(arr[x])
            break
        if (j >= e2):
            for x in range (i, e1):
                copy.append(arr[x])
            break
        if (arr[i] < arr[j]):
            copy.append(arr[i])
            i+=1
        else:
            copy.append(arr[j])
            j+=1
    for x in range (s1,e2):
        arr[x] = copy[x - s1]

if __name__ == "__main__":
    import random as rand

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
    print(arr)
    mergesort(arr)
    print(arr)