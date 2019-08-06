def factorial(n):

    """
    Return the factorial of a given positive number n.
    The factorial of n is defined as the product
    1*2*...*(n-1)*n
    """

    if (n==0):
        return 1
    elif (n==1):
        return 1
    else:
        return n*factorial(n-1)
    
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(4) == 1*2*3*4