#include "queue.h"

Node* create_queue(double val) {
    Node* head = new Node;
    head -> value = val;
    head -> next = nullptr;
    return head;
}

void enqueue(Node* head, double val) {
    Node* newNode = new Node;
    newNode -> value = val;
    newNode -> next = nullptr;

    Node* temp = head;
    while (temp -> next != nullptr) {
        temp = temp -> next;
    }
    temp -> next = newNode;
}

Node* dequeue(Node** head) {
    if (*head == nullptr) {
        cout << "Queue is empty, cannot dequeue." << endl;
        return nullptr;
    }

    Node* temp = *head;
    *head = (*head) -> next;
    temp -> next = nullptr;
    return temp;
}

void print_queue(Node* head) {
    if (head == nullptr) {
        cout << "Queue is empty." << endl;
        return;
    }

    int pos = 0;
    Node* temp = head;
    while (temp != nullptr) {
        cout << pos << ": " << temp -> value << endl;
        temp = temp -> next;
        pos++;
    }
}

void delete_queue(Node** head) {
    Node* current = *head;
    while (current != nullptr) {
        Node* nextNode = current -> next;
        delete current;
        current = nextNode;
    }
    *head = nullptr;
}