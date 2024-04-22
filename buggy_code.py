def generate_primes(limit):
    primes = []
    for num in range(2, limit):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

primes = generate_primes(100)
print(primes)