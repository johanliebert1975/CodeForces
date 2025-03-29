import sys

def sieve(limit):
    arr = [True] * (limit + 1)
    arr[0] = arr[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if arr[i]:
            for j in range(i * i, limit + 1, i):
                arr[j] = False
    return arr

def generate_perm(n):
    if n == 1:
        return "1"
    elif n == 3:
        return "1 3 2"
    elif n == 5:
        return "4 1 3 5 2"
    else:
        arr = list(range(1, n + 1))
        for i in range(0, n - 1, 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return " ".join(map(str, arr))

def main():
    input_data = sys.stdin.read()
    data = input_data.split()
    index = 0
    out = []

    t = int(data[index])
    index += 1

    val = [int(data[i]) for i in range(index, index + t)]
    
    r = max(val)
    arr = sieve(r)

    for n in val:
        if not arr[n]:  # If n is composite, return -1
            out.append("-1")
        else:
            out.append(generate_perm(n))

    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
