#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n). Having the while  loop in the function makes it atleast O(n). The part where it says `n * n * n` can be done as a constant time operation and `n` never increased during the loop.

b) O(nlogn). There is two for-loops that depend on the size of n. The first for-loop iterates from 0 to `n`, this makes the function at least O(n). Inside that loop, there is another loop that iterates from `j` to `n` with each pass.


c) O(n). This is a simple case of recursion. The single call for recursion acts as a single for loop inside of an iterative function.

## Exercise II
* My approach to this would be to use a binary method of finding the correct floor. Using a binary method would help minimize the amount of eggs needed to be dropped.
* Time complexity is O(logn) because I am using a binary method to speed up the operation significantly.
* Solution:
    I would define a function that takes in `f` the amount of floors. I would store the current high (default to `f`) and low (default to 1). Do (high + low) / 2 to find the middle. Check to see if it breaks.

    If it doesn't break, I would move the low pointer to the middle floor and then repeat the process.

    If it does break, I would move the high pointer to middle floor and then repeat the process.

    Rinse and repeat until the lowest floor is found without breaking.  