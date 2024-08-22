### **Exercise Scenario: Triangle Solver**

**Project:** Triangle Solver

**Objective:** Develop a Python tool that assists users with problems related to triangle side lengths and the Pythagorean theorem.

---

#### **Scenario:**

You are creating a Python program called "Triangle Solver" with the following features:

1. **Calculate Missing Sides:**
   - Given two sides of a right triangle, calculate the length of the third side using the Pythagorean theorem.
   - Example: If the user inputs two sides (base and height), calculate the hypotenuse.

2. **Determine Triangle Type:**
   - Given three side lengths, determine if the triangle is a right triangle.
   - Classify the triangle as equilateral, isosceles, or scalene.

3. **Input Validation:**
   - Handle invalid inputs, such as non-numeric values or sides that do not form a valid triangle.

---

#### **Detailed Steps:**

1. **Menu Function:**
   - Provide a menu with options:
     1. Calculate the length of the third side of a right triangle.
     2. Check if a triangle is a right triangle.
     3. Classify the type of triangle.
     4. Exit the program.

2. **Calculation Functions:**
   - **Calculate Third Side (Right Triangle):**
     - Input: Two sides of a right triangle.
     - Output: Length of the hypotenuse.
   
   - **Check Right Triangle:**
     - Input: Three sides of a triangle.
     - Output: Determine if the triangle is a right triangle.

   - **Classify Triangle:**
     - Input: Three sides of a triangle.
     - Output: Type of triangle (equilateral, isosceles, or scalene).
a = b != c or a = c!= b or b = c != a
3. **Input Validation:**
   - Ensure the program handles invalid inputs properly.

---

#### **Example Output:**

```
Welcome to Triangle Solver!

1. Calculate the length of the third side of a right triangle
2. Check if a triangle is a right triangle
3. Classify the type of triangle
4. Exit

Please select an option: 1

Enter the length of the first side: 3
Enter the length of the second side: 4

The length of the hypotenuse is: 5.0

Do you want to perform another operation?
1. Yes
2. No

Please select an option: 2

Thank you for using Triangle Solver. Goodbye!
```

---

**Your task is to implement the functionality based on the given steps and ensure the program handles user inputs and performs the required calculations accurately.**