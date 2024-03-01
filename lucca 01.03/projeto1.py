id_livro = 0
numero_membro = 0

class Livro:
    def __init__(self, titulo:str, autor:str, id:int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.disponivel = True

class Membro:
    def __init__(self, nome:str, numero:int) -> None:
        self.nome = nome
        self.numero = numero
        self.historico = []
    
class Biblioteca:
    def __init__(self) -> None:
        self.catalogo_livros = []
        self.registro_membros = []
    
    def adicionar_livro(self):
        global id_livro
        titulo_livro = str (input("Digte o nome do titulo: "))
        autor_livro = str (input("Digte o nome do autor: "))

        livro = Livro(titulo=titulo_livro,autor=autor_livro,id=id_livro)
        self.catalogo_livros.append(livro)
        id_livro += 1
        return "Livro adicionado"

    def adicionar_membro(self):
        global numero_membro
        nome_membro= str(input("Digite o nome do membro:"))

        membro= Membro(nome=nome_membro,numero=numero_membro)
        self.registro_membros.append(membro)
        numero_membro +=1

    def emprestar_livro(self):
        nome_emprestimo = str(input("Qual seu nome de membro:"))
        livro_emprestimo = str(input("Qual o nome do livro:"))

        nomesDeMembros = list(map(lambda membro: membro.nome, self.registro_membros))
        nomesDeLivros = list(map(lambda livro: livro.titulo, self.catalogo_livros))
        

        if nome_emprestimo in nomesDeMembros and livro_emprestimo in nomesDeLivros:
            print("Você ja esta registrado, é seu livro esta disponivel")
        elif nome_emprestimo not in nomesDeMembros and livro_emprestimo in nomesDeLivros:
             print("Voce nao esta registrado,seu livro esta disponivel")
        elif nome_emprestimo in nomesDeMembros and livro_emprestimo not in nomesDeLivros:
             print("Você ja esta registrado, porem o livro ja esta alugado")
        else:
            print("Registro invalido, e livro ja alugado")
    
    def devolver_livro(self):
        pass

    def pesquisar_livro(self):
       pesquisa_digitada = str(input("Digite o título, autor ou ID do livro que você deseja: "))
       for livro_atual in self.catalogo_livros:
            if livro_atual.titulo == pesquisa_digitada or livro_atual.autor == pesquisa_digitada or str(livro_atual.id) == pesquisa_digitada:
                livro_existe = True
                print(f"""
                Informações do Livro:
                ID do livro: {livro_atual.id}
                Título do livro: {livro_atual.titulo}
                Autor do livro: {livro_atual.autor}
                Disponibilidade do livro: {livro_atual.disponivel}
                """)
       if livro_existe == False:
           print("Livro noa encontrado")      

biblioteca1 = Biblioteca()

while True:
    menu= int(input("""
    Escolha uma opção
    1 - Adicionar Livro
    2 - Adicionar Membro
    3 - Emprestar Livro
    4 - Devolver Livro
    5 - Pesquisar Livro
    0 - Sair
    """))
    match menu:
        case 1:
            print(biblioteca1.adicionar_livro())
        case 2:
            print(biblioteca1.adicionar_membro())
        case 3:
            biblioteca1.emprestar_livro()
        case 4:
            biblioteca1.devolver_livro()
        case 5:
            biblioteca1.pesquisar_livro()
        case 0:
            print("Valeu meu fi, volte mais nao")
            break
        case _:
            print("Opção inválida")