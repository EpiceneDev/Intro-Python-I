import time

def prime_number(n):
    '''if number is prime, return true, otherwise false'''
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


''' TEST '''
for n in range(1, 50):
    print(n, prime_number(n))

''' TIME '''
t0 = time.time()
for n in range(1, 10000):
    prime_number(n)
t1 = time.time()
print("Completed in: ", t1 - t0)
