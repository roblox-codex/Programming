def extended_gcd(a, b):
    """
    Returns the GCD of a and b, and coefficients x and y such that ax + by = gcd(a, b).
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

def multiplicative_inverse(a, m):
    """
    Returns the multiplicative inverse of a modulo m, if it exists.
    """
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None  # a does not have a multiplicative inverse modulo m
    else:
        return x % m
