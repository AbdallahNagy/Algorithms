
# fibonacci function using Dynamic Programming
# Taking 1st two fibonacci numbers as 0 and 1
FibArray = [0, 1]
 
def fibonacci(n):
   
    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")
         
    # Check is n is less
    # than len(FibArray)
    elif n < len(FibArray):
        return FibArray[n]
    else:       
        FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
        return FibArray[n]
 
# Driver Program
print(fibonacci(8))
