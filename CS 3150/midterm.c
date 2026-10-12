#include <stdio.h>
#define hexmax 9          
#define max 16777215  


void hexConvert(int value, char hex[]) {
    const char hex_digits[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};
    hex[0] = '0';
    hex[1] = 'x';

    for (int iter = 7; iter >= 2; iter--) {
        hex[iter] = hex_digits[value % 16];
        value /= 16;
    }

    hex[8] = '\0';
}

int main() {
    int number;
    char hex[hexmax];
    int valid = 0;

    while (!valid) {
        printf("Enter an integer between 0 and %d (-1 to quit): ", max);
        scanf("%d", &number);

        if (number == -1) {
            printf("Exiting program.\n");
            valid = 1;
        } 
        
        else if (number < 0 || number > max) {
            printf("Invalid input. Try again.\n");
        }

        hexConvert(number, hex);
        printf("Number converted to Hexadecimal: %s\n", hex);
    }

}