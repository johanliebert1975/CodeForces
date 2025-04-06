import sys

def min_steps(s):
    n = len(s)
    s = list(s)
    mod = 26
    offset = ord('a')

    total_even = [0] * mod
    total_odd = [0] * mod
    for i in range(n):
        idx = ord(s[i]) - offset
        if i % 2 == 0:
            total_even[idx] += 1
        else:
            total_odd[idx] += 1

    # If even length, no deletion needed
    if n % 2 == 0:
        return n - max(total_even) - max(total_odd)

    # Otherwise, try deleting each character
    res = float('inf')
    pref_even = [0] * mod
    pref_odd = [0] * mod

    for i in range(n):
        idx = ord(s[i]) - offset

        # Remove s[i], so skip adding it to prefix before computing
        temp_even = pref_even[:]
        temp_odd = pref_odd[:]

        if i % 2 == 0:
            suf_odd = [total_odd[j] - temp_odd[j] for j in range(mod)]
            suf_even = [total_even[j] - temp_even[j] - (1 if j == idx else 0) for j in range(mod)]
        else:
            suf_odd = [total_odd[j] - temp_odd[j] - (1 if j == idx else 0) for j in range(mod)]
            suf_even = [total_even[j] - temp_even[j] for j in range(mod)]

        new_even = [temp_even[j] + suf_odd[j] for j in range(mod)]
        new_odd = [temp_odd[j] + suf_even[j] for j in range(mod)]

        max_even = max(new_even)
        max_odd = max(new_odd)

        res = min(res, n - 1 - max_even - max_odd)

        # Update prefix after computing
        if i % 2 == 0:
            pref_even[idx] += 1
        else:
            pref_odd[idx] += 1

    if(n%2 == 0): return res
    else: return res+1

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
        s = data[index]
        index += 1
        out.append(str(min_steps(s)))

    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()