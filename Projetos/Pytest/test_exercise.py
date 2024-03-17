import unittest

def str_to_bool(value):
    try:
        value = value.lower()  #reatribuir a variável value para minúscula
    except AttributeError:
        raise AttributeError(f"{value} must be of type string")
    
    true_values = ['y','yes']
    false_values = ['no', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False

class TestStrToBool(unittest.TestCase):
    def test_y_is_true(self):  # teste se y é true
        result = str_to_bool('y') 
        self.assertTrue(result)

    def test_yes_is_true(self):  # teste se yes é true
        result = str_to_bool('Yes')
        self.assertTrue(result)

    def test_invalid_input(self):  # teste se AttributeError é gerado pela entrada não cadeia de caracteres
        with self.assertRaises(AttributeError):
            str_to_bool(1)

if __name__ == '__main__':
    unittest.main() 
