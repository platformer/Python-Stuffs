def mergesort(arr):
    size = len(arr)
    if size <= 1:
        return arr
    l1 = [x for x in arr[0:size//2]]
    l2 = [x for x in arr[size//2:size]]
    return merge(mergesort(l1), mergesort(l2))

def merge(l1, l2):
    size1 = len(l1)
    size2 = len(l2)
    merged = []
    i = 0;
    j = 0;
    while (len(merged) < size1 + size2):
        if (i >= size1):
            merged += l2[j:size2]
            break
        if (j >= size2):
            merged += l1[i:size1]
            break
        if (l1[i] < l2[j]):
            merged.append(l1[i])
            i+=1
        else:
            merged.append(l2[j])
            j+=1
    return merged

if __name__ == "__main__":
    arr = [5,4,3,2,1]
    print(mergesort(arr))
    arr = [8,3,5,6,1,2,10]
    print(mergesort(arr))
    print(mergesort([]))