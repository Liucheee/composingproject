###1.5


***Control***
-

- Expressive power of the function that we can define is limited
- Statement is different from expression 
- They don't have a value 
- The control statement determines what the interpreter does next.

###1.5.1


***Statements***
-

- Contains expressions as components 
- Statements are executed rather than being just evaluated
- Statements describe change while execution applies the named change
- Expressions executed as statements are evaluated but the values are discarded.
- Pure functions have no effect but non-pure function can cause effects as consequence of function application
- Python interpreter's job is to execute programs, composed of statements
- Statements govern relationship between different expressions
- 

###1.5.2

***Compound Statements***
-

- Python is a sequence of statements 
- Header with indented statements is a clause
- Compound statements have one or more clauses

``` 
<header>
    <Statement>
    <Statement>
    ...
<seperating header>
    <Statement>
    <Statement>
    ...
...
```

- Simple statements = Expression,return and assignment statements 
- Compound statement = Def statements because there is a clause. Def statements acts as a header.
- Special rules for headers, dictate when and if they are executed. 
- Specialised evaluation rules dictate when and if the statements are executed
- Execution works via the first statement executing and then the following statements.
- As a result some later statements may not be reached because of redirect control which would mean they won't execute.

####Practical note

- Use the same amount of spaces when indenting otherwise python will throw error messages. 

###1.5.3

***Defining Functions II: Local Assignment***
-

- Originally, we stated that the body of a user-defined
- Functions can define a sequence of operations that extend a single expression
- When User-defined functions are applied, a local frame is created by calling that function
- A return redirects control: Process of function terminates whenever the first return is executed and that value is returned
- Assignment statement can appear within a function body

``` 
def percent_difference(x, y):
    difference = abs(x-y)
    return 100 * difference / x
result = percent_difference(40, 50)

```

- Effect of an Assignment statement is to bind name to value in the first frame
- Assignment statements within a function body cannot affect the global frame
- Functions can only manipulate their local is critical to creating modular programs
- Modular programs can be better to simplify expressions.

E.g. 
``` 
>>> def percent_difference(x, y):
        return 100 * abs(x-y) / x
>>> percent_difference(40, 50)
25.0
```
- Local Assignment increase expressive power of function definitions 

###1.5.4

***Conditional Statements***
-

- Absolute values cna be computed with "abs(x)"
- Conditional statements cna be used to manually implement this
- E.g. Return a certain number if positive or another value if negative


**Conditional Statements:** A series of headers and suites: a required if clause, an optional Sequence of elif clauses, and finally an optional else clause:

```
if <expression>:
    <suite>
elif <expression>:
    <suite>
else:
    <suite>
```  

- Conditional statements are considered in order.
- Evaluate the header expression
- If true then execute the suite otherwise skip over the subsequent clauses 
- if the else clause is reached (if and elif expression evaluate to false) then it is executed.

***Boolean contexts***
- The expression inside the header statements of conditional blocks are boolean contexts.
- This truth value matters to control flow otherwise those values aren't assigned or returned.

***Boolean Values***
- Boolean values can be true or false
- built in operations can return these true or false values
- Greater or equal to value can also return these values

***Boolean operators***
``` 
True and False
    False
True or False
    True
not False
    True
```

- Logical expressions have corresponding evaluation procedures
- Short-circuiting: This exploits the fact that the truth value of a logical expression without evaluating all of its subexpressions

<"left"> ***and*** <"right">
1) Evaluate the subexpression <"left">
2) If result is a false value v, then the expression evaluates to v
3) Otherwise, the expression evaluates to the value of the subexpression<"right"> 

<"left"> ***or*** <"right">
1) Evaluate the subexpression<"left">
2) If the result is a true value, then the expression evaluates to v
3) Otherwise, the expression evaluates to the value of the subexpression<"right"> 

***not*** <"exp">
1) Evaluate <"exp">; The value is true uf the result is a false value and false otherwise

- These values,rules and operators provide us with a way to combine the results of comparisons.
- Functions that perform comparisons and return boolean values typically begin with "is" not followed by an underscore(E.g. isfinite,isdigit)

###1.5.5

***Iteration***
-

- Iterative Control statements can be used to express repetition of the same statements

E.g. fibonacci sequence 
- This is constructed via repeatedly applying the sum of previous 2 values rule
- A While statement can be used to enumerate N Fibonacci numbers
- In the example the binding statement of previous and current values works because the right-hand side of the = sign is evaluated before the left 

- While clauses contain header expression followed by suites:
```
while<expression>:
    <suite>
```
- To prevent an infinite loop the while loop should change some binding in each pass
- <"control"> + C to force python to stop looping

###1.5.5

***Testing***
- 

- Testing is to ensure that the behaviour matches the expectation

***Assertions***
- "Assert" statements are used to verify the expected outcome 
- The expression displays a quoted line of text if the outcome is determined to be false boolean value

``` 
assert <statement>, 'printed if statement is false'
```
- There is no statement printed if the statement returns a true value
- Test are normally written in the same file or a neighbouring file with the suffix _test.py
- Generally the tests would have several arguments including extreme test cases

***Doctests***
- First lines of docstrings should contain a one liner describing the function followed by a blank line
- Detailed description of arguments and behaviour may follow.
- The doctest module can be used to verify an interaction in the global environment
``` 
>>>from doctest import testmod
>>>testmod()
Testresults(failed=0, attmped = 2) 
```

- Verifying doctest insertions for only a single function uses the "run_docstring_examples"
- Its first argument is the function to test 
- The second should be the result of the expression globals() which is a built-in function that returns the global environment
- The third argument is true to indicate that we would like a catalog of all tests run
- A mismatch in result and expected result will report this problem as a test failure.
- All doctests in a file can be run by starting python with doctest command line
``` 
python3 -m doctest <python_source_file> 
```
- It is good practice writing in testing after implementing new functions.





















