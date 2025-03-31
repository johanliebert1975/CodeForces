import sys

def f(arr):
    total_sum = 0
    num_odd = 0
    n = len(arr)
    for i in range(n):
        total_sum += arr[i]
        if arr[i] % 2 == 1:
            num_odd += 1
    if num_odd == n or num_odd == 0:
        return max(arr)
    else:
        return total_sum - num_odd + 1

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1

    out = []

    for _ in range(t):
        n = int(data[index])
        index += 1  # Increment index to skip the number of elements
        arr = list(map(int, data[index:index + n]))
        index += n  # Increment index by 'n' for the array
        out.append(str(f(arr)))

    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()