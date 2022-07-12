#write code to find the repeated elements in an array
#there is also another solution by using nested loops

def repeatedElementsDict(arr):
    repeated = dict()
    for ele in arr:
        if ele not in repeated.keys():
            repeated[ele] = 1
        else:
            repeated[ele] += 1
        
    repeatedList = list()
    for k, v in repeated.items():
        if v > 1:
            repeatedList.append(k)
    
    return repeatedList

arr = [2, 4, 5, 4, 2]
print(repeatedElementsDict(arr))
