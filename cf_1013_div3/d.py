import sys
import math

def bench_len(n,m,k):
    bench_size = 1
    if(m%2 == 0):
        m0 = math.ceil(m/2)
        while(m0 < m):
            if n*m0 >= k:
                return bench_size
            else:
                m0 += 1
                bench_size += 1
    else:
        m0 = 2
        parity = m0%2
        while(m0 < m):
            if n*m0 >= k:
                return bench_size
            elif m0%2 == parity :
                m0 += 1
                bench_size += 1
            elif m0%2 != parity:
                m0 += 1
    return m

def main():
    input_data = sys.stdin.read().split()
    index = 0
    t = int(input_data[index])
    index += 1
    out = []

    for _ in range(t):
        n, m, k = map(int, input_data[index:index+3])
        index += 3
        out.append(str(bench_len(n, m, k)))
    
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    print(bench_len(1,5,3))



# print(bench_len(5,5,5))
# print(bench_len(1,13,2))
# print(bench_len(2,4,7))
# print(bench_len(1,5,4))

