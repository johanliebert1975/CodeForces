import sys

def main():
    lines = sys.stdin.read()
    index = 0
    out = []

    data = lines.split()
    t = int(data[index])
    index += 1

    for _ in range(t):
        n = int(data[index])
        index += 1

        if n % 2 == 1:
            out.append("YES")
        else:
            out.append("NO")
    
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()