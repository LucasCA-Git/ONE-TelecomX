import os
import pandas as pd
import requests

# Definir pasta de destino
caminho_csv = r"D:\Lucas\ONE-TelecomX\dados\telecomx_dados_tratados.csv"
os.makedirs(os.path.dirname(caminho_csv), exist_ok=True)  # Garante que a pasta existe

# Baixar JSON da URL
url = "https://raw.githubusercontent.com/ingridcristh/challenge2-data-science/refs/heads/main/TelecomX_Data.json"
response = requests.get(url)
data = response.json()

# Transformar JSON em DataFrame
df = pd.DataFrame(data)
customer_df = pd.json_normalize(df['customer'])
phone_df = pd.json_normalize(df['phone'])
internet_df = pd.json_normalize(df['internet'])
account_df = pd.json_normalize(df['account'])

# Juntar os dados
df_final = pd.concat([
    df.drop(columns=['customer', 'phone', 'internet', 'account']),
    customer_df, phone_df, internet_df, account_df
], axis=1)

# Salvar como CSV
df_final.to_csv(caminho_csv, index=False, encoding='utf-8')
print(f"✅ CSV salvo com sucesso em: {caminho_csv}")
