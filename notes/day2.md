***1.2.1***
- 
**Expressions**
E.g. Number

***1.2.2***
- 
**Call Expression**

- A Function with some arguments 

E.g. max function maps input to single out 

- The order of arguments in a call expression matter.
This is can be seen in the example of the power to.

```
pow(100, 2)
10000
pow(2, 100)
1267650600228229401496703205376
```

- Function notation has 3 principal advantages over mathematical
convention of infix notation
- No ambiguity can arise because function name before agument
``` 
- max(min(1, -2), min(pow(3, 5), -4))
- 2
```

- No limit to depth of nesting and the overall complexity 
but it should be understandable

***1.2.3***
- 

**Importing Libary Functions**
``` 
from "libary" import "module"
```
- Import libaries to utilise already prebuilt libary 
- Import statements designates module name and then lists the specific attributes wanted


``` 
from "operator" import "function"
```
- Operator functions cna be substituted for the symbols instead 
- E.g (Add vs +)


***1.2.4***
- 
**Names and the Environment**

- Binding statements assign values 
- name must be left and value must be right 
``` 
Name = Value 
```
- names can also be bound via the import statements
- " = " symbol is assignment operator
- Abstraction allows for us to refer to the result of operations
- Environments act as the memory for interpreters to store what values were bound to what names. 
- Names can also be bound to function. 
- Successive statements can rebind that name to a new value or function 
- Variable names can be bound to different value as a result of executing a program. 
- Assignment of multiple variables to multiple names is also possible by using the "," to separate them 

``` 
- name1, name2 = value1, value2
```
- Changing the value of 1 of those names would not affect the other names
- To update the value stored inside the name that would require another assignment statement  
- ALL expressions to the right are evaluated before any names are bound
- Swapping values bound to two names can be performed in single statement 
```
x,y = 3,4.5
y,x = x,y

x = 4.5
y = 3
```

***1.2.5***
- 
**Evaluating Nested Expressions**

1) Evaluate the operater and operand subexpression, then
2) Apply the funciton that is the vlaue of the operator subexpression tot he arguments that are the value of the operand subexpression 

- Evaluation for call expressions first must evaluate other expression.
- As a result the evaluation procedure is recursive in nature; which as a result includes the need to revoke the rule itself.

![](../../AppData/Local/Temp/expression_tree.png)
- 
- This example is an expression tree
- Evaluating the root expression requires first evaluating all the nodes first
- The nodes have 2 parts (The call expression and the result)
- This tree expression  allows us to visualise how the notes travel upwards and combine at higher levels
- Environment is crucial because it determines the meaning of symbols in expressions.


- Python is a language which executes rather than evaluates
- As a result they would often make a change rather than produce a value 


***1.2.6***
- 
**The Non-Pure Print Function**

Pure Function: No effects other than returning a value
![](../../AppData/Local/Temp/function_abs.png)
- Must return the same value when called twice within the same argument


Non-Pure Functions: In addition to returning a value they can generate side effects, which may result in changes to interpreter or computer
![](../../AppData/Local/Temp/function_print.png)
- Common side effect is additional outputs beyond just the value when using the print function 
- E.g. The Print function returns a special value of none. The value being outputted is a side effect of being called.
- If outputs are unexpected, draw an expression tree to clarify what may have caused it
- Because print returns none, it should not be used as the expression in an assignment statement

TLDR:
- Pure functions are restricted because cannot change behaviour but also have no side effects
- They are also more reliable in compound call expressions
- Non-pure expressions are less reliable and don't return useful results when used in operand expressions.
- Pure functions also easier to test because they have consistent results 