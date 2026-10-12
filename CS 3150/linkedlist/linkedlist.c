#include "linkedlist.h"

// take in nothing, return no value; 
// next ref set to NULL
Node* createList() {
    return NULL;
}

// take in list, an index value, a data value. 
// determine if node exists
// if no, print list empty
// if yes, set data of node -> data of input; head of list is index = 0
void changeValue(Node* head, int index, int value) {
    Node* current = head;
    int count = 0;

    while (current != NULL && count < index) {
        current = current -> next;
        count++;
    }

    if (current == NULL) {
        printf("Node at index %d does not exist.\n", index);
    } 
    
    else {
        current -> data = value;
    }
}

// iterate through list, printing each value nodes
void printList(Node* head) {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }

    Node* current = head;
    printf("List: ");
    while (current != NULL) {
        printf("%d ", current -> data);
        current = current -> next;
    }
    printf("\n");
}

// take in a list and int
// create and append a node to the end; set data to input
void appendItem(Node** head, int value) {
    Node* newNode = (Node*) malloc(sizeof(Node));
    newNode -> data = value;
    newNode -> next = NULL;

    if (*head == NULL) {
        *head = newNode;
        return;
    }

    Node* current = *head;
    while (current -> next != NULL) {
        current = current -> next;
    }
    current -> next = newNode;
}

// take in list and index, determine if exists
// if no, same as print list
// if yes, delete node, and update ref
void deleteItem(Node** head, int index) {
    if (*head == NULL) {
        printf("List is empty.\n");
        return;
    }

    Node* temp = *head;

    if (index == 0) {
        *head = temp -> next;
        free(temp);
        return;
    }

    Node* prev = NULL;
    int count = 0;

    while (temp != NULL && count < index) {
        prev = temp;
        temp = temp -> next;
        count++;
    }

    if (temp == NULL) {
        printf("Node at index %d does not exist.\n", index);
        return;
    }

    prev -> next = temp -> next;
    free(temp);
}

// take in index and list
// determine if index == valid (0 and -1 inclusive)
// if yes, insert data at specified index and shift indices down +1 node
void insertItem(Node** head, int index, int value) {
    if (index < 0) {
        printf("Invalid index.\n");
        return;
    }

    Node* newNode = (Node*) malloc(sizeof(Node));
    newNode -> data = value;

    if (index == 0) {
        newNode -> next = *head;
        *head = newNode;
        return;
    }

    Node* current = *head;
    int count = 0;

    while (current != NULL && count < index - 1) {
        current = current -> next;
        count++;
    }

    if (current == NULL) {
        printf("Index %d out of range.\n", index);
        free(newNode);
        return;
    }

    newNode -> next = current -> next;
    current -> next = newNode;
}