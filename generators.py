import sys

def test_generator(num):
    for i in range(num):
        yield num
        num -=1


test = test_generator(10)
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# or
res = 100
# for i in test:
#     res +=i
# print(res)

# print(sum(test))

sorted_test = sorted(test)
# print(sorted_test)


def dummy_generator(n):
    num, nums = 0, []
    while num < n:
        # nums.append(num)
        yield num
        num+=1
    # return nums


sum_of = sum(dummy_generator(1000))
print(sum_of)
print(sys.getsizeof(dummy_generator(1000)), 'bytes')

def fibonacci_generator(limit):
    a, b = 0, 1
    while a < limit:
        # nums.append(num)
        yield a
        a, b = b, a+b

sum_of = list(fibonacci_generator(1000))
print(sum_of)
print(sys.getsizeof(fibonacci_generator(1000)), 'bytes')


cus_generator = (i for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(cus_generator), "bytes", cus_generator)

# list comprehension
cus_list = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(cus_list), "bytes", cus_list==list(cus_generator))