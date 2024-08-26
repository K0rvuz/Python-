Nome = input(
        "Digite o nome do aluno, quando o nome for [FIM]  o programa será encerrado: ")
while Nome.upper() != "FIM":
    Nome = input(
        "Digite o nome do aluno, quando o nome for [FIM]  o programa será encerrado: ")
    if Nome.upper() == "FIM":
        break
    
    nota1 = float(input("Primeira nota"))
    while nota1 < 0 or nota1 > 10:
        print("Nota invalida, por favor digite uma nota entre 0 e 10")
        nota1 = float(input("Primeira nota"))
        
    nota2 = float(input("Segunda nota"))
    while nota2 < 0 or nota2 > 10:
        print("Nota invalida, por favor digite uma nota entre 0 e 10")
        nota2 = float(input("Segunda nota"))
        
    nota3 = float(input("Segunda nota"))
    while nota3 < 0 or nota3 > 10:
        print("Nota invalida, por favor digite uma nota entre 0 e 10")
        nota3 = float(input("Segunda nota"))
        
    nota4 = float(input("Quarta nota"))
    while nota4 < 0 or nota4 > 10:
        print("Nota invalida, por favor digite uma nota entre 0 e 10")
        nota4 = float(input("Quarta nota"))
        
    nota5 = float(input("Quinta nota"))
    while nota5 < 0 or nota5 > 10:
        print("Nota invalida, por favor digite uma nota entre 0 e 10")
        nota5 = float(input("Quinta nota"))
        
    media = (nota1+nota2+nota3+nota4+nota5)/5

    if media >= 7:
        print(f"{Nome} foi aprovado")
    else:
        print(f"{Nome} foi reprovado")
        

print("Fim do programa")
