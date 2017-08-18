
# Edit these according to your environment
COMPILER=g++-7       # icpc or g++
VERSION=-std=c++11 # -std=c++11 or -std=gnu++11
OPENMP=-fopenmp    # -qopenmp or -fopenmp

RPATH=-Wl,-rpath,${CONDA_PREFIX}/lib

a1: assignment1.cc timer.cc 
	$(COMPILER) $(VERSION) $(OPENMP) $(RPATH) assignment1.cc timer.cc -o a1

a2: assignment2.cc timer.cc 
	$(COMPILER) $(VERSION) $(OPENMP) $(RPATH) assignment2.cc timer.cc -o a2

a3: assignment3.cc timer.cc 
	$(COMPILER) $(VERSION) $(OPENMP) $(RPATH) assignment3.cc timer.cc -o a3

a4: assignment4.cc timer.cc
	$(COMPILER) $(VERSION) $(OPENMP) $(RPATH) assignment4.cc timer.cc -o a4 

a5: assignment5.cc timer.cc
	$(COMPILER) $(VERSION) $(OPENMP) $(RPATH) assignment5.cc timer.cc -o a5

clean:
	rm -f *.o a1 a2 a3 a4 a5

.PHONY: clean
