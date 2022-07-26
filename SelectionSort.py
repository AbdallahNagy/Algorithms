
def selection(arr, n):

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        # temp = arr[i]
        # arr[i] = arr[min_idx]
        # arr[min_idx] = temp

    return arr

# Driver Code.
arr = [4, 6, 9, 1, 5, 10, 3]
n = len(arr)

print(selection(arr, n))
