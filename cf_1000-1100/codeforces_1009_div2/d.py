import math
import sys

def num_points(x,r):
    # x and r are arrays of equal length
    num_points = 0
    min_x = min(xi-ri for xi,ri in zip(x,r))
    max_x = max(xi + ri for xi,ri in zip(x,r))

    for i in range(min_x, max_x + 1):  # Include max_x
        max_y = 0
        for x0, r0 in zip(x, r):
            d = r0**2 - (i - x0)**2
            if d >= 0:  # Ensure non-negative before sqrt
                max_y = max(max_y, math.floor(math.sqrt(d)))
        num_points += 2 * max_y + 1  # Count points in this column

    return num_points

def main():
    input_data = sys.stdin.read().split()
    index = 0
    t = int(input_data[index])
    index += 1
    out = []
    for _ in range(t):
        n, m = map(int, input_data[index:index+2])
        index += 2
        x = list(map(int, input_data[index:index+n]))
        index += n
        r = list(map(int, input_data[index:index+n]))
        index += n
        
        out.append(str(num_points(x, r)))
    
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()