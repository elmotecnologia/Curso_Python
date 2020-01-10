num1 = input("Primeiro número: ")
num2 = input("Segundo número: ")
num3 = input("Terceiro número: ")

if num1 > num2 and num1 > num3:
    print("O maior número é: ", num1)
elif num2 > num3 and num2 > num1:
    print("O maior número é: ", num2)
else:
    print("O maior número é: ", num3)

if num1 < num2 and num1 < num3:
    print ("O menor número é: ", num1)
elif num2 < num2 and num2 <num1:
    print ("O menor número é: ", num2)
else:
    print ("O menor número é: ", num3)