import sympy as sym

def sigmoid(x):
    s = 1 / (1 + sym.exp(-x))
    return s

x, z, a, b = sym.symbols('x z a b')
f = (4 * a * x**2 + a) + 3 + sigmoid(z) + (sigmoid(b))**2

der_x = sym.diff(f, x)
der_z = sym.diff(f, z)
der_a = sym.diff(f, a)
der_b = sym.diff(f, b)

print("Derivative of x: " + str(der_x))
print("Derivative of z: " + str(der_z))
print("Derivative of a: " + str(der_a))
print("Derivative of b: " + str(der_b))

'''
*OUTPUT*
Derivative of x: 8*a*x
Derivative of z: exp(-z)/(1 + exp(-z))**2
Derivative of a: 4*x**2 + 1
Derivative of b: 2*exp(-b)/(1 + exp(-b))**3
'''




