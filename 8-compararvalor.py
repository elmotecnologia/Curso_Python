produ1 = input ("Valor do primeiro produto: ")
produ2 = input ("Valor do segundo produto: ")
produ3 = input ("Valor do tereiro produto: ")

if produ1 < produ2 and produ1 < produ3:
    print ("O produto mais em conta é o: ", produ1)

elif produ2 < produ3 and produ2 < produ1:
    print ("O produto mais em conta é o: ", produ2)

else:
    print ("O produto mais em conta é o: ", produ3)