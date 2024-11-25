'''
Há alghum tempo eu já haviia feito alguns códigos similares, que realizavam o sorteio de números para algumas apostas lotéricas, no entanto esses arquivos se perderam.
Hoje, com a necessidade de praticar e utilizar o github eu resolvi brincar novamente e trazer a implementação de várias outras modalidades de apostas, porém em um unico arquivo.
'''
import random #importando o módulo random para geração de números aleatórios

# Definindo as funções de sorteio para cada tipo de loteria e suas peculiaridades.
## Função para o calculo da mega-sena
def mega_sena(total_dezenas=6, intervalo=(1, 60)):
    numeros_sorteados = random.sample(range(intervalo[0], intervalo[1] + 1), total_dezenas)
    return sorted(numeros_sorteados)

## Função para o calculo da dupla-sena
def dupla_sena(total_dezenas=6, intervalo=(1, 50)):
    numeros_sorteados = random.sample(range(intervalo[0], intervalo[1] + 1), total_dezenas)
    return sorted(numeros_sorteados)

## Função para o calculo da quina
def quina(total_dezenas=5, intervalo=(1, 80)):
    numeros_sorteados = random.sample(range(intervalo[0], intervalo[1] + 1), total_dezenas)
    return sorted(numeros_sorteados)

## Função para o calculo da lotofacil
def lotofacil(total_dezenas=15, intervalo=(1, 25)):
    numeros_sorteados = random.sample(range(intervalo[0], intervalo[1] + 1), total_dezenas)
    return sorted(numeros_sorteados)

## Função para o calculo da milionária
def milionaria(total_dezenas=6, intervalo=(1, 50)):
    numeros_sorteados = random.sample(range(intervalo[0], intervalo[1] + 1), total_dezenas)
    return sorted(numeros_sorteados)
## Função para o calculo dos trevos da milionária.
def trevo(total_trevos=2, intervalo=(1, 6)):
    trevos = random.sample(range(intervalo[0], intervalo[1] + 1), total_trevos)
    return sorted(trevos)

## Função para o calculo da lotomania.
def lotomania(total_dezenas=50, intervalo=(1, 100)):
    numeros_sorteados = random.sample(range(intervalo[0], intervalo[1] + 1), total_dezenas)
    return sorted(numeros_sorteados)

## Função para o calculo da dia de sorte.
def dia_de_sorte(total_dezenas=7, intervalo=(1, 31)):
    numeros_sorteados = random.sample(range(intervalo[0], intervalo[1] + 1), total_dezenas)
    return sorted(numeros_sorteados)
## Função para o calculo do mês da dia de sorte.
def mes(mes_num=1):
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    if 1 <= mes_num <= 12:
        return meses[mes_num - 1]
    else:
        return "Mês inválido! Informe um número entre 1 e 12."

# Função que solicita que o usuário escolha qual a loteria que ele deseja realizar o sorteio das desenas. Entre () a quantidade mín. e a máx permitida em cada tipo de aposta.
def escolher_loteria():
    escolha = int(input("Escolha uma opção:\n1 - Mega Sena\n2 - Dupla Sena\n3 - Quina\n4 - Lotofácil\n5 - Milionária\n6 - Lotomania\n7 - Dia de Sorte\nDigite a sua opção: "))
    if escolha == 1:
        return mega_sena, (6, 20)
    elif escolha == 2:
        return dupla_sena, (6, 15)
    elif escolha == 3:
        return quina, (5, 15)
    elif escolha == 4:
        return lotofacil, (15, 20)
    elif escolha == 5:
        return (milionaria, trevo), (6, 6)
    elif escolha == 6:
        return lotomania, (50, 50)
    elif escolha == 7:
        return (dia_de_sorte, mes), (7, 15)
    else:
        print("Opção inválida!")
        return None, None

#Função responsável pela realização do sorteio com base na opção escolhida pelo usuário.
def realizar_sorteio():
    funcao_escolhida, intervalo_dezenas = escolher_loteria()
    if funcao_escolhida is None:
        return

    if funcao_escolhida == (milionaria, trevo):
        resultado = funcao_escolhida[0]()
        resultado_trevo = funcao_escolhida[1]()
        print("Números sorteados:", resultado)
        print("Trevos:", resultado_trevo)
    elif funcao_escolhida == lotomania:
        quantidade_numeros = 50
        resultado = funcao_escolhida(total_dezenas=quantidade_numeros)
        print("Números sorteados:", resultado)
    elif funcao_escolhida == (dia_de_sorte, mes):
        resultado = funcao_escolhida[0]()
        resultado_mes = mes(random.randint(1, 12))
        print("Números sorteados:", resultado)
        print("Mês:", resultado_mes)
    else:
        quantidade_numeros = int(input(f"Informe a quantidade de dezenas desejadas, entre {intervalo_dezenas[0]} e {intervalo_dezenas[1]}: "))
        if intervalo_dezenas[0] <= quantidade_numeros <= intervalo_dezenas[1]:
            resultado = funcao_escolhida(total_dezenas=quantidade_numeros)
            print("Números sorteados:", resultado)
        else:
            print(f"Erro: O número deve estar entre {intervalo_dezenas[0]} e {intervalo_dezenas[1]}.")

# Chamada para realizar o sorteio
realizar_sorteio()
