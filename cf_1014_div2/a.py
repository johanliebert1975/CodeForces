import sys

def val(arr):
    return max(arr)-min(arr)

def main():
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1

    out = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int,data[index:index+n]))
        index += n

        out.append(str(val(arr)))

    sys.stdout.write("\n".join(out)+ "\n")

if __name__ == "__main__":
    main()