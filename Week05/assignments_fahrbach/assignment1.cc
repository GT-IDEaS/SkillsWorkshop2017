// Assignment 1 - Hello World!
// IDEaS Workshop Week 5: HPC

#include <stdlib.h>
#include <stdio.h>
#include <omp.h>

int main() 
{
    // OpenMP function 
    int nthreads = omp_get_max_threads();

    // OpenMP pragma and clause
    #pragma omp parallel num_threads(nthreads)
    {
        // Part 1: Let thread 0 be the master thread.
        int thread_id = omp_get_thread_num();
        if (thread_id == 0) {
          printf("Hello World! ~ from master thread %d\n", omp_get_thread_num()); 
        }
        
        // Challenge: Print threads in order.
        #pragma omp for ordered
        for (int i = 0; i < nthreads; i++) {
          #pragma omp ordered
          printf("Hello World! ~ from thread %d\n", omp_get_thread_num());
        }

    }
}
