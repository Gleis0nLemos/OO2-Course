#Class são usadas para criação de objetos
class Filme:
    #inicializador __init__(self ... valores chamados de 'atributos' atribuidos a instância/objetos
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

# vingadores = Filme("Vingadores-Guerra Infinita", 2018, 160)
# print(vingadores)
