import unittest

class TestAssertions(unittest.TestCase): #classe qe define os testes
    def test_equals(self):  #método de teste
        self.assertEqual("one string", "one string") #compara se são iguais
        
if __name__ == '__main__':  # verifica se o script está sendo executado diretamente como um programa principal
    unittest.main() # chama a função main() do módulo unittest, que executa todos os testes da classe TestAssertions

# Nomenclatura padrão com 'test'

# Classe unittest.TestCase contém métodos próprios, como é o cado do assertEquals
    ## mais usados:
    ## self.assertTrue(value): verifique se value é true.
    ## self.assertFalse(value): verifique se value é false.
    ## self.assertNotEqual(a, b): confirme que a e b não são iguais.

'''
Exemplo de teste que verifica o cadastramento e exclusão de contas num sistema

class TestAccounts(unittest.TestCase):

    def test_creation(self):
        self.assertTrue(account.create())

    def test_deletion(self):
        self.assertTrue(account.delete())

'''