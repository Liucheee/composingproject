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















