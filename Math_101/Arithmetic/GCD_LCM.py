def GCD(a,b):
    while b != 0:
        a, b = b, a % b
    return a 

def LCM(a,b):
    return abs(a*b) // GCD(a, b)

def main():
    # Input 
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))

    result_gcd = GCD(a,b)
    print(f"GCD of {a} and {b} is {result_gcd}")

    result_lcm = LCM(a,b)
    print(f"LCM of {a} and {b} is {result_lcm}")

if __name__ == "__main__":
    main()

