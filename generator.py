#Generators - subset of iterable, generates values, doesn't store in memory, usually functions

#iterable - any data structure we can loop through, with __iter__ method

def generator_function(num):
    for i in range(num):
        yield i #pauses function til next() call

g = generator_function(100)
print(next(g)) #0
next(g)
next(g)
print(next(g)) #3

#So, when we use "for-range(num)" loops- the whole range isn't stored in memory
#instead, the generator generates a new value, when it's called

from time import time
def performance(fn):
    t1 = time()
    fn()
    t2 = time()
    print(f'took {t2 -t1} seconds')

@performance
def long_time():
    print('1')
    for i in range(1000000): #not in memory
        i*5

@performance
def long_time2():
    print('2')
    for i in list(range(1000000)): #held in list
        i*5

while True:
    try: 
        long_time() 
        long_time2()  # this is ~2x slower! b/c of holding in memory
    except: 
        break


##making our own range function
def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break

special_for([1,2,3])

## creating our own generator
class MyGen():
    current = 0 #manages state interactions
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration

gen = MyGen(0, 100)
for i in gen:
    print(i)

##Implement a fibonacci
## Just numbers
def Fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a #gives up a value to print at this point in the loop without modification
        temp = a 
        a = b #update a
        b = temp + b #update b with old a


for x in Fib(20):
    print(x)

#Modified to return a list

def Fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a) #send old a
        temp = a # we want to hold onto the old value of a, before modifying it
        a = b #update a
        b = temp + b #update b with old value of a
    return result

    # append, a, b, temp
    # 0, 1, 1, 0
    # 1, 1, 2, 1
    # 1, 2, 3, 1
    # 2, 3, 5 , 2
    # 3, , , 3


print(Fib2(100))
        
   #print([x for x in range(number)])

Fib(20)
