print("***************************************")
print("Bem vindo ao jogo de adivinhação")
print("***************************************")

numero_secreto = 42

chute = int(input("Digite o seu numero: "))

print("Voce digitou ", chute)

while(chute!=numero_secreto):
        if (chute > numero_secreto):
            print("Numero é menor!")
        else:
            print("Numero é maior!!")
        chute= int(input("Digite novamente: "))
print("Você acertou!!!\nFim do jogo!!")