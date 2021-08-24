###1.3


***Defining new functions***
-

- Function definitions consists of "def" statement which has a "name"
- Afterwards a return statement, 
- 

``` 
def <name>(<formal parameters>):
    return <return expression>
```

- Second line indented (4 spaces)
- Return expression isn't evaluated right away.
- Stored as part of a newly defined function and evaluated only when it is applied


- Pre-defined functions can be used as a building block in defining other functions
- User-defined function are used the same way as the built-in functions.

###1.3.1

***Environments***
-

- "Def" binds a user-defined function created by the definition
- Every function is structured as: 
``` 
- func/function name/(formal paramters)
  def /square       / (x)

```
- Name of functions is repeated twice, once in the frame and once in the function itself
- Name appearing within the function is the intrinsic name
- Name in frame is the bound name
- Difference is the function itself can only have 1 intrinsic name

- Functions cannot be used as an operator once it has been bound to integers

####function signatures 

- function signatures are the brackets at the end which determines how many arguments a function can take
- E.g in the square example it can only take 1 argument being (x)

- other functions such as "max" can take an arbitrary number of arguments.
- This is because all built-in functions will be rendered as <name>(...)
- because they were never explicitly defined.

###1.3.2

***Calling user - defined Functions***

Process for applying user-defined functions to some arguments
- Bind arguments to the names of the functions formal parameters in a new local frame first
- Execute the body of the function in the environment that starts with this frame


- Environment where the body is evaluated has 2 frames
- Frame 1:
- Outer file (day 3.py)

- Frame 2:
- Global frame containing everything  (Main methods)
  
- Frame 3:
- Inside the function (inside the function definitions)

###Refer to the day3.py file for example 

- Within this example there are 3 frames.

####Name Evaluation
- A name evaluates to the value bound to that name in the earliest frame of the current environment in which that name is found



###1.3.3
***Calling user-defined function***
``` 
from operator import add, mul

def square(x):
    return mul(x, x)
    
def sum_squares(x, y):
    return add(square(x), square(y))

result = sum_squares(5, 12)

```
- Runs through the global frame first 
- binds sum_squares to a user-defined function in global frame
- Binds 5 to x and 12 to y
- *refer to the evaluation tree diagram*
- evaluates the square(x), square(y)
- carry those results back to sum_square and then result


- names are bound to value, which are spread across various different environments
- New local frame is introduced every time a function is called, 
- Even if the function is called twice
- This is to ensure that the names resolve to the correct value at the appropriate time during execution
- This can be seen through x where it has a different values in all 3 frames
- Local frames keep the names separate



###1.3.4
***Local names***
- Functions implementation shouldn't affect the behaviour 
- This principle, that the meaning of a function should be independent of the parameter names
- Parameter names of functions mus remain local to the body of that function
- If a name isn't accessible it is out of scope.


###1.3.5
***Choosing Names***

- Formal parameter names DO matter
- Well-chosen names are key for readability and essential for interpretability

####Rules

- Function names are lowercase, words are separated by underscores. Descriptive names are encouraged
- Function names evoke operations applied to arguments by the interpreter(e.g. print,add, square)
- Parameter names are lowercase, with words separated by underscores. Single word names better
- Parameter names should evoke the role of the parameter in the function, not just the kind of argument that is allowed 
- Single letter parameter names are acceptable when their role is obvious, but avoid 
  - "l"(lowercase ell)
  - "O"(capital oh)
  - "I"(capital i)
- This is to avoid confusion with numerals

- Exceptions to these guidelines exist

###1.3.6
***Functions as Abstractions***

- Functions can be an abstract of another function.
- E.g. Sum_square can be written first without concerning ourselves with how to square a number. 
- Function definition should be able to suppress details
- Users of function may not have written the function themselves, making it a "black box"
- E.g. Python Library

######Aspects of a functional abstraction

- 3 core components of functional abstraction (E.g. Square functions used for sum_square)
  - Domain(set of arguments it can take): is any single real number
  - Range(set of values it can return): is any non-negative real number
  - intent(: is that the output is the square of the input 

###1.3.7
***Operators***

- Mathematical operators provided our first example of a method of combination
- Python expressions, with infix operators each have their own evaluation procedures, but it can be thought of as a short-hand call expression
``` 
2+3  
>>> 5
```
could be thought of 
``` 
add(2,3)
>> 5
```

Another example: 
``` 
2+3*4+5 
>>> 19
```
equals
``` 
add(add(2, mul(3,4)),5)
>>> 19 
```

- For division, Python has 2 infix operators:
  - "/" : normal division
  - Shorthand version
    - truediv(x,y)
``` 
  > 5/4
1.25
  > 8/4
2.0
  > truediv(5/4)
1.25
  
```
  - "//": rounds down the to an integer:
  - Shorthand  version 
    - floordiv(x,y))
``` 
 > 5 / / 4
1
 > -5 / /4
-2
  > floordiv(5,4)
1
```

Two operators are shorthanded for 
- truediv











