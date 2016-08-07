from functools import reduce

#calculate the GCD of two numbers using Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

#calculate the LCM of two numbers
def lcm(a, b):
    return abs(a*b)/gcd(a,b)

#calculate the LCM of 1 ... 20
def solution():
    #lcm((..lcm(lcm(1, 2), 3)..))
    return reduce(lcm, range(1,20,1))

print(str(solution()))
