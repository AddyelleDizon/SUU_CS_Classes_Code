#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* createList();
void printList(Node* head);
void appendItem(Node** head, int value);
void changeValue(Node* head, int index, int value);
void deleteItem(Node** head, int index);
void insertItem(Node** head, int index, int value);

#endif