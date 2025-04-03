import sys

def main():
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1

    out = []

    for _ in range(t):
        a, b = map(int,data[index:index+2])
        index += 2

        if (2*b - a)%2 == 0:
            if(a == 0 and b%2 == 1):
                out.append("No")
                continue
            out.append("Yes")
            continue
        else: 
            out.append("No")
            continue

    sys.stdout.write("\n".join(out)+"\n")

if __name__ == "__main__":
    main()