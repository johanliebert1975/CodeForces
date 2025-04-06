import sys

def check_square(l,r,d,u):
    if((-l+r == 0) and (-d+u == 0) and (abs(u) == abs(l))):
        return "yes"
    return "no"

def main():
    index = 0
    input = sys.stdin.read

    inp  = input().split()
    out = []
    t = int(inp[index])
    index += 1

    for _ in range(t):
        l,r,d,u = map(int,inp[index:index+4])
        index += 4
        out.append(check_square(l,r,d,u))

    sys.stdout.write("\n".join(out)+"\n")

if __name__ == "__main__":
    main()
