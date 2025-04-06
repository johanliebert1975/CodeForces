import sys

def solve_permutation(arr, black):
    n = len(arr)
    cycles = []
    visited = set()
    black_counts = []

    for i in range(1, n + 1):  # 1-based indexing
        if i in visited:
            continue  # Skip already visited indices

        cycle = []
        black_count = 0
        current = i  # Start from 1-based index

        while current not in visited:
            visited.add(current)
            cycle.append(current)
            if black[current - 1] == '0':  # Check using 1-based index (convert to 0-based for string access)
                black_count += 1
            current = arr[current - 1]  # Move to the next 1-based index

        cycles.append(cycle)
        black_counts.append(black_count)

    # Create result array
    result = [0] * n
    for cycle, black_count in zip(cycles, black_counts):
        for i in cycle:
            result[i - 1] = black_count  # Store in 1-based index (convert to 0-based for list access)

    return result

def main():
    input_data = sys.stdin.read().split()

    index = 0
    t = int(input_data[index])
    index += 1

    out = []

    for _ in range(t):
        n = int(input_data[index])
        index += 1

        arr = list(map(int, input_data[index:index + n]))  # 1-based permutation
        index += n

        black = input_data[index]  # Binary string of length n
        index += 1

        # Convert result to a string and append to output
        out.append(" ".join(map(str, solve_permutation(arr, black))))  

    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
