from logging import exception


def input_checker(func):
    def helper(x):
        if type(x) == int and x  > 0:
            return func(x)
        else:
            raise Exception('value must be an integer greater than 0')
    return helper

@input_checker
def factorial(n):
    if n == 1:
        return 1
    else: 
        return n* factorial(n-1)

print(factorial(3))