# functions and variables act similarly in python
# if you delete a function name, after assigning it to a new function name
# the value still exists in memory

# decorators super-charge function (similar to some paradigms in React)
# Higher Order Functions - function that accepts a function, or, returns a function (map, reduce, filter)
from time import time


def greet(func):
    func()


def hi():
    print("HIIII")

# greet(hi)

# OR


def greet2():
    def func():
        print("working under the hood")
        return 0
    print("HIIII AGAIN")
    return func


greet(greet2())

# Decorator - function that wraps another function and changes it


def hello():
    print('helloooooo')

# Decorator pattern - using *args and **kwargs, we can accept multiple args


def my_decorator(func):
    def wrap_function(*args, **kwargs):
        print('*****')
        func(*args, **kwargs)
        print('*****')
    return wrap_function


@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)


@my_decorator
def bye():
    print('See Ya Laterz!')


hello('hiii')
bye()

# practical apps: @classmethod, @staticmethod -> we've seen before

# create @performance, to time functions


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(1000):
        i*5


long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


def authenticated(fn):
    def wrap(*args, **kwargs):
        if args[0]['valid'] == True:
            # user1['valid] was my solution. Only problem is that it defeats purpose of decorator formula
            fn(*args, **kwargs)
        else:
            print('You are not a valid user!')
    return wrap


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
print(user1['valid'])
