import sys

def get_exponent(m):
    exponent = 0
    while m % 2 == 0:
        exponent += 1
        m //= 2
    return exponent

def modify_arr(a, b):
    exp_arr = [get_exponent(a[i]) for i in range(len(a))]

    max_val = max(exp_arr)
    index = 0

    # Move index to the first usable value in b
    while index < len(b) and b[index] > max_val:
        index += 1

    while not all(x == 0 for x in exp_arr):
        if index < 0:  # Prevent infinite loop
            break
        
        if index < len(b) and b[index] > max_val:
            index -= 1
            continue
        elif index < len(b) and b[index] < max_val:
            exp_arr = [x - 1 if x == max_val else x for x in exp_arr]
            continue
        elif index < len(b) and b[index] == max_val:
            indices = [i for i in range(len(a)) if exp_arr[i] == max_val]
            for i in indices:
                a[i] += 2**(max_val-1)
            exp_arr = [get_exponent(a[i]) for i in range(len(a))]
            max_val = max(exp_arr)

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
    main()
