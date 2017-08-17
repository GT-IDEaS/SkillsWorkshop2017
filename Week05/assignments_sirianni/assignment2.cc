// Assignment 2 - Basic for loop parallelization
// IDEaS Workshop Week 5: HPC

#include <stdlib.h>
#include <stdio.h>
#include <omp.h>
#include <unistd.h>
#include "timer.h"

#define ITERATIONS 100
#define WORK_TIME 1000

int main() 
{
    // setup ~
    int max_threads = omp_get_max_threads();
    double times[max_threads];

    for(int m = 0; m < max_threads; m++){
        
        // get nthreads ~ use this in your pragma!
        int nthreads = m + 1;
        
        double t0 = time_in_seconds();

        // ==> Drop a pragma on the loop below! <== //    
        #pragma omp parallel for num_threads(nthreads)
        for(int i = 0; i < ITERATIONS; i++){
            // emulate work 
            usleep(WORK_TIME);
        }
        
        // ==> Drop a pragma on the loop above! <== //    

        double t1 = time_in_seconds();
        times[m] = t1 - t0;    
        printf("(%d): Time: %f, Speedup: %f\n", m + 1, times[m], 
            times[0]/times[m]);
    }
    
}
