def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    # Recebe a escolha do usuário
    escolha = input("Digite a opção (1/2/3/4): ")
    
    # Recebe os números do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    match escolha:
        case "1":
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
        case "2":
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
        case "3":
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
        case "4":
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        case _:
            print("Opção inválida")

# Executa a calculadora
calculadora()