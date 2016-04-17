# -*- coding: utf-8 -*-

from math import factorial
from typing import Optional, Iterator


def is_prime(n: int) -> bool:

    """
    Miller-Rabin primality test.
    This code was adapted from https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
    :param n: integer
    :return: True if n is probably a prime number, False if it is not
    """

    if not isinstance(n, int):
        raise TypeError("Expecting an integer")

    if n < 2:
        return False
    if n in __known_primes:
        return True
    if any((n % p) == 0 for p in __known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1

    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    return not any(try_composite(a) for a in __known_primes[:16])

__known_primes = [2, 3]
__known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]


def find_divisors(n: int) -> Iterator[int]:

    """
    Find all the positive divisors of the given integer n.
    :param n: strictly positive integer
    :return: a generator of positive divisors of n
    """

    if not isinstance(n, int):
        raise TypeError("Expecting a strictly positive integer")
    if n <= 0:
        raise ValueError("Expecting a strictly positive integer")

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors = {i, n//i}
            for divisor in divisors:
                yield divisor


def prime_generator(p_min: int=2, p_max: Optional[int]=None) -> Iterator[int]:

    """
    Generator of prime numbers using the sieve of Eratosthenes.
    :param p_min: prime numbers lower than p_min will not be in the resulting primes
    :param p_max: the generator will stop when this value is reached, it means that there
                  will be no prime bigger than this number in the resulting primes. If p_max
                  is None, there will not be any upper limit
    :return: a generator of consecutive primes between p_min and p_max
    """

    if not isinstance(p_min, int):
        raise TypeError("Expecting an integer")
    if p_max is not None and not isinstance(p_max, int):
        raise TypeError("Expecting an integer")

    q = max(p_min, 3)
    if p_min <= 2 and (p_max is None or p_max >= 2):
        yield 2  # outside the while block to make the double increment optimization work
    while p_max is None or q <= p_max:
        if is_prime(q):
            yield q
        q += 2  # avoid losing time in checking primality of even numbers


def sieve_of_eratosthenes(p_min: int=2, p_max: Optional[int]=None) -> Iterator:

    """
    Generator of prime numbers using the sieve of Eratosthenes.
    Adapted from http://code.activestate.com/recipes/117119/
    :param p_min: prime numbers lower than p_min will not be in the resulting primes
    :param p_max: the generator will stop when this value is reached, it means that there
                  will be no prime bigger than this number in the resulting primes. If p_max
                  is None, there will not be any upper limit
    :return: a generator of consecutive primes between p_min and p_max
    """

    if not isinstance(p_min, int):
        raise TypeError("Expecting an integer")
    if p_max is not None and not isinstance(p_max, int):
        raise TypeError("Expecting an integer")

    sieve = {}
    q = 2

    while p_max is None or q <= p_max:
        if q not in sieve:
            if q >= p_min:
                yield q
            sieve[q * q] = [q]
        else:
            for p in sieve[q]:
                sieve.setdefault(p + q, []).append(p)
            del sieve[q]

        q += 1


def binomial_coefficient(n: int, k: int) -> int:

    """
    Calculate the binomial coefficient indexed by n and k
    :param n: positive integer
    :param k: positive integer
    :return: the binomial coefficient indexed by n and k
    """

    if not isinstance(k, int) or not isinstance(n, int):
        raise TypeError("Expecting positive integers")
    if k > n:
        raise ValueError("k must be lower or equal than n")
    if k < 0 or n < 0:
        raise ValueError("Expecting positive integers")

    return factorial(n) // (factorial(k) * factorial(n - k))
