import functools

def start_end_decorator(func):
    @functools.wraps(func)
    def test(*args, **kwargs):
        # print('Start some functions')
        result = func(*args, **kwargs)
        # print('End all')
        return result
    return test

def over_wrap(num):
    def start_end_decorator(func):
        @functools.wraps(func)
        def test(*args, **kwargs):
            result = 0
            for i in range(num):
                result += func(*args, **kwargs)
            return result
        return test
    return start_end_decorator

@start_end_decorator
def dummy(x : int) -> int:
    # print(f'dummy {x}')
    return x+1

@over_wrap(num=3)
def drummer(x : int) -> int:
    return x+1


res = dummy(55)
# print(res, dummy.__name__)

res = drummer(500)
# print(res, drummer.__name__)

# help(dummy)

def deco_1(func):
    @functools.wraps(func)
    def test(*args, **kwargs):
        # print('Start some functions')
        result = func(*args, **kwargs)
        # print('End all')
        return result
    return test

def deco_2(func):
    @functools.wraps(func)
    def test(*args, **kwargs):
        # print("oi")
        result = func(*args, **kwargs)
        # print("oy oy oy")
        return result
    return test


@deco_1
@deco_2
def bass(x : int) -> int:
    return x

ds = bass(x =0)
# print(ds)


class Deco:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"helo world {self.num_calls}")
        return self.func(*args, **kwargs)

@Deco
def pianist(num):
    print("ding dong!")

pianist(5)
pianist(5)


