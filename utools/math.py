# -*- coding: utf-8 -*-

""" Useful mathematical functions.
"""

from math import factorial


def is_prime(n):

    """ Miller-Rabin primality test. Keep in mind that this is not a deterministic algorithm: if it return True,
    it means that n is probably a prime.

    Args:
        n (int): the integer to check

    Returns:
         True if n is probably a prime number, False if it is not

    Raises:
        TypeError: if n is not an integer

    Note:
        Adapted from https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python

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


def find_divisors(n):

    """ Find all the positive divisors of the given integer n.

    Args:
        n (int): strictly positive integer

    Returns:
        A generator of all the positive divisors of n

    Raises:
        TypeError: if n is not an integer
        ValueError: if n is negative

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


def prime_generator(p_min=2, p_max=None):

    """ Generator of prime numbers using the sieve of Eratosthenes.

    Args:
        p_min (int): prime numbers lower than p_min will not be in the resulting primes
        p_max (int): the generator will stop when this value is reached, it means that there
            will be no prime bigger than this number in the resulting primes. If p_max
            is None, there will not be any upper limit

    Returns:
        A generator of all the consecutive primes between p_min and p_max

    Raises:
        TypeError: if p_min or p_max is not an integer

    """

    if not isinstance(p_min, int):
        raise TypeError("Expecting an integer")
    if p_max is not None and not isinstance(p_max, int):
        raise TypeError("Expecting an integer")

    q = max(p_min, 3)
    if q % 2 == 0:
        q += 1
    if p_min <= 2 and (p_max is None or p_max >= 2):
        yield 2  # outside the while block to make the double increment optimization work

    while p_max is None or q <= p_max:
        if is_prime(q):
            yield q
        q += 2  # avoid losing time in checking primality of even numbers


def sieve_of_eratosthenes(p_min=2, p_max=None):

    """ Generator of prime numbers using the sieve of Eratosthenes.

    Note:
        Adapted from http://code.activestate.com/recipes/117119/

    Args:
        p_min (int): prime numbers lower than p_min will not be in the resulting primes
        p_max (int): the generator will stop when this value is reached, it means that there
            will be no prime bigger than this number in the resulting primes. If p_max
            is None, there will not be any upper limit

    Returns:
        A generator of all the consecutive primes between p_min and p_max

    Raises:
        TypeError: if p_min or p_max is not an integer

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


def binomial_coefficient(n, k):

    """ Calculate the binomial coefficient indexed by n and k.

    Args:
        n (int): positive integer
        k (int): positive integer

    Returns:
        The binomial coefficient indexed by n and k

    Raises:
        TypeError: If either n or k is not an integer
        ValueError: If either n or k is negative, or if k is strictly greater than n

    """

    if not isinstance(k, int) or not isinstance(n, int):
        raise TypeError("Expecting positive integers")
    if k > n:
        raise ValueError("k must be lower or equal than n")
    if k < 0 or n < 0:
        raise ValueError("Expecting positive integers")

    return factorial(n) // (factorial(k) * factorial(n - k))
