import math
import sys

def main():
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1

    out = []

    for _ in range(t):
        l, r = map(int,data[index:index+2])
        index += 2

        val = int(math.floor((1+math.sqrt(1+8*(r-l)))/2))
        out.append(str(val))

    sys.stdout.write("\n".join(out)+"\n")

if __name__ == "__main__":
    main()