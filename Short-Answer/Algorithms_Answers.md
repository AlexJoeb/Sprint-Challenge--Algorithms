#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) I believe the first exercise is O(n^3). The functions appears to scale to the power of 3 based on n; because of the n * n * n.

b) O(2^n) - because there is two for loops that depend on the size of n.


c) O(n) - because the single instance of recursion acts as a single for loop.

## Exercise II
define minFloorBeforeBreak, takes `n` as number of stories in building:
    initalize at 0 and store `current_floor` to keep track of current floor
    run a loop while current_floor is less than or equal to n:
        check to see if egg would break
        if egg breaks, return current_floor as `f`
        else increment current_floor by one and go to top of loop to check next floor
