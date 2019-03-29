from src.functions import Fila

f1 = Fila()
f2 = Fila()
i = 0

while f1.tamanho() != 10:
    user_input2 = input("Digite um número a adicionar: \n")
    val2 = int(user_input2)
    f1.inserir(val2)

print("INÍCIO// FILA F1: ", f1, "")

while 10 > i:
    if f1.iniciodafila() % 2 == 0:
        f2.inserir(f1.iniciodafila())
        f1.excluir()
        print("INSERINDO F2// FILA F1: ", f1, "FILA F2: ", f2)
    else:
        f1.inserir(f1.iniciodafila())
        f1.excluir()
        print("INSERINDO/EXCLUINDO F1// FILA F1: ", f1, "FILA F2: ", f2)
    i = i + 1

print("FINAL// FILA F1: ", f1, "FILA F2: ", f2)
