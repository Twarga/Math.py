### **Project: Angle Finder**

#### **Objective:**
Create a Python program that takes user input for an angle in degrees and classifies it into specific categories based on its measurement.

#### **Project Requirements:**
1. **User Input:**
   - The program should prompt the user to enter an angle in degrees.
   - Ensure that the input is validated to handle non-numeric entries and out-of-range values.

2. **Angle Classification:**
   - Classify the entered angle into the following categories:
     - **Acute Angle:** An angle greater than 0° and less than 90°.
     - **Right Angle:** An angle exactly equal to 90°.
     - **Obtuse Angle:** An angle greater than 90° and less than 180°.
     - **Straight Angle:** An angle exactly equal to 180°.
     - **Reflex Angle:** An angle greater than 180° and less than 360°.
     - **Full Rotation:** An angle exactly equal to 360°.
     - **Invalid Angle:** Angles less than or equal to 0° and greater than 360° should be considered invalid.

3. **Output:**
   - After classification, the program should output a clear and concise message indicating the type of angle entered.
   - In case of invalid input, provide an appropriate error message and prompt the user to try again or exit.

4. **Additional Features (Optional):**
   - Allow the user to enter multiple angles in a single session until they choose to exit.
   - Provide the option to input angles in different units (e.g., radians) and convert them accordingly.
   - Include a graphical representation of the angle using ASCII art or a simple plotting library.
   - Implement exception handling to manage unexpected errors gracefully.

#### **Implementation Steps:**

1. **Setup Development Environment:**
   - Ensure Python is installed on your system.
   - Choose an IDE or text editor of your choice (e.g., VS Code, PyCharm, Sublime Text).

2. **Create the Program Structure:**
   - Initialize a new Python script file.
   - Define a main function to control the flow of the program.

3. **Handle User Input:**
   - Use the `input()` function to receive user input.
   - Validate the input to ensure it is a numeric value.
   - Implement checks to handle inputs outside the valid range (0° - 360°).

4. **Implement Classification Logic:**
   - Use conditional statements (`if`, `elif`, `else`) to determine the category of the angle based on its value.
   - Ensure all edge cases are covered (e.g., exactly 0°, 90°, 180°, 360°).

5. **Display Output:**
   - Print out the classification result in a user-friendly format.
   - In case of invalid input, display an error message and provide options to retry or exit.

6. **Add Optional Features (If Implemented):**
   - For multiple entries, implement a loop that continues to prompt the user until they decide to quit.
   - For different units, include conversion functions between degrees and radians.
   - To display a graphical representation, explore libraries such as `matplotlib` for plotting or use simple text-based illustrations.

7. **Testing the Program:**
   - Test the program with a variety of inputs to ensure all classifications work correctly.
   - Test with invalid inputs such as strings, negative numbers, and numbers greater than 360° to ensure error handling is effective.
   - Verify that optional features work as intended if implemented.

8. **Documentation and Comments:**
   - Add comments throughout your code to explain the functionality of different sections.
   - Create a README file explaining how to use the program, its features, and any dependencies.

9. **Run and Debug:**
   - Execute the program and observe the outputs.
   - Debug any issues that arise during testing and ensure the program runs smoothly.

#### **Testing Scenarios:**

- **Valid Inputs:**
  - *Input:* 45 → *Output:* "Acute Angle"
  - *Input:* 90 → *Output:* "Right Angle"
  - *Input:* 135 → *Output:* "Obtuse Angle"
  - *Input:* 180 → *Output:* "Straight Angle"
  - *Input:* 270 → *Output:* "Reflex Angle"
  - *Input:* 360 → *Output:* "Full Rotation"

- **Invalid Inputs:**
  - *Input:* -30 → *Output:* "Invalid angle. Please enter a value between 0° and 360°."
  - *Input:* 400 → *Output:* "Invalid angle. Please enter a value between 0° and 360°."
  - *Input:* "abc" → *Output:* "Invalid input. Please enter a numerical value."

#### **Enhancements (Optional):**
- **User Interface:**
  - Develop a simple GUI using libraries like Tkinter to make the program more interactive.
  
- **Angle Operations:**
  - Add functionality to calculate complementary and supplementary angles where applicable.

- **Saving Results:**
  - Implement a feature to save the classification results to a file for future reference.

- **Unit Testing:**
  - Write unit tests for your classification function to ensure reliability and ease of maintenance.

#### **Project Submission:**
- **Files to Submit:**
  - The Python script file containing your code.
  - A README.md file with instructions on how to run the program and a brief description.
  - Any additional files if optional features are implemented (e.g., requirements.txt for dependencies).

- **Submission Guidelines:**
  - Ensure your code is well-formatted and follows standard coding conventions.
  - Double-check that all features work as intended and that there are no runtime errors.
  - Include examples in your README to demonstrate how the program works.

#### **Conclusion:**
This project will help reinforce your understanding of conditional statements, user input handling, and basic error management in Python. By optionally extending the project's functionality, you can also explore more advanced topics such as GUI development, data visualization, and unit testing.

**Good luck with your project!**