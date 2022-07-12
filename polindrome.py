
def isPalindrome(arr, n):
    flag = 0
    
    i = 0
    while (i <= n//2 and n != 0):
        
        if arr[i] != arr[n - 1 - i ]:
            flag = 1
            break
        i += 1

    if flag == 1:
        print("Not Polindrome")
    else:
        print("Polindrome")

# Driver code.
arr = [ 1, 2, 3, 3, 1 ]
n = len(arr)

isPalindrome(arr, n)