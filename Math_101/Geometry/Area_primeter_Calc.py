import math 

PI = math.pi
session = True 
def display():
    print("Welcome to the Area and Perimeter Calculator")
    print("--------------------------------------")
    print("1. Rectangle")
    print("2. Square")
    print("3. Circle")
    print("4. Triangle")
    print("5. Exit")
    print("---------------------------------------")

def rec_ap(l,w):
    area = l * w 
    perimeter = 2*(l+w)
    print(f"Your Rectangle Area is : {area}")
    print(f"Your rectangle perismeter is : {perimeter}")


def s_ap(s):
    area = math.pow(s,2)
    perimeter = 4 * s 
    print(f"Your sqaure Area is : {area} ")
    print(f"Your square perimeter is : {perimeter}")

def C_ac(r):
    area = PI * math.pow(r,2)
    Circumference = 2 * PI * r
    print(f"Your Circle Area is : {area}")
    print(f"Your Circle Circumference is : {Circumference}") 

def t_area(b,h):
    area = 0.5 * b * h
    print(f"Your Triangle area is :{area}" )

def t_perimeter(s1,s2,s3):
    perimeter = s1+s2+s3
    print(f"Your Triangle Perimeter is {perimeter} ")

def session_handler():
    while True : 
        print("did you want to calculate another expression or quite")
        print("1. calculate another expression")
        print("2. quit ")
        s_choice = int(input("Your choice : "))
        if s_choice == 1 :
            session = True
            break
        elif s_choice == 2 :
            session = False
            break
        else : 
            print("Please enter a valid option 1 or 2 ")
    return session       
def main():
    session = True 
    while session == True:
        display()
        choice = int(input("Select a shape to calculate :  "))
        if choice == 1:
            length = float(input("Please enter the Length : "))
            width = float(input("Please enter the width : "))
            rec_ap(length,width)
            session_handler()
        elif choice == 2 : 
            s_length = float(input("Enter the side length :  "))
            s_ap(s_length)
            session_handler()
        elif choice == 3 : 
            rad = float(input("Enter Your Circle radius : "))
            C_ac(rad)
            session_handler()
        elif choice == 4 :
            print("did you want to calculate the area or perimeter : ")
            print("1. Area ")
            print("2. Perimeter")
            tchoice = int(input("your choice : "))
            if tchoice == 1 :
                base = float(input("Please enter the base of the Triangle : "))
                height = float(input("Please enter the height of the triangle: "))
                t_area(base,height)
                session_handler()
            elif tchoice == 2 : 
                s1 = float(input("Pleaseenter the lengt of side A: "))
                s2 = float(input("Please enter the length of side B: "))
                s3 = float(input("Please enter the kength of side C: "))
                t_perimeter(s1,s2,s3)
                session_handler()
        elif choice == 5 :
            print("by have a great day :) !!")
            break
        else :
            print("Please enter a valid choice : ")


if __name__ == "__main__":
    main()