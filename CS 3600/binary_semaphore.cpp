#include <iostream>
#include <queue>
#include <unistd.h>
#include <signal.h> // For signal handling

struct Semaphore {
    int value;
    std::queue<int> q;
};

void P(Semaphore &s) {
    if (s.value == 1) {
        s.value = 0;
    } else {
        // Add the process to the waiting queue
        s.q.push(getpid());
        sleep(1); // Sleep for a short duration
    }
}

void V(Semaphore &s) {
    if (s.q.empty()) {
        s.value = 1;
    } else {
        // Select a process from the waiting queue
        int pid = s.q.front();
        s.q.pop();
        kill(pid, SIGCONT); // Wake up the process using kill() and SIGCONT
    }
}

int main() {
    Semaphore sem;
    sem.value = 1;

    P(sem); // Process will acquire the semaphore
    std::cout << "Process acquired the semaphore." << std::endl;

    V(sem); // Release the semaphore

    return 0;
}
