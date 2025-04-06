import math
from collections import Counter

def find_k(a, b):
    sum_a = sum(a)
    sum_b = sum(b)
    delta = sum_a - sum_b
    
    # Case 1: Delta == 0
    if delta == 0:
        counter_a = Counter(a)
        counter_b = Counter(b)
        if counter_a == counter_b:
            return max(a) + 1
        return -1
    
    # Case 2: Delta != 0
    abs_delta = abs(delta)
    divisors = set()
    
    # Optimize divisor calculation
    for i in range(1, int(math.sqrt(abs_delta)) + 1):
        if abs_delta % i == 0:
            divisors.add(i)
            if i != abs_delta // i and abs_delta // i <= 10**9:
                divisors.add(abs_delta // i)
    
    # Use frequency counters instead of sorting
    counter_b = Counter(b)
    
    for k in sorted(divisors):
        if k == 0:
            continue
        
        # Use generator expression for memory efficiency
        remainder_counter = Counter(x % k for x in a)
        if remainder_counter == counter_b:
            return k
    
    return -1

def main():
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        results.append(str(find_k(a, b)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
