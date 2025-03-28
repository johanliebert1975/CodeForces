import sys

def check_universal(word, swap):
    if word < word[::-1]:  
        return "yes"
    
    if word == word[::-1]:  # Check if it's a palindrome
        if len(set(word)) == 1:  # All characters are the same
            return "no"
        return "yes" if swap > 0 else "no"
    
    return "yes" if swap > 0 else "no"

read_input = sys.stdin.read
data = read_input().split()

index = 0
t = int(data[index])
index += 1

results = []

for _ in range(t):
    n, k = map(int, data[index:index + 2])
    index += 2
    word = data[index]  # Read the next string
    index += 1

    results.append(check_universal(word, k))

sys.stdout.write("\n".join(results) + "\n")
