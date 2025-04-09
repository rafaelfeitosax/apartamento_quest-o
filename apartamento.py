valor_do_apt = float(input("digite o valor do apartamento: "))
entrada = valor_do_apt *0.10
financiamento = valor_do_apt - entrada
pessoas = int(input("quantas pessoas vao contribuir?: "))

contador = 1
renda_total = 0 

while contador <= pessoas:
    renda_total += float(input(f"valor da pessoa {contador}:")) 
    contador +=1

if renda_total >= financiamento:
    print("financiamento aprovado")
else:
    print ("financiamento negado, está faltando: ", financiamento - renda_total)
