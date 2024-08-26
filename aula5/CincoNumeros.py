'''
Faça um programa que leia 5 números e informe o maior número.
'''
maior= -6000 #número extremamente baixo

for i in range (5): #repete a estrutura 5 vezes
    
    a= int(input ("Digite um número: ")) #recebe novo número
    
    if a>maior: #caso esse novo número seja maior que "maior" (que provavelmente vai ser), "maior" recebe o valor desse novo número. 
        
        maior=a #maior recebendo o valor do novo número para caso ele seja maior que o anterior. 


print(maior) #mostra qual o maior número após a estrutura de repetição. (Fora o 'For').
    