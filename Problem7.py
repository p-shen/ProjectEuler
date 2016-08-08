# copied from problem 3 where we have to generate primes
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
    primes = filter(is_prime, range(1, 1000000, 1))
    n = 1
    for prime in primes:
        print(n)
        if n == 10001:
            print("the 10001th prime is" + str(prime))
            return
        n += 1

# 104743
if __name__ == "__main__":
    main()
