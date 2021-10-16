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
        
        
def escolhaUsuario():
    opcaoUsuario = 0
    listaUsuario = []

    while (opcaoUsuario < 7 ):
        opcaoUsuario = int(input("Defina qual ação quer fazer: "))
        if(opcaoUsuario == 1):
            usuarioAluno = criarAluno()
            listaUsuario.append(usuarioAluno)

        elif(opcaoUsuario == 2):
            mostrarUsuario(listaUsuario)

        elif(opcaoUsuario == 3):
            listaUsuario.sort()
            ordemAlfabetica()
            

        elif(opcaoUsuario == 7):
            print("Saindo da sala...")
            break
        else:
            print("Opção não foi reconhecida..")
            break
            
            

def main():
    escolhaUsuario()
    
       
    
if(__name__ == "__main__"):
    main()