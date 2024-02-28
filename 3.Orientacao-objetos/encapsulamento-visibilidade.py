# exemplo aula
class Pessoa:
    def falar_oi(self):
        self.nome = 'Thais'
        print(f'Oi, meu nome é {self.nome}')

    @property
    def nome(self):
        return self.__nome

pessoa = Pessoa()
pessoa.falar_oi()

#### Erro. Não é possível atribuir valor a propriedade sem método setter