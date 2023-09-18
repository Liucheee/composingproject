###1.7

***Recursive functions***
- 


- Recursive functions are just if the body of the function calls the function itself either directly or indirectly


**Sum_digits Example**
- This example is both complete and correct despite the function calling itself within 
- This problem is broken down into 2 parts this is the first part where the sum is found and then afterwards the last digit would be added to the value.
- 

###1.7.1
***The Anatomy of Recursive Functions***
- 

- Basic pattern that can be seen is that they begin with a base case.
- The Base case is the conditional statement that defines what the behaviour of the functions are simplest to process
- In the example "sum_digits" the base case is the single-digit argument. That argument is constantly being returned.
- Base case is a Single-digit argument which we can return
- Recurisve functions can have multiple base cases


Difference 
Iterative
- Build upon the base case by mulitplying each term

Recursive
- Works by calcualting each case of n starting fromt he base case until 1 is reached. 


- Iterative version of facotrial also has 2 additonal names
- A local state must be maintained to hold the current values which have been processed and also the values which are yet to be processed. 


###1.7.2
*** Mutual Recursion***








