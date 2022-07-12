#write a code to reverse a string
Str = "abdallah nagy"
reversedStr = []
for i in range(len(Str)-1, -1, -1):
    reversedStr.append(Str[i])

print(''.join(reversedStr))