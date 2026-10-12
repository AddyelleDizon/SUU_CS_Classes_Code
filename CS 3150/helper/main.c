#include <stdio.h>
#include "helper.h"
#include "helper.c"

int main(){
    int size = 10;
    int arr[size];
    int userChoice;
    int full = 0;

    while (1){
        printf("Menu:\n");
        printf("1. Fill array\n");
        printf("2. Print array\n");
        printf("3. Sort array\n");
        printf("4. Quit\n");
        printf("Enter choice: ");
        scanf("%d", &userChoice);

        if (userChoice == 1){
            int fill;
            void (*fill_function)(int[], int) = NULL;

            printf("\nYour options to fill the array are:\n");
            printf("1. With odd numbers\n");
            printf("2. With even numbers\n");
            printf("3. With random numbers between 1-1000\n");

            do {
                printf("Enter choice: ");
                scanf("%d", &fill);
            } 
            
            while (userChoice < 1 || userChoice > 3);
                

            switch (fill){
                case 1: fill_function = fill_array_odd; break;
                case 2: fill_function = fill_array_even; break; 
                case 3: fill_function = fill_array_random; break;
            }

            fill_function(arr, size);
            full = 1;
            printf("Array has been filled.\n");
        }

        else if (userChoice == 2){
            if (!full){
                printf("Array is not full.\n");
            }
            else {
                print_array(arr, size);
            }
        }

        else if (userChoice == 3){
            if (!full){
                printf("Array is not full.\n");
            }
            else {
                int sort;
                void (*sort_function)(int[], int) = NULL;

                printf("\nSorting options:\n");
                printf("1. Ascending order\n");
                printf("2. Descending order\n");

                while (sort < 1 || sort > 2){
                    printf("Enter choice: ");
                    scanf("%d", &sort);
                }

                switch (sort){
                    case 1: sort_function = sort_array_ascend; break;
                    case 2: sort_function = sort_array_descend; break;
                }

                sort_function(arr, size);
                printf("Array has been sorted.\n");
            }
        }

        else if (userChoice == 4){
            printf("Quitting...\n");
            return 0;
        }

        else {
            printf("Invalid option, please try again.\n");
        }
    }
}