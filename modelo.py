#Class são usadas para criação de objetos
class Programa:
    #inicializador __init__(self ... valores chamados de 'atributos' atribuidos a instância/objetos
    def __init__(self, nome, ano):
        self._nome = nome.title()#title deixa as palavras a serem exibidas com a primeira letra maiúscula
        self.ano = ano
        self._likes = 0 #O número de likes só irá mudar de acordo com a interação

                                    #o property permite que você declare uma função para obter o valor
                                    #de um atributo, e, opcionalmente, funções para funcionarem como
    @property                       #o 'setter' e 'deleter' daquele atributo. dentro da classe.
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def likes(self):
        return self._likes

    def add_likes(self):
        self._likes += 1

    def __str__(self):
        return f"{self._nome} - {self.ano} : {self._likes} Likes"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.duracao}min   {self._likes} Likes"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self._nome} - {self.ano} - {self.temporadas} Temporadas   {self._likes} Likes"

vingadores = Filme("Vingadores: Guerra Infinita", 2018, 160)
vingadores.add_likes()
vingadores.add_likes()
#f, usado para formatar a apresentação do print
# print(f"{vingadores.nome} - {vingadores.duracao}min : {vingadores.likes} Likes")

atlanta = Serie("Atlanta", 2018, 2)
atlanta.add_likes()
atlanta.add_likes()
atlanta.add_likes()
# print(f"{atlanta.nome} - {atlanta.temporadas} Temporadas : {atlanta.likes} Likes")



filmes_series = [vingadores, atlanta]           #para criar uma playlist, fazer uma lista nos ajudará a
                                                #ter um acesso mais especificado para buscas de nosso programa de TV

for programa in filmes_series:
    print(programa)
    # detalhes = programa.duracao if hasattr(programa, "duracao") else programa.temporadas
    # print(f"{programa.nome} - {detalhes} : {programa.likes} Likes")