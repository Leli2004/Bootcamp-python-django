''' 
    POO
    Gerenciamento de Biblioteca
    Vamos criar um sistema orientado a objetos para representar um sistema de biblioteca seguindo os requisitos abaixo
    - Cada livro pode ter um ou mais autores;
    - A biblioteca controla apenas o nome, o telefone e a nacionalidade de cada usuário;
    - Cada livro tem um título, editora, uma lista de gêneros aos quais pertence e uma lista de exemplares disponíveis;
    - Quando um exemplar é emprestado, ele é removido da lista de exemplares disponíveis;
    - Alguns livros podem ter um número máximo de renovações permitidas; 
    - A biblioteca mantém um registro de todos os empréstimos realizados, incluindo detalhes como data de empréstimo, data de devolução e estado do exemplar (por exemplo, emprestado ou devolvido);
    Para modelar o sistema, utilize obrigatoriamente os conceitos de classe, herança, propriedade, encapsulamento e classe abstrata.
'''

class Livro():
    def livro(self, autor, titulo, editora, genero, emprestado):
        self.autor = autor
        self.titulo = titulo
        self.editora = editora
        self.genero = genero
        self.emprestado = emprestado

class Usuario():
    def usuario(self, nome, telefone, nacionalidade):
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade

