import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sieve_of_eratosthenes(m):
    if m < 2:
        return []
    is_prime = [True] * (m + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(m)) + 1):
        if is_prime[i]:
            for multiple in range(i * i, m + 1, i):
                is_prime[multiple] = False
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

# Example usage
number = int(input("Enter a number to check if it is prime: "))
print(f"Is {number} prime? {'Yes' if is_prime(number) else 'No'}")

limit = int(input("Enter the upper limit to generate primes up to: "))
print(f"Prime numbers up to {limit}: {sieve_of_eratosthenes(limit)}")
