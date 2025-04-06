import sys

def modify_arr(a, q):
    min_val = q[0]
    q0 = [min_val]
    for i in range(1,len(q)):
        if q[i]<min_val:
            min_val = q[i]
            q0.append(min_val)
    for x in q0:
        for i in range(len(a)):
            if(a[i]%(2**x) == 0):
                a[i] += 2**(x-1)

    return a

def main():
    input_data = sys.stdin.read()
    index = 0
    out = []

    data = input_data.split()

    t = int(data[index])
    index += 1

    for _ in range(t):
        n = int(data[index])
        index += 1

        q = int(data[index])
        index += 1

        a = list(map(int, data[index:index+n]))
        index += n

        b = list(map(int, data[index:index+q]))
        index += q

        out.append(" ".join(map(str, modify_arr(a, b))))
    
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    a = [1,2,3,4,4]
    b = [2,3,4]
    print(modify_arr(a,b))
