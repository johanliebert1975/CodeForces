import sys

def min_steps(s):
    s = list(s)
    n = len(s)
    
    # For even-length strings, count even and odd indices
    if n % 2 == 0:
        counts_even = {}
        counts_odd = {}
        for i in range(n):
            if i % 2 == 0:
                counts_even[s[i]] = counts_even.get(s[i], 0) + 1
            else:
                counts_odd[s[i]] = counts_odd.get(s[i], 0) + 1
        return n - max(counts_even.values(), default=0) - max(counts_odd.values(), default=0)
    
    # For odd-length strings, try deleting one character and evaluate the steps needed
    else:
        min_s = 10**10
        for del_index in range(n):
            # Create a new string with the character at del_index removed
            new_s = s[:del_index] + s[del_index+1:]
            new_n = len(new_s)
            new_counts_even = {}
            new_counts_odd = {}

            for i in range(new_n):
                if i % 2 == 0:
                    new_counts_even[new_s[i]] = new_counts_even.get(new_s[i], 0) + 1
                else:
                    new_counts_odd[new_s[i]] = new_counts_odd.get(new_s[i], 0) + 1
            
            # Calculate steps
            max_even = max(new_counts_even.values(), default=0)
            max_odd = max(new_counts_odd.values(), default=0)
            steps = new_n - max_even - max_odd + 1

            if steps == 1:
                return 1  # If we can get to 1, return early
            min_s = min(min_s, steps)

        return min_s

def main():
    input_data = sys.stdin.read()
    data = input_data.split()
    
    index = 0
    out = []

    t = int(data[index])
    index += 1

    for _ in range(t):
        n = int(data[index])
        index += 1

        s = data[index]  # string of length n
        index += 1

        out.append(str(min_steps(s)))

    sys.stdout.write("\n".join(out) + "\n")  # Properly formatted output


if __name__ == "__main__":
    #print(min_steps("aab"))
    main()