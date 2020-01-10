PriNota = int (input ("Informe sua primeira nota: "))
SecNota = int (input ("Informe sua segunda nota: "))

media = (PriNota+SecNota)/2

if media >= (70) and media <= (99):
    print ("Você está aprovado")

elif media < (70):
    print ("Você está reprovado")

else:
    print ("Você está aprovado com 'Distinção' ")

print ("Sua média é: ", media)