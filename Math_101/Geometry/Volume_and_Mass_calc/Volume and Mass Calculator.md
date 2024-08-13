### Exercise Scenario: Volume and Mass Calculator

#### **Project Description:**
Create a Python program that calculates the volume and mass of different geometric objects based on user input. The program should allow the user to select the type of object, input the necessary dimensions, and then calculate and display the volume and mass based on a given density.

#### **Requirements:**

1. **Geometric Objects:**
   - **Sphere**
   - **Cylinder**
   - **Rectangular Prism**
   - **Cone**

2. **User Inputs:**
   - The user should be able to select the type of geometric object.
   - For each selected object, the user should input the required dimensions:
     - **Sphere:** Radius
     - **Cylinder:** Radius and Height
     - **Rectangular Prism:** Length, Width, and Height
     - **Cone:** Radius and Height
   - The user should input the density of the material in units of mass per cubic unit (e.g., g/cm³ or kg/m³).

3. **Calculations:**
   - **Volume Calculations:**
     - **Sphere:** \( V = \frac{4}{3} \pi r^3 \)
     - **Cylinder:** \( V = \pi r^2 h \)
     - **Rectangular Prism:** \( V = l \times w \times h \)
     - **Cone:** \( V = \frac{1}{3} \pi r^2 h \)
   - **Mass Calculation:**
     - Mass = Volume × Density

4. **Output:**
   - Display the calculated volume and mass of the selected object with appropriate units.

5. **Validation:**
   - Ensure that the user inputs valid numeric values for dimensions and density.
   - Provide error messages for invalid inputs and prompt the user to re-enter correct values.

#### **Bonus Features (Optional):**
- Allow the user to select units (e.g., cm³, m³, g, kg) and convert inputs and outputs accordingly.
- Implement a feature to handle multiple objects in a single session, allowing the user to calculate the volume and mass for several objects and display a summary at the end.

#### **Sample Scenario:**
1. The program starts and displays a menu:
   ```
   Welcome to the Volume and Mass Calculator!
   Please select the type of object:
   1. Sphere
   2. Cylinder
   3. Rectangular Prism
   4. Cone
   5. Exit
   ```
2. The user selects "2. Cylinder."
3. The program prompts the user to enter the radius and height of the cylinder:
   ```
   Please enter the radius of the cylinder: 5
   Please enter the height of the cylinder: 10
   ```
4. The program asks for the density of the material:
   ```
   Please enter the density of the material (e.g., g/cm³): 7.85
   ```
5. The program calculates the volume and mass of the cylinder and displays the results:
   ```
   The volume of the cylinder is: 785.4 cm³
   The mass of the cylinder is: 6153.39 g
   ```
6. The program asks if the user wants to calculate another object or exit.

#### **What You Will Learn:**
- Understanding and applying geometric formulas.
- Handling user input and validation.
- Structuring a program with functions for modularity.
- Performing basic error handling.
- Working with mathematical constants and functions in Python (e.g., `math.pi`).
- Implementing a loop to allow repeated operations within the program.