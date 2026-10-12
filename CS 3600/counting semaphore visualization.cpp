#include <iostream>
#include <thread>
#include <mutex>
#include <chrono>

std::mutex mtx; // Mutex to protect shared resources
int shared_var = 0; // Shared variable
const int NUM_THREADS = 5; // Number of threads
int semaphore = 1; // Binary semaphore

// Down operation (wait)
void P() {
    while (semaphore <= 0) {} // Wait until semaphore is available
    semaphore--; // Decrease semaphore value
}

// Up operation (signal)
void V() {
    semaphore++; // Increase semaphore value
}

// Function executed by each thread
void threadFunc(int id) {
    P(); // Wait until semaphore is available

    // Critical section
    mtx.lock(); // Lock the mutex before accessing shared resource
    std::cout << "Thread " << id << " is in critical section." << std::endl;
    shared_var++; // Access the shared variable
    std::this_thread::sleep_for(std::chrono::milliseconds(100)); // Simulate some work
    std::cout << "Thread " << id << " updated shared variable to: " << shared_var << std::endl;
    mtx.unlock(); // Unlock the mutex after accessing shared resource

    V(); // Release semaphore
}

int main() {
    std::thread threads[NUM_THREADS];

    // Create threads
    for (int i = 0; i < NUM_THREADS; ++i) {
        threads[i] = std::thread(threadFunc, i);
    }

    // Join threads
    for (int i = 0; i < NUM_THREADS; ++i) {
        threads[i].join();
    }

    return 0;
}