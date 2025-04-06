import sys
from collections import defaultdict

def min_steps(s):
    s = list(s)
    n = len(s)

    pref1 = [defaultdict(int) for _ in range(n+1)] # number of times char c appears at even indices before i
    pref2 = [defaultdict(int) for _ in range(n+1)] # number of times char c appears at odd indices before i
    suff1 = [defaultdict(int) for _ in range(n+1)] # number of times char c appears at even indices after i
    suff2 = [defaultdict(int) for _ in range(n+1)] # number of times char c appears at odd indices after i

    for i in range(n):
        pref1[i+1] = pref1[i].copy()
        pref2[i+1] = pref2[i].copy()
        if i % 2 == 0:
            pref1[i+1][s[i]] += 1
        else:
            pref2[i+1][s[i]] += 1

    for i in range(n-1, -1, -1):
        suff1[i] = suff1[i+1].copy()
        suff2[i] = suff2[i+1].copy()
        if i % 2 == 0:
            suff1[i][s[i]] += 1
        else:
            suff2[i][s[i]] += 1

    # For even-length strings, count even and odd indices
    if n % 2 == 0:
        max_even = max(pref1[n].values(), default=0)
        max_odd = max(pref2[n].values(), default=0)
        return n - max_even - max_odd
    else:
        res = n
        for i in range(n):
            # we loop through every index and checking and updating moves
            # moves = n - max(even_values for all the characte..) - max(odd values for all characters)
            # however we do need to update the even and odd values for all the characters using the precomputed arrays

            even_counts = defaultdict(int)
            odd_counts = defaultdict(int)

            for c in 'abcdefghijklmnopqrstuvwxyz':
                even_counts[c] = pref1[i][c] + suff2[i+1][c]
                odd_counts[c] = pref2[i][c] + suff1[i+1][c]

            max_even = max(even_counts.values(), default=0)
            max_odd = max(odd_counts.values(), default=0)
            res = min(res, n - 1 - max_even - max_odd)

        return res + 1
    
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

        s = data[index]  # string of length n
        index += 1

        out.append(str(min_steps(s)))

    sys.stdout.write("\n".join(out) + "\n")  # Properly formatted output


if __name__ == "__main__":
    main()

