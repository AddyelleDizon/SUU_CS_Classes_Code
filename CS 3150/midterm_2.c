#include <stdio.h>
#include <stdlib.h>


#define contacts_max 100
#define string_max 20

struct Contact {
    char firstName[string_max];
    char lastName[string_max];
    char phoneNumber[string_max];
};

int main() {
    struct Contact phoneBook[100];
    int count = 0;
    int valid = 0;
    int user_choice;

    while (!valid) {
        printf("1. Print Contacts\n");
        printf("2. Add Contact\n");
        printf("3. Quit\n");
        printf("Enter choice: ");
        scanf("%d", &user_choice);

        if (user_choice == 1) {
            if (count == 0) {
                printf("No contacts to display.\n");
            } 
            else {
                for (int i = 0; i < count; i++) {
                    printf("%d: %s, %s - %s\n", i + 1, phoneBook[i].lastName, phoneBook[i].firstName, phoneBook[i].phoneNumber);
                }
            }
        } 
        
        else if (user_choice == 2) {
            if (count >= contacts_max) {
                printf("Phone book is full!\n");
            } 
            
            else {
                printf("Enter first name: ");
                scanf("%s", phoneBook[count].firstName);

                printf("Enter last name: ");
                scanf("%s", phoneBook[count].lastName);

                printf("Enter phone number: ");
                scanf("%s", phoneBook[count].phoneNumber);

                count++;
                printf("Contact added!\n");
            }
        } 
        
        else if (user_choice == 3) {
            printf("Goodbye!\n");
            valid = 1;
        } 
        
        else {
            printf("Invalid choice, please try again.\n");
        }

    };

    return 0;
}