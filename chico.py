import re

def carregar(programa, gaveteiro):

    if len(programa) > 100:
        return "O programa não pode ultrapassar 100 linhas"

    for i in range (len(programa)):

        programa[i] = re.sub('\n','',programa[i])

        if len(programa[i]) < 3:
            return "Comando curto na linha " + str(i+1)

        if len(programa[i]) > 3:
            return "Comando inválido na linha " + str(i+1)
        
        if programa[i][0:2] != "0-":
            try:
                code = int(programa[i])
            except:
                return "Caractere inválido na linha " + str(i+1)

        gaveteiro[i] = programa[i]
        # print(gaveteiro)

    return "Carregado com sucesso"

def usuario_input():
    while True:
        numero = input("Insira um número de 3 digitos: ")
        
        if len(numero) !=3:
            print("Eu disse 3 digitos")
            continue

        try:
            n = int(numero)

            return numero
        except:
            print("Insira apenas números")

def rodar(gaveteiro):
    
    epi = 0

    acumulador = 0

    gaveteiro[12] = 5
    gaveteiro[13] = 3

    while gaveteiro[epi]:

        if gaveteiro[epi] == "000":
            return "Programa finalizado com sucesso"
        
        if gaveteiro[epi][:2] == "0-":
            acumulador = int(gaveteiro[epi][-1])
            epi += 1

        if epi > 99:
            return "Programa atingiu última 'gaveta' sem finalizar"

        match gaveteiro[epi][0]:
            case '0': # Gaveta para Acumulador
                
                ende = int(gaveteiro[epi][1:])
                
                # print(gaveteiro)
                acumulador = int(gaveteiro[ende])

                epi +=1

            case '1': # Acumulador para Gaveta
                ende = int(gaveteiro[epi][1:])
                gaveteiro[ende] = str(acumulador)


                while len(gaveteiro[ende]) < 3:

                    gaveteiro[ende] = "0"+gaveteiro[ende]

                epi+=1

            case '2': # Somar com Acumulador
                ende = int(gaveteiro[epi][1:])
                print((acumulador))
                acumulador += int(gaveteiro[ende])

                epi+=1

            case '3': # Subtrair com Acumulador
                ende = int(gaveteiro[epi][1:])
                acumulador -= int(gaveteiro[ende])

                epi+=1

            case '4': # Multiplicar com Acumulador
                ende = int(gaveteiro[epi][1:])
                acumulador *= int(gaveteiro[ende])

                epi+=1

            case '5': # Dividir com Acumulador
                ende = int(gaveteiro[epi][1:])

                try:
                    acumulador //= int(gaveteiro[ende])
                except ZeroDivisionError:
                    return "Divião por zero, programa finalizado"

                epi+=1

            case '6': # Voltar se Ac > 0
                ende = int(gaveteiro[epi][1:])
                
                if(acumulador > 0):
                    epi = ende
                else:
                    epi +=1

            case '7': # Ler do usuário
                ende = int(gaveteiro[epi][1:])
                gaveteiro[ende] = usuario_input()

                epi+=1

            case '8': # Escrever na saída
                ende = int(gaveteiro[epi][1:])
                print(gaveteiro[ende])

                epi+=1

            case '9': # Ir para endereço
                ende = int(gaveteiro[epi][1:])
                epi = ende