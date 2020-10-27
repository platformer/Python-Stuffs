import random as rand

def quicksort(arr):
    quicksortimp(arr, 0, len(arr)-1)

def quicksortimp(arr, beg, end):
    if beg < end:
        pivot = arr[end]
        i = beg-1
        for j in range(beg, end):
            if arr[j] < pivot:
                i+=1
                arr[j], arr[i] = arr[i], arr[j]
        arr[i+1], arr[end] = arr[end], arr[i+1]
        quicksortimp(arr, beg, i)
        quicksortimp(arr, i+2, end)

if __name__ == "__main__":
    arr = [5,4,3,2,1]
    quicksort(arr)
    print(arr)
    arr = [8,3,5,6,1,7,2,10,4,9]
    quicksort(arr)
    print(arr)
    arr = []
    quicksort(arr)
    print(arr)
    arr = [1]
    quicksort(arr)
    print(arr)
    for x in range(100):
        arr.append(rand.randint(0, 100))
    quicksort(arr)
    print(arr)