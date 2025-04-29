Relatório Financeiro
Este projeto tem como objetivo gerar relatórios financeiros a partir de dados fornecidos em um arquivo CSV. Ele processa os dados, cria visualizações gráficas e exporta os resultados em formato PDF.

📁 Estrutura do Projeto
relatory.py: Script principal que processa os dados, gera gráficos e cria o relatório PDF.

financial_data.csv: Arquivo de entrada contendo os dados financeiros a serem analisados.

financial_pie_chart.png: Gráfico de pizza gerado a partir dos dados, utilizado no relatório.

financial_report.pdf: Relatório final em PDF contendo as análises e visualizações.

README.txt: Instruções básicas sobre o projeto.

⚙️ Como Utilizar
Preparar os Dados: Edite o arquivo financial_data.csv com seus próprios dados financeiros. Certifique-se de manter o formato correto para que o script possa processá-lo adequadamente.

Executar o Script:

Certifique-se de ter o Python instalado em sua máquina. Execute o script relatory.py para processar os dados e gerar o relatório:

bash
Copiar
Editar
python relatory.py
Resultado: Após a execução, serão gerados:

Um gráfico de pizza (financial_pie_chart.png) representando a distribuição dos dados.

Um relatório em PDF (financial_report.pdf) contendo o gráfico e outras informações relevantes.

✅ Requisitos
Python 3.x

Bibliotecas Python necessárias (certifique-se de instalá-las antes de executar o script):

pandas

matplotlib

reportlab

Você pode instalar as bibliotecas necessárias utilizando o pip:

bash
Copiar
Editar
pip install pandas matplotlib reportlab
📌 Observações
Os valores podem ser alterados no arquivo financial_data.csv.

Certifique-se de que os dados estejam no formato esperado para evitar erros durante a execução.

📄 Licença
Este projeto está licenciado sob a MIT License.
