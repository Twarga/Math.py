import math 

def handle_exp(exp):
    allowed_globals = {
        "__builtins__": None,
        "math": math,
        "abs": abs,
        "round": round,
        "pow":pow,
    }

    return eval(exp, allowed_globals)

def main():
    print("Welcome to pycalc")
    print("enter 'quit' or 'ctrl+c' to exit")
    while True:
        exp = input("Enter your expression : ")
        if exp.lower() == "quit":
            break
        try:
            result = handle_exp(exp)
            print("Result:", result)
        except SyntaxError:
            print("Error: Invalid syntax.")
        except NameError:
            print("Error: Invalid function or variable name.")
        except ZeroDivisionError: 
            print("Error: Division by zero.")
        except Exeception as e :
            print(f"Error:{e}")

if __name__ == "__main__":
    main()

