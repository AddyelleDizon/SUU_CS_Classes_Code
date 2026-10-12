#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "helper.h"

void fill_array_odd(int arr[], int size){
    for (int count = 0; count < size; count++){
        arr[count] = 2 * count + 1;
    }
}

void fill_array_even(int arr[], int size){
    for (int count = 0; count < size; count++){
        arr[count] = 2 * count;
    }
}

void fill_array_random(int arr[], int size){
    srand(time(NULL)); // to seed the rng using the current time? apparently provides a unique seed using the current system time
    for (int count; count < size; count++){ // i do not know why it is stating that count is not initialized, when it is initialize with the 'int' prefix
        arr[count] = rand() % 1000 + 1;
    }
}

void print_array(int arr[], int size){
    printf("[");
    for (int count = 0; count < size; count++){
        printf("%d", arr[count]);
        if (count < size - 1) {
            printf(", ");
        }
    }
    printf("]\n");
}

void sort_array_ascend(int arr[], int size){
    // bubble sort, ascension
    for (int i = 0; i < size - 1; i++){
        for (int j = 0; j < size - i - 1; j++){
            if (arr[j] > arr[j + 1]){
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void sort_array_descend(int arr[], int size){
    // same bubble sort from above, but uses less than to indicate descension
    for (int i = 0; i < size - 1; i++){
        for (int j = 0; j < size - i - 1; j++){
            if (arr[j] < arr[j + 1]){
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
