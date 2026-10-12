#include <stdio.h>
#include <math.h>

// Function to calculate factorial
double factorial(int n) {
    double fact = 1.0;
    for (int i = 1; i <= n; i++) {
        fact *= i;
    }
    return fact;
}

// Function to approximate e^x using Maclaurin series
double exp_maclaurin(double x, int terms) {
    double sum = 0.0;

    for (int n = 0; n < terms; n++) {
        sum += (1.0 * pow(x, n)) / factorial(n);
    }

    return sum;
}

int main() {
    double x;
    int terms;

    printf("Enter value of x: ");
    scanf("%lf", &x);

    printf("Enter number of terms in Maclaurin series: ");
    scanf("%d", &terms);

    double result = exp_maclaurin(x, terms);

    printf("Approximation of e^%.2f using %d terms = %.10f\n", x, terms, result);

    return 0;
}