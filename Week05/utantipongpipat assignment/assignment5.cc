// Assignment 5 - Summing across one dimension of a matrix
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
#define N 20000

// How much RAM?
#define MEMORY 50

int main() 
{
    // memory check
    if((double)(N / 1e9) * N * 4 > MEMORY * 0.8){
        printf("Not enough memory! ~~ ");
        printf("Needed: %6.3fGB\n", N / 1e9 * N * 4 / 0.8);
        exit(1);
    }

    // setup ~
    int max_threads = omp_get_max_threads();
    double times[max_threads];

    // NxN matrix to be collapsed to N vector (initialized to all 1s)
    std::vector<std::vector<int>> mat(N, std::vector<int>(N, 1));

    for(int m = 0; m < max_threads; m++){
        
        int nthreads = m + 1;
        double t0 = time_in_seconds();
    
        // write answer to this vec (initialized to all 0s)
        std::vector<int> vec(N, 0);

        // ==> implement solution below! <== //    
		/* //collapse solution
			#pragma omp parallel for num_threads(nthreads) collapse(2)
			for (int i=0; i<N; i++)
			{
				for (int j=0; j<N; j++)
				{
					vec[i] += mat[i][j];
				}
			}
		*/
		/* //outer loop only
			#pragma omp parallel for num_threads(nthreads)
			for (int i=0; i<N; i++)
			{
				for (int j=0; j<N; j++)
				{
					vec[i] += mat[i][j];
				}
			}
		*/
		//inner loop mainly
		#pragma omp parallel for num_threads(nthreads)
			for (int i=0; i<N; i++)
			{
				int mysum = 0;
				#pragma omp parallel for num_threads(nthreads) reduction(+:mysum)
				for (int j=0; j<N; j++)
				{
					mysum += mat[i][j];
				}
				vec[i] = mysum;
			}
 
        // ==> implement solution above! <== //    
        
        //check solution
        bool correct = 0;
        for(int i = 0; i < N; i++)
            correct = (vec[i] == N ? true : false);

        double t1 = time_in_seconds();
        times[m] = t1 - t0;    
        printf("(%d): Correct? %d, Time: %f, Speedup: %f\n", m, correct, times[m], 
            times[0]/times[m]);
    }
}
