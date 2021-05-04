import time
import random

NUMEROUSUARIOS = 10000

def cadastramento_completo(usuarios):
    """ Testa se todos os usuário foram cadastrados """
    for i in range(NUMEROUSUARIOS):
        if i not in usuarios:
            return False
    return True

def algoritmo1():
    usuarios = []

    for i in range(NUMEROUSUARIOS):
        
        while True:
            id_aleatorio = random.randrange(NUMEROUSUARIOS)
            if id_aleatorio not in usuarios:
                usuarios.append(id_aleatorio)
                break

def algoritmo2():
    pass


comeco = time.time()
algoritmo1()
fim = time.time()

duracao = fim - comeco

print (f"{duracao:.4f}")
