# CS2-Ermitanio-DenzelAldrich

# Electricity Bill Calculator
## Description
This program calculates the electricity consumption of the user from the previous reading to the current reading.

## Version 1 - Original code without input validation
- Input: Accepts a user's name and the previous and current meter reading.
- Process: Calculates the difference of the current and the previous reading and multiplies it by a fixed rate. 
- Output: The difference of the two readings and the total bill.
- Does not include input validation.

## Version 2 - Updated code with input validation
- Input 1: Accepts a user's name.
    - Validation: Checks for the presence of an input and requires the user to input if there is none.
- Input 2: Accepts the user's previous meter reading.
    - Validation: Checks if the reading is at least zero, and requires the user to input another value if it is lower.
- Input 3: Accepts the user's current meter reading.
    - Validation: Checks if the reading is at least the value of the previous reading, and requires the user to input another value if it is lower.
- Process: Calculates the difference of the current and the previous reading and multiplies it by a fixed rate. 
- Output: The difference of the two readings and the total bill.
- Now includes input validation.
