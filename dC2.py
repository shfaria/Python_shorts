# binary search



def binar(length, arr, find):
    
    if arr[length-1] ==find:
        
        return length-1
    elif arr[length//2]>find:
        
        arr = arr[0:(length//2)]
        print(arr)
    else:
        
        arr = arr[(length//2):-1]
        print(arr)


    return binar(length//2, arr, find)
        


alist = [2,4,6,7,34,233,654]
for i in alist:
    print(i)
    dbo = binar(7, alist, i)
    print(dbo)
