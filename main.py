# Arquivo Principal

# Importação de módulos/classes
from app.autenticacao import Autenticacao as aut

# Função para "Tela" principal

def main():
    print("Bem vindo ao Sistema EasyConsult") # Saída
    # Entrada
    tipo_de_registro = input("Você tem duas opções de entrada. Digite 'M' para médico ou 'P' para paciente:\t").lower()
    
    # Condição
    if tipo_de_registro == 'p':
        usuario = input('Digite seu usuário:\t') # Entradas
        senha = input('Digite sua senha:\t')
        autenticacao = aut(usuario, senha)
        
        if autenticacao.autenticacao():
            
        else:
            print('Aceso negado!')
            
    elif tipo_de_registro == 'm':
        print('Bem Vindo!')
    else:
        print("\nOpção inválida. Por favor, responda 'M' ou 'P'.\n")
        
#Chamando função main

main()

