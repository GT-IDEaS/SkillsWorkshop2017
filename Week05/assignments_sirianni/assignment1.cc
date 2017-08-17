// Assignment 1 - Hello World!
// IDEaS Workshop Week 5: HPC

//#include <cxxabi.h>
//#include <cstdio>
#include <stdlib.h>
#include <stdio.h>
//#include <iostream>
#include <omp.h>

int main() 
{
    // OpenMP function 
    int nthreads = omp_get_max_threads();

    // OpenMP pragma and clause
    #pragma omp parallel num_threads(nthreads)
    {

        int thread_id = omp_get_thread_num();
//        cout << "HI" << endl;
        printf("Hello World! ~ from thread %d\n", thread_id); 

    }

}
