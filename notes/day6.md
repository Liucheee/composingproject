1.6
- 

- Working in terms of high level functions are crucial in order to act as a higher level language
- General patterns can be made into concepts which can accept other functions as arguments or return functions as values

###1.6.1

***Functions as arguments***
- 

**Summation Example**
- The example creates the function summation which can be shared
- The "combination example" works via 2 components
- First being the summation of the values
- Second being the special transformation to the values

**Identity Example**
- The identity function can be used to return its argument
- This example highlights how additional transformations could be added in

**Direct Example**
- Function can be used directly without defining another function
- Prebuilt functions can be utilised 

**Pi Example**
- Summation can be used as a white label solution 

###1.6.2

***Functions as General Methods***
- 

- Golden ratio  is often called phi which is a number which is near 1.6
- Iterative improvement algorithm begins with a guess of an equation 
- It uses the update function to improve that guess and a close comparison check to whether the current guess is "close enough" is considered correct.

**Improve function**
- This is a repetitive refinement function
- Golden ratio  properties include being able to be computed by repeatedly summing the inverse of any positive number with 1
- It is also 1 less than its square

**Approx_eq**
- It is meant to return true if arguments are approximately equal to each other
- This works by comparing the absolute values of the difference with a small tolerance value 

**Improve**
- Finally, calling improve with the 2 arguments above golden_update and square_close_to_successor computes a finite approximation

**Overall**
- This works by first a local frame being made for improve with update,close and guess
- Inside improve the name close is bound to square_close_to_successor which calls the initial value of guess
- Naming and functions allows us to remove a large amount of complexity

**Maths example**
- The test can be generated for this to check correctness
- Golden ratio can provide a test because it has an exact closed-form solution which can be used to compare
- If no output then that means the asset statement executed successfully

###1.6.3

***Defining functions 3: Nested Definitions***
- 

- Nested functions solve the problem of global functions becoming cluttered with smaller functions and the constraint of particular function signatures

**2 arguments**
- This calculation for square roots wouldn't work with the improve function from 1.6.2 because it has 2 arguments
- This issue can be resolved by simply nesting one function definition inside the body of the other
- local def statements only affect the current local frame
- These functions are only in scope while sqrt is being evaluated
- They don't get evaluated until sqrt is called

**Lexical scope**



















