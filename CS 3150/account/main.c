#include <stdio.h>
#include "account.h"
#include "account.c"

int main(){
    double amt;
    int user_choice;

    while (1) {
        printf("Enter initial deposit to open account (min. $50.00): ");
        scanf("%lf", &amt, "\n");
        if (open_account(amt)) {
            break;
        }
    }

    while (1) {
        printf("Menu:\n");
        printf("1. Deposit\n");
        printf("2. Withdraw\n");
        printf("3. Check Balance\n");
        printf("4. Quit\n");
        printf("Enter choice: ");
        scanf("%d", &user_choice);

        switch (user_choice) {
            case 1:
                printf("Enter amount to deposit: ");
                scanf("%lf", &amt);
                deposit(amt);
                break;

            case 2:
                printf("Enter amount to withdraw: ");
                scanf("%lf", &amt);
                withdraw(amt);
                break;

            case 3:
                check_balance();
                break;

            case 4:
                printf("Quitting...\n");
                return 0;

            default:
                printf("Invalid choice. Try again.\n");
        }
    }
}