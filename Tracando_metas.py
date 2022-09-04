import time

#Apresentação do prpjeto

print("*******Seja bem-vindo ao nosso sistema de Metas e Objetivos!*******\nVamos entender como funciona, primeiro você deve definir o nome do seu objetivo, seu valor e por fim em quantos meses deseja alcaça-lo.\nNosso sistema retornará os o valor que deve guardar a cada mês para coseguir alça-lo.")

#Perguntas/variaveis

objetivo1 = input ("Qual nome deseja aplicar a este Objetvo?: ")

valor_objetivo1 = int(input ("Qual o valor desse seu objetivo? "))

meses_objetivo1 = int(input ("Em quantos meses deseja alcançar esse objeivo? "))

#Só pra deixar mais "Real"

print("                       ...             ")
time.sleep(1)
print("*************calculando resultado...*************")
time.sleep(1)

#Armazenando resultado do Calculo 

valoremmeses = valor_objetivo1 / meses_objetivo1

#Resposta dos valores

print('Para você alcaçar seu' , objetivo1, f'você precisará guardar a seguinte quantia por mês R$ {valoremmeses:.2f}') 

input()