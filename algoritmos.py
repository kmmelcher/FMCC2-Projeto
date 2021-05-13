import time

def gera_semente_aleatoria(digitos):
    """ Retorna uma semente aleatória com um dado número de dígitos.
    Essa semente é composta pelos últimos digitos do tempo, em nanossegundos,
    desde que o computador atual ligou
    
    :digitos número de digitos 

    autores Kilian
    """
    if not digitos:
        digitos = 4

    return int(str(time.clock_gettime_ns(time.CLOCK_BOOTTIME))[digitos:])


def adiciona_zeros(numero, digitos):
    """ Adiciona zeros na frente do número de acordo com o seu tamanho.
    Se o número de dígitos for um número par, multiplica-se por dois
    e adiciona zeros até completar a quantidade de digitos desejada.
    Se for ímpar, multiplica-se por dois e soma-se um.
    De forma que seja possível pegar o número do meio.
    
    :numero (str) número a ser adicionado zeros
    :digitos (int) quantidade de digitos a ser checado
    
    autores Kilian, Vitor
    """

    if digitos % 2 == 0:
        numero.zfill(digitos * 2)
    else:
        numero.zfill(digitos * 2 + 1)

    return numero

def numero_do_meio(numero, digitos):
    """ Retorna os digitos do meio de um número
    
    :numero (str) numero para extrair o meio
    :digitos (int) quantidade de digitos a serem extraidos do numero
    
    autores Kilian, Vitor
    """
    meio = len(numero) // 2
    variavel = digitos//2

    if digitos % 2 == 0:
        numero_do_meio = int(str(numero[meio-variavel : meio+variavel]))
    else:
        numero_do_meio = int(str(numero[meio-variavel : meio+variavel+1]))
      
    return numero_do_meio

def quadrado_do_meio(semente_geradora, digitos):
    """ Retorna o período de repetição de uma semente do algoritmo do quadrado
    do meio.
    Se nenhuma semente for passada, será uma semente aleatória.
    
    :semente_geradora (str) semente geradora da sequência de números aleatórios
    :digitos (str) digitos da semente geradora
    
    autores Kilian, Vitor
    """
    
    if not semente_geradora:
        semente_geradora = gera_semente_aleatoria(digitos)
    
    semente = int(semente_geradora)
    digitos_semente_geradora = len(semente_geradora)
    periodo = set()

    while semente not in periodo:
        periodo.add(semente)

        quadrado_da_semente = str(semente ** 2)

        if len(quadrado_da_semente) <= digitos_semente_geradora:
            semente = int(quadrado_da_semente)
        else:
            quadrado_da_semente = adiciona_zeros(quadrado_da_semente, digitos_semente_geradora)
            semente = numero_do_meio(quadrado_da_semente, digitos_semente_geradora)

    return periodo

def menu():
    """ Menu para interação com o usuário 
    
    autores Kilian
    """
    mensagem = "\n\n--- Gerador de números aleatórios ---\n"
    mensagem += "\nQual algoritmo você deseja usar?"
    mensagem += "\n(1) - Algoritmo do quadrado do meio"
    mensagem += "\n(2) - Algoritmo da congruência linear"
    mensagem += "\n(3) - Sair\n\n"

    while True:
        escolha = int(input(mensagem))
        if escolha == 1:
            semente = input("Insira uma semente: ")
            
            if not semente:
                digitos = int(input("Quantos digitos terá o número?"))
            else:
                digitos = len(semente)
            
            periodo = quadrado_do_meio(semente, digitos)
            
            print (f"Essa semente gerou uma sequência de números aleatórios que se repetem a cada {len(periodo)} elementos")
            print ("Conjunto dos elementos gerados: \n" + str(periodo))
        elif escolha == 2:
            pass
        elif escolha == 3:
            break
    
menu()