Week 05: High Performance Computing
==================

This week, we delve into parallel computing.  In our project, we will investigate
 the shared memory programming model using OpenMP (Open Multi-Processing).
  OpenMP is an API that supports shared memory multiprocessing programming in
 C, C++, and Fortran. Learn more at http://www.openmp.org/.

For the hands-on session, we have provided several assignments in C++ found in
GT-IDEaS/SkillsWorkshop2017/Week05/assignments/.  We attempt to decouple the
 difficulty of simultaneously learning C++ and OpenMP by providing nearly
 completed codes and only requiring simple tasks involving OpenMP.  These
 assignments are tailored to touch upon some fundamental concepts and difficulties
 that OpenMP programmers deal with.  These topics are generally summarized as:

1.  Assignment 1 - Hello World
2.  Assignment 2 - Speedups
3.  Assignment 3 - Workloads and Scheduling
4.  Assignment 4 - Resource Sharing
5.  Assignment 5 - Challenge Problem

Before we begin, some initial setup is required.  We need to ensure everyone
 has a c++ compiler.  Since compatability between Mac OS and OpenMP is non-trivial,
 we have designed a work-around.  First, execute the following from the 
 command line:

```
conda create -n ideas gcc-5-mp -c psi4
```

This will create a python envoriment using conda, which you should have installed in Week 1.
  Importantly, this environment contains a GNU g++ compiler. To activate the environment,
 execute the following:

```
source activate ideas
```

Now, everyone should have access to the g++ compiler.  Within the `Week05/assignments/` directory, go into the `Makefile` and
 edit the `COMPILER` option accordingly.  You should have:

```
COMPILER=g++
```

If you already had access to Intel compilers and want to use `icpc`, feel free.  The three
 options in `Makefile` should be completed as:

```
COMPILER=g++      
VERSION=-std=gnu++11
OPENMP=-fopenmp   
```
OR
```
COMPILER=icpc     
VERSION=-std=c++11
OPENMP=-qopenmp   
```

Now that the Makefile is configured correclty, you can execute the following on the command line:

`make a1`

Doing so compiles the `assignment1.cc` file.  To run the executable, execute:

`./a1`

The same process is done for all other assignments.
Now, we will discuss each assignment and how to complete it.
Assignment submission will be done entirely through Github.  Create a file, `writeup.pdf`, which will contain
all necessary workup.  Each assignment should correspond to a section in your writeup.  
To complete the project, you will push your `writeup.pdf` file and all code alterations. 

1.  Assignment 1 is an introductory program containing "Hello World" for OpenMP.  The program is already
 completed.  Compile and run the executable.  Notice the outputs.  Is there a particular order in which threads print?  
 Try to change `assignment1.cc` so that only one master thread prints to the console.
Challenge: Use the `omp barrier` pragma to have each thread print in order, from lowest thread number to highest.
 Comment on your strategy in your writeup.

2.  Assignment 2 contains a basic loop which can be parallelized.  First, compile and execute the program.
  Notice the outputs.  Now, insert a pragma in `assignment2.cc` to parallelize the loop.  This should only require one
 line of code.  Recompile and run the program.  How well is the loop parallelized?  Now, tweak the `ITERATIONS`
 and `WORK_TIME` variables at the top of `assignment2.cc` and re-evaluate the performance.  You should be able to get 
 very good speedups!  Briefly discuss your analysis and include a speedup plot of this program in your writeup. 

3.  Assignment 3 is nearly identical to Assignment 2, but the work of the loop is severely non-uniform.
  First, go into `assignment3.cc` and try to understand how the work is changing for each iteration of the loop.
  After, parallelize the loop, compile, and run the program.  How does the output compare to what was found previously in Assignment 2?
  The resulting speedups should be worse!
  Add a `schedule()` clause to the loop and see if you can acquire better speedups.
 Plot your speedups under some different scheduling assignments and include it in your writeup.  Comment on performance.

4.  Assignment 4 contains a parallel prefix sum evaluator.  First, compile and run the program.  Evaluate the outputs.
  The speedups should get worse as more threads are used.  After you understand why this is, edit the code and fix the issue.
  This may take a few lines of code.  After, recompile and run the program.  You should be able to acquire some good speedups.
  Depending on your machine, you may have to crank up the `N` variable quite a bit.  Unfortunately, after about 10,000, you will likely get
 an integer overflow.  Programming in C++ does not come with the luxury of unlimited precision, so we are limited to what can be 
 stored in an `unsigned long long int` type.  You will probably have to go well past this limit to start to see good speedups.
  If necessary, prevent overflow by changing the summation `sum == i` to either `sum += 1` or `sum += 0`.  Briefly discuss your
 strategy and analysis in the writeup. 

5.  Assignment 5 contains the skeleton for a code which collapses an N x N matrix to an N vector by summing accross one dimension.  Using what
 has been previously covered, implement the remaining code.  To check for correctness, the initial matrix contains all ones.  Discuss
 briefly your strategy and push your solution.

