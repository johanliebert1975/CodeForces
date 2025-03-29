import math
import sys

def count_points_in_circle(h, k, r):
    """Count integer points inside or on the circle without storing them."""
    count = 0
    for x in range(h - r, h + r + 1):  # Iterate over x within the circle
        y_range = math.isqrt(r**2 - (x - h)**2)  # Max |y - k|
        count += (2 * y_range + 1)  # Count points in this column
    return count

def num_points(x, r):
    """Count unique points inside multiple circles."""
    unique_points = set()
    for h, radius in zip(x, r):  # Iterate over centers & radii
        unique_points |= set((h, radius))  # Only track unique (h, r)
    total = 0
    for h, radius in unique_points:
        total += count_points_in_circle(h, 0, radius)
    return total

def main():
    input = sys.stdin.read
    data = input().split()

    out =[]
    index = 0

    t = int(data[0])
    index += 1
    
    for _ in range(t):
        n = int(data[index])
        index += 2

        x = list(map(int,data[index:index+n]))
        index += n
        r = list(map(int,data[index:index+n]))
        index += n

        out.append(str(num_points(x,r)))

    sys.stdout.write("\n".join(out)+"\n")

if __name__ == "__main__":
    main()