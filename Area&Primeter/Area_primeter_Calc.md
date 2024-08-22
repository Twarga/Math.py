

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
   ```
   Welcome to the Area and Perimeter Calculator!
   Select a shape to calculate:
   1. Rectangle
   2. Square
   3. Circle
   4. Triangle
   ```

2. **User selects a shape (e.g., Rectangle):**
   ```
   You selected: Rectangle
   Please enter the Length: 5
   Please enter the Width: 3
   ```

3. **Program calculates and displays the results:**
   ```
   Area of the Rectangle: 15 square units
   Perimeter of the Rectangle: 16 units
   ```

4. **Option to calculate again or exit:**
   ```
   Would you like to calculate another shape? (yes/no): yes
   ```

5. **Repeat the process or end the program:**
   ```
   Select a shape to calculate:
   1. Rectangle
   2. Square
   3. Circle
   4. Triangle
   ```

## Bonus Features (Optional)
1. **Add support for more shapes:** Such as trapezoids, pentagons, hexagons, etc.
2. **Graphical User Interface (GUI):** Use a library like Tkinter (Python) or JavaFX (Java) to create a GUI version of the calculator.
3. **Save Results:** Allow users to save the results to a file for future reference.
4. **History:** Maintain a history of calculations performed in the current session.

## Submission
- Submit your source code along with a README file explaining how to run the program.
- Include sample inputs and outputs for testing purposes.
```
