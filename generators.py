def test_generator(num):
    for i in range(num):
        num -=1
        yield num
        print(num)

test = test_generator(10)
print(next(test))
print(next(test))
print(next(test))
print(next(test))
# op = next(test)
# print(op)