import sys
import math

def create_mat_string(n):
    """Generate a string representing an n x n matrix with 1s on the border and 0s inside."""
    s = []
    for i in range(n):
        for j in range(n):
            s.append('1' if (i == 0 or i == n-1 or j == 0 or j == n-1) else '0')
    return ''.join(s)  # Return a single string

def is_perfect_square(n):
    """Check if a number is a perfect square."""
    sqrt_n = math.sqrt(n)
    return sqrt_n * sqrt_n == n

def check_string(n, s):
    """Verify if the given string represents a valid bordered matrix."""
    if not is_perfect_square(n):
        return "No"

    size = int(math.sqrt(n))
    if s.count('1') != 4 * size - 4:  # Expected number of border 1s
        return "No"

    if create_mat_string(size) != s:
        return "No"
    return "Yes"

def main():
    input_data = sys.stdin.read().split()
    index = 0
    t = int(input_data[index])  # Number of test cases
    index += 1

    results = []
    
    for _ in range(t):
        n = int(input_data[index])  # Length of the string
        index += 1
        s = input_data[index]  # The binary string of length n
        index += 1
        results.append(check_string(n, s))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()