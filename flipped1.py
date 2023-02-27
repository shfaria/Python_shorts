matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
# [112, 42, 83, 119, 56, 125, 56, 49, 15, 78, 101, 43, 62, 98, 114, 108]
n = len(matrix)
alist= []
for i in matrix:
    for x in range(n):
        alist.append(i[x])
    i=alist.reverse()

# print(matrix)

def summ(matrix, n):
    n = n//2
    summ= 0
    for i in range(n):
        for j in range(n):
            summ += matrix[i][j]
    return summ
alist= []

for i in range(n-1, -1, -1):
    for j in range(n//2):
        print(matrix[j][i])
        alist.append(matrix[j][i])
    print(alist)
    alist=[]
