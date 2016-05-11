# -*- coding: utf-8 -*-

import pytest
import types
import utools.math as umath


# --- utools.math.is_prime ---

@pytest.mark.parametrize("n, expected_result", [
    (-1, False), (0, False), (1, False), (2, True), (3, True),
    (4, False), (5, True), (17, True), (102, False),
    (2**19 - 1, True), (2**127 - 1, True), (2**128 - 1, False),
    (179425063, True), (3215031751, False), (32416189919, True)
])
def test_is_prime(n, expected_result):
    assert umath.is_prime(n) is expected_result


@pytest.mark.parametrize("n, expected_exception", [
    (1.0, TypeError), (None, TypeError), ([1], TypeError), ("1", TypeError)
])
def test_is_prime_with_bad_parameters(n, expected_exception):
    with pytest.raises(expected_exception):
        umath.is_prime(n)


# --- utools.math.binomial_coefficient ---

@pytest.mark.parametrize("n, k, expected_result", [
    (0, 0, 1), (1, 0, 1), (1, 1, 1), (2, 1, 2), (3, 2, 3),
    (536, 12, 1036996651419873917836700)
])
def test_binomial_coefficient(n, k, expected_result):
    assert umath.binomial_coefficient(n, k) == expected_result


@pytest.mark.parametrize("n, k, expected_exception", [
    (1, -1, ValueError), (-1, 1, ValueError), (-1, -1, ValueError),
    (1, 3, ValueError), (1, "1", TypeError), (1.0, 1, TypeError),
    (1, [1], TypeError), ("1", None, TypeError)
])
def test_binomial_coefficient_with_bad_parameters(n, k, expected_exception):
    with pytest.raises(expected_exception):
        umath.binomial_coefficient(n, k)


# --- utools.math.find_divisors ---

@pytest.mark.parametrize("n, expected_result", [
    (1, {1}), (2, {1, 2}), (4, {1, 2, 4}), (12, {1, 2, 3, 4, 6, 12}),
    (1442, {1, 2, 7, 14, 103, 206, 721, 1442}), (2**19 - 1, {1, 2**19 - 1})
])
def test_find_divisors(n, expected_result):
    generator = umath.find_divisors(n)
    assert isinstance(generator, types.GeneratorType)  # the method returns a generator
    enumerated_result = [d for d in generator]
    assert len(enumerated_result) == len(set(enumerated_result))  # no duplicates
    assert set(enumerated_result) == expected_result


@pytest.mark.parametrize("n, expected_exception", [
    (-1, ValueError), (0, ValueError), (None, TypeError),
    ("1", TypeError),  (1.0, TypeError), ([1], TypeError)
])
def test_find_divisors_with_bad_parameters(n, expected_exception):
    generator = umath.find_divisors(n)
    with pytest.raises(expected_exception):
        next(generator)


# --- utools.math.sieve_of_eratosthenes ---
@pytest.mark.parametrize("p_min, p_max, expected_result", [
    (1, 12, [2, 3, 5, 7, 11]),
    (2, 2, [2]),
    (1, 1, []),
    (3, 2, []),
    (2, 211, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
              79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
              167, 173, 179, 181, 191, 193, 197, 199, 211])
])
def test_sieve_of_eratosthenes(p_min, p_max, expected_result):
    last_prime = 0
    primes = []
    for prime in umath.sieve_of_eratosthenes(p_min, p_max):
        assert prime > last_prime
        assert p_min <= prime <= p_max
        assert umath.is_prime(prime)
        primes.append(prime)
        last_prime = prime
    assert primes == expected_result


@pytest.mark.parametrize("p_min, p_max, expected_exception", [
    (None, 5, TypeError), ("1", 5, TypeError), (1, 5.0, TypeError)
])
def test_sieve_of_eratosthenes_with_bad_parameters(p_min, p_max, expected_exception):
    generator = umath.sieve_of_eratosthenes(p_min, p_max)
    with pytest.raises(expected_exception):
        next(generator)


# --- utools.math.prime_generator ---
@pytest.mark.parametrize("p_min, p_max, expected_result", [
    (1, 12, [2, 3, 5, 7, 11]),
    (2, 2, [2]),
    (1, 1, []),
    (3, 2, []),
    (2, 211, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
              79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
              167, 173, 179, 181, 191, 193, 197, 199, 211])
])
def test_prime_generator(p_min, p_max, expected_result):
    last_prime = 0
    primes = []
    for prime in umath.prime_generator(p_min, p_max):
        assert prime > last_prime
        assert p_min <= prime <= p_max
        assert umath.is_prime(prime)
        primes.append(prime)
        last_prime = prime
    assert primes == expected_result


@pytest.mark.parametrize("p_min, p_max, expected_exception", [
    (None, 5, TypeError), ("1", 5, TypeError), (1, 5.0, TypeError)
])
def test_prime_generator_with_bad_parameters(p_min, p_max, expected_exception):
    generator = umath.prime_generator(p_min, p_max)
    with pytest.raises(expected_exception):
        next(generator)


# we want to test that the two prime generators functions return the same primes
@pytest.mark.parametrize("p_min, p_max,", [
    (2, 4), (4, 2), (3, None), (2, None), (-1, 21), (20, 101), (20, None)
])
def test_prime_generator_and_sieve_of_eratosthenes(p_min, p_max):
    count_max = 1000
    count = 0
    for p1, p2 in zip(umath.prime_generator(p_min, p_max),
                      umath.sieve_of_eratosthenes(p_min, p_max)):
        assert p1 == p2
        count += 1
        if count == count_max:
            break
