def repeated_elements(arr, n):
    repeatedElements = []
    for i in range(n):

        for j in range(i+1, n):
            if arr[i] == arr[j] and arr[i] not in repeatedElements:
                repeatedElements.append(arr[i])
    
    return repeatedElements

#Driver Code.
arr = [3, 5, 4, 3, 5, 3, 9, 4]
n = len(arr)
print(repeated_elements(arr, n))