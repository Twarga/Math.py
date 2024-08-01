To create software that converts between fractions, decimals, and percentages, you can follow this algorithm. This will guide you through the process of building a converter with functionalities for all three conversions.

### **Algorithm for Fraction, Decimal, and Percentage Converter**

#### **1. User Interface**

1. **Display Options:**
   - **Convert Fraction to Decimal and Percentage**
   - **Convert Decimal to Fraction and Percentage**
   - **Convert Percentage to Fraction and Decimal**

2. **Get User Input:**
   - Prompt the user to select the conversion type.
   - Based on the selection, prompt the user for the input value.

#### **2. Conversion Functions**

**Function 1: Fraction to Decimal and Percentage**
1. **Input**: Fraction (e.g., `3/4`)
2. **Process**:
   - **Convert to Decimal**: 
     - Divide the numerator by the denominator.
     - `decimal = numerator / denominator`
   - **Convert to Percentage**: 
     - Multiply the decimal by 100.
     - `percentage = decimal * 100`
3. **Output**: Display the decimal and percentage.

**Function 2: Decimal to Fraction and Percentage**
1. **Input**: Decimal (e.g., `0.75`)
2. **Process**:
   - **Convert to Fraction**:
     - Convert the decimal to a fraction by finding the GCD of the numerator and denominator.
     - `fraction = decimal_to_fraction(decimal)`
     - `fraction = simplified_fraction(numerator, denominator)`
   - **Convert to Percentage**:
     - Multiply the decimal by 100.
     - `percentage = decimal * 100`
3. **Output**: Display the fraction and percentage.

**Function 3: Percentage to Fraction and Decimal**
1. **Input**: Percentage (e.g., `75%`)
2. **Process**:
   - **Convert to Decimal**:
     - Divide the percentage by 100.
     - `decimal = percentage / 100`
   - **Convert to Fraction**:
     - Convert the decimal to a fraction by finding the GCD of the numerator and denominator.
     - `fraction = decimal_to_fraction(decimal)`
     - `fraction = simplified_fraction(numerator, denominator)`
3. **Output**: Display the fraction and decimal.

#### **3. Helper Functions**

**Convert Decimal to Fraction**
1. **Input**: Decimal (e.g., `0.75`)
2. **Process**:
   - Determine the place value of the decimal.
   - Convert to fraction form.
   - Simplify the fraction.
3. **Output**: Fraction (e.g., `3/4`)

**Simplify Fraction**
1. **Input**: Numerator and Denominator
2. **Process**:
   - Find the Greatest Common Divisor (GCD) of the numerator and denominator.
   - Divide both the numerator and the denominator by the GCD.
3. **Output**: Simplified Fraction

**Find GCD**
1. **Input**: Two numbers
2. **Process**:
   - Use the Euclidean algorithm to find the GCD.
3. **Output**: GCD

### **Flowchart**

1. **Start**
2. **Display Menu**: Choose Conversion Type
3. **Get User Input**: Based on selection
   - If **Fraction**:
     - **Convert Fraction to Decimal and Percentage**
   - If **Decimal**:
     - **Convert Decimal to Fraction and Percentage**
   - If **Percentage**:
     - **Convert Percentage to Fraction and Decimal**
4. **Display Results**
5. **End**

### **Example Code Outline**

Here’s a simple outline in Python for your converter:

```python
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def fraction_to_decimal(numerator, denominator):
    return numerator / denominator

def decimal_to_fraction(decimal):
    precision = 10**10
    denominator = precision
    numerator = int(decimal * precision)
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)

def simplify_fraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)

def convert_fraction(numerator, denominator):
    decimal = fraction_to_decimal(numerator, denominator)
    percentage = decimal * 100
    return decimal, percentage

def convert_decimal(decimal):
    numerator, denominator = decimal_to_fraction(decimal)
    percentage = decimal * 100
    return simplify_fraction(numerator, denominator), percentage

def convert_percentage(percentage):
    decimal = percentage / 100
    numerator, denominator = decimal_to_fraction(decimal)
    return simplify_fraction(numerator, denominator), decimal

# Main Function
def main():
    print("Choose Conversion Type:")
    print("1. Fraction to Decimal and Percentage")
    print("2. Decimal to Fraction and Percentage")
    print("3. Percentage to Fraction and Decimal")

    choice = int(input("Enter choice (1/2/3): "))

    if choice == 1:
        numerator = int(input("Enter numerator: "))
        denominator = int(input("Enter denominator: "))
        decimal, percentage = convert_fraction(numerator, denominator)
        print(f"Decimal: {decimal}")
        print(f"Percentage: {percentage}%")

    elif choice == 2:
        decimal = float(input("Enter decimal: "))
        fraction, percentage = convert_decimal(decimal)
        print(f"Fraction: {fraction[0]}/{fraction[1]}")
        print(f"Percentage: {percentage}%")

    elif choice == 3:
        percentage = float(input("Enter percentage: "))
        fraction, decimal = convert_percentage(percentage)
        print(f"Fraction: {fraction[0]}/{fraction[1]}")
        print(f"Decimal: {decimal}")

if __name__ == "__main__":
    main()
```

This code provides a basic structure for the converter. You can extend it with additional features and a more user-friendly interface as needed.