📈 Relatório Financeiro

Bem-vindo ao projeto Relatório Financeiro!Este projeto permite processar dados financeiros de um arquivo CSV, gerar gráficos de análise e exportar um relatório final em PDF.

✨ Funcionalidades

📥 Importa dados de um arquivo CSV.

📊 Cria um gráfico de pizza ilustrando a distribuição dos dados.

📝 Gera um relatório financeiro completo em PDF contendo o gráfico e resumos.

🔎 Permite visualizar o relatório diretamente no Visual Studio Code com extensão PDF Viewer.

📂 Estrutura do Projeto

Relatorio-Finance/
├── financial_data.csv         # Arquivo de dados financeiros
├── financial_pie_chart.png    # Gráfico gerado automaticamente
├── financial_report.pdf       # Relatório financeiro final
├── relatory.py                # Script principal do projeto
└── README.txt                 # Anotações adicionais

🛠️ Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:

Python 3.8 ou superior

Visual Studio Code (VSCode) (opcional para edição/visualização)

Extensão vscode-pdf no VSCode (opcional para abrir PDFs)

Instalando o PDF Viewer no VSCode:

Acesse o VSCode.

Pressione Ctrl + Shift + X para abrir a aba de extensões.

Procure por vscode-pdf e clique em Instalar.

📦 Instalar dependências

No terminal, instale as bibliotecas necessárias:

pip install pandas matplotlib reportlab

🚀 Como Executar o Projeto

Clone o repositório:

git clone https://github.com/MiguelEduardoMazocho/Relatorio-Finance.git

Acesse a pasta do projeto:

cd Relatorio-Finance

Edite o arquivo financial_data.csv com seus próprios dados financeiros, respeitando o formato.

Execute o script para gerar o relatório:

python relatory.py

Visualize o relatório gerado (financial_report.pdf) diretamente no VS Code ou em qualquer leitor de PDF.

🧹 Formato Esperado do CSV

O arquivo financial_data.csv deve ter no mínimo duas colunas:

Categoria

Valor

Aluguel

1200

Alimentação

800

Transporte

300

...

...

Categoria: Nome da despesa/receita.

Valor: Quantia numérica associada.

📊 Resultado

O script irá gerar:

Um gráfico de pizza salvo como financial_pie_chart.png.

Um relatório financeiro em PDF chamado financial_report.pdf, contendo o gráfico e as informações extraídas do CSV.

❗ Observações

Certifique-se de que o arquivo financial_data.csv esteja formatado corretamente para evitar erros.

Se quiser mudar o visual do gráfico ou do relatório, edite o código no relatory.py.

📄 Licença

Este projeto está licenciado sob a Licença MIT.Sinta-se à vontade para usar, modificar e distribuir.

🤝 Contribuindo

Contribuições são sempre bem-vindas!Se você tiver sugestões de melhorias, abra uma issue ou envie um pull request.

🎯 Autor

Desenvolvido por Miguel Eduardo Mazocho