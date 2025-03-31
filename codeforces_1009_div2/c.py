import sys

def calc_y(x):
    if x == 0:  # Edge case: No bits set
        return -1

    msb_pos = x.bit_length() - 1  # Position of the MSB (leftmost 1-bit)

    # Check if all bits are 1 (i.e., x is of the form 111...111₂)
    if x == (1 << (msb_pos + 1)) - 1:
        return -1

    # Check if there exists another '1' bit after MSB
    if x & ((1 << msb_pos) - 1) == 0:
        return -1  # No other 1-bit found

    # Construct the result: Set all bits below MSB to 1
    return (1 << msb_pos) - 1


def main():
    input = sys.stdin.read
    data = input().split()
    index = 0
    output = []

    t = int(data[index])
    index += 1

    for _ in range(t):
        x = int(data[index])
        index += 1
        output.append(str(calc_y(x)))

    sys.stdout.write("\n".join(output)+ "\n")

if __name__ == "__main__":
    main()