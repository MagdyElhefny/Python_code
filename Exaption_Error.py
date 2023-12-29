#exaeption hendling


#Diffrance between Syntaxs Error and Exaption :


#----- > This is Syntax Error :
#amount = 1000
#if (amount  >1000 )
#print("You are eligible to purchase Dsa Self Paced")

#----- > This is ZeroDivition Error :
# amount = 1000 ;
# b = amount / 0
# print(b)


#----- > Type Error
# x= 10
# y="Hello"
# print(x+y)

#----- > try catch blook with brevious code
# x= 10
# y="Hello"
# try :
#     z=x+y
# except TypeError :
#     print("Can't Add int to string ")


#----- > IndexError
# a=[0,1,2,3,4]
#
# try :
#     print(f"Scound element = {a[1]}")
#     print(f"fifth element = {a[5]}")
# except IndexError :
#     print("This number not in index")

#----- > Catching Specific Exception

# def func(a):
#     if(a < 4) :
#         b=a / (a-3)
#         print(f"value of b is : {b}")
# try :
#     func(3)
#     func(5)
# except ZeroDivisionError :
#     print("ZeroDivisionError Occurred and Handled")
# except NameError :
#     print("NameError Occurred and Handled")
#
# func(2)

#----- > Try with else clause

# def AbyB(a , b):
#     try :
#         c =((a+b) / (a-b))
#
#     except ZeroDivisionError:
#         print("ZeroDivisionError Occurred and Handled")
#     else :
#         print(c)
# AbyB(5 , 4)
# AbyB(5,5)

#----- > Finally Keyword in Python

# try :
#     k =5//0
#     print(k)
# except ZeroDivisionError :
#     print("ZeroDivisionError Occurred and Handled")
# finally:
#     print('This is always executed')

#----- > Raising Exception

# try:
#  raise  ZeroDivisionError("Hi there")
# except ZeroDivisionError:
#  print ("An exception")
#  raise

# Example in Raising Exception

# y="Magdy"
# if type(y) != int :
#     raise ValueError("only integer number ")
#
# print("print message After if conditin ") # >>> it will not work .