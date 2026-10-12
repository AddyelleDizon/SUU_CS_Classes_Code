#include <stdio.h>
#include <math.h>

int main(void){
    
    int choice;
    float x;
    int iter;

    printf("Choose a function to approximate: \n");
    printf("1. cos(x)\n2. sin(x)\n3. e^x\n4. Quit\n");
    scanf("%d", &choice);

    // This is to calculate the cos(x) Taylor Series approx.
    if (choice == 1) {

        printf("Enter a value of 'x' to approximate: \n");
        scanf("%f", &x);

        printf("Enter the number of iterations: \n");
        scanf("%d", &iter);

        if(iter > 0){
            printf("Approximating cos(x) using a Taylor Series expansion. \n");
            
            double sum = 0;
            for (int ind = 0; ind < iter; ind++){
                int factVal = 1;
                for (int secInd = ind; secInd > 1; secInd++){
                    factVal *= ((2 * secInd));
                }

                // (-1)^(n-1) * (x^(2x-1))/(2x-1)!
                // 2x-1! is factVal
                sum += pow(-1, ind) * (pow(x, (2 * ind)))/factVal;
            }
            printf("The approximation is: %f", sum);
            printf("\n");
            printf("\n");
            main();
        }

        else{
            printf("Invalid 'n' value, please try again. \n");
            main();
        }  

    } 
    
    // This is to calculate the sin(x) Taylor Series approx.
    else if (choice == 2) {
        printf("Enter a value of 'x' to approximate: \n");
        scanf("%f", &x);

        printf("Enter the number of iterations: \n");
        scanf("%d", &iter);

        if(iter > 0){
            printf("Approximating sin(x) using a Taylor Series expansion. \n");

            double sum = 0;
            for (int ind = 0; ind < iter; ind++){
                int factVal = 1;
                for (int secInd = ind; secInd > 1; secInd++){
                    factVal *= ((2 * secInd) - 1);
                }

                // (-1)^(n-1) * (x^(2x-1))/(2x-1)!
                // 2x-1! is factVal
                sum += pow(-1, (ind - 1)) * (pow(x, (2 * ind)) -  1)/factVal;
            }
            printf("The approximation is: %f", sum);
            printf("\n");
            printf("\n");
            main();
        }

        else{
            printf("Invalid 'n' value, please try again. \n");
            main();
        }   
    } 
    
    // This is to calculate the e^x Taylor Series approx.
    else if (choice == 3) {
        printf("Enter a value of 'x' to approximate: \n");
        scanf("%f", &x);

        printf("Enter the number of iterations: \n");
        scanf("%d", &iter);

        if(iter > 0){
            printf("Approximating e^x using a Taylor Series expansion. \n");

            double sum = 0;
            for (int ind = 0; ind < iter; ind++){
                int factVal = 1;
                for (int secInd = ind; secInd > 1; secInd++){
                    factVal *= secInd;
                }

                // x^n/n!
                sum += pow(x, ind)/factVal;
            }
            printf("The approximation is: %f", sum);
            printf("\n");
            printf("\n");
            main();
        }

        // This is to repeat the whole process if an invalid n value is inputted
        else{
            printf("Invalid 'n' value, please try again. \n");
            main();
        }  
    } 
    
    // This is to break out of the menu
    else if (choice == 4) {
        return 0;
    }

    // This is to ensure no wrong menu choice can be picked
    else{
        printf("Invalid choice, please try again. \n");
        main();
    }
}
