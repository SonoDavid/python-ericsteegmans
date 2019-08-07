def factorial(n):

    """ 
    Return te factorial of the given integer number.
    - The resulting value is equal to the factorial of the
      given integer number, i.e. n*(n-1)*(n-2)*...*2*1
    """

    fac = 1
    counter = 1

    # INVARIANT
    #   fac is equal to the factorial of counter
    # VARIANT: n-couter
    #
    while counter != n:
        counter += 1
        fac = fac * counter

    return fac

assert factorial(5) == 5*4*3*2*1