import sys

def can_do(arr, p, k):
    seen = [False] * k
    got = 0
    segments = 0
    for x in arr:
        if 0 <= x < k and not seen[x]:
            seen[x] = True
            got += 1
        if got == k:
            segments += 1
            if segments == p:
                return True
            seen = [False] * k
            got = 0
    return False

def max_min_mex(arr, p):
    lo, hi = 0, len(arr) + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if can_do(arr, p, mid):
            lo = mid
        else:
            hi = mid
    return lo

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        p = int(data[idx]); idx += 1
        arr = list(map(int, data[idx:idx+n]))
        idx += n

        out.append(str(max_min_mex(arr, p)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()