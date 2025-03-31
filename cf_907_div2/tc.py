import sys
import math

def moves(a):
    a.sort()
    left = 0
    m = 0
    x = 0
    right = len(a)-1
    while(left < right):
        if(a[left] + x > a[right]):
            m += a[right] - x + 1
            a[left] = a[left] + x - a[right]
            a[right] = 0
            print(a)
            right -= 1
            x = 0
            print(m,x)

        elif(a[left] + x == a[right]):
            m += a[left] + 1
            a[left] = 0
            a[right] = 0
            print(a)
            right -= 1
            left += 1
            x = 0
            print(m,x)
     
        
        elif(a[left] + x < a[right]):
            m += a[left]
            x += a[left]
            a[left] = 0
            print(a)
            left += 1
            print(m,x)
    
    if(x>a[left] and left == right and a[left] != 1):
        return int(m+a[left])
    elif(x<a[left] and left == right and a[left] != 1):
        return int(m + 2 + math.floor(0.5*(a[left]-x-1)))
    elif(a[left] == 1):
        return int(m+1)
    
    
    return m

def main():
    # Use fast input reading for large test cases
    input_data = sys.stdin.read().split()
    index = 0
 
    t = int(input_data[index])  # Number of test cases
    index += 1
    results = []
 
    for _ in range(t):
        n = int(input_data[index])  # Number of hordes
        index += 1
        a = list(map(int, input_data[index:index + n]))  # Read the hordes
        index += n
        results.append(str(moves(a)))
 
    # Print all results at once for efficiency
    sys.stdout.write("\n".join(results) + "\n")
 
if __name__ == "__main__":
    print(moves([6,3,4,4,4]))
        
        