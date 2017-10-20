from eulerChallenge003 import is_prime


def nth_prime(n: object) -> object:

    number_of_primes = 0
    number = 2
    while True:
        if is_prime(number):
            number_of_primes += 1
            if number_of_primes == n:
                break
        number += 1

    return number


x = nth_prime(10001)
print('solution:', x, x == 104743)
