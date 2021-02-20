"""
https://github.com/pravinmane-123/code.git
"""
""" 

def info(firstname='pravin',age=30):
    print ('firstname',firstname)
    print ('age',age)
info ('mane',10)


def res(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * res(n-1)
print(res(5))



list = ["pravin","kashinath","mane",(1,2),10,[100,200]]
for i in list:
    x = list.index(i)
    print(i,'index value of element is:',x)
    



# Python Program for n-th Fibonacci number
def fabinoci(n):
    if n < 0:
        print(n, 'is a wrong input')
    elif n == 1:
        return 0
    elif n== 2 :
        return 1
    else:
        x = fabinoci(n-1)+fabinoci(n-2)
        return x
print(fabinoci(5))
 

x = 'madam'
x1 = x[::-1]
if x == x1 :
    print("this is palindrome")
else:
    print("this is not palindrome")


def pal(x):
    return x == x[::-1]
x = 'madam'
ans =pal(x)
if x == x:
    print("done")
else:
    print("not done")
    

import os.path
if os.path.isfile ("C:\\Users\HP\PycharmProjects\oop\k.py"):
    print("file exist")
else:
    print("file not exist")


# membership operator
list = [1,2,3,4,5,6]
x = 10
if (x not in list):
    print("present")
else:
    print("not present")


# identity operator
x = 6.5
if (type  (x)  is not int ):
    print("yes")
else:
    print("no")

"""