tamanho = int(input("Digite o tamanho do vetor: "))
vetor = [None] * tamanho
for i in range(tamanho):
    elemento = int(input(f"Digite o elemento {i+1} do vetor: "))
    vetor[i] = elemento
print("Vetor preenchido:", vetor)

vetor2 = [None] * tamanho
for i in range(tamanho):
    elemento2 = int(input(f"Digite o elemento {i+1} do vetor 2: "))
    vetor2[i] = elemento2
print("Vetor preenchido:", vetor2)

while True:
    print("Bem-vindo ao Menu Principal!")
    print("Escolha uma opção:")
    print("1 - Exercícios Nivel 1")
    print("2 - Exercícios Nivel 2")
    print("3 - Sair")
    opcao = input("\n Digite o número da opção desejada: ")

    match opcao:
        case "1":
            while True:
                print("\nBem-vindo ao Menu de Exercícios Nivel 1!")
                print("Escolha uma opção:")
                print("1 - Primeiro Elemento ")
                print("2 - Numero Negativo ")
                print("3 - Soma Vetor")
                print("4 - Media vetor")
                print("5 - Impar ")
                print("6 - Primeiro e Ultimo")
                print("7 - Pares")
                print("8 - Valor Passado")
                print("9 - ordenar")
                print("10 -  Voltar para o Menu Principal")
                opcao_nivel1 = input("Digite o número da opção desejada: \n")

                match opcao_nivel1:
                    case "1":
                        def primeiroElem(vetor: list) -> int:
                            primeiro = len(vetor)
                            return vetor[primeiro - 5]
                        exb = primeiroElem(vetor)
                        print("Resposta: ")
                        print(exb)

                    case "2":
                        def nNegativo(vetor: list) -> None:
                            for i in range(len(vetor)):
                                if (vetor[i] < 0):
                                    print(f"{vetor[i]}")
                        print("Resposta: ")
                        exb = nNegativo(vetor)

                    case "3":
                        def somaVetor(vetor: list) -> int:
                            soma = 0
                            for i in range(len(vetor)):
                                soma = vetor[i] + soma
                            return soma
                        print("Resposta: ")
                        print(somaVetor(vetor))

                    case "4":
                        def mediaElem(vetor: list) -> int:
                            soma = 0
                            for i in range(len(vetor)):
                                soma += vetor[i]
                            media = soma / i
                            return media
                        print("Resposta: ")
                        print(mediaElem(vetor))
                    case "5":
                        def listImpar(vetor: list) -> None:
                            for i in range(len(vetor)):
                                if (vetor[i] % 2 == 1):
                                    print(vetor[i])
                        print("Resposta: ")
                        listImpar(vetor)

                    case "6":
                        def primUltElem(vetor: list) -> None:
                            primeiro = vetor[0]
                            ultimo = vetor[4]
                            print(primeiro, ultimo)
                        print("Resposta: ")
                        primUltElem(vetor)

                    case "7":
                        def paresNum(vetor: list) -> None:
                            for i in range(len(vetor)):
                                if (vetor[i] % 2 == 0):
                                    print(vetor[i])
                        print("Resposta: ")
                        paresNum(vetor)

                    case "8":
                        n = int(input(print("Digite um numero: ")))
                        def valPassad(vetor: list, n: int) -> int:
                            for i in range(len(vetor)):
                                if (vetor[i] == n):
                                    return True
                                else:
                                    return False
                        print("Resposta: ")
                        print(valPassad(vetor, n))

                    case "9":
                        def ordenar(vetor: list) -> int:
                            for i in range(len(vetor)):
                                for aux2 in range(i, len(vetor)):
                                    if (vetor[i] > vetor[aux2]):
                                        aux1 = vetor[i]
                                        vetor[i] = vetor[aux2]
                                        vetor[aux2] = aux1
                            return vetor
                        print("Resposta: ")
                        exb = ordenar(vetor)
                        print(exb)
                    case "10":
                        break
                    case _:
                        print("Opção inválida. Por favor, tente novamente.")

        case "2":
            while True:
                print("\nBem-vindo ao Menu de Nivel 2!")
                print("Escolha uma opção:")
                print("1 - Copiar Vetor")
                print("2 - Inverter Vetor")
                print("3 - Ordena Crescente")
                print("4 - Ordena Decrescente")
                print("5 - Ordena Vetor")
                print("6 - Separa Vetor")
                print("7 - Conta Acima Media")
                print("8 - Maior Elemento")
                print("9 - Busca Vetor")
                print("10 - Voltar ao Menu Principal")
                opcao_nivel2 = input("Digite o número da opção desejada: \n")

                match opcao_nivel2:
                    case "1":
                        def copiaVetor(vetor: list, vetor2: list) -> None:
                            for i in range(len(vetor)):
                                vetor2[i] = vetor[i]
                            print(f"v1 = {vetor} e v2 = {vetor2}")
                        copiaVetor(vetor, vetor2)

                    case "2":
                        def inverteVetor(vetor1: list, vetor2: list) -> None:
                            for i in range(len(vetor)):
                                vetor2[i] = vetor[i]
                                ultimo = len(vetor2)
                                for i in range(len(vetor2)):
                                    vetor2[i] = ultimo
                                    ultimo -= 1
                            print(vetor2)
                        inverteVetor(vetor, vetor2)

                    case "3":
                        def ordena_vetor_crescente(vetor: list, vetor2: list) -> None:
                            for i in range(len(vetor)):
                                vetor2[i] = vetor[i]
                                for i in range(len(vetor2)):
                                    for aux2 in range(i, len(vetor2)):
                                        if (vetor2[i] > vetor[aux2]):
                                            aux1 = vetor2[i]
                                            vetor2[i] = vetor[aux2]
                                            vetor[aux2] = aux1
                            print(vetor2)
                        ordena_vetor_crescente(vetor, vetor2)

                    case "4":
                        def ordena_vetor_decrescente(vetor: list, vetor2: list) -> None:
                            for i in range(len(vetor)):
                                vetor2[i] = vetor[i]
                                for i in range(len(vetor2)):
                                    for aux2 in range(len(vetor2)):
                                        if (vetor2[i] > vetor2[aux2]):
                                            aux1 = vetor2[i]
                                            vetor2[i] = vetor2[aux2]
                                            vetor2[aux2] = aux1
                            print(vetor2)
                        ordena_vetor_decrescente(vetor, vetor2)

                    case "5":
                        def ordena_vetor(vetor: list, vetor2: list, forma: str) -> None:
                            if (forma == 'c'):
                                for i in range(len(vetor)):
                                    vetor2[i] = vetor[i]
                                    for i in range(len(vetor2)):
                                        for aux2 in range(i, len(vetor2)):
                                            if (vetor2[i] > vetor[aux2]):
                                                aux1 = vetor2[i]
                                                vetor2[i] = vetor[aux2]
                                                vetor[aux2] = aux1
                                print(vetor2)
                            elif (forma == 'd'):
                                for i in range(len(vetor)):
                                    vetor2[i] = vetor[i]
                                    for i in range(len(vetor2)):
                                        for aux2 in range(len(vetor2)):
                                            if (vetor2[i] > vetor2[aux2]):
                                                aux1 = vetor2[i]
                                                vetor2[i] = vetor2[aux2]
                                                vetor2[aux2] = aux1
                                print(vetor2)
                        ordena_vetor(vetor, vetor2, 'c')

                    case "6":
                        def sepera_vetor(vetor: list) -> None:
                            for i in range(0, len(vetor)):
                                if (vetor[i] % 2 == 0):
                                    for j in range(0, len(vetor)):
                                        if (vetor[j] % 2 == 1):
                                            aux = vetor[i]
                                            vetor[i] = vetor[j]
                                            vetor[j] = aux
                            print(vetor)
                        sepera_vetor(vetor)

                    case "7":
                        def conta_acima_media(vetor: list) -> int:
                            total = 0
                            j = 0
                            for i in range(0, len(vetor)):
                                total += vetor[i]
                            div = total / len(vetor)
                            for i in range(len(vetor)):
                                if vetor[i] > div:
                                    j += 1
                            return j
                        print(conta_acima_media(vetor))

                    case "8":
                        def maior_elemento(vetor: list) -> int:
                            maior = 0
                            for i in range(len(vetor)):
                                if maior < vetor[i]:
                                    maior = vetor[i]
                            return maior
                        print(maior_elemento(vetor))

                    case "9":
                        n = int(input(print("Digite um numero: ")))
                        def busca_vetor(vetor: list, n: int) -> int:
                            for i in range(len(vetor)):
                                if n == vetor[i]:
                                    return True
                            return False
                        print(busca_vetor(vetor, n))

                    case "10":
                        break
                    case _:
                        print("Opção inválida. Por favor, tente novamente.")

        case "3":
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida. Por favor, tente novamente")