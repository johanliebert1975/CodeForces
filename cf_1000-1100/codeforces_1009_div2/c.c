#include <stdio.h>

int calc_y(int x) {
    for (int i = 1; i < x; i++) {
        if ((x & i) == 0) {  // Bitwise AND
            continue;
        }
        else if (i + (x ^ i) > x) {  // Bitwise XOR
            return i;
        }
    }
    return -1;
}

int main() {

    for (int i =2; i < 100; i++)
    {
        if (calc_y(i) != -1)
        {
            printf("%i %i\n",i,calc_y(i));
        }
        
    }
    
    return 0;
}