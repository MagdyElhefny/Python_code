# Function in python '


def n_range ():
    for i in range(15) :
        print(i)

n_range()


# function Use  ass a peramiter

def twise (x,y):
    return x(x(y))
def mul (y) :
    return  y*5

func=twise(mul , 5)
print(func)


# function inside function

def func_one (x):
    def func_two (y):


        return y*2
    return 2 *func_two(x)

f=func_one(5)
print(f)


# gloobal and local

x=1
def add (x):
    x=x+1
    return x

n1=add(5)
print(n1)  # it will print local x => 6
print(x) # it will print global x => 1


# Example in function



def factorial (n) :
    if n==1 :
        return 1
    else :
        return (n*factorial(n-1))

f1=factorial(5)
print(f1)


#function to calculate permutation useing factorial

def permutation (n,r):
   return factorial(n)/factorial(n-r)

p1=permutation(5,3)
print(p1)

# function to  calculate combination useing factorial

def combination (n,r) :
    return factorial(n) / (factorial(r) * factorial(n-r) )

c1=combination(5,3)
print(c1)






