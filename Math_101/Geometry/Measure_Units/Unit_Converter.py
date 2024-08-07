import math 


session = True 
def menu_display():
    print("Welcome to Twarga Unit Converter ! ")
    print("Choose the Conversion Type : ")
    print("1. Length ")
    print("2. Weight ")
    print("3. Volume ")
    print("4. Temperature ")
    print("5. Exit ")

def L_display():
    print("Choose the Length Conversion that You Want by number: ")
    print("1. Meters (m) to Feet (ft):  ")
    print("2. Feet (ft) to Meters (m): ")
    print("3. kilometers (km) to Miles (mi): ")
    print("4. Miles (mi) to kilometers (km): ")

def W_display():
    print("Choose the Weight Conversions that You want by number :  ")
    print("1. kilograms (kg) to Pounds (lbs) ")
    print("2. Pounds (lbs) to Kilograms (Kg) ")
    print("3. Grams (g) to Ounce (oz) ")
    print("4. Ounce (oz) to Grams (g) ")

def V_display():
    print("Choose the Volume Conversion that You want : ")
    print("1. Liters (L) to Gallons (gal)")
    print("2. Gallons (gal) to Liters (L) ")
    print("3. Milliliters (ml) to Fluid ounces (fl.oz) ")
    print("4. Fluid ounces (fl.oz) to Milliliters (ml) ")


def T_display():
    print("Choose the Temperature Conversions that You Want by number : ")
    print("1. Celsius (°C) to Fahrenheit (°F) ")
    print("2. Fahrenheit (°F) to Celsius (°C) ")
    print("3. Celsius (°C) to Kelvin (°K) ")
    print("4. Kelvin (°K) to Celsius (°C)")



def meters_to_feet(m):
    feet = m * 3.28084
    print(f"{m} m in feet is {feet} ft")


def feets_to_meters(f):
    meters = f / 3.28084
    print(f"{f} ft in meters is {meters} m")

def kilometers_to_miles(k):
    miles = k * 0.621371
    print(f"{k} k in Miles is {miles} mi ")

def miles_to_kilometers(mi):
    kilometers = mi / 0.621371
    print(f"{mi} mi in kilometers is {kilometers} km")


def kilograms_to_pounds(kg):
    pounds = kg * 2.20462
    print(f"{kg} kg in pounds is {pounds} lbs")


def pounds_to_kilograms(lbs):
    kg = lbs / 2.20462
    print(f"{lbs} lbs is {kg} kg  ")

def grams_to_ounce(g):
    oz = g * 0.035274
    print(f"{g} g is {oz} oz ")


def ounce_to_grams(oz):
    g = oz / 0.035274
    print(f"{oz} is {g} g ")


def liters_to_gallons(l):
    gal = l * 0.264172 
    print(f"{l} is {gal} gal")

def gallons_to_liters(gal):
    l = gal / 0.264172
    print(f"{gal} is {l} l")

def milliliters_to_fluid(mil):
    fluid = mil * 0.033814
    print(f"{mil} mil is {fluid} ft.oz")

def fluid_to_milliliters(ft_oz):
    mil = ft_oz / 0.033814
    print(f"{ft_oz} ft.oz is {mil} mil ")


def celsius_to_fahrenheit(c):
    fahrenheit = (c*9/5)+ 32
    print(f"{c} °C is {fahrenheit} °F ")


def fahrenheit_to_celsius(fah):
    celsius = (fah - 32 ) * 5/9
    print(f"{fah} °F is {celsius} °C ")

def celsius_to_kelvin(c):
    kelvin = c + 273.15 
    print(f"{c} °C  is {kelvin} °K ")

def kelvin_to_celsius(kel):
    celsius = kel - 273.15 
    print(f"{kel} °K  is {celsius} °C")
def session_handler():
    while True : 
        print("did you want to Convert another Units or quite")
        print("1. Convert another Units")
        print("2. quit ")
        s_choice = int(input("Your choice : "))
        if s_choice == 1 :
            return True
        elif s_choice == 2 :
            return False
            
        else : 
            print("Please enter a valid option 1 or 2 ")
    return session  
