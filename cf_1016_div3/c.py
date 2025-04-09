import sys

def is_prime(n):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in [2, 3, 5, 7, 11]:  # good enough for up to ~2e18
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def repeat_number_str(x, n):
    return int(str(x) * n)

def main():
    lines = sys.stdin.read()
    index = 0
    out = []

    data = lines.split()
    t = int(data[index])
    index += 1

    x = []
    n =[]
    for _ in range(t):
        x.append(data[index])
        index += 1
        n.append(data[index])
        index += 1

    num = []
    for i in range(t):
        num.append(repeat_number_str(x[i], int(n[i])))  # convert n[i] to int here

    for i in range(t):
        if is_prime(num[i]):
            out.append("YES")
        else:
            out.append("NO")
    
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()