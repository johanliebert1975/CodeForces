import sys

def val(nums):
    l = len(nums)
    index = 0
    for i in range(1,l):
        nums.append(nums[index]+nums[index+1]-1)
        index+=2

    return nums[-1]

def main():
    input = sys.stdin.read
    inp = input().split()
    out = []
    index = 0

    t = int(inp[index])
    index +=1

    for _ in range(t):
        n = int(inp[index])
        index += 1
        nums = list(map(int,inp[index:index+n]))
        index += n

        out.append(str(val(nums)))

    sys.stdout.write("\n".join(out)+"\n")

if __name__ == "__main__":
    main()
