salario = float (input ("Informe o seu salario: "))

if salario > (0 ) and salario <= (280.00):
    aumento = 20
    novosalario = salario * aumento / 100

elif salario > (280.00) and salario < (700.00):
    aumento = 15
    novosalario = (salario * aumento) / 100

elif salario > (700.00) and salario < (1500.00):
    aumento = 10
    novosalario = (salario * aumento) / 100

#elif valordoaumento = (novosalario-salario):

else:
    aumento = 5
    novosalario = (salario * aumento) / 100

print ("Seu salario original era de: ", salario)
print ("O percentual do seu aumento é: ", aumento ,"%")
#print ("O valor do seu aumento foi de: ", valordoaumento)
#print ("O novo valor so seu salario é: ", novosalario)
