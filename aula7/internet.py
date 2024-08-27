'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''
# Recebendo o tamanho do arquivo e a velocidade do link
tamanho_arquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidade_link = float(input("Digite a velocidade do link em Mbps: "))
# Calculando o tempo de download
tempo_download = (tamanho_arquivo * 8) / (velocidade_link * 60)  # Convertendo MB para bytes e Mbps para bytes/s
# Imprimindo o resultado
print(f"O tempo aproximado de download do arquivo é de {tempo_download:.2f} minutos")