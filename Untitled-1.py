arr = ["333","1","22","4444","55555","fgeg","d","aaa","aa","dsdds"]
index = 0 # schetchik indexa
arr2 = [] # Pustoy massiv 
while index < len(arr):
    b = arr[index]
    if  len(b) > 2:
        arr2.append(b)
    index += 1 # dvizhenie na 1 element po massivu
print(arr2)
