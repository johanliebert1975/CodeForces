import sys

# use the sieve of eratosthenes to mark the prime numbers
def sieve(limit):
    is_prime = [True]*(limit+1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit ** 0.5) + 1):  # Step 1: Iterate from 2 to sqrt(limit)
        if is_prime[i]:  # Step 2: If i is still marked as prime
            for j in range(i * i, limit + 1, i):  # Step 3: Mark all multiples of i
                is_prime[j] = False  # Not a prime number

    return is_prime

def precompute_prime_count(is_prime):
    prime_count = [0] * len(is_prime)
    
    for i in range(1, len(is_prime)):
        prime_count[i] = prime_count[i-1] + (1 if is_prime[i] else 0)
    
    return prime_count

def count_interesting_ratios(n, prime_count):
    total_count = 0
    a = 1
    
    while a <= n:
        limit = n // a  # Compute floor(n / a)
        if limit <= 1:  # Stop when limit becomes 1
            break
        total_count += prime_count[limit]  # Get number of primes ≤ limit
        a += 1  # Move to next a
    
    return total_count


def main():
    # Read input
    input = sys.stdin.read
    data = list(map(int, input().split()))

    t = data[0]  # Number of test cases
    test_cases = data[1:]  # List of n values for each test case

    limit = max(test_cases)  # Find the largest n to precompute up to
    is_prime = sieve(limit)
    prime_count = precompute_prime_count(is_prime)

    results = []
    for n in test_cases:
        results.append(str(count_interesting_ratios(n, prime_count)))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
