#include "linkedlist.h"
#include "linkedlist.c"

int main() {
    Node* list = NULL;
    int choice, value, index;
    int valid = 0;

    while (!valid) {
        printf("1. Make a new list\n");
        printf("2. Print the list\n");
        printf("3. Append an item\n");
        printf("4. Delete an item\n");
        printf("5. Insert an item\n");
        printf("6. Change a value\n");
        printf("7. Quit\n");

        printf("Please select an option: ");
        if (scanf("%d", &choice) != 1) {
            printf("Invalid input. Try again.\n");
        }

        switch (choice) {
            case 1:
                while (list != NULL) {
                    Node* temp = list;
                    list = list->next;
                    free(temp);
                }
                list = createList();
                printf("New list created.\n");
                break;

            case 2:
                printList(list);
                break;

            case 3:
                printf("Enter value to append: ");
                scanf("%d", &value);
                appendItem(&list, value);
                break;

            case 4:
                printf("Enter index to delete: ");
                scanf("%d", &index);
                deleteItem(&list, index);
                break;

            case 5:
                printf("Enter index to insert at: ");
                scanf("%d", &index);
                printf("Enter value: ");
                scanf("%d", &value);
                insertItem(&list, index, value);
                break;

            case 6:
                printf("Enter index to change: ");
                scanf("%d", &index);
                printf("Enter new value: ");
                scanf("%d", &value);
                changeValue(list, index, value);
                break;

            case 7:
                printf("Exiting program.\n");
                while (list != NULL) {
                    Node* temp = list;
                    list = list -> next;
                    free(temp);
                }
                return 0;

            default:
                printf("Invalid choice. Try again.\n");
        }
    }
    return 0;
}