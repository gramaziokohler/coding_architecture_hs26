## Assignment 00 (ungraded)

### Main Task

The task is to create a simple calculator program that can perform four basic arithmetic operations: addition, subtraction, multiplication, and division. The calculator could also handle division by zero and invalid operations.

The calculator should accept two input numbers and an arithmetic operation from a Grasshopper value list input component. ("addition", "subtraction", "multiplication", "division"). Based on the selected operation it should perform the correct arithmetic calculation. 

Optionally, introduce an error handling in case a number is divided by zero or if the operation name is invalid.

The starting point for your assignment is this [Grasshopper definition](00_calculator_hs26.gh)

### Challenge 01

Create more user-friendly messages, that not only display the result but also explain the operation being performed.

Create a custom print statement for each operation.

Example: addition: `"The result of [num_01] + [num_02] is: [result]"`

### Challenge 02

Increase the readability of the code. Use a set of functions for each operation and one funtion for the main calculator
