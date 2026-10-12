#include <stdio.h>
#include <math.h>

const int loanLength = 10;
const double interest = 0.03;

int main() {
    int salary, housing, car, grocery, utility;
    printf("Welcome! Let's calculate your maximum loan amount \n");
    printf("Please enter the following: \n");

    // Request for the expenses
    printf("\tAnnual Salary: $");
    scanf("%d", &salary);

    printf("\tMonthly Housing Expenses: $");
    scanf("%d", &housing);

    printf("\tMonthly Car Expenses: $");
    scanf("%d", &car);

    printf("\tMonthly Grocery Expenses: $");
    scanf("%d", &grocery);

    printf("\tMonthly Utility Expenses: $");
    scanf("%d", &utility);

    float netMoney = salary / 12 - housing - car - grocery - utility;
    float monthly = 0.1 * netMoney;

    printf("Calculating...\nYour monthly payment is: $%.2f\n", monthly);

    int monthlyLoan = loanLength * 12;
    float monthlyInterestAmnt = interest / 12;

    int maxLoanAmount = 0.1 * (netMoney/monthlyInterestAmnt * (1 - (1 / pow((1 + monthlyInterestAmnt), monthlyLoan))));

    printf("Maximum loan amount: $%d", maxLoanAmount);
}