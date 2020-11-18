"""
Author: Joseph Bidinger

This module performs numerical integration of a lambda function using the
trapezoidal method of approximation.
"""

# Example function x^x
xX = lambda x: x**x

"""
Note: function does not need to be defined outside of trapIntegrate; the lambda
expression can be written in the input parameters.
Example: trapIntegrate(lambda x: x*2.0,0,5,1)   integrates f(x) = 2x from 0 to 5
"""

def trapIntegrate(f,a,b,n=1):
    """ f is the function to integrate (passed in the form of a lambda expression)
        a and b are the limits of integration
        n is the number of subintervals for the approximation
        """
    ans = 0
    n *= 1.0
    c = (b-a)/n
    fA_2 = f(a)/2.0
    fB_2 = f(b)/2.0
    k = 1
    while k < (n-1):
            ans += f(a+k*c)
            k += 1
    ans += fA_2
    ans += fB_2
    ans *= c
    return ans
