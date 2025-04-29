import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GeradorRelatorioFinanceiroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Relatório Financeiro")
        self.root.geometry("600x650")

        self.receita = 0
        self.despesa = 0
        self.lucro = 0

        self.titulo = tk.Label(self.root, text="Gerador de Relatório Financeiro", font=("Arial", 16))
        self.titulo.pack(pady=20)

        self.label_receita = tk.Label(self.root, text="Digite o valor da Receita (R$):")
        self.label_receita.pack()
        self.entry_receita = tk.Entry(self.root)
        self.entry_receita.pack(pady=5)

        self.label_despesa = tk.Label(self.root, text="Digite o valor da Despesa (R$):")
        self.label_despesa.pack()
        self.entry_despesa = tk.Entry(self.root)
        self.entry_despesa.pack(pady=5)

        self.btn_gerar = tk.Button(self.root, text="Gerar Relatório", command=self.gerar_relatorio)
        self.btn_gerar.pack(pady=10)

        self.canvas = None
        self.label_resultado = None

    def gerar_relatorio(self):
        receita_texto = self.entry_receita.get()
        despesa_texto = self.entry_despesa.get()

        try:
            self.receita = float(receita_texto)
            self.despesa = float(despesa_texto)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
            return

        if self.receita < 0 or self.despesa < 0:
            messagebox.showerror("Erro", "Valores não podem ser negativos.")
            return

        self.lucro = self.receita - self.despesa

        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        if self.label_resultado:
            self.label_resultado.destroy()

        fig, ax = plt.subplots()
        labels = ['Receita', 'Despesa', 'Lucro']
        valores = [self.receita, self.despesa, self.lucro]
        cores = ['#66bb6a', '#ef5350', '#42a5f5']
        explode = (0.1, 0, 0)

        ax.pie(valores, labels=labels, autopct='%1.1f%%', startangle=90, colors=cores, explode=explode, shadow=True)
        ax.axis('equal')

        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(pady=20)

        porcentagem_lucro = (self.lucro / self.receita) * 100 if self.receita != 0 else 0

        self.label_resultado = tk.Label(self.root, text=f"Lucro: R$ {self.lucro:.2f} ({porcentagem_lucro:.2f}%)", font=("Arial", 14))
        self.label_resultado.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = GeradorRelatorioFinanceiroApp(root)
    root.mainloop()
