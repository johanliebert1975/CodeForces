import sys
import math

MODULO = 10**9 + 7

def log_sum(l, r):
    total = 0
    for i in range(l, r + 1):
        if i == 1:
            continue  # Avoid division by zero
        total += int(math.floor(math.log(i) / (math.log(math.floor(math.log2(i))))))
    return total % MODULO

def main():
    input_data = sys.stdin.read().split()
    index = 0
    out = []
    
    t = int(input_data[index])
    index += 1

    for _ in range(t):
        l, r = map(int, input_data[index:index + 2])
        index += 2
        out.append(str(log_sum(l, r)))

    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
