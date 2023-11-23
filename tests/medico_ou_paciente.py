
def main():
    print("Bem vindo ao sistema EasyConsult") # Saída
    # Entrada. Perguntando se é médico ou paciente.
    tipo_de_registro = input("Você tem duas opções de entrada. Digite 'M' para médico ou 'P' para paciente:\t").lower()
    
    # Verificando opção da entrada
    if tipo_de_registro == 'p':
        print('Bem vindo Paciente!')
    elif tipo_de_registro == 'm':
        print('Bem vindo Médico!')
    else:
        print("\nOpção inválida. Por favor, responda 'M' ou 'P'.\n")
main()