import sys

def status(a, b):
    ones_even = 0  # Count of '1's at even indices
    ones_odd = 0   # Count of '1's at odd indices

    for i in range(len(a)):  
        if a[i] == '1':  
            if i % 2 == 0:  # Even index
                ones_even += 1
            else:  # Odd index
                ones_odd += 1

    zeroes_even = 0
    zeroes_odd = 0

    for i in range(len(b)):  
        if b[i] == '0':  
            if i % 2 == 0:  # Even index
                zeroes_even += 1
            else:  # Odd index
                zeroes_odd += 1

    if zeroes_even >= ones_odd and zeroes_odd >= ones_even:
        return "YES"  # Use uppercase as standard format
    else:
        return "NO"

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1

    out = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        a = data[index]   # Use direct indexing instead of list slicing
        index += 1
        b = data[index]
        index += 1

        out.append(status(a, b))

    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
