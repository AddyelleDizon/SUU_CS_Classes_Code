#include <stdio.h>
#include "account.h"

static double bal = 0.0;

void deposit(double amt){
    if (amt > 0) {
        bal += amt;
        printf("You have deposited: $%0.2f\n", amt);
    } 
    else {
        printf("Invalid deposit. Please ensure the amount is positive.\n");
    }
}

int withdraw(double amt){
    if (amt <= 0){
        printf("Invalid withdrawal. Please ensure the amount is positive.\n");
        return 0;
    }
    else if (amt > bal) {
        printf("Invalid withdrawal. Insufficient funds.\n");
        return 0;
    }
    bal -= amt;
    printf("You have withdrew: $%.2f", amt);
    return 1;
}

void check_balance(){
    printf("Current balance: $%.2f\n", bal);
}

int open_account(double initial_amt){
    if (initial_amt >= 50) {
        bal = initial_amt;
        printf("Account opened with balance: $%.2f", bal);
        return 1;
    }
    else {
        printf("Failed to open account. Minimum deposit is $50.00\n");
        return 0;
    }
}