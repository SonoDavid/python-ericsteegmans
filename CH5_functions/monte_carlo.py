def calc_p(ran):
    """ 
    Calculate the value of pi using a random generator.
    The random generator generate two values between
    -1 and 1 and calculates if they are inside of a
    circle with radius 1 inscribed in the square.
    The result is returned as an approx. of pi.
    """
    import random
    from math import sqrt

    p = None; hits = 0; misses = 0

    for i in range(ran):
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1
        r = sqrt(x**2 + y**2)
        if r <= 1:
            hits += 1
    
    p = 4 * hits / ran

    return p