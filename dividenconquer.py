# def sumo(arr):
#     if arr == []:
#         return 0
#     demo = arr[-1]
#     arr.remove(demo)
#     return demo + sumo(arr)

# print(sumo([2,100]))


# binary search
# def binary(arr, find):
#     length = len(arr)
# global alist
# alist = []
# global counter
# # counter = 0
# def binar(length, arr, find):
#     print(1)
#     # counter +=1
#     if arr[length-1] ==find:
        
#         return length-1
#     elif arr[length//2]>find:
        
#         arr = arr[0:(length//2)]
#         print(arr)
#     else:
        
#         arr = arr[(length//2):-1]
#         print(arr)
#     # else:
#     #     print("no")

#     return binar(length//2, arr, find)
        

# dbo = binar(7, [2,4,6,7,34,233,654], 34)
# print(dbo)
# # print(alist)



# actual
def binar(l,r, arr, find):
    mid = (l+r) // 2
    print(mid)
    if arr[mid] == find:
        return mid
    elif arr[mid]>find:    
        return binar(l, mid-1, arr, find)
    else:
        return binar( mid+1,r, arr, find)
        
alist = [2,4,6,7,34,233,654]
length = len(alist)
dbo = binar(0, length-1, alist, 654)
print(dbo)