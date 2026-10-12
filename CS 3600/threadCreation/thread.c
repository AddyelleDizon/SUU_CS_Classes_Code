#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define NUM_THREADS 10

pthread_t threads[NUM_THREADS];

void* thread_function(void* arg)
{
    int id = *((int*)arg);

    printf("Thread %d started (pthread id: %lu)\n",
           id, pthread_self());

    while (1)
    {
        printf("Thread %d working...\n", id);
        sleep(1);

        pthread_testcancel();
    }

    return NULL;
}

int main()
{
    int ids[NUM_THREADS];

    printf("Creating threads...\n\n");

    for (int i = 0; i < NUM_THREADS; i++)
    {
        ids[i] = i + 1;

        if (pthread_create(&threads[i], NULL,
                           thread_function, &ids[i]) != 0)
        {
            perror("pthread_create failed");
            exit(1);
        }

        printf("Created thread %d\n", ids[i]);
        sleep(3);
    }

    printf("\nAll pthreads created:\n");
    for (int i = 0; i < NUM_THREADS; i++)
    {
        printf("Thread %d -> pthread id %lu\n",
               i + 1, threads[i]);
    }

    printf("\nJoining first 6 threads...\n");

    for (int i = 0; i < 6; i++)
    {
        pthread_cancel(threads[i]); 
        pthread_join(threads[i], NULL);
        printf("Thread %d joined successfully\n", i + 1);
    }

    printf("\nForcefully destroying last 4 threads...\n");

    for (int i = 6; i < NUM_THREADS; i++)
    {
        pthread_cancel(threads[i]);
        printf("Thread %d cancelled\n", i + 1);
    }

    printf("\nCleaning up remaining threads...\n");

    for (int i = 6; i < NUM_THREADS; i++)
    {
        pthread_join(threads[i], NULL);
    }

    printf("\nProgram finished.\n");
    return 0;
}