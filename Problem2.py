

print("By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.")

fib_i = 1
fib_j = 2

#do not consider fib_i init of 1 to be in the sum
sum = 0;

while fib_i <= 4000000:
    if fib_j%2 == 0:
        sum += fib_j
    fib_i, fib_j = fib_j, fib_j+fib_i

print("ith term is " + str(fib_i) + "\njth term is " + str(fib_j))
print(sum)
