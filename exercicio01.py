num1=int(input("Digite um numero: "))
num2=int(input("Digite um numero: "))
num3=int(input("Digite um numero: "))
soma=num1+num2
if soma < num3:
    print(f"A soma entre a e b é: {soma} e é menor que c")
elif soma==num3 :
    print(f"A soma é igual a c")
else:
    print(f"A soma é maior que c")