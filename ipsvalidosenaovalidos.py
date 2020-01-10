entrada = open("ips.txt", "r")
linhas = entrada.readlines

for linha in linhas:
    linha = linha.replace("\n", "")
    linha = linha.split(".")

    