class Funcionario:
    def __init__(self, nome:str, cargo:str, salario:float) -> None:
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Empresa:
    def __init__(self) -> None:
        self.lista_de_funcionarios = []
    
    def adicionar_funcionario(self):
        nome_funcionario = str(input("Digite o nome do funcionário: "))
        cargo_funcionario = str(input("Digite o cargo do funcionário: "))
        salario_funcionario = float(input("Digite o salario do funcionário: "))

        funcionario = Funcionario(nome=nome_funcionario, cargo=cargo_funcionario, salario=salario_funcionario)
        
        self.lista_de_funcionarios.append(funcionario)

        return "Funcionário adicionado com sucesso"

    def excluir_funcionario(self):
        nome_do_excluido = str(input("Digite o nome do funcinonário que você quer excluir: "))
        for func_atual in self.lista_de_funcionarios:
            if func_atual.nome == nome_do_excluido:
                self.lista_de_funcionarios.remove(func_atual)
                return "Funcionário excluído com sucesso"


    def listar_funcionarios(self):
        for func_atual in self.lista_de_funcionarios:
            print(f"""
            Nome do Funcionário: {func_atual.nome}
            Cargo do Funcionário: {func_atual.cargo}
            Salário do Funcionário: {func_atual.salario}
            """)


empresa1 = Empresa()

while True:
    menu = int(input("""
    Escolha uma opção:
    1 - Adicionar funcionário
    2 - Excluir funcionário
    3 - Listar funcionários
    0 - Sair
"""))
    match menu:
        case 1:
            print(empresa1.adicionar_funcionario())
        case 2:
            print(empresa1.excluir_funcionario())
        case 3:
            print(empresa1.listar_funcionarios())
        case 0:
            break
        case _:
            print("Opção inválido")