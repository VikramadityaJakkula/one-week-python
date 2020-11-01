def linearsearch(A,Key):
    i = 0
    flag = False
    while ((i<len(A)) and (flag != True)):
        if A[i] == Key:
            return True
        else:
            i = i + 1
    return False

A = [12,34,6,7,8]
Key =10
Found = linearsearch(A,Key)
print("The element", Key,"is:",Found )
