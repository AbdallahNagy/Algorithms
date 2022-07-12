
def selection(arr):
    for idx in range(len(arr)):
        min_idx = idx
        for j in range(idx+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]

arr = [10, 50, 40, 20, 30]
selection(arr)
print(arr)