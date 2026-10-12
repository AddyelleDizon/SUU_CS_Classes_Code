#include <iostream>
#include <vector>
#include <limits>
#include <random>
#include "payroll.cpp"
#include "payroll.h"

void clear_input() {
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}

// i had to look up how to do a randomizer
int random_id() {
    static std::random_device rand;
    static std::mt19937 gen(rand());
    static std::uniform_int_distribution<> dis(10000, 99999);
    return dis(gen);
}

// same as previous statement
double random_double(double min, double max) {
    static std::random_device rand;
    static std::mt19937 gen(rand());
    std::uniform_real_distribution<> dis(min, max);
    return dis(gen);
}

int main() {
    std::vector<Employee*> employees;
    int choice;
    bool valid = 0;

    while (!valid){    // no infinite loops
        std::cout << "\n--- Payroll Menu ---\n";
        std::cout << "1. Add Full Time Employee\n";
        std::cout << "2. Add Part Time Employee\n";
        std::cout << "3. List All Employees\n";
        std::cout << "4. Total Payroll\n";
        std::cout << "5. Quit\n";
        std::cout << "Choice: ";
        std::cin >> choice;

        if (!std::cin) { 
            clear_input(); 
            continue; 
        }

        // make full time employee
        if (choice == 1) {
            std::string first, last;
            double salary, bonus;
            std::cout << "First Name: "; 
            std::cin >> first;
            std::cout << "Last Name: "; 
            std::cin >> last;
            std::cout << "Salary: "; 
            std::cin >> salary;
            std::cout << "Bonus: "; 
            std::cin >> bonus;

            std::vector<std::string> benefits;
            std::cout << "Select Benefits (enter numbers separated by space, 0 to finish):\n";
            for (size_t i = 0; i < VALID_BENEFITS.size(); ++i)
                std::cout << i + 1 << ". " << VALID_BENEFITS[i] << "\n";
            std::cout << "Selection: ";

            int b;
            
            while (std::cin >> b) {
                if (b == 0) break;
                if (b >= 1 && b <= (int)VALID_BENEFITS.size())
                    benefits.push_back(VALID_BENEFITS[b - 1]);
                else std::cout << "Invalid number. Try again: ";
            }

            clear_input();
            employees.push_back(new FullTimeEmployee(random_id(), first, last, salary, bonus, benefits));
        }

        // make part time employee
        else if (choice == 2) {
            std::string first, last;
            double wage, hours, sick = random_double(0, 40);
            std::cout << "First Name: "; std::cin >> first;
            std::cout << "Last Name: "; std::cin >> last;
            std::cout << "Wage: "; std::cin >> wage;
            std::cout << "Hours Worked: "; std::cin >> hours;
            employees.push_back(new PartTimeEmployee(random_id(), first, last, wage, hours, sick));
        }

        // view added employees, if none show nothing
        else if (choice == 3) {
            std::cout << "\n--- Employee List ---\n";
            for (auto* e : employees)
                std::cout << *e << "\n";
        }

        // view total pay
        else if (choice == 4) {
            double total = 0;
            for (auto* e : employees)
                total += e->pay();
            std::cout << "Total Payroll: $" << total << "\n";
        }
        
        else if (choice == 5) {
            valid = 1;
        }

        else {
            std::cout << "Please enter a valid number.";
        }

    };

    // erase all dynamic memory
    for (auto* e : employees) delete e;
    std::cout << "Quitting program...\n";
    return 0;
}