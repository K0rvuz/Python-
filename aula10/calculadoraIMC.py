import tkinter as tk
from tkinter import messagebox, ttk# importa a biblioteca para  criar tabelas

# função da calculadora 
def calcular_imc():
    try:
        nome = entry_nome.get() #metodo pra pegar o nome
        peso = float(entry_peso.get()) #metodo de pegar o peso
        altura = float(entry_altura.get()) #metodo de pegar a altura (NÃO É PRA COLOCAR VIRGULA!!!!)
        
        if altura <= 0 or peso <= 0:  #se um dos dois for menor que zero, mostra mensagem de erro e o código não continua (vai ter que inserir os valores outra vez)

            messagebox.showerror("Erro", "Peso e altura devem ser maiores que zero.")  #mostra mensagem de erro

            return
        
        imc = round( peso / (altura ** 2),2)  #fórmula do imc

        classificacao = ""   #variável pra armazenar a classificação do imc (é tipo uma variavel acumulativa mas pra str)
    ########################### bloco de operações
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            classificacao = "Peso normal"
        elif 25 <= imc < 29.9:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"
        
        resultado = f"{imc:.2f}"
        ########################################
# Tabela usando o tkinter 
        tabela.insert("", "end", values=(nome, resultado, classificacao))   #insere os dados na tabela

        
        # Limpa os campos de entrada
        entry_nome.delete(0, tk.END) #metodo de deletar  o conteúdo de um campo de entrada

        entry_peso.delete(0, tk.END)
        entry_altura.delete(0, tk.END)
    
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# titulo e etc
root = tk.Tk()
root.title("Calculadora de IMC")
#########################################
# tela  de entrada

tk.Label(root, text="Nome do aluno:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Peso (kg):").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="Altura (m):").grid(row=2, column=0, padx=10, pady=10)

entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_peso = tk.Entry(root)
entry_peso.grid(row=1, column=1, padx=10, pady=10)

entry_altura = tk.Entry(root)
entry_altura.grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Calcular IMC", command=calcular_imc).grid(row=4, columnspan=2, pady=10)
#######################################
#######################################
# bloco pra mostrrar os resultados e tabela 
tabela = ttk.Treeview(root, columns=("Nome", "IMC", "Classificação"), show="headings")
tabela.heading("Nome", text="Nome do Aluno")
tabela.heading("IMC", text="IMC")
tabela.heading("Classificação", text="Classificação")

tabela.grid(row=5, columnspan=2, padx=10, pady=10)
#######################
#####deixa a tela rodando

root.mainloop()