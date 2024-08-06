# Exercise Scenario: Area and Perimeter Calculator

## Objective
Create a program that takes the dimensions of various geometric shapes as input and calculates their area and perimeter.

## Requirements
1. **Shape Selection:**
   - The program should allow the user to select from a list of shapes:
     - Rectangle
     - Square
     - Circle
     - Triangle

2. **Input Dimensions:**
   - Based on the selected shape, prompt the user to input the required dimensions:
     - **Rectangle:** Length and Width
     - **Square:** Side Length
     - **Circle:** Radius
     - **Triangle:** Base and Height for area, all three sides for perimeter

3. **Calculations:**
   - Implement functions to calculate the area and perimeter for each shape:
     - **Rectangle:**
       - Area = Length × Width
       - Perimeter = 2 × (Length + Width)
     - **Square:**
       - Area = Side Length²
       - Perimeter = 4 × Side Length
     - **Circle:**
       - Area = π × Radius²
       - Circumference (Perimeter) = 2 × π × Radius
     - **Triangle:**
       - Area = 0.5 × Base × Height
       - Perimeter = Sum of all three sides

4. **Output Results:**
   - Display the calculated area and perimeter to the user in a clear and concise manner.

5. **Error Handling:**
   - Ensure the program can handle invalid inputs gracefully. For example, dimensions should be positive numbers.

6. **User Interface:**
   - Create a simple user interface (command-line or graphical) to interact with the user.

## Example Workflow
1. **Start the Program:**
