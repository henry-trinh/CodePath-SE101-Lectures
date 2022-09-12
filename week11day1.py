#RECURSIVE 1
def modulo(a, b):
    '''
    Given two positive integers a and b, return the integer
    remainder of a divided by b.
    '''
    if b > a:
        return a
    return modulo(a - b, b)

#RECURSIVE 2
def reverse(mystring):
    '''
    Given a string mystring, return a new string with the
    characters of mystring in the reverse order.
    '''
    if not mystring:
        return ''
    return reverse(mystring[1:]) + mystring[0]

#RECURSIVE 3
def multiply(a, b):
    '''
    Given positive integers a and b, return the product of
    a and b.
    '''
    if b == 1:
        return a
    return a + multiply(a, b - 1)
