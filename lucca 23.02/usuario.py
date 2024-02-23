class Tarefa:
    def __init__(self,prioridade=str,categoria=str,desc=str) -> None:
        self.prioridade=prioridade
        self.desc=desc
        self.categoria= categoria


class Projeto:
    def __init__(self,nome=str,objetivo=str, lista_tarefas=list) -> None:
        self.nome = nome
        self.objetivo = objetivo
        self.lista_tarefas = lista_tarefas

tarefa1= Tarefa(desc="Estudar POO em Python",categoria="Academico",prioridade="alta")
tarefa2= Tarefa(desc="treino de perna",categoria="saude",prioridade="media")
tarefa3= Tarefa(desc="Lavar louça",categoria="Domestica",prioridade="media")
tarefa4= Tarefa(desc="conhecer uma nova linguagem",categoria="Academico",prioridade="baixa")
tarefa5= Tarefa(desc="ir para um supermodolo",categoria="Academico",prioridade="alta")
tarefa6= Tarefa(desc="fazer cardio",categoria="saude",prioridade="media")
tarefa7= Tarefa(desc="tomar suplemento",categoria="saude",prioridade="media")

projeto1= Projeto(nome="fit",objetivo= "ficar gostoso",lista_tarefas=[tarefa2,tarefa6,tarefa7])

projeto2 = Projeto(nome="Programador",objetivo="ficar mais focado",lista_tarefas=[tarefa1,tarefa4,tarefa5])

for item_atual in projeto1.lista_tarefas:
    print(f"""
    Descrição: {item_atual.desc}
    Categoria: {item_atual.categoria}
    Prioridade: {item_atual.prioridade}
""")
