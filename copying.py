import copy
# normal! copy

a = [10]
b = a
b[0] =90
print(a,b)

# shallow - level 1
a = [10, [1,2]]
b = copy.copy(a)
b[0] =90
b[1][1] = 80
print(a,b)

# deep
a = [10, [1,2, ["tom", "jerry", "harry"]]]
b = copy.deepcopy(a)
b[0] =90
b[1][1] = 80
b[1][2][2] = "warder"
print(a,b)