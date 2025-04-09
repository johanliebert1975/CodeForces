import sys

def min_cost(n):
    #print(n)
    count_0 = 0
    count_nonzero = 0
    while n % 10 == 0:
        #print("loop is entered")
        count_0 += 1
        n //= 10
    # print("zero_count")
    # print(count_0)
    while n:
        if n % 10 != 0:
            count_nonzero += 1
        n //= 10
    #print("non_zero count")
    #print(count_nonzero)
    return count_0 + count_nonzero - 1

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

        out.append(str(min_cost(n)))
    
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()