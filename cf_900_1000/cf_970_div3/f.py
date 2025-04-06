import sys
from collections import Counter

MOD = 10**9 + 7

def calc_expected(arr):
    freq = Counter(arr)

    total = 0
    freq_weighted_sum = 0
    freq_sum = 0

    for val in sorted(freq):  # Sort to ensure i < j ordering
        f = freq[val]

        # Contribution from distinct pairs (i != j): f_i * f_j * i * j
        total += f * val * freq_weighted_sum
        total %= MOD

        # Contribution from same elements (i == j): C(f, 2) * i^2 = (f * (f - 1) / 2) * i^2
        total += ((f * (f - 1) // 2) * val * val) % MOD
        total %= MOD

        freq_weighted_sum += f * val
        freq_weighted_sum %= MOD

        freq_sum += f
        freq_sum %= MOD

    # Now compute expected value: total / C(n, 2) = total * inverse(freq_sum_C2)
    total_pairs = freq_sum * (freq_sum - 1) // 2
    if total_pairs == 0:
        return 0  # No pairs

    inv = pow(total_pairs, MOD - 2, MOD)  # Modular inverse
    return (total * inv) % MOD

def main():
    input_data = sys.stdin.read()
    data = input_data.split()
    
    index = 0
    out = []

    t = int(data[index])
    index += 1

    for _ in range(t):
        n = int(data[index])
        index += 1

        arr = list(map(int, data[index:index + n]))
        index += n

        out.append(str(calc_expected(arr)))

    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
