lista=[]

if len(lista)==0:
    n = "si"
    while n == "si":
        lista.append(input("Dame una palabra o frase: ").upper())
        n=input("Deseas solicitar otra frase? (Si/No): ").lower().strip()
    print(lista)