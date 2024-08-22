import math 
session = True 


def menu():
    print("-------------------------------")
    print("                               ")
    print("                               ")
    print("Welcome to Triangle Solver ! ")
    print("1. Calculate the length of the third side of a right triangle !")
    print("2. Check if a triangle is a right triangle ")
    print("3. Classify the type of triangle ")
    print("4. Exit")


def session_handler():
    while True: 
        print("Do you want to perform another operation?")
        print("1. Yes")
        print("2. No")
        try : 
            s_choice = int(input("Your choice: "))
        except ValueError:
            print("Please enter a valid Number")
        if s_choice == 1:
            return True
        elif s_choice == 2:
            return False
        else: 
            print("Please enter a valid option: 1 or 2")


def calculate_third_side():
    print("Let's calculte the third side of a a right triangle ! :) ")
    try : 
        a = float(input("Please enter the length of the first side : "))
        b = float(input("Pleae enter the length of the second side : "))
    except ValueError:
        print("please enter a valid Values : ")

    if a  > 0 and b > 0:
        c_2 = pow(a,2) + pow(b,2)
        c = math.sqrt(c_2) 
        print(f"The Length of your third side (Hypotenuse ) is {c} ")
    else:
        print("Please enter a positive number ! !! ! ")



def Check_Right_Triangle():
    print("let's check if your triangle : ")
    try : 
        a = float(input("Please enter the length of the first side : " ))
        b = float(input("Please enter the length of the second side : "))
        c = float(input("Pleae enter the length of the third side : "))
    
    except ValueError:
        print("Please enter a valid Values : ")

    if a > 0 and b > 0 and c > 0 :
        if pow(c,2) == pow(a,2) + pow(b,2):
            print("Yes , This is a right triangle ")
        else : 
            print("No, your triangle is not a right triangle")
    else : 
        print("Please enter a positive Numbers !!!!!! ")

def classify_triangle_type():
    print("Let's calassify the type of your triangle : ")
    try : 
        a = float(input("Please enter the length of the first side : "))
        b = float(input("Please enter the length of the second side : "))
        c = float(input("Pleae enter the length of the third side : "))
    
    except ValueError:
        print("Please enter a valid Values")

    if a > 0 and b > 0 and c > 0 :
        
        if a == b == c : 
            print("Your Triangle is equilateral")
        elif a == b != c or a == c != b or b == c!= a:
            print("Your Triangle is isosceles")
        else: 
            print("Your Triangle is scalene")

    else: 
        print("Please enter a positive Numbers !   !!!")

def main():
    session = True 
    while session:
        menu()
        try:
            choice = int(input("Please enter you choice number : " ))
        except ValueError:
            print("Plese enter a valid Choice number ")
        
        if choice == 1 : 
            calculate_third_side()
            session = session_handler()
        elif choice == 2: 
            Check_Right_Triangle()
            session = session_handler()
        elif choice == 3 : 
            classify_triangle_type()
            session = session_handler()
        elif choice == 4 : 
            session = False
    


if __name__ == "__main__":
    main()