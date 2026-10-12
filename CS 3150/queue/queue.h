#ifndef QUEUE_H
#define QUEUE_H

#include <iostream>
using namespace std;

struct Node {
    double value;
    Node* next;
};

Node* create_queue(double val);
void enqueue(Node* head, double val);
Node* dequeue(Node** head);
void print_queue(Node* head);
void delete_queue(Node** head);

#endif