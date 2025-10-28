import os 
from datetime import datetime

# Usaremos chaves curtas e padronizadas para facilitar
CHAVES_TREINO = [
    "dia_semana",
    "grupo_muscular",
    "exercicios",
    "series",
    "repeticoes",
    "observacao"
]

def limpar_terminal():
    """Limpa o terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def registrar_log(acao_do_usuario):
    """Registra a ação do usuário no arquivo de log, usando 'with open'."""
    try:
        # Caminho corrigido para a pasta 'Dados'
        with open("Dados/logs.sistema", "a", encoding="utf-8") as arquivo_de_log:
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            arquivo_de_log.write(f"[{data_hora}] {acao_do_usuario} \n")
    except FileNotFoundError:
        print("AVISO: Arquivo de log não encontrado. O log não foi registrado.")

def carregar_dados(treinos):
    """Carrega os treinos do arquivo para a lista, com lógica corrigida e tratamento de erro."""
    try:
        # Caminho corrigido para a pasta 'Dados'
        with open("Dados/treinos.sistema", "r", encoding="utf-8") as arquivo_de_treinos:
            linhas = arquivo_de_treinos.readlines()
            
            # Limpa a lista antes de carregar novos dados
            treinos.clear() 
            
            for linha in linhas:
                # Ignora linhas vazias ou de cabeçalho
                if not linha.strip():
                    continue
                
                # Usado para evitar erros se a linha estiver incompleta
                partes = linha.strip().split(";")
                if len(partes) == len(CHAVES_TREINO):
                    treino_dict = dict(zip(CHAVES_TREINO, partes))
                    treinos.append(treino_dict)
                else:
                    registrar_log(f"ERRO: Linha de treino ignorada devido a formato incorreto: {linha.strip()}")
            
    except FileNotFoundError:
        # Cria o arquivo se ele não existir
        print("AVISO: Arquivo de treinos não encontrado. Iniciando com lista vazia.")
        salvar_dados(treinos) # Cria o arquivo vazio
    except Exception as e:
        registrar_log(f"ERRO ao carregar dados: {e}")
        print(f"ERRO: Não foi possível carregar os dados. {e}")

