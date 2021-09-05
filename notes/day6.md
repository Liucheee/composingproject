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
- Locally defined functions have access to name bindings in the scope they are defined.
- Sharing names among nested definitions is called lexical scoping 
- Inner functions have access to the names in environment where they are defined(not where they are called)
- Each user-defined function has a parent environment: The one where it was defined
- When they are called, its local frame extends past its parent's environment 



**Sqrt**
- Parent of a function value is the first frame of the environment where it was defined
- Functions without parent annotations were defined in the global environment.
- User-defined functions create a frame which share the same parent as the function 

**Extended Environments**
- Arbitrarily long chain of frames which ends with global frame
- Longer chains can be made by calling functions that are defined in other functions and nested via def statements
- E.g. The Sqrt_update function has 3 frames (The one where it is defined, sqrt frame and the global)

**Benefits**
- Local function names don't interfere with names external functions because the name is bound to the current local frame where it was defined
- Local function can access the environment of the enclosing function because the body is evaluated in an enviroment that extends the evaluation enviroment which it was defined.

###1.6.4

***Functions as Returned Values***
- 

- Functions can be created so that the returned value is a function itself

**Example**
- The example shows the values for "f" and "g" are both resolved correctly with conflicting names present in the global frame 
- The results of square and successor are loaded via f and g into compose1


###1.6.5

***Example: Newton's Method***
- 

**Newton_update**
- Shows the computational process of following tangent to 0

**find_zero**
- This can be defined in terms of "newton_update" and "improve" and a comparison to see if near 0


**Computing Roots**
- This method can be used to compute roots of arbitrary degree n
- Second root of 64 is 8
- Third root of 64 is 4
- Sixth root of 64 is 2

- The approximation error can be reduced via changing the tolerance in approx_eq to be smaller
- It may not always converge
- The initial guess must be sufficiently close to the zero and several other conditions must be met


###1.6.6

***Currying***
- 

- Higher-order functions can convert a function that takes multiple arguments into chain of function that takes a single argument
- function f(x, y) can be defined into a single function g so that g(x)(y) is equivalent to f(x, y)
- g is a higher- order function that takes a single argument x and returns another function that takes in single argument y. This is called currying














