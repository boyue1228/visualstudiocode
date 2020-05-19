#!/usr/bin/env python3

import time
import wrapt

# version branch features/node add more words here
# Test of yield 
def createNewGenerator():
    mylist = range(10)
    for i in mylist:
        yield i**i


# test of lambda, map func in python
def newTest():
    temperature = [20.9, 30.9, 40.5, 60, 100, 120]
    mytransform = list(map(lambda x: (x+10.2)*(x+10.3), temperature))
    return mytransform 


#closure
def primaryFunc(n):
    def myInnerFunc(x):
        return x*n
    return myInnerFunc

# decorator 
def decorator(func):
    def wrapper(*args, **kwargs):
        results = func(*args,**kwargs)
        return results
    return wrapper

def with_arguments(arg1, arg2):
    @wrapt.decorator
    def logging(wrapped,instance, args,kwargs):
        print("[debug]: enter {}() {} {} ".format(wrapped.__name__, arg1, arg2))
        return wrapped(*args, **kwargs)
    return logging


@with_arguments(arg1=1,arg2="Niubility.com")
def hello(something,arg1,arg2):
    if arg1 != 1:
        print("hello, ",something)
    else:
        print("KO, ",something)

def main():
    hello("world",1,"Nein")

    '''
    a3 = primaryFunc(3)
    b5= primaryFunc(5)
    print(a3(10))
    print(b5(15))
    mygenerator = createNewGenerator()
    for i in mygenerator:
        print(i)
    for k in newTest():
        print(k)
    first, *rest = [1,2,3,4]
    first, *l, rest =[1,2,3,4,5,6,7]
    print(rest)
    print(l)
    '''

if __name__ == "__main__":
    main()
