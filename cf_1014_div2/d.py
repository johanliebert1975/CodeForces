def get_different_char(a, b):
    # Returns the unique character among 'L', 'I', 'T' that is not equal to a or b.
    for c in "LIT":
        if c != a and c != b:
            return c
    return None  # This should never happen

def solve_case(s):
    # Convert string to list for easier insertions.
    s = list(s)
    ops = []  # To record the 1-indexed positions of insertions
    # Dictionary to keep current counts.
    counts = { 'L': s.count('L'), 'I': s.count('I'), 'T': s.count('T') }
    
    def is_balanced():
        # The drink is balanced if counts are equal.
        return counts['L'] == counts['I'] == counts['T']
    
    # We allow up to 2*n moves.
    max_ops = 2 * len(s)
    
    for _ in range(max_ops):
        if is_balanced():
            return ops, "".join(s)
        
        # Identify the letter that is most needed (i.e. the one with the smallest count).
        needed = min(counts, key=counts.get)
        
        pos_found = None
        # First, try to find a valid adjacent pair that would yield the needed letter.
        for i in range(len(s) - 1):
            if s[i] != s[i+1]:
                candidate = get_different_char(s[i], s[i+1])
                if candidate == needed:
                    pos_found = i
                    break
        
        # If no position produces the needed letter, try to avoid worsening the imbalance:
        # Avoid inserting a letter that is already most frequent.
        if pos_found is None:
            most = max(counts, key=counts.get)
            for i in range(len(s) - 1):
                if s[i] != s[i+1]:
                    candidate = get_different_char(s[i], s[i+1])
                    if candidate != most:
                        pos_found = i
                        break
        
        # As a fallback, if nothing else works, take the first valid position.
        if pos_found is None:
            for i in range(len(s) - 1):
                if s[i] != s[i+1]:
                    pos_found = i
                    break
        
        # If still no allowed insertion exists, break out of the loop.
        if pos_found is None:
            break
        
        # Insert the allowed letter at the chosen position.
        candidate = get_different_char(s[pos_found], s[pos_found+1])
        s.insert(pos_found+1, candidate)
        # Record the 1-indexed position.
        ops.append(pos_found+1)
        counts[candidate] += 1

    # Final check
    if is_balanced():
        return ops, "".join(s)
    else:
        return None, None

# Main I/O handling (if running interactively or in a file)
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        
        ops, final_str = solve_case(s)
        if ops is None:
            results.append("-1")
        else:
            # First output the number of operations.
            result = [str(len(ops))]
            # Then output each operation (the insertion positions).
            for pos in ops:
                result.append(str(pos))
            results.append("\n".join(result))
    
    sys.stdout.write("\n".join(results))
