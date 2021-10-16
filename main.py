def criarAluno():
    usuarioAluno = {}
    usuarioAluno["nome"] = input("Digite o nome completo do aluno: ")
    usuarioAluno["email"] = input("Digite o email do aluno: ")
    return usuarioAluno

def mostrarUsuario(listaUsuario):
    for aluno in listaUsuario:
        print(aluno["nome"])
        print(aluno["email"])
        print("")

def ordemAlfabetica(listaUsuario):
      for aluno in listaUsuario:
        print(aluno["nome"])
        print(aluno["email"])

def buscaUsuario(listaUsuario):
    
    usuario = print(input("Digite o nome que deseja buscar: "))
    
    if usuario in listaUsuario:
        print("ta na lista")
    else:
        print("nao ta na lista")    

    return usuario
        
def desenharMenu():
    print("Defina qual ação quer fazer: ")
    print("[1] - Criar um usuário")
    print("[2] - Ver todos os usuários")
    print("[3] - Ver usuários por ordem alfabética")
    print("[4] - Buscar usuário pelo nome")
    print("[5] - Remover um usuário pelo email")
    print("[6] - Alterar nome de um usuário pelo email")
    print("[7] - Sair")
    
   

def escolhaMenu(opcaoUsuario):
    desenharMenu()
    opcaoUsuario = int(input(("Escolha: ")))

    return opcaoUsuario
        
        
def escolhaUsuario():
    escolhaAtual = 0
    listaUsuario = []

    while (escolhaAtual < 7 ):
        opcaoUsuario = escolhaMenu(escolhaAtual)
        while(opcaoUsuario > 7):
            opcaoUsuario = escolhaMenu(escolhaAtual)
        if(opcaoUsuario == 1):
            usuarioAluno = criarAluno()
            listaUsuario.append(usuarioAluno)

        elif(opcaoUsuario == 2):
            mostrarUsuario(listaUsuario)

        elif(opcaoUsuario == 3):
            ordemAlfabetica()

        elif(opcaoUsuario == 4):
            buscaUsuario(listaUsuario)
        elif(opcaoUsuario == 7):
            print("Saindo da sala...")
            break
        
def main():
    escolhaUsuario()
    

if(__name__ == "__main__"):
    main()