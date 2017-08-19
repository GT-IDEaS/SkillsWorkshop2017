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

        int thread_id = omp_get_thread_num();
        printf("Hello World! ~ from thread %d\n", thread_id); 
	 /* Only master thread does this */
		if (thread_id == 0) 
		{
			printf("I am the main thread. Number of threads = %d\n", nthreads);
		}
    }
	
	printf("Now in order using barrier\n");
	
	//run the loop n times. Each time it must be done before the next loop can run (a barrier)
	for (int i=0; i<nthreads; i++)
	{
		#pragma omp parallel num_threads(nthreads)
		{
			int thread_id = omp_get_thread_num();
			if (thread_id == i) 
			{
				printf("Hello World! ~ from thread %d\n", thread_id); 
			}
			
		}
	}

}
