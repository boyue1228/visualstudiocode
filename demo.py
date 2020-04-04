#!/usr/bin/env python

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

def main():
    mygenerator = createNewGenerator()
    for i in mygenerator:
        print(i)
    for k in newTest():
        print(k)
        

if __name__ == "__main__":
    main()
