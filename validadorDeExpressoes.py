## 1120366 - Guilherme de Rezende Lima
## 1133554 - Vitor Almeida Machado

formula = str(input("Insira sua expressão númerica: "))
## Toda string é uma lista

pilha = []

for x in formula:
    if x == '(':
        pilha.append('(')
    elif x == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

for x in formula:
    if x == '{':
        pilha.append('{')
    elif x == '}':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append('}')
            break

for x in formula:
    if x == '[':
        pilha.append('[')
    elif x == ']':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(']')
            break


if len(pilha) == 0:
    print("Sua expressão é valída!")
else:
    print("Sua expressão é inválida!")