# Importação de módulos/classes
# Importando o dicionario de usuários
import app.dicionarios as dic



# Criando classe referente as autenticações

class Autenticacao:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
    
    # Criando função 
    def autenticacao(self):
        # Condição com base no nome de usuário e senha da entrada main
        if self.usuario in dic.medicos_autorizados and dic.medicos_autorizados[self.usuario] == self.senha:
            print(f'Usuário {nome} entrou no sistema com sucesso.')
            return True

        else:
            print(f'Acesso negado! {usuario}')
    
    
        
        
