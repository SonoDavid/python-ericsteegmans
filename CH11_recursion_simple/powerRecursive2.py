def calc_power(x, n):
    ''' Write a function to calculate the 
    power of n.
    - Use
    '''
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif (n%2 == 0):
        halve_power = calc_power(x, n/2)
        return halve_power * halve_power
    else:
        return x * calc_power(x, n-1)
    
assert calc_power(2, 3) == 8
assert calc_power(10, 2) == 100
assert calc_power(-7, 2) == 49
assert calc_power(4, 3) == 4*4*4
assert calc_power(4, 4) == 4*4*4*4