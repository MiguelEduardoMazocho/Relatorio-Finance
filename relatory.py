import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

class FinancialReportGenerator:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
        self.revenue = None
        self.expenses = None
        self.profit = None
        self.generate_metrics()

    def generate_metrics(self):
        self.revenue = self.data[self.data['Type'] == 'Revenue']['Amount'].sum()
        self.expenses = self.data[self.data['Type'] == 'Expense']['Amount'].sum()
        self.profit = self.revenue - self.expenses

    def generate_report(self, output_pdf):
        pdf = FPDF()
        pdf.add_page()
    
        pdf.set_font("Arial", size = 24)
        pdf.cell(200, 10, txt = "Financial Report", ln = True, align = 'C')
        

        pdf.set_font("Arial", size = 12)
        pdf.ln(10)
        

        pdf.cell(200, 10, txt = f"Total Revenue: ${self.revenue:.2f}", ln = True, align = 'L')
        
        
        pdf.cell(200, 10, txt = f"Total Expenses: ${self.expenses:.2f}", ln = True, align = 'L')
        

        pdf.cell(200, 10, txt = f"Total Profit: ${self.profit:.2f}", ln = True, align = 'L')
        
        
        pdf.output(output_pdf)

    def plot_metrics(self, output_image):
        labels = 'Revenue', 'Expenses', 'Profit'
        sizes = [self.revenue, self.expenses, self.profit]
        colors = ['#ff9999','#66b3ff','#99ff99']
        explode = (0.1, 0, 0)  

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  

        plt.savefig(output_image)
        plt.show()

if __name__ == "__main__":
    csv_file = "financial_data.csv"  
    output_pdf = "financial_report.pdf"
    output_image = "financial_pie_chart.png"

    generator = FinancialReportGenerator(csv_file)
    generator.generate_report(output_pdf)
    generator.plot_metrics(output_image)
    print(f"Report generated: {output_pdf}")
    print(f"Chart generated: {output_image}")
