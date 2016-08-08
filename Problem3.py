import math


def solution(primes, n):
    for prime in primes:
        while n % prime == 0:
            print(str(n) + "/" + str(prime) + "=" + str(n / prime))
            n = n / prime
            largestFactor = prime


def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True


def main():
    n = 600851475143
    largestFactor = 2
    primes = filter(is_prime, range(1, math.ceil(math.sqrt(n))))
    solution(primes, n)
    print(largestFactor)

if __name__ == "__main__":
    main()
