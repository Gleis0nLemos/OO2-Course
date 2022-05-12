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

#"herança é o mecanismo pelo qual estendemos a funcionalidade de uma classe. usando uma built-in por exemplo
# class Playlist(list):
class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

#Este método define algo que é iterável e, no caso, precisaremos receber um item
#para que este seja repassado à lista interna que estamos utilizando, isto é, programas.
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas


    def __len__(self):
        return len(self._programas)

########


vingadores = Filme("Vingadores: Guerra Infinita", 2018, 160)
atlanta = Serie("Atlanta", 2018, 2)
peakyB = Serie("Peaky blinders", 2019, 6)
dark = Serie("Dark", 2020, 3)
interes = Serie("Interestelar", 2014, 150)
#f, usado para formatar a apresentação do print
# print(f"{vingadores.nome} - {vingadores.duracao}min : {vingadores.likes} Likes")

########

peakyB.add_likes()
peakyB.add_likes()
peakyB.add_likes()
peakyB.add_likes()
dark.add_likes()
interes.add_likes()
interes.add_likes()
interes.add_likes()
dark.add_likes()
dark.add_likes()
peakyB.add_likes()
peakyB.add_likes()
vingadores.add_likes()
peakyB.add_likes()
dark.add_likes()
dark.add_likes()
vingadores.add_likes()
vingadores.add_likes()
vingadores.add_likes()
atlanta.add_likes()
atlanta.add_likes()
atlanta.add_likes()
# print(f"{atlanta.nome} - {atlanta.temporadas} Temporadas : {atlanta.likes} Likes")

########

filmes_series = [peakyB, dark, interes]           #para criar uma playlist, fazer uma lista nos ajudará a
                                                #ter um acesso mais especificado para buscas de nosso programa de TV
playlist_fds = Playlist("Fim de semana", filmes_series)
print(f"Tamanho da Playlist: {len(playlist_fds)} Programas")

#detalhes = programa.duracao if hasattr(programa, "duracao") else programa.temporadas
#print(f"{programa.nome} - {detalhes} : {programa.likes} Likes")


for programa in playlist_fds:
    print(programa)

print(f"Pertence a Playlist? {vingadores in playlist_fds}")


# Inicialização	__init__                                                                 Inicialização	obj = Novo()
# Representação	__str__, __repr__                                                        Representação	print(obj), str(obj), repr(obj)
# Container, sequência	__contains__, __iter__, __len__, __getitem__                     Container, sequência	len(obj), item in obj, for i in obj, obj[2:3]
# Numéricos	__add__, __sub__, __mul__, __mod__                                           Numéricos	obj + outro_obj, obj * obj
