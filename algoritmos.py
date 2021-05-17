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

    return str(time.clock_gettime_ns(time.CLOCK_BOOTTIME))[digitos:]

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

def meio_do_quadrado(semente_geradora, digitos):
    """ Retorna o período de repetição gerado por uma semente no algoritmo do meio do quadrado.
    Se nenhuma semente for passada, será uma semente aleatória.
    
    :semente_geradora (str) semente geradora da sequência de números aleatórios
    :digitos (str) digitos da semente geradora
    
    autores Kilian, Vitor
    """
    if not semente_geradora:
        semente_geradora = gera_semente_aleatoria(digitos)
    
    semente = int(semente_geradora)
    digitos_semente_geradora = len(semente_geradora)
    periodo = list()

    while semente not in periodo:
        periodo.append(semente)

        quadrado_da_semente = str(semente ** 2)
        quadrado_da_semente = adiciona_zeros(quadrado_da_semente, digitos_semente_geradora)
        semente = numero_do_meio(quadrado_da_semente, digitos_semente_geradora)

    return periodo

def is_primo(numero):
    """ Checa se um número é primo 
    
    autores Kilian
    """
    if numero == 1: return False
    
    for i in range(2, numero//2+1):
        if (numero % i) == 0:
            return False
    return True

def get_fatores_primos(numero):
    """ Retorna os fatores primos do número
    
    autores Kilian
    """
    fatores = []

    for i in range(1, numero//2+1):
        if is_primo(i) and numero % i == 0:
            fatores.append(i)

    return fatores

def get_A(m):
    """
    Condições de A:
    p: 4 | M
    q: 4 | A-1
    r: A > 0
    s: A-1 é divisivel por todos os fatores primos de m. 
    (p → q) ∧ r ∧ s

    autores Kilian, Daniel
    """
    a = 1
    if m % 4 == 0:
        a = 5
    
    fatores = get_fatores_primos(m)

    while True:
        for f in fatores:
            if (a-1) % f == 0:
                return a 
        a += 1

def get_C(m):
    """
    Condições de C:
    p: C > 0
    q: C é primo relativo a M
    p ∧ q

    autores Kilian, Daniel
    """
    c = 2
    while True:
        if m % c != 0:
            return c
        c += 1

def congruencia_linear(semente_geradora, m):
    """ Retorna o período de repetição gerado por uma semente no algoritmo da congruência linear.
    
    autores Kilian, Daniel
    """
    a = get_A(m)
    c = get_C(m)
    
    periodo = list()

    semente_geradora = int(semente_geradora)
    elemento = semente_geradora

    while elemento not in periodo:
        periodo.append(elemento)
        elemento = ( a * elemento + c ) % m

    return periodo

def salvar(saida):
    """ Salva a saida do programa em um arquivo 
    
    autores Kilian
    """ 
    escolha = input("Você deseja salvar esse resultado? (y/N)")

    if escolha == "y" or escolha == "Y":
        arquivo = open("saida.txt", "w")
        arquivo.write(saida)    
        arquivo.close()

def saida(periodo):
    """ Retorna uma mensagem com a saida do programa 
    
    autores Kilian
    """
    mensagem = f"Essa semente gerou um período de {len(periodo)} elementos"
    mensagem += "\nConjunto dos elementos gerados: \n" + str(periodo)     
    return mensagem

def menu():
    """ Menu para interação com o usuário 
    
    autores Kilian
    """
    mensagem = "\n\n--- Gerador de números pseudo-aleatórios ---\n"
    mensagem += "\nQual algoritmo você deseja usar?"
    mensagem += "\n(1) - Algoritmo do meio do quadrado"
    mensagem += "\n(2) - Algoritmo da congruência linear"
    mensagem += "\n(3) - Sair\n\n"

    while True:
        escolha = int(input(mensagem))
        if escolha == 1:

            semente = input("Insira uma semente: ")
            if not semente:
                digitos = int(input("Quantos digitos terá a semente aleatória?"))
            else:
                digitos = len(semente)
            
            periodo = meio_do_quadrado(semente, digitos)
            
            resultado = saida(periodo)
            print (resultado)

            if len(periodo) > 1000:
                salvar(resultado)

        elif escolha == 2:

            semente = input("Insira uma semente: ")
            m = int(input("Escolha o módulo: "))

            if not semente:
                semente = gera_semente_aleatoria(4)

            if m > 65536:
                print ("\nNúmero grande demais! Por razões de segurança isso não é permitido")
                continue

            periodo = congruencia_linear(semente, m)
            
            resultado = saida(periodo)
            print (resultado)

            if len(periodo) > 1000:
                salvar(resultado)

        elif escolha == 3:
            break

menu()