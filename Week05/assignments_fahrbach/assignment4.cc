// Assignment 4 - Resource sharing with prefix sum
// IDEaS Workshop Week 5: HPC

#include <stdlib.h>
#include <stdio.h>
#include <omp.h>
#include <unistd.h>
#include <vector>
#include <tuple>
#include <math.h>
#include "timer.h"

// N > max_threads
#define N 100000000

int main() 
{
    // setup ~
    int max_threads = omp_get_max_threads();
    double times[max_threads];
    
    for(int m = 0; m < max_threads; m++){
        
        // init sum 
        unsigned long long int sum = 0;
        
        int nthreads = m + 1;
        double t0 = time_in_seconds();

        // ==> Improve strategy below! <== //    
        
        // determine blocking
        std::vector<std::pair<size_t, size_t>> blocks;
        for(int i = 0, start = 1, size; i < nthreads; i++, start += size){
            size = ((N % nthreads) / (i + 1) ? ceil((double)N / nthreads) : 
                floor((double)N / nthreads)); 
            blocks.push_back(std::make_pair(start, start + size));
        }
        
        #pragma omp parallel num_threads(nthreads) 
        {
            // get block info
            int id = omp_get_thread_num();
            size_t start = std::get<0>(blocks[id]);
            size_t stop  = std::get<1>(blocks[id]);

            unsigned long long int tmp_sum = 0;
            for(int i = start; i < stop; i++){
                tmp_sum += 1;
            }
            #pragma omp atomic
            sum += tmp_sum;
        }        
    
        // ==> Improve strategy above! <== //    
        
        double t1 = time_in_seconds();
        times[m] = t1 - t0;    
        printf("(%d): Answer: %llu, Time: %f, Speedup: %f\n", m, sum, times[m], 
            times[0]/times[m]);
    }
}
