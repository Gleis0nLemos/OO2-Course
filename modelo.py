#Class são usadas para criação de objetos
class Filme:
    #inicializador __init__(self ... valores chamados de 'atributos' atribuidos a instância/objetos
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()#title deixa as palavras a serem exibidas com a primeira letra maiúscula
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0 #O número de likes só irá mudar de acordo com a interação

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def likes(self):
        return self.__likes

    def add_likes(self):
        self.__likes += 1

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def add_likes(self):
        self.__likes += 1



vingadores = Filme("Vingadores: Guerra Infinita", 2018, 160)
vingadores.add_likes()
#f, usado para formatar a apresentação do print
print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}")

atlanta = Serie("Atlanta", 2018, 2)
atlanta.add_likes()
atlanta.add_likes()
print(f"Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}")
