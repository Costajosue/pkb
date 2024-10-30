''' 
Crie uma classe Calculadora em Python que contenha os métodos: somar,
subtrair, multiplicar e dividir. Crie um programa que importa esta classe e a
utiliza.        
                                                                      '''
class calculadora:
    def soma(self, x, y):
        return x + y
    
    def sub(self, x,y):
        return x - y
    
    def mul(self, x,y):
        return x * y
    
    def div(self,x,y):
        return x / y
    

c = calculadora()
print('soma:' , c.soma(2, 3))
print('sub:' , c.sub(2, 3))
print('mul:' , c.mul(2, 3))
print('div:' , c.div(2, 3))