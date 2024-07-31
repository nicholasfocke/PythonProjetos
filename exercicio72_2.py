def par_impar(numero):
    multiplo_de_dois =  numero % 2 == 0
    if multiplo_de_dois:
        return f"{numero} é par"
    
    return f"{numero} é impar"

numero_usuario = int(input("Digite um número: "))

resultado = par_impar(numero_usuario)
print(resultado)


#print(par_impar(2))
#print(par_impar(3))
#print(par_impar(15))
#print(par_impar(18))