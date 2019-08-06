def calc_power(x, n):
    ''' Write a function to calculate the 
    power of n.
    - Uses the property that x**n = x**n-1 * x
    and x**1 = x
    '''
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * calc_power(x, n-1)
    
assert calc_power(2, 3) == 8
assert calc_power(10, 2) == 100