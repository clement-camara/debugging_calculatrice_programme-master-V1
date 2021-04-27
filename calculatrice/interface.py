from calculatrice import addition, multiplication, division, soustraction


def display_interface():
    choice = input(""" Si tu veux quitter le programme Tape QUIT sinon
                       Additionner Tape 1
                       Soustraire Tape 2
                       Multiplier Tape 3
                       Diviser Tape 4
                   """)
    while choice.isdigit():
        choice = int(choice)  # do_something
        if choice == 1:
            choice = input("Saisir un chiffre à ADDITIONNER ou cliquer sur '=' ")
            result = addition(choice)
        elif choice == 2:
            choice = input("Saisir un chiffre à SOUSTRAIRE ou cliquer sur '=' ")
            result = soustraction(choice)
        elif choice == 3:
            choice = input("Saisir un chiffre à MULTIPLIER ou cliquer sur '=' ")
            result = multiplication(choice)
        elif choice == 4:
            choice = input("Saisir un chiffre à DIVISER ou cliquer sur '=' ")
            result = division(choice)
        elif choice == 'quit'.upper():
            print('merci pour votre visite et à bientot :)')
            break
        return print(f"Le resultat est ==> {result}")


display_interface()
