debut = "Saisir un chiffre à "
fin = " ou cliquer sur '=' "


def ask_user(sentence="Saisir un chiffre"):
    choice = input(f"{sentence}\n")
    return choice


def addition(number):
    list_numbers = []
    while number.isdigit():
        list_numbers.append(int(number))
        number = ask_user(debut + "ADDITIONNER" + fin)
    result = sum(list_numbers)
    return result


def soustraction(number):
    list_numbers = []
    while number.isdigit():
        list_numbers.append(int(number))
        number = ask_user(debut + "SOUSTRAIRE" + fin)
    for index, list_number in enumerate(list_numbers):
        if index == 0:
            result = list_number
        else:
            result = result - list_number
    return result


def multiplication(number):
    list_numbers = []
    while number.isdigit():
        list_numbers.append(int(number))
        number = ask_user(debut + "MULTIPLIER" + fin)
    for index, list_number in enumerate(list_numbers):
        if index == 0:
            result = list_number
        else:
            result = result * list_number
    return result


def division(number):
    list_numbers = []
    while number.isdigit():
        list_numbers.append(int(number))
        number = ask_user(debut + "DIVISER" + fin)
    for index, list_number in enumerate(list_numbers):
        if index == 0:
            result = list_number
        else:
            result = result // list_number
    return result


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
