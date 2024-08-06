def display():
    print("Welcome to FDP Converter")
    print("Choose Your Operation Number:")
    print("Convert Fraction to Decimal and Percentage")
    print("Convert Decimal to Fraction and Percentage")
    print("Convert Percentage to Fraction and Decimal")

def GCD(a,b):
    while b:
        a, b = b, a % b
    return a 

def fraction_to_decimal(numerator, denominator):
    return numerator / denominator

def decimal_to_fraction(decimal):
    precision = 10**10 
    denominator = precision
    numerator = int(decimal * precision)
    common_divisior = GCD(numerator , denominator)
    return (numerator // common_divisior , denominator // common_divisior )

def simplify_fraction(numerator , denominator):
    common_divisior = GCD(numerator , denominator)
    return (numerator // common_divisior , denominator // common_divisior)

def convert_fraction(numerator, denominator):
    decimal = fraction_to_decimal(numerator, denominator)
    percentage = decimal * 100
    return decimal, percentage 

def convert_decimal(decimal):
    numerator , denominator = decimal_to_fraction(decimal)
    percentage = decimal * 100 
    return simplify_fraction(numerator, denominator), percentage 

def convert_percentage(percentage):
    decimal = percentage / 100
    numerator, denominator = decimal_to_fraction(decimal)
    return simplify_fraction(numerator, denominator), decimal

def main():
    display()

    choice = int(input("Enter choice (1/2/3):"))

    if choice == 1 : 
        numerator = int(input("Enter numerator: "))
        denominator = int(input("Enter denominator: "))
        decimal, percentage = convert_fraction(numerator, denominator)
        print(f"Decimal: {decimal}")
        print(f"Percentage : {percentage}%")
    

    elif choice == 2 : 
        decimal = float(input("Enter decimal: "))
        fraction , percentage = convert_decimal(decimal)
        print(f"Fraction:{fraction[0]}/{fraction[1]}")
        print(f"Percentage:{percentage}%")

    elif choice == 3 : 
        percentage = float(input("Enter percentage:"))
        fraction , decimal = convert_percentage(percentage)
        print(f"Fraction: {fraction[0]}/{fraction[1]}")
        print(f"Decimal: {decimal}")


if __name__ == "__main__":
    main()