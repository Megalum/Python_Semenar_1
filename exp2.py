# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = False
Y = True
Z = True

for i in range(1, 9):
    Z = not Z
    if i % 2 != 0:
        Y = not Y
    if i % 5 == 0:
        X = not X
    print(not(X or Y or Z) == (not(X) and not(Y) and not(Z)))