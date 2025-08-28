def calculator(Operator):
    Addition_sign = "+"
    Subtraction_sign = "-"
    Multiplication_sign = "*"
    Division_sign = "/"


    Number1 = float(input("Enter 1st number: "))
    Number2 = float(input("Enter 2nd number: "))

    if Operation == Addition_sign:
        Addition = Number1 + Number2
        print(Addition)
    elif Operation == Subtraction_sign:
        Subtraction = Number1 - Number2
        print(Subtraction)
    elif Operation == Multiplication_sign:
        Multiplication = Number1*Number2
        print(Multiplication)
    elif Operation == Division_sign:
        Division = Number1 / Number2
        print(Division)
    else:
        print("Operaton not match!")

    return

Operation = input("Choose your operator: +, -, *, / : ")

calculator(Operation)