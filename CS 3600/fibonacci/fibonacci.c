#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {

    pid_t pid;
    int n;

    if (argc != 2) {
        fprintf(stderr, "Usage: %s <non-negative integer>\n", argv[0]);
        return 1;
    }

    n = atoi(argv[1]);

    if (n < 0) {
        fprintf(stderr, "Error: Please enter a non-negative integer.\n");
        return 1;
    }

    pid = fork();

    if (pid < 0) {
        perror("fork failed");
        return 1;
    }
    else if (pid == 0) {
        printf("Child process generating Fibonacci sequence:\n");

        long long a = 0, b = 1, next;

        for (int i = 0; i < n; i++) {
            if (i == 0)
                printf("%lld ", a);
            else if (i == 1)
                printf("%lld ", b);
            else {
                next = a + b;
                printf("%lld ", next);
                a = b;
                b = next;
            }
        }

        printf("\n");
        exit(0);
    }
    else {
        wait(NULL);
        printf("Parent process: Child completed.\n");
    }

    return 0;
}