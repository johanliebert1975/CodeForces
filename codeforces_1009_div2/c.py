import sys

def calc_y(x):
    i = 2
    while(i<x):
        if(x&i == 0):
            continue
        elif(i + (x^i)>x):
            return i
        i = i**2 
    return -1

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