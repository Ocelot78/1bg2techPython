#zad 1
# a = int(input())
# b = int(input())
# if (a + b) % 2 == 0:
#   print("TAK")
# else:
#   print("NIE")

#zad 2
# import math
# a = int(input())
# g = int(input())
# if (a + g) / 2 > math.sqrt(a * g):
#   print("TAK")
# else:
#   print("NIE")

#zad 3
# k = int(input())
# l = int(input())
# m = int(input())
# if  k == l == m:
#   print("TAK, Wszystkie liczby są równe")
# elif k == l:
#  print("TAK, liczby", k, "i", l, "są równe")
# elif l == m:
#   print("TAK, liczby", l, "i", m, "są równe")
# elif k == m:
#   print("TAK, liczby", k, "i", m, "są równe")
# else:
#   print("NIE")

#zad 4
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(min(a,b,c,d))

#zad 5
# a = int(input())
# b = int(input())
# c = int(input())
# if a+b>c and b+c>a and a+c>b:
#   print("Tak")
# else:
#   print("NIE")

#zad6
# a = int(input())
# b = int(input())
# c = int(input())
# i = int(0)
# if a+b>c and b+c>a and a+c>b:
#   i = int(1)
# else:
#   print("Nie da się zbudować trójkąta")
#   print("Program zatrzymany")
#   quit()
# if a**2 + b**2 == c**2:
#   print("Trójkąt Prostokątny")
# elif a**2 + b**2 < c**2:
#   print("Trójką Rozwatokątny")
# elif a**2 + b**2 > c**2:
#   print("Trójkąt ostrokątny")