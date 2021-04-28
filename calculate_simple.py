def calculate():
    result = None
    signe = None
    app_run = True
    while True:
        if signe == '=':
            print(f"Le résultat est: {result}")
            break
        elif app_run:
            while True:
                try:
                    number = float(input("Entre un nombre: "))
                except ValueError:
                    print("Oops! Ce n'est pas un nombre essaie encore.")
                else:
                    if result is None:
                        result = number
                    else:
                        if signe == '+':
                            result += number
                        elif signe == '-':
                            result -= number
                        elif signe == '*':
                            result *= number
                        elif signe == '/':
                            result /= number
                    break
            app_run = False
        else:
            while True:
                signe = input("Entre un des opérateurs suivants +, -, *, /, =: ")
                if signe in ('+', '-', '*', '/', '='):
                    break
                else:
                    print("Attention! c'est pas un bon opérateur. retente ta chance.")
            app_run = True

