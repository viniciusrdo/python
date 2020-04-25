p = input("Digite seu peso em quilogramas: ")
h = input("Digite sua altura em metros(Por favor substitua vírgula por ponto .): ")
x = float(h) ** 2

imc = ( float(p) / float(x) )
print("O seu IMC é: ", imc)