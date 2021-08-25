###1.4


***Designing functions***
- 
####Qualities of good functions 

- Functions have exactly one job. Job should be identifiable (short + characterized in a single line )
- Don't repeat yourself (DRY) Principle states multiple fragments should not describe redundant logic. If you are repeating code blocks then it is an opportunity for functional abstraction
- Functions should be defined generally. 

###1.4.1

***Documentation***
-

- Function definition will include documentation (docstring).
- This is indented along with function body and triple quoted.

```` 
>>> def pressure(v, t, n):
        """Compute the pressure in pascals of an ideal gas.

        Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

        v -- volume of gas, in cubic meters
        t -- absolute temperature in degrees kelvin
        n -- particles of gas
        """
        k = 1.38e-23  # Boltzmann's constant
        return n * k * t / v
````

- Code is written once but read many times, Python docs include docstring guidelines that 

####Comments

- Comments in python are attached by including a "#" symbol 


###1.4.2

***Default Argument Values***
- 

- Consequence of general functions is the additional arguments
- Default values of arguments can be provided but is optional
- If values are not provided then it is bound to formal parameter name

``` 
>>> def pressure(v, t, n=6.022e23):
        """Compute the pressure in pascals of an ideal gas.

        v -- volume of gas, in cubic meters
        t -- absolute temperature in degrees kelvin
        n -- particles of gas (default: one mole)
        """
        k = 1.38e-23  # Boltzmann's constant
        return n * k * t / v

```
in practice:

``` 
>>> pressure(1, 273.15)
2269.974834
>>> pressure(1, 273.15, 3 * 6.022e23)
6809.924502

```
- the "=" symbol has 2 different meaning. Depending on context
  - In the def statement it indicates a default value when pressure is used
  - It is used as an assignment statement to bind K in the body 

- In the pressure function 3 are defined but only 2 are provided in first call
- This is an example of when the default value would be used
- However, if a third is provided then the default is ignored

#### Guideline Convention 

- Data values used in the function body should be expressed as default values to named arguments 
- Fundamental constants can be bound in the function body or in the global frame






