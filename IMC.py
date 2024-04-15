'''
Solicite para o úsuario informar:
- Nome;
- Altura; 
- peso. 
Com base nestes dados realize o calcúlo para descobrir qual o IMC (Índice de massa corporea) da pessoa. 
Para o cálculo utilize a tabela padrão do IMC.
abaixo de 18,5 - Abaixo do Peso (Pegue suplementos do Cariani) 
    entre 18,6 e 24,9 - Peso Ideal (Para Bens)
    entre 25,0 e 29,9 - Sobrepeso
    entre 30,0 e 34,9 - Obesidade Grau 1
    entre 35,0 e 39,9 - Obesidade Grau 2
    acima de 40,0 - Obesidade Grau 3 (Dr. Nowzaradan te espera)
    formula: IMC = peso / altura²
'''

Nome = input("Dígite seu nome: ")
altura = float(input("Dígite á altura correspondente (CM): "))
peso = float(input("Dígite o peso correspondente: (Kg)"))


altura_m = altura / 100

IMC = peso / (altura_m *altura_m)

if IMC >= 18.5: 
    classificacao = "Abaixo do Peso (Pegue suplementos do Cariani)"
elif IMC >= 18.6 and IMC <= 24.9:
    classificacao = "Peso Ideal (Parabéns)"
elif IMC >= 25.0 and IMC <= 29.9:
    classificacao = "Sobrepeso"
elif IMC >= 30.0 and IMC <= 34.9:
    classificacao = "Obesidade Grau 1"
elif IMC >= 35.0 and IMC <= 39.9:
    classificacao = "Obesidade Grau 2"
else: 
    classificacao = "Obesidade Grau 3 (Dr. Nowzaradan te espera)"

texto=f'''
ólá, {Nome} você apresenta {IMC:.2f} de IMC (Índice de massa corporea), o que índica {classificacao}
'''
print(texto)