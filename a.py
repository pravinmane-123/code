"""
https://github.com/pravinmane-123/code.git
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


