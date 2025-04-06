from collections import Counter
import sys

def unique_3(arr1,arr2):
    d1 = Counter(arr1)
    d2 = Counter(arr2)

    count  = 0
    seen = set()  # This is used to store unique i + j values

    for i in d1:
        while d1[i] > 0:
            for j in d2:
                while d2[j] > 0:
                    if (i + j) not in seen:
                        seen.add(i + j)
                        count += 1
                        if count == 3:
                            return "Yes"
                    d2[j] -= 1
                    d1[i] -= 1
                    break  # Move to next j after one match
            break  # Move to next i after one inner pass

    return "No"    

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
        arr1 = list(map(int,data[index:index+n]))
        index += n
        arr2 = list(map(int,data[index:index+n]))
        index += n
        

        out.append(unique_3(arr1,arr2))

    sys.stdout.write("\n".join(out)+"\n")

if __name__ == "__main__":
    main()

