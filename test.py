import pytest
from buggy_code import generate_primes

def test_generate_primes():
    
    assert generate_primes(10) == [2, 3, 5, 7]  # Primes up to 10 should be [2, 3, 5, 7]
    assert generate_primes(2) == []  # Primes up to 2 should be empty
