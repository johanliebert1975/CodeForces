import sys

def is_non_decreasing(arr, start, end):
    return all(arr[i] <= arr[i + 1] for i in range(start, min(end - 1, len(arr) - 1)))

def status(arr):
    index = 1
    while 2**index < len(arr):  # Fix condition to avoid OOB
        if not is_non_decreasing(arr, 2**index, 2**(index + 1)):
            return "NO"
        index += 1
    
    if 2**index < len(arr) and not is_non_decreasing(arr, 2**index, len(arr)):  # Fix last segment check
        return "NO"
    
    return "YES"

def main():
    input_data = sys.stdin.read()
    index = 0
    out = []

    data = input_data.split()

    t = int(data[index])
    index += 1

    for _ in range(t):  # Fix iteration over t
        n = int(data[index])
        index += 1

        arr = list(map(int, data[index:index + n]))
        index += n
        out.append(status(arr))
    
    sys.stdout.write("\n".join(out) + "\n")  # Ensure newline at the end

if __name__ == "__main__":
    main()
