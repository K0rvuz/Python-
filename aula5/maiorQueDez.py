num=int(input("Digite um número"))
if num>10:
    for i in range(11,num):
        print(i)
else:
    print(10-num, f"É a diferença entre 10 e {num}")