def addition(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
        number = input("Saisir un chiffre à additionner ou cliquer sur '=' ")
    result = sum(list_numbers)
    return result


def multiplication(number):
    list_numbers = []
    result = 0
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
        number = input("Saisir un chiffre à multiplier ou cliquer sur '=' ")
    for index, list_number in enumerate(list_numbers):  # refactoriser
        result = list_number if index == 0 else result * list_number
    return result


def division(number):
    list_numbers = []
    result = 0
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
        number = input("Saisir un chiffre à multiplier ou clicker sur '=' ")
    for index, list_number in enumerate(list_numbers):
        result = list_number if index == 0 else result // list_number
    return result


def soustraction(number):
    list_numbers = []
    result = 0
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
        number = input("Saisir un chiffre à additionner ou clicker sur '=' ")
    i = 0
    for list_number in list_numbers:
        result = list_number if i == 0 else result - list_number
        i = i + 1
    return result


