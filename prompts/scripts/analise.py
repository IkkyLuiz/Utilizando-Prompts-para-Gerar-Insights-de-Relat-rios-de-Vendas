import pandas as pd

# Caminhos dos arquivos
files = {
    "AliExpress": "/mnt/data/Meganium_Sales_Data_-_AliExpress.csv",
    "Etsy": "/mnt/data/Meganium_Sales_Data_-_Etsy.csv",
    "Shopee": "/mnt/data/Meganium_Sales_Data_-_Shopee.csv",
}

# Dicionário para armazenar os dados de vendas por país
sales_summary = {}

# Processar cada arquivo
for platform, file_path in files.items():
    # Tentar carregar o arquivo CSV
    try:
        df = pd.read_csv(file_path)

        # Identificar colunas relevantes (buscando nomes comuns)
        country_col = next((col for col in df.columns if 'country' in col.lower()), None)
        sales_col = next((col for col in df.columns if 'sales' in col.lower() or 'quantity' in col.lower()), None)

        if country_col and sales_col:
            # Agrupar vendas por país
            country_sales = df.groupby(country_col)[sales_col].sum().to_dict()

            # Acumular os valores por país
            for country, sales in country_sales.items():
                if country in sales_summary:
                    sales_summary[country] += sales
                else:
                    sales_summary[country] = sales

    except Exception as e:
        print(f"Erro ao processar {platform}: {e}")

# Criar um DataFrame para exibir a tabela
sales_summary_df = pd.DataFrame(sales_summary.items(), columns=["País", "Total de Vendas"])
sales_summary_df = sales_summary_df.sort_values(by="Total de Vendas", ascending=False)

# Mostrar as primeiras linhas da tabela
sales_summary_df.head()
