"""
Author: Joseph Bidinger
4/26/2020

This module calculates a numerical approximation of a derivative at a certain value.
The function passed in will be in the form of a lambda expression, and the
calculation will be performed using the following definition of the derivative:

f'(x) = lim_{h->0}(f(x + h) - f(x))/h

"""
def differentiate(f, x, h=10**(-7)):
    """
    f is the function to differentiate (passed in the form of a lambda expression)
    x is the value at which the derivative will be evaluated
    h is the which x approaches in the limit

    """
    return (f(x + h) - f(x))/h
    
