from src.functions import Fila

f1 = Fila()
f2 = Fila()
f3 = Fila()

user_input1 = input("Quantos elementos terá a fila? \n")
val1 = int(user_input1)

while f1.tamanho() != val1:
    user_input2 = input("Digite um número a adicionar: \n")
    val2 = int(user_input2)
    f1.inserir(val2)

print("INÍCIO// Fila F1: ", f1)

while f1.tamanho() > 0:
    if f1.iniciodafila() % 2 == 0:
        f2.inserir(f1.iniciodafila())
        f1.excluir()
        print("INSERINDO F2// FILA F1: ", f1, "FILA F2: ", f2)
    else:
        f3.inserir(f1.iniciodafila())
        f1.excluir()
        print("INSERINDO F3// FILA F1: ", f1, "FILA F3: ", f3)

while f3.tamanho() > 0:
    f1.inserir(f3.iniciodafila())
    f3.excluir()
    print("INSERINDO F1// FILA F1: ", f1, "FILA F3: ", f3)

print("FINAL// Fila F1: ", f1, "Fila F2: ", f2,  "Fila F3: ", f3)
