import tkinter as tk
from tkinter import ttk

def calcular():
    try:
        escolha = operacao.get()
        valor = entrada.get()

        if escolha == "Fatorial":
            resultado = fatorial(int(valor))
        elif escolha == "Inverter String":
            resultado = inverter_string(valor)
        elif escolha == "Decimal para Binário":
            resultado = decimal_para_binario(int(valor))
        else:
            resultado = "Operação inválida!"

        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Entrada inválida!")

def decimal_para_binario(n):
    # Caso base
    if n < 2:
        return str(n)
    else:
        # Passo recursivo: chama a função para n // 2 e concatena o resto
        return decimal_para_binario(n // 2) + str(n % 2)

def inverter_string(s):
    # Caso base: string vazia ou com 1 caractere
    if len(s) <= 1:
        return s
    else:
        # Passo recursivo: inverte o restante e adiciona o primeiro caractere no final
        return inverter_string(s[1:]) + s[0]

def fatorial(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    else:
        # Passo recursivo: n * fatorial(n-1)
        return n * fatorial(n - 1)

# Criar janela
janela = tk.Tk()
janela.title("Recursividade")
janela.geometry("500x400")

# Aplicar tema ttk
style = ttk.Style(janela)
style.theme_use("clam")

# Personalizar botões
style.configure("TButton",
                font=("Arial", 14, "bold"),
                foreground="white",
                background="#1abc9c",
                padding=10)

# Personalizar labels
style.configure("TLabel",
                font=("Arial", 14),
                foreground="#2c3e50")

# Título
titulo = ttk.Label(janela, text="Recursividade",
                   font=("Arial", 20, "bold"), foreground="#34495e")
titulo.pack(pady=20)

# Campo de entrada
ttk.Label(janela, text="Digite o valor:").pack()
entrada = ttk.Entry(janela, width=30, font=("Arial", 14))
entrada.pack(pady=10)

# Menu de operações
operacao = tk.StringVar(value="Fatorial")
menu = ttk.OptionMenu(janela, operacao, "Fatorial", "Inverter String", "Decimal para Binário")
menu.pack(pady=10)

# Botão de calcular
botao = ttk.Button(janela, text="Calcular", command=calcular)
botao.pack(pady=20)

# Resultado
label_resultado = ttk.Label(janela, text="Resultado: ", font=("Arial", 16))
label_resultado.pack(pady=20)

janela.mainloop()
