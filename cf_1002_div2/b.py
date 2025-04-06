import sys

def partitions(arr,p):
    count = 0
    n = len(arr)

    if p == n:
        e = []
        for i in range(n):
            if((i+1)%2 == 0):
                e.append(arr[i])
        e.append(0)
        for i in range((n//2)+1):
            if i+1 != e[i]:
                return i+1     
    else:
        for i in range(1,n-p+2):
            if(arr[i] == 1):
                count += 1
        if count >= 0 and count < n-p+1:
            return 1
        else: return 2

def main():
    input = sys.stdin.read
    data = input().split()

    out = []
    index = 0

    t = int(data[index])
    index += 1

    for _ in range(t):
        n = int(data[index])
        index += 1
        p = int(data[index])
        index += 1
        arr1 = list(map(int,data[index:index+n]))
        index += n

        out.append(str(partitions(arr1,p)))

    sys.stdout.write("\n".join(out)+"\n")

if __name__ == "__main__":
    main()