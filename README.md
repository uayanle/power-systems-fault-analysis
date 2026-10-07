This is a python based electrical engineering project I built to explore power system fault analysis and protection while also devloping my python skills.

The whole idea behind this project was to model a simplified industrial power system and use python to help calculate system impedance, prospective fault current and fault level, then use the calculated fault current to select a suitable breaker. 

I wanted this project of mine to be more than just simply doing calculations into python so I also want to practice object-oriented porgramming, input validation, working with CSV data and more!




What the program calculates:

The program calculates the following:

-Transformer impedance
The transformer's percentage impedance is converted into an impedance in ohms on the system voltage side.

-Cable impedance
The cable impedance is calculated from:
Cable impedance = impedance per km × cable length

-Total system impedance
The transformer and cable impedances are combined to give the simplified fault-path impedance.

-Three-phase fault current
The prospective three-phase fault current is calculated using:
I₍f₎ = V / (√3 × Z₍total₎)

-Fault level
The fault level is calculated from the prospective fault current:
S₍fault₎ = √3 × V × I₍fault₎

-Circuit breaker selection
The calculated fault current is compared against a small CSV database of circuit breakers.

The program was designed in a way that it will select the smallest breaker rating that is greater than or equal to the calculated fault current. 




Python Implementation

I split the project into separate modules rather than putting everything into one file.

-calculations.py
Contains the electrical engineering calculations, including transformer impedance, cable impedance, fault current, fault level and voltage drop.

-components.py
Contains the classes used to represent the different parts of the system:
Transformer
Cable
PowerSystem

This was one of the parts of the project where I used object-oriented programming rather than keeping everything as separate variables.

-validations.py
Handles input validation and makes sure values such as transformer rating, voltage and cable length are positive valid numbers.

-protections.py
Loads the breaker data from the CSV file and selects a suitable breaker based on the calculated fault current.

-data/breakers.csv
Contains the breaker ratings and types used by the protection selection logic.





Limitations

This is an educational simplified model, rather than a complete industrial protection study.

The current version does not include things such as:

-Different fault types such as line-to-ground or line-to-line faults
-Detailed cable resistance and reactance
-X/R ratio
-Motor fault contribution
-Detailed protection coordination
-Protection relay settings
-Detailed breaker making and breaking duties
-Full network impedance modelling

The breaker selection is also simplified to demonstrate the basic principle of selecting a breaker with a rating greater than or equal to the prospective fault current.

These are areas I could build on in a future version.


