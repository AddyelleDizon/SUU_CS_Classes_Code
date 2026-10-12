#include <iostream>
#include <cmath>
using namespace std; //

bool is_prime(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;

    int limit = static_cast<int>(sqrt(n));
    for (int i = 3; i <= limit; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    cout << "\nWelcome to the Prime Number Program!" << endl;

    int* user_number = new int;
    int valid = 0;

    while (!valid) {
        cout << "Enter a number or 0 to quit: ";
        cin >> *user_number;

        if (*user_number == 0) valid = 1;

        if (is_prime(*user_number)) {
            cout << *user_number << " is a prime number!\n" << endl;
        } 
        
        else {
            cout << *user_number << " is not a prime number!\n" << endl;
        }

    };

    cout << "Ending program, goodbye." << endl;

    delete user_number;
    return 0;
}