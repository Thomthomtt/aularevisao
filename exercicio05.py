peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura: "))
formula=peso/(altura)**2
if formula<18.6:
    print(f"Você está abaixo do peso. O seu imc é {formula:.2f}")
elif formula<24.9:
    print(f"Você está no peso ideal. Parabéns! O seu imc é {formula:.2f}")
elif formula < 29.9:
    print(f"Você está levemente acima do peso!. O seu imc é {formula:.2f}")
elif formula < 34.9:
    print(f"Obesidade grau I. O seu imc é {formula:.2f}")
elif formula<39.9:
    print(f"Obesidade grau II. O seu imc é {formula:.2f}")
else:
    print(f"Obesidade grau III. O seu imc é {formula:.2f}")