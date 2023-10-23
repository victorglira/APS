import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt


def calcular_emissao_co2():
    tipo_combustivel = tipo_combustivel_entry.get().lower()
    quilometros_percorridos = float(quilometros_entry.get())
    
    # Dicionário de fatores de emissão em kg de CO2 por unidade (litro ou metro cúbico) do combustível
    fatores_emissao = {
        "gasolina": 2.31,   # kg de CO2 por litro de gasolina
        "diesel": 2.68,     # kg de CO2 por litro de diesel
        "gas natural": 2.75,  # kg de CO2 por metro cúbico de gás natural (metano)
        "carvão": 2.21      # kg de CO2 por quilo de carvão
    }
    
    # Verifica se o tipo de combustível está no dicionário
    if tipo_combustivel in fatores_emissao:
        fator_emissao = fatores_emissao[tipo_combustivel]
        emissao_co2 = fator_emissao * quilometros_percorridos
        resultado_label.config(text=f"A emissão de CO2 é de {emissao_co2:.2f} kg.")
        
        # Calcula quantas árvores seriam necessárias para compensar as emissões
        arvores_necessarias = emissao_co2 / 22  # Estimativa média de absorção de CO2 por árvore por ano
        arvores_label.config(text=f"Para compensar, seriam necessárias aproximadamente {arvores_necessarias:.2f} árvores.")
        
        # Atualiza o gráfico
        atualizar_grafico(emissao_co2, arvores_necessarias)
    else:
        resultado_label.config(text="Tipo de combustível não reconhecido")
        arvores_label.config("")
        info_credito_label.config(text="")
        # Limpa o gráfico
        plt.clf()

def atualizar_grafico(emissao, arvores):
    fig, ax = plt.subplots()
    categorias = ['Emissão de CO2 (kg)', 'Árvores necessárias']
    valores = [emissao, arvores]
    ax.bar(categorias, valores)
    ax.set_ylabel('Valores')
    ax.set_title('Emissão de CO2 vs. Árvores Necessárias')

    plt.show()

janela = tk.Tk()
janela.title("Calculadora de Emissão de CO2 ")
janela.geometry("800x600")
janela.resizable(width=True, height=True)
meu_label = tk.Label(janela, text="Minha etiqueta", width=25, height=5)





# Rótulos e campos de entrada
tipo_combustivel_label = tk.Label(janela, text="Tipo de Combustível: ", width= 25, height= 1)
tipo_combustivel_label.pack()
tipo_combustivel_entry = tk.Entry(janela)
tipo_combustivel_entry.pack()

quilometros_label = tk.Label(janela, text="Quilômetros Percorridos:", width= 25, height= 1)
quilometros_label.pack()
quilometros_entry = tk.Entry(janela)
quilometros_entry.pack()

# Botão para calcular
calcular_button = tk.Button(janela, text="Calcular", width= 10, height= 2 , command=calcular_emissao_co2)
calcular_button.pack()

# Exibir resultado
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

arvores_label = tk.Label(janela, text="")
arvores_label.pack()

info_credito_label = tk.Label(janela, text="")
info_credito_label.pack()

# Cria uma estrutura para o gráfico (inicialmente vazio)
plt.figure(figsize=(4, 4))
plt.tight_layout()
plt.clf()

janela.mainloop()
