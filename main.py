from time import sleep
def criarAluno(usuario):
    
    nome = input('Qual seu nome: ')
    email = input('Qual seu e-mail: ')
    
    usuario.append((nome, email))

def mostrarUsuario(usuario):
    for mostrar in usuario:
        nome, email = mostrar
        print(f'Nome: {nome} - email: {email}')

def ordemAlfabetica(usuario):   
    ordem = usuario
    ordem.sort()
    print(f"Lista ordenada: ", ordem)
        

    
        
def buscaUsuario(usuario):
    nome_desejado = input('qual nome voce quer procurar: ')
    for pessoa in usuario:
        nome, email = pessoa
        if nome == nome_desejado:
            print(f'Nome: {nome}, email: {email}')
            break
        else:
            print(f'Usuario com nome {nome_desejado} não foi encontrado')

def removerUsuario(usuario):
    email_desejado = input('qual email voce quer procurar: ')
    for pessoa in usuario:
        nome, email = pessoa
        if email == email_desejado:
            usuario.remove((nome, email))
            print("Usuario foi removido com sucesso!")
            break
        else:
            print(f'Usuario com email {email_desejado} não foi encontrado')
     

def alterarUsuario(usuario):
    
    email_desejado = input('qual email voce quer procurar: ')
    for pessoa in usuario:
        nome, email = pessoa
        if email == email_desejado:
            usuario.remove((nome))
            nome = input('Qual seu novo nome: ')
            usuario.append((nome))
            print("Usuario esta com o nome trocado!")
            break
        else:
            print(f'Usuario com email {email_desejado} não foi encontrado')
    #não conseguimos
        
def desenharMenu():
    print("---------------------------------------------------")
    print("")
    print("Defina qual ação quer fazer: ")
    print("[1] - Criar um usuário")
    print("[2] - Ver todos os usuários")
    print("[3] - Ver usuários por ordem alfabética")
    print("[4] - Buscar usuário pelo nome")
    print("[5] - Remover um usuário pelo email")
    print("[6] - Alterar nome de um usuário pelo email")
    print("[7] - Sair")
    print("")
    print("---------------------------------------------------")
    
   

def escolhaMenu(opcaoUsuario):
    desenharMenu()
    opcaoUsuario = int(input(("Escolha: ")))

    return opcaoUsuario
        
        
def escolhaUsuario():
    escolhaAtual = 0
    usuario = []

    while True:
        opcaoUsuario = escolhaMenu(escolhaAtual)
        while(opcaoUsuario > 7):
            print("Numero não foi reconhecido...Escolha outro!")
            print("")
            sleep(2)
            opcaoUsuario = escolhaMenu(escolhaAtual)
        if(opcaoUsuario == 1):
            criarAluno(usuario)

        elif(opcaoUsuario == 2):
            mostrarUsuario(usuario)

        elif(opcaoUsuario == 3):
            ordemAlfabetica(usuario)
            
        elif(opcaoUsuario == 4):
            buscaUsuario(usuario)

        elif(opcaoUsuario == 5):
            removerUsuario(usuario)

        elif(opcaoUsuario == 6):
            alterarUsuario(usuario)
            
        elif(opcaoUsuario == 7):
            print("Saindo da sala...")
            break
        sleep(2)
        
def main():
    escolhaUsuario()
    

if(__name__ == "__main__"):
    main()