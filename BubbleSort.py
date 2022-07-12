#bubble sort

def bubblesort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp

arr = [30, 20, 40, 50, 60, 10]
bubblesort(arr)
print(arr)