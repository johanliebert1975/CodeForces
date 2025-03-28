import sys

def find_k(x, y):
    xor_val = x ^ y
    sum_val = x + y
    
    # Check if the required condition is possible
    if (xor_val - sum_val) % 2 != 0:
        return -1
    
    k = (xor_val - sum_val) // 2
    
    # Verify that (x + k) & (y + k) == 0
    if k >= 0 and ((x + k) & (y + k)) == 0:
        return k
    else:
        return -1

# Read input and process test cases
def main():
    input = sys.stdin.read().split()
    t = int(input[0])
    index = 1
    results = []
    for _ in range(t):
        x = int(input[index])
        y = int(input[index + 1])
        index += 2
        results.append(str(find_k(x, y)))
    print('\n'.join(results))

if __name__ == "__main__":
    main()
