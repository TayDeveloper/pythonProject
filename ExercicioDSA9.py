# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string,
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e
# o quarto elemento um valor do tipo float.
# Imprima a lista.

list_1 = "melancia"

print(list_1)

tupla = (1, 2, 2, 3, 4, 4, 4, 5)

t = tupla.count(4)

print(t)

study = {"Mouse6" :1, "Notebook3" :2, "Chair1" :8}

print(study.keys())

print(study.values())


f = float(60)

print(f)

List_2 = [list_1, study["Chair1"], (t), (f)]

print(List_2)