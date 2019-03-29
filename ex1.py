from src.functions import Pilha

p1 = Pilha()
p2 = Pilha()
p3 = Pilha()
user_input1 = input("Quantos elementos terá a lista? \n")
val1 = int(user_input1)

while p1.tamanho() != val1:
    user_input2 = input("Digite um número a adicionar: \n")
    val2 = int(user_input2)
    p1.empilha(val2)

print("INÍCIO// Lista P1: ", p1)

while p1.tamanho() > 0:
    p3.empilha(p1.topo())
    p1.desempilha()

print("APÓS P1 -> P3// Lista P1: ", p1, "Lista P2: ", p2, "Lista P3: ", p3)

while p3.tamanho() > 0:
    if p3.topo() % 2 == 0:
        p2.empilha(p3.topo())
        p3.desempilha()
        print("EMPILHANDO P2// Lista P2: ", p2, "Lista P3: ", p3)
    else:
        p1.empilha(p3.topo())
        p3.desempilha()
        print("EMPILHANDO P1// Lista P1: ", p1, "Lista P3: ", p3)


print("FINAL// Lista P1: ", p1, "Lista P2: ", p2,  "Lista P3: ", p3)
