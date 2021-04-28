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

