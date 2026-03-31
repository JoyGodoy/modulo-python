print("Exemplo de importação de módulo padrão")
from math import sqrt

raiz_quadrada = sqrt(25)
print (f"A raiz quadrada de 25 é: {raiz_quadrada}")

print("\nExemplo de criação e utilização de um módulo personalizado")
import meu_modulo

mensagem = meu_modulo.saudacao("Jorge")
resultado_dobro = meu_modulo.dobro(5)
print(mensagem)
print(f"O dobro de 5 é {resultado_dobro}")