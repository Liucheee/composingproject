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
- Functions can define a sequence of operations that extend 





















