import time

def prime_number(n):
    '''if number is prime, return true, otherwise false'''
    for divisor in range(2, n):
        if n % 2 == 0:
            return False
    return True


''' TEST '''
for n in range(1, 50):
    print(n, prime_number(n))
