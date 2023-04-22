import random
import time

# Linear search function
def linear_search(S, x):
    for i in range(len(S)):
        if S[i] == x:
            return True
    return False

# Binary search function
def binary_search(S, x):
    left = 0
    right = len(S) - 1
    while left <= right:
        mid = (left + right) // 2
        if S[mid] == x:
            return True
        elif S[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Fibonacci search function
def fibonacci_search(S, x):
    # Generating the Fibonacci series
    fib_m2 = 0
    fib_m1 = 1
    fib = fib_m1 + fib_m2
    while fib < len(S):
        fib_m2 = fib_m1
        fib_m1 = fib
        fib = fib_m1 + fib_m2

    # Performing the search
    offset = -1
    while fib > 1:
        i = min(offset + fib_m2, len(S) - 1)
        if S[i] < x:
            fib = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib - fib_m1
            offset = i
        elif S[i] > x:
            fib = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib - fib_m1
        else:
            return True
    if fib_m1 and offset < len(S) - 1 and S[offset + 1] == x:
        return True
    return False

# Generating the list S and integer x
S = random.sample(range(10000), 10)
x = random.randint(0, 9999)

# Executing the search algorithms for 5 times and calculating the mean execution time
linear_time = 0
binary_time = 0
fibonacci_time = 0
for i in range(5):
    start_time = time.time()
    linear_search(S, x)
    linear_time += time.time() - start_time

    start_time = time.time()
    binary_search(sorted(S), x)
    binary_time += time.time() - start_time

    start_time = time.time()
    fibonacci_search(sorted(S), x)
    fibonacci_time += time.time() - start_time

linear_time /= 5
binary_time /= 5
fibonacci_time /= 5
print("Linear search execution time:", linear_time)
print("Binary search execution time:", binary_time)
print("Fibonacci search execution time:", fibonacci_time)

# Executing the search algorithms for n = 10, 20, 30, ..., 1000 and recording their average execution times
results = []
for n in range(10, 1010, 10):
    S = random.sample(range(10000), n)
    x = random.randint(0, 9999)

    linear_time = 0
    binary_time = 0
    fibonacci_time = 0
    for i in range(100):
        start_time = time.time()
        linear_search(S, x)
        linear_time += time.time() - start_time

        start_time = time.time()
        binary_search(sorted(S), x)
        binary_time += time.time() - start_time

        start_time = time.time()
        fibonacci_search(sorted(S), x)
        fibonacci_time += time.time() - start_time
