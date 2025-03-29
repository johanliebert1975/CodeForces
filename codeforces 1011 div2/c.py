import sys

def find_k(x, y):
    if x==y:
        return -1
    else: return 2**48 - max(x,y)

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
