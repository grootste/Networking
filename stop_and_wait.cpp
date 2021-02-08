#include <iostream>
#include <chrono>
using namespace std;
using namespace chrono;

#include <stdio.h>
#include <time.h>
 
void loop(void) {
    time_t start, end;
    double elapsed;
 
    time(&start);  /* start the timer */
 
    do {
        time(&end);
 
        elapsed = difftime(end, start);
        /* For most data types one could simply use
            elapsed = end - start;
            but for time_t one needs to use difftime(). */
 
        printf("Time elapsed: &#37;f\n", elapsed);
    } while(elapsed < 10);  /* run for ten seconds */
}
