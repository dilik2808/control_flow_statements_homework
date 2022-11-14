def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    x = a+b+c
    if a>0:
        return 1
    if a<0:
        return 0
    if b>0:
        return 1
    if b<0:
        return 0
    if c>0:
        return 1
    if c<0:
        return 0
    return x
print (main (8, 5, 7))