def main():
    global session
    while session == True :
        menu_display()
        menu_choice = int(input("Enter Your choice : "))
        if menu_choice == 1:
            try : 
                L_display()
                L_choice = int(input("Enter your Length Conversions Type:  "))
                if L_choice == 1 : 
                    try : 
                        meters = float(input("Please enter the meters Value : "))
                        meters_to_feet(meters)
                        session_handler()
                    except ValueError:
                        print("Invalid input. Please enter numeric values.")
                elif L_choice == 2 : 
                    try :
                        feets = float(input("Please enter the feets Value :  "))
                        feets_to_meters(feets)
                        session_handler()
                    except ValueError:
                        print("Invalid input. Please enter numeric values.")

                elif L_choice == 3 : 
                    try : 
                        kilometers = float(input("Please enter the Kilomters Value "))
                        kilometers_to_miles(kilometers)
                        session_handler()
                    except ValueError:
                        print("Invalid input. Please enter numeric values.")

                elif L_choice == 4 : 
                    try : 
                        miles = float(input("Please enter you Miles Value : "))
                        miles_to_kilometers(miles)
                        session_handler()
                    except ValueError:
                        print("Invalid input. Please enter numeric values.")
                else:
                    print("Choice Invalid please enter one of the choices in the menu ")
            except ValueError:
                print("Invalid input. Please enter numeric values.")

            session_handler()
        elif menu_choice == 2 : 
            try : 
                W_display()
                W_choice = int(input("Enter your Weight Conversions Type : "))
                if W_choice == 1 : 
                    try : 
                        kilograms = float(input("Please enter your Kilograms Values "))
                        kilograms_to_pounds(kilograms)
                        session_handler()
                    except ValueError:
                        print("Invalid input. Please enter numeric values.")
                elif W_choice == 2 : 
                    try : 
                        pounds = float(input("Please enter your lbs value : "))
                        pounds_to_kilograms(pounds)
                        session_handler()
                    except ValueError:
                        print("Invalid input. Please enter numeric values.")
                elif W_choice == 3 : 
                    try :
                        grams = float(input("Please enter your grams Value : "))
                        grams_to_ounce(grams)
                        session_handler()
                    except ValueError:
                        print("Invalid input. Please enter numeric values.")
                elif W_choice == 4 : 
                    try : 
                        ounce = float(input("Please enter your oz Value : "))
                        ounce_to_grams(ounce)
                        session_handler()
                    except ValueError:
                        print("Invalid input. Please enter numeric values.")
                else : 
                    print("PLease Enter a valid choice Number  Number ")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        
        elif menu_choice == 3 : 
            try : 
                V_display()
                V_choice = int(input("Enter yout Volume Conversions Type : "))
                if V_choice == 1 : 
                    try : 
                        liters = float(input("Please enter your Liters Value : "))
                        liters_to_gallons(liters)
                        session_handler()
                    except ValueError:
                        print("Invalid input. Please enter numeric values.")
                
                elif V_choice == 2 :
                    try : 
                        gallons = float(input("Please enter your gallons Value : "))
                        gallons_to_liters(gallons)
                        session_handler()
                    except ValueError:
                        print("Invalid input. Please enter numeric values.")
                
                elif V_choice == 3 : 
                    try : 
                        mili = float(input("Please enter your milliliters Value "))
                        milliliters_to_fluid(mili)
                        session_handler()
                    except ValueError:
                        print("Invalid input. Please enter numeric values.")
                elif V_choice == 4 : 
                    try : 
                        fluid = float(input("Please enter your ft.oz value :  "))
                        fluid_to_milliliters(fluid)
                        session_handler()
                    except ValueError:
                        print("Invalid input. Please enter numeric values.")
                
                else : 
                    print("Please enter a valid choice Number : ")
            except ValueError:
                 print("Invalid input. Please enter numeric values.")

        elif menu_choice == 4 : 
            try :
                T_display()
                T_choice = int(input("Your Choice 1-4  : "))
                if T_choice == 1 : 
                    try : 
                        celisus = float(input("Please enter your celisus value : "))
                        celsius_to_fahrenheit(celisus)
                        session_handler()
                    
                    except ValueError:
                         print("Invalid input. Please enter numeric values.")
                
                elif T_choice == 2 : 
                    try : 
                        fah = float(input("Please enter your fahenheit value : "))
                        fahrenheit_to_celsius(fah)
                        session_handler()
                    
                    except ValueError:
                         print("Invalid input. Please enter numeric values.")
                
                if T_choice == 3 : 
                    try : 
                        celisus = float(input("Pleas Enter your celisus Value : "))
                        celsius_to_kelvin(celisus)
                        session_handler()
                    except ValueError : 
                         print("Invalid input. Please enter numeric values.")
                    
                if T_choice == 4 : 
                    try : 
                        kelvin = float(input("Please enter your kelvin Value : "))
                        kelvin_to_celsius(kelvin)
                        session_handler()
                    except ValueError:
                         print("Invalid input. Please enter numeric values.")
            
            except ValueError:
                 print("Invalid input. Please enter numeric values.")
        elif menu_choice == 5 : 
            try : 
                print("BY HAVE A GOOD DAY ! ")
                session = False
            except:
                print("Invalid input. Please enter numeric values.")
        else : 
             print("Invalid input. Please enter a Valid Choice.")

    
    


if __name__ == '__main__':
    main()