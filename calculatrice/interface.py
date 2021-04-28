from calculatrice import *

def display_interface():
        choice = ask_user("""
        Tu veux :
        1. Additionner Tape 1
        2. Soustraire Tape 2
        3. Multiplier Tape 3
        4. Diviser Tape 4""")
        while choice.isdigit():
            choice = int(choice)
            if choice == 1:
                num = ask_user(debut + "ADDITIONNER" + fin)
                result = addition(num)
            elif choice == 2:
                num = ask_user(debut + "SOUSTRAIRE" + fin)
                result = soustraction(num)
            elif choice == 3:
                num = ask_user(debut + "MULTIPLIER" + fin)
                result = multiplication(num)
            elif choice == 4:
                num = ask_user(debut + "DIVISER" + fin)
                result = division(num)
            return print(f"Le resultat est ==> {result}")

display_interface()
