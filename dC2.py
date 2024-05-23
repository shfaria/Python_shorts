# binary search

list0 = []

def binar(length, arr, find):
    mid = (length-1)//2
    if arr[mid] ==find:
        list0.append('mid')
        
        return mid
    elif arr[mid]>find:
        list0.append('left')
        
        arr = arr[0:(mid)]
       
        
    else:
        list0.append('right')
        
        arr = arr[(mid)+1:]
        
        


    return binar(mid, arr, find)
        


alist = [2,4,6,7,34,233,677,877,988,1899,2000,3000,4000]
# alist = [2,4,6,7,34,233,677,877,988,1899,2000,3000]

le = (len(alist))
# for i in alist:
    
#     dbo = binar(le, alist, i)
#     print(dbo)
dbo = binar(le, alist, 2)
print(dbo)
print(le)
print(list0)
