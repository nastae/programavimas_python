import numpy as np
from numpy import linalg as LA
from sympy import *

print("1. Padalinkite intervalą nuo -1.3 iki 2.5 tolygiai į 64 dalis:")
print(np.linspace(-1.3, 2.5, 64))

print("2. Sugeneruokite masyvą dydžio 3n ir užpildykite jį cikliniu šablonu [1, 2, 3]:")
n = 10
print(np.tile(np.array([1, 2, 3]), n))

print("3. Sukurkite masyvą iš pirmųjų 10 nelyginių sveikųjų skaičių:")
n = 10
print(np.arange(1, 2 * n, 2))

print("4. Sukurkite masyvą dydžio 10 x 10 iš nulių ir \"įrėminkite\" jį vienetais:")
n = 10
matrix = np.zeros((n ,n))
matrix.fill(1)
print(matrix)

print("5. Sukurkite masyvą dydžio 8 x 8, kur 1 ir 0 išdėlioti šachmatine tvarka (panaudokite slicing+striding metodą):")
n = 8
matrix = np.zeros((n ,n))
matrix[::2, 1::2] = 1
matrix[1::2, ::2] = 1
print(matrix)

print("6. Sukurkite masyvą dydžio n×n , kurio (i,j)-oji pozicija lygi i+j:")
n = 10
matrix = np.zeros((n ,n))
for j in range(n):
    for i in range(n):
        matrix.itemset((i,j), i*j)
print(matrix)

print("7. kurkite atsitiktinį masyvą dydžio 3×5 naudodami np.random.rand(3, 5) funkciją ir suskaičiuokite: sumą, eilučių sumą, stulpelių sumą:")
matrix = np.random.rand(3, 5)
print(matrix)
print("Suma: ", matrix.sum())
print("Eilučių suma: ", matrix.sum(axis=0))
print("Stulpelių suma: ", matrix.sum(axis=1))

print("8. Sukurkite atsitiktinį masyvą dydžio 5×5 naudodami np.random.rand(5, 5). Surūšiuokite eilutes pagal antrąjį stulpelį. Tam pamėginkite apjungti masyvo slicing + argsort + indexing metodus:")
matrix = np.random.rand(5, 5)
print("Sukurta matrica: ")
print(matrix)
print("Eilučių rūšiavimo tvarka pagal stulpelius: ")
print(np.argsort(matrix[::, 1], axis=0))
print("Surūšiuota matrica: ")
print(matrix[np.argsort(matrix[::, 1], axis=0), ::])

print("9. Atvirkštinę matricą:")
matrix = np.random.rand(5, 5)
print("Sukurta matrica: ")
print(matrix)
print("Atvirkštinė matrica: ")
print(np.transpose(matrix))

print("10. Apskaičiuokite matricos tikrines reikšmes ir tikrinį vektorių:")
# Teorija: https://mathworld.wolfram.com/Eigenvalue.html
# API: https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.eig.html
matrix = np.random.rand(2, 2)
print("Sukurta matrica: ")
print(matrix)
eigvalue, eigvector = LA.eig(matrix)
print("Tikrinė reikšmė:")
print(eigvalue)
print("Tikrinis vektorius:")
print(eigvector)

print("11. Pasirinktos funkcijos išvestinę:")
x = Symbol('x')
f = 4*x**3+3
f_derivative = f.diff(x)
print("Funkcija: ", f)
print("Funkcijos išvestinė: ", f_derivative)
f_derivative = lambdify(x, f_derivative)
print("Funkcijos išvestinės reikšmė, kai x = 0: ", f_derivative(0))

print("12. Pasirinktos funkcijos apibrėžtinį ir neapibrėžtinį integralus:")
x = Symbol('x')
f = 4*x**3+3
f_integral = f.integrate(x)
print("Funkcija: ", f)
print("Neapibrėžtas integralas: ", f_integral)
a = 0
b = 1
print("Apibrėžtas integralas ", f_integral,  " (funkcijos", f, ") nuo ", a, " iki ", b, ":", f.integrate((x, a, b)))
