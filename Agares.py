 import itertools
import sys

# Função para verificar se a senha está correta (simulação)
def verificar_senha(senha):
    senha_correta = "senha123"  # Defina a senha correta aqui
    return senha == senha_correta

# Função para gerar combinações de senha e verificar
def quebrar_senha():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # Caracteres possíveis
    tamanho_maximo = 8  # Tamanho máximo da senha a ser verificada
    
    for tamanho in range(1, tamanho_maximo + 1):
        for tentativa in itertools.product(caracteres, repeat=tamanho):
            senha = ''.join(tentativa)
            if verificar_senha(senha):
                print(f"Senha quebrada: {senha}")
                return

    print("Senha não encontrada.")

# Verifica se há argumentos na linha de comando
if len(sys.argv) != 2:
    print("Uso: python3 agares.py <arquivo>")
    sys.exit(1)

arquivo = sys.argv[1]

# Executa a quebra de senha
print(f"Tentando quebrar a senha do arquivo: {arquivo}")
quebrar_senha()
