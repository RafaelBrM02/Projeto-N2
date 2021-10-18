from time import sleep
def criarAluno(usuario):
    
    nome = input('Nome? ')
    email = input('email? ')
    
    usuario.append((nome, email))

def mostrarUsuario(usuario):
    for mostrar in usuario:
        nome, email = mostrar
        print(f'Nome: {nome} - email: {email}')

def ordemAlfabetica(usuario):
        usuario.sort(reverse=False)
        print("Lista Ordenada:", usuario)
       

def buscaUsuario(usuario):
    nome_desejado = input('qual nome: ')
    for pessoa in usuario:
        nome, email = pessoa
        if nome == nome_desejado:
            print(f'Nome: {nome}, email: {email}')
            break
    else:
        print(f'Usuario com nome {nome_desejado} não encontrado')

def removerUsuario(usuario):
    email = input('email? ')
    
    usuario.remove((email)) 

def alterarUsuario(usuario):
     print("ok")
        
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
            print("Usuario foi removido!!")

        
            
        elif(opcaoUsuario == 7):
            print("Saindo da sala...")
            break
        sleep(2)
        
def main():
    escolhaUsuario()
    

if(__name__ == "__main__"):
    main()