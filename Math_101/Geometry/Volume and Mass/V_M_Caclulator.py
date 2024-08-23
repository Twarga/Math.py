import math 

PI = math.pi
session = True 

def display():
    print("Welcome to the Volume and Mass Calculator! ")
    print("Please select the type of object:")
    print("1. Sphere ")
    print("2. Cylinder")
    print("3. Rectangular Prism ")
    print("4. Cone")
    print("5. Exit")

def session_handler():
    while True: 
        print("Do you want to calculate another volume and mass?")
        print("1. Calculate another expression")
        print("2. Quit")
        s_choice = int(input("Your choice: "))
        if s_choice == 1:
            return True
        elif s_choice == 2:
            return False
        else: 
            print("Please enter a valid option: 1 or 2")



def Sphere(radius, density):
    V = 4/3 * PI * pow(radius, 3)
    M = V * density
    return f"The Volume of the Sphere is {V}, and the Mass is {M}."



def Cylinder(radius, height, density):
    V = PI * pow(radius, 2) * height
    M = V * density
    return f"The Volume of the Cylinder is {V}, and the Mass is {M}."



def Rectangular_Prism(length, width, height, density):
    V = length * width * height
    M = V * density
    return f"The Volume of the Rectangular Prism is {V}, and the Mass is {M}."

def Cone(radius, height, density):
    V = 1/3 * PI * pow(radius, 2) * height
    M = V * density
    return f"The Volume of the Cone is {V}, and the Mass is {M}."

def main():
    global session

    while session:
        display()
        menu_choice = int(input("Enter your choice from 1-5: "))
        if menu_choice == 1: 
            try: 
                radius = float(input("Please enter the radius value: "))
                density = float(input("Please enter the density of the material: "))
                print(Sphere(radius, density))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
            session = session_handler()

        elif menu_choice == 2: 
            try:
                radius = float(input("Please enter the radius value: "))
                height = float(input("Please enter the height value: "))
                density = float(input("Please enter the density of the material: "))
                print(Cylinder(radius, height, density))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
            session = session_handler()

        elif menu_choice == 3: 
            try: 
                length = float(input("Please enter the length value: "))
                width = float(input("Please enter the width value: "))
                height = float(input("Please enter the height value: "))
                density = float(input("Please enter the density of the material: "))
                print(Rectangular_Prism(length, width, height, density))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
            session = session_handler()

        elif menu_choice == 4: 
            try: 
                radius = float(input("Please enter the radius value: "))
                height = float(input("Please enter the height value:")) 
                density = float(input("Please enter the density of the material: "))
                print(Cone(radius, height, density))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
            session = session_handler()

        elif menu_choice == 5: 
            print("Goodbye, have a great day!") 
            session = False

        else:
            print("Please enter a valid choice from 1-5.")

if __name__ == "__main__":
    main()
