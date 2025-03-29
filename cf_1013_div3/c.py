import sys

def construct_arr(n):
    if n % 2 == 0:
        return "-1"  # Even numbers return -1 immediately
    arr = list(range(1, n + 1)) 
    arr.reverse()  # Append 1 at the end
    return " ".join(map(str, arr))  # Convert to space-separated string

def main():
    input_data = sys.stdin.read().split()
    t = int(input_data[0])  # Number of test cases

    results = []
    for i in range(1, t + 1):
        n = int(input_data[i])
        results.append(construct_arr(n))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
