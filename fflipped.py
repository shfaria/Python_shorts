matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]

# def flipped(matrix):
n = len(matrix)
nh = n//2
sum = newsum= 0
alist=[]
for b in range(nh):
    for c in range(nh):
        sum += matrix[b][c]
print(sum)

rangefor = list(range(n))
rangerev = list(range(n-1, -1, -1))
print(rangefor, rangerev)
# rangefor = list(range(n//2))
# rangerev = list(range((n//2)-1, -1, -1))
# print(rangefor, rangerev)

for i in rangefor:
    for j in rangerev:
        matrix[i]