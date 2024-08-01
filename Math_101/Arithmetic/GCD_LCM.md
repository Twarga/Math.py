Sure! Here’s a simplified and clear algorithm for finding the Greatest Common Divisor (GCD) and Least Common Multiple (LCM) of two numbers:

### **Algorithm for GCD and LCM Finder**

#### **1. GCD Finder**

**Goal**: Find the Greatest Common Divisor (GCD) of two numbers.

**Steps**:

1. **Input**: Two positive integers, \(a\) and \(b\).
2. **Process**:
   - **Step 1**: If \(b\) is 0, then the GCD is \(a\). This is because any number divided by 0 is undefined, so the last non-zero remainder is the GCD.
   - **Step 2**: Otherwise, do the following:
     - Divide \(a\) by \(b\) and find the remainder. (Use the modulus operator `%` to get the remainder.)
     - Replace \(a\) with \(b\) and \(b\) with the remainder.
     - Repeat until the remainder is 0.
3. **Output**: When \(b\) is 0, the GCD is \(a\).

**Example**:
- **Input**: \(a = 48\), \(b = 18\)
- **Steps**:
  - Divide 48 by 18: Remainder is 12
  - Replace \(a = 18\), \(b = 12\)
  - Divide 18 by 12: Remainder is 6
  - Replace \(a = 12\), \(b = 6\)
  - Divide 12 by 6: Remainder is 0
  - \(b\) is 0, so GCD is \(a = 6\)
- **Output**: GCD = 6

#### **2. LCM Finder**

**Goal**: Find the Least Common Multiple (LCM) of two numbers.

**Steps**:

1. **Input**: Two positive integers, \(a\) and \(b\).
2. **Process**:
   - **Step 1**: Find the GCD of \(a\) and \(b\) (using the GCD Finder algorithm).
   - **Step 2**: Calculate the LCM using the formula:
     \[
     \text{LCM} = \frac{a \times b}{\text{GCD}(a, b)}
     \]
   - **Step 3**: The result is the LCM.
3. **Output**: The LCM of the two numbers.

**Example**:
- **Input**: \(a = 48\), \(b = 18\)
- **Steps**:
  - Find GCD: 6 (using the GCD Finder algorithm)
  - Calculate LCM:
    \[
    \text{LCM} = \frac{48 \times 18}{6} = 144
    \]
- **Output**: LCM = 144

### **Complete Algorithm Overview**

1. **Start**
2. **Input**: Read two positive integers \(a\) and \(b\)
3. **Find GCD**:
   - Apply the GCD Finder algorithm
4. **Find LCM**:
   - Use the formula with the previously calculated GCD
5. **Output**:
   - Print the GCD
   - Print the LCM
6. **End**

### **Python Code Implementation**

Here's the corresponding Python code to perform these operations:

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def main():
    # Input
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    
    # Calculate GCD
    result_gcd = gcd(a, b)
    print(f"GCD of {a} and {b} is {result_gcd}")
    
    # Calculate LCM
    result_lcm = lcm(a, b)
    print(f"LCM of {a} and {b} is {result_lcm}")

if __name__ == "__main__":
    main()
```

### **Summary**

- **GCD**: Find the largest number that divides both \(a\) and \(b\) using the Euclidean Algorithm.
- **LCM**: Find the smallest number that both \(a\) and \(b\) divide into, calculated using the GCD.

This cheat sheet should help you understand the concepts and steps involved in finding GCD and LCM. If you have any more questions or need further clarification, feel free to ask!