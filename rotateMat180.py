#code to rotate a matrix 180 degrees
#Time complexity: O(N*N) 
#Space complexity: O(1)

def rotateMat(mat, n):
    
    for i in range(n-1, -1, -1):

        for j in range(n-1, -1, -1):
            print(mat[i][j], end=' ')
        
        print()

#Driver code.
n = 3
mat = [
    [1, 5, 4],
    [9, 2, 0],
    [3, 6, 7]]

rotateMat(mat, n)