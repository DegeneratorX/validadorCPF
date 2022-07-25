while True:

    cpf_digitado = input("Digite um CPF (pode incluir ou não traços e pontos): ")
    caracteres = ".-"  # Caracteres que eventualmente podem aparecer ao digitar
    if "." or "-" in cpf_digitado:  # Se tiver esses caracteres...
        for x in range(len(caracteres)):  # Remove através de string vazia.
            cpf_digitado = cpf_digitado.replace(caracteres[x], "")

    if len(cpf_digitado) != 11 or not cpf_digitado.isdecimal():  # Se o input for bizarro, erro.
        print("Algo deu errado! CPF com caracteres indevidos ou fora do padrão. Tente novamente.")
        continue

    soma1 = 0
    soma2 = 0
    cont = 0

    for x in range(10, 1, -1):  # Decrementa a multiplicação
        soma1 = soma1 + (int(cpf_digitado[cont]) * x)
        cont += 1

    alg1 = 11 - (soma1 % 11)  # Atribui ao algarismo 1 (10° número do CPF)

    if alg1 > 9:  # Se o algarismo for maior que 9, vira 0.
        digito1 = 0  # Armazeno em uma variável dígito como inteiro e como string para comparação futura.
        strdigito1 = str(0)
    else:
        digito1 = alg1
        strdigito1 = str(alg1)

    cont = 0

    for x in range(11, 2, -1):  # Mesma coisa, só que com o 11° dígito.
        soma2 = soma2 + (int(cpf_digitado[cont]) * x)
        cont += 1

    soma2 = soma2 + (digito1 * 2)  # Reutiliza o 10° dígito para o cálculo do segundo algarismo.
    alg2 = 11 - (soma2 % 11)

    if alg2 > 9:
        digito2 = str(0)
    else:
        digito2 = str(alg2)

    if cpf_digitado[9] == strdigito1 and cpf_digitado[10] == digito2:  # Compara os dois últimos algarismos gerados com
        print("Parabéns, o CPF é válido.")                             # o CPF digitado.
        break
    else:
        print("CPF Inválido!")
