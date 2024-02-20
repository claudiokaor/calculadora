import tkinter as tk
from tkinter import ttk

def calcular(operador):
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: divisão por zero!"
    label_resultado.config(text="Resultado: " + str(resultado))

# Cria a janela
janela = tk.Tk()
janela.title("Calculadora")

# Estilo dos botões
style = ttk.Style()
style.configure('TButton', font=('calibri', 12, 'bold'), foreground='black')

# Cria os widgets
label_num1 = ttk.Label(janela, text="Número 1:")
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = ttk.Entry(janela, font=('calibri', 12))
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = ttk.Label(janela, text="Número 2:")
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = ttk.Entry(janela, font=('calibri', 12))
entry_num2.grid(row=1, column=1, padx=10, pady=10)

button_adicao = ttk.Button(janela, text="+", command=lambda: calcular("+"))
button_adicao.grid(row=2, column=0, padx=10, pady=10)

button_subtracao = ttk.Button(janela, text="-", command=lambda: calcular("-"))
button_subtracao.grid(row=2, column=1, padx=10, pady=10)

button_multiplicacao = ttk.Button(janela, text="*", command=lambda: calcular("*"))
button_multiplicacao.grid(row=3, column=0, padx=10, pady=10)

button_divisao = ttk.Button(janela, text="/", command=lambda: calcular("/"))
button_divisao.grid(row=3, column=1, padx=10, pady=10)

label_resultado = ttk.Label(janela, text="Resultado: ", font=('calibri', 12, 'bold'))
label_resultado.grid(row=4, columnspan=2, padx=10, pady=10)

# Loop principal da janela
janela.mainloop()
