def sort(arr):
    arrLen = len(arr)
    for _ in range(arrLen):
        for i in range(arrLen):
            if i < arrLen-1:
                if arr[i] > arr[i+1]:
                    a = arr[i]
                    b = arr[i+1]
                    arr[i] = b
                    arr[i+1] = a
    return arr