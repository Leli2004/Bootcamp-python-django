# 1. Crie uma classe que modele o objeto "carro"
class Carro:
# 2. Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
    def tipo(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        print(f'Tipo -> Cor={cor} Modelo={modelo}')
    
# 3. Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera
    def liga(self):
        self.ligado = 'Carro ligado'
        print(self.ligado)
    
    def desliga(self):
        self.ligado = 'Carro desligado'
        print(self.ligado)

    def acelera(self):
        self.velocidade = 'Carro acelerando'
        print(self.velocidade)

    def desacelera(self):
        self.velocidade = 'Carro desacelerando'
        print(self.velocidade)

# 4. Crie uma instância da classe carro.
carro = Carro()
carro.tipo("Vermelho", "Sandero")
carro.tipo("Preto", "Argo")
print(' ')
# 5. Faça o carro "andar" utilizando os métodos da sua classe
carro.liga()
carro.acelera()

# 6. Faça o carro "parar" utilizando os métodos da sua classe
carro.desacelera()
carro.desliga()