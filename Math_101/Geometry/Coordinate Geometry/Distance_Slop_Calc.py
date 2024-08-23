# Project : Distance and Slope Calculator 
# Create a tool to calculate the distance between two points and find the slope of the line connecting them , given their coordinates 

import math 
session = True 

# menu display
def menu():
    print("Welcome to Twarga Distance and Slope cordinate Calculator !!")
    print("-------------------------------")
    print("                               ")
    print("Choose the Operation you want from 1 - 3  : ")
    print("1. Caculate Distance :")
    print("2. Find the Slope : ") 
    print("3. Exit : ")   
    print("                               ")
    print("-------------------------------")

# function to handle session 
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

# Function for the first choice , calculate distance
def Caculate_Distance():
    try: 
        x1 = float(input("Please enter the value of x1 : "))
        x2 = float(input("Please enter the value of x2 : "))
        y1 = float(input("Please enter the value of y1 :"))
        y2 = float(input("Please enter the value of y2 : "))

    except ValueError :
        print("Please enter a valid points value")


    d = math.sqrt(pow(x2-x1,2) + pow(y2-y1,2))
    print(f"The distance between (x1={x1}, x2={x2}) and (y1={y1}, y2={y2}) is {d}") 
def Find_Slope():
    try:
        x1 = float(input("Please enter the value of x1 : "))
        x2 = float(input("Please enter the value of x2 : "))
        y1 = float(input("Please enter the value of y1 :"))
        y2 = float(input("Please enter the value of y2 : "))

    except ValueError :
        print("Please enter a valid points value")

    m = (y2 - y1) / (x2 - x1)
    print(f"The slope of the line between (x1={x1}, x2={x2}) and (y1={y1}, y2={y2}) is {m}")

 

# The main Function
def main():
    # Main Programe Loop
    session = True
    while session:
        menu()
        # Choice Error Handler
        try:
            choice = int(input("Please enter Your Choice here 1-3 : "))
        except ValueError:
            print("Please enter a valide choice number from 1-3")
        # Choice Stament Handler
        if choice == 1: 
            Caculate_Distance()
            session = session_handler()
        elif choice == 2 : 
            Find_Slope()
            session = session_handler()
        elif choice == 3 : 
            # Exit Choice Handler
            session = False


# Main call Handler 
if __name__ == "__main__":
   main() 

# The end of the Code 