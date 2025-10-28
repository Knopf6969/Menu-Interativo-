import funcoes # Importei as funções que defini anteriormente 
import sys # Importa o módulo sys para sair do programa

treinos = []

def main():

    funcoes.registrar_log("Iniciando menu interativo")
    funcoes.carregar_dados(treinos)

    while True: # Criando mensagem de introdução ao menu interativo 
        funcoes.limpar_terminal()
        print("""
------------- Sistema de registro de treinos -------------
                  1 - Cadastrar treino
                  2 - Listar treinos existentes 
                  3 - Editar treinos existentes 
                  4 - Deletar treinos 
                  5 - Sair do menu
--------------------------------------------------------
""")
