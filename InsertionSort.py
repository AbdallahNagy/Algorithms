
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        
        # J or i-1 (index) 
        arr[j+1] = key

arr = [10, 50, 40, 20, 30]
insertion_sort(arr)
print(arr)
