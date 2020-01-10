nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota:" )
nota3 = input("Digite a terceira nota: ")

if nota1 > nota2  and nota1 > nota3:
    print ("A maior nota é : ",nota1)
elif nota2 > nota3 and nota2 > nota1:
    print ("A maior nota é: ", nota2)
else:
    print ("A maior nota é: ", nota3)