import functools

def my_decorators(func):
    @functools.wraps(func)
    def My_function():
        print("HI")
        func()
    return My_function

@my_decorators
def new_function():
    print("world")

#new_function()



#decorators with argu
def decorator_with_number(number):
    def first_decorators(func):
        @functools.wraps(func)
        def second_decorator(*args,**kwargs):
            print("HI")
            if number == 58:
                print("this works")
            else:
                func(*args,**kwargs)
            print("end")
        return second_decorator
    return first_decorators


@decorator_with_number(57)
def my_function_new(x, y):
    print(x+y)

my_function_new(57,66)
