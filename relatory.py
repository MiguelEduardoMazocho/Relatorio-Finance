import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

class GeradorRelatorioFinanceiro:
    def __init__(self, arquivo_csv):
        self.data = pd.read_csv(arquivo_csv)
        self.receita = None
        self.despesa = None
        self.lucro = None
        self.gerar_metricas()

    def gerar_metricas(self):
        self.receita = self.data[self.data['Tipo'] == 'Receita']['Valor'].sum()
        self.despesa = self.data[self.data['Tipo'] == 'Despesa']['Valor'].sum()
        self.lucro = self.receita - self.despesa

    def gerar_relatorio(self, output_pdf):
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Arial", size=24)
        pdf.cell(200, 10, txt="Relatório Financeiro", ln=True, align='C')

        pdf.set_font("Arial", size=12)
        pdf.ln(10)

        pdf.cell(200, 10, txt=f"Total de Receitas: R$ {self.receita:.2f}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Total de Despesas: R$ {self.despesa:.2f}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Lucro Total: R$ {self.lucro:.2f}", ln=True, align='L')

        pdf.output(output_pdf)

    def gerar_grafico(self, output_imagem):
        labels = ['Receitas', 'Despesas', 'Lucro']
        tamanhos = [self.receita, self.despesa, self.lucro]
        cores = ['#66b3ff', '#ff9999', '#99ff99']
        explode = (0.1, 0, 0)

        fig1, ax1 = plt.subplots()
        ax1.pie(tamanhos, explode=explode, labels=labels, colors=cores, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Deixa o gráfico circular

        plt.savefig(output_imagem)
        plt.show()

if __name__ == "__main__":
    arquivo_csv = "financial_data.csv"  
    output_pdf = "relatorio_financeiro.pdf"
    output_imagem = "grafico_financeiro.png"

    gerador = GeradorRelatorioFinanceiro(arquivo_csv)
    gerador.gerar_relatorio(output_pdf)
    gerador.gerar_grafico(output_imagem)
    print(f"Relatório gerado: {output_pdf}")
    print(f"Gráfico gerado: {output_imagem}")
