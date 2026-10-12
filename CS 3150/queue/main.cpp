#include "queue.h"
#include "queue.cpp"

int main() {
    Node* head = nullptr;
    int choice;
    bool valid = 0;

    while (!valid) {
        cout << "1. Create Queue\n";
        cout << "2. Enqueue\n";
        cout << "3. Dequeue\n";
        cout << "4. Print Queue\n";
        cout << "5. Quit\n";
        cout << "Enter your choice: ";

        cin >> choice;

        if (cin.fail()) {
            cin.clear();
            cout << "Invalid input. Please enter a number between 1 and 5.\n";
            continue;
        }

        switch (choice) {
        case 1: {
            if (head != nullptr) {
                cout << "Queue already exists. Delete it first to create a new one.\n";
                continue;
            }
            double val;
            cout << "Enter the first value for the queue: ";
            cin >> val;
            head = create_queue(val);
            cout << "Queue created successfully.\n";
            continue;
        }

        case 2: {
            if (head == nullptr) {
                cout << "Queue not created yet. Please create it first.\n";
                continue;
            }
            double val;
            cout << "Enter value to enqueue: ";
            cin >> val;
            enqueue(head, val);
            cout << "Value enqueued successfully.\n";
            continue;
        }

        case 3: {
            if (head == nullptr) {
                cout << "Queue is empty.\n";
            }
            Node* removed = dequeue(&head);
            if (removed != nullptr) {
                cout << "Dequeued value: " << removed->value << endl;
                delete removed;
            }
            continue;
        }

        case 4:
            print_queue(head);
            continue;

        case 5:
            valid = 1;
            delete_queue(&head);
            cout << "Exiting program. Memory freed.\n";
            return 1;

        default:
            cout << "Invalid option. Try again.\n";
        }
    }

    return 0;
}