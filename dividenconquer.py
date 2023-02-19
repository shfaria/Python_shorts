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
alist = []
def binar(length, arr, find):
    if arr[length-1] ==find:
        alist.append({(length-1):arr[length-1]})
        return length-1
    elif arr[length//2]>find:
        alist.append({(length//2):arr[length//2]})
        arr = arr[0:(length//2)]
        print(arr)
    elif arr[length//2]<find:
        alist.append({(length//2):arr[length//2]})
        arr = arr[(length//2):-1]
        print(arr)

    return binar(length//2, arr, find)
        

dbo = binar(7, [2,4,6,7,34,233,654], 34)
print(dbo)
print(alist)