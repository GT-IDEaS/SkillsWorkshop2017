#include "timer.h"
#include <stdlib.h>
#include <sys/time.h>

double time_in_seconds()
{
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return (double)tv.tv_sec + (double)tv.tv_usec / 1000000.0;
}
