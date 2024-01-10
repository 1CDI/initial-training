import math
def f(x):
    return math.exp(x)

def g(x):
    return math.log(x)

def dfdx_approx(x):
    dh = 0.0001
    return (f(x + dh) - f(x)) / dh

print("exp")

for i in range(-3, 4): 
    result_exp = dfdx_approx(i)
    print (f'x = {i}:   {result_exp}')

print("log")

a = 0.25
for i in range(6):
    result_log = dfdx_approx(a)
    print(f'x = {a}:  {result_log}')
    a += a
