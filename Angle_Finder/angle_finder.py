import math 
session = True

def menu():
    print("Welcome to angle finder : ")
    print("Enter your angle degrees and I will give you the name of the Angle !! ")

def session_handler():
    while True: 
        print("Do you want to find another angle ! ?")
        print("1. Find another angle")
        print("2. Quit")
        s_choice = int(input("Your choice: "))
        if s_choice == 1:
            return True
        elif s_choice == 2:
            return False
        else: 
            print("Please enter a valid option: 1 or 2")

def main():
    global session
    while session:
        menu()
        try :
            angle_degree = int(input("Enter your angle degree here : "))
        except ValueError :
            print("Enter a valid Number between 0 - 360 ")
            continue
        if angle_degree > 0 and angle_degree < 90 : 
            print("Your Angle is an Acute Angle because is greater then 0° and less then 90°")
            session = session_handler()
        elif angle_degree == 90:
            print("Your Angle is a Right angle because is eqaul 90° ")
            session = session_handler()
        elif angle_degree > 90 and angle_degree < 180 :
            print("Your angle is a an Obtus Angle because is greater than 90° and less then 180° ")
            session = session_handler()
        elif angle_degree == 180 : 
            print("Your Angle is a Straight Angle because is exactly equal to 180° ")
            session = session_handler()
        elif angle_degree > 180 and angle_degree < 360 :
            print("Your Angle is a Reflex Angle becuase is greater then 180° and less than 360°")
            session = session_handler()
        elif angle_degree == 360 :
            print("Your angle is a full rotation angle because is exactly equal 360°")
            session = session_handler()
        else:
            print("Invalid Angle : Angle less then or equal to 0° and greater than 360° should be considered invalid")
            session = session_handler()


if __name__ == "__main__":
    main()