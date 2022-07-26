#bubble sort
def bubblesort(arr, n):

    for i in range(n):
        swap = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                #swap 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True

        #check if arr is sorted
        if swap == False:
            return arr
    
# Driver Code.
arr = [4, 6, 9, 1, 5, 3, 2, 7, 10, 8]
n = len(arr)

print(bubblesort(arr, n))
