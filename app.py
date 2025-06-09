import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Dashboard TelecomX", layout="wide")

st.title("📊 Dashboard de Evasão de Clientes - TelecomX")

# 📁 Carregar dados
csv_path = r"D:\Lucas\ONE-TelecomX\dados\telecomx_dados_tratados.csv"
df_final = pd.read_csv(csv_path).rename(columns={'Churn': 'Evasão'})

# 🎨 Configurações de estilo
px_defaults = {
    "color_discrete_sequence": px.colors.qualitative.Pastel,
    "template": "plotly_white"
}

# 📊 Gráficos Principais
st.subheader("📈 Análise de Evasão por Diferentes Fatores")
col1, col2 = st.columns(2)

with col1:
    # Gráfico de Contrato com rótulos diretamente nas barras
    fig1 = px.histogram(df_final, x='Evasão', color='Contract', barmode='group',
                       title='Evasão por Tipo de Contrato',
                       text_auto=True,  # Mostra valores nas barras
                       labels={'Contract': 'Tipo de Contrato'},
                       **px_defaults)
    fig1.update_traces(textfont_size=12, textposition="outside")
    st.plotly_chart(fig1, use_container_width=True)
    tabela_contrato = df_final.groupby(['Evasão', 'Contract']).size().unstack(fill_value=0)
    st.dataframe(tabela_contrato)

# 🍕 Tipos de contrato
st.subheader("🍕 Distribuição dos Tipos de Contrato")
contract_counts = df_final['Contract'].value_counts().reset_index()
fig_pie = px.pie(contract_counts, values='count', names='Contract', 
                title='Distribuição dos Tipos de Contrato',
                hole=0.3, **px_defaults)
fig_pie.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig_pie, use_container_width=True)
contract_counts.columns = ['Contract', 'count']
st.dataframe(contract_counts)

with col2:
    # Gráfico de Pagamento melhorado
    fig2 = px.histogram(df_final, x='Evasão', color='PaymentMethod', barmode='group',
                       title='Evasão por Forma de Pagamento',
                       labels={'PaymentMethod': 'Método de Pagamento'},
                       **px_defaults)
    st.plotly_chart(fig2, use_container_width=True)
    tabela_pagamento = df_final.groupby(['Evasão', 'PaymentMethod']).size().unstack(fill_value=0)
    st.dataframe(tabela_pagamento)


# 🔍 Análises Adicionais
st.subheader("🔎 Análises Detalhadas de Evasão")

# Gráfico de Internet com rótulos
fig4 = px.histogram(df_final, x='InternetService', color='Evasão', barmode='group',
                   title='Evasão por Tipo de Internet',
                   text_auto=True,
                   labels={'InternetService': 'Tipo de Internet'},
                   **px_defaults)
fig4.update_layout(xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig4, use_container_width=True)
tabela_internet = df_final.groupby(['InternetService', 'Evasão']).size().unstack(fill_value=0)
st.dataframe(tabela_internet)


# 📺 Análise de Streaming (Expandida)
st.subheader("🎬 Análise Completa de Streaming")

tab1, tab2, tab3 = st.tabs(["Streaming TV", "Streaming Movies", "Comparativo"])

with tab1:
    df_tv = df_final[df_final['InternetService'] != 'No']
    fig_tv = px.histogram(df_tv, x='StreamingTV', color='Evasão', barmode='group',
                         title='Evasão entre Usuários de Streaming TV (com Internet)',
                         text_auto=True,
                         **px_defaults)
    st.plotly_chart(fig_tv, use_container_width=True)
    
    # Análise adicional: Streaming TV por tipo de internet
    fig_tv_combo = px.histogram(df_tv, x='InternetService', color='StreamingTV', 
                               facet_col='Evasão', barmode='group',
                               title='Uso de Streaming TV por Tipo de Internet e Evasão',
                               **px_defaults)
    st.plotly_chart(fig_tv_combo, use_container_width=True)

with tab2:
    df_movies = df_final[df_final['InternetService'] != 'No']
    fig_movies = px.histogram(df_movies, x='StreamingMovies', color='Evasão', barmode='group',
                            title='Evasão entre Usuários de Streaming de Filmes (com Internet)',
                            text_auto=True,
                            **px_defaults)
    st.plotly_chart(fig_movies, use_container_width=True)
    tabela_streaming_movies = df_movies.groupby(['StreamingMovies', 'Evasão']).size().unstack(fill_value=0)
    st.dataframe(tabela_streaming_movies)


with tab3:
    # Comparação entre Streaming TV vs Movies
    streaming_comparison = df_final.groupby(['StreamingTV', 'StreamingMovies', 'Evasão']).size().unstack().reset_index()
    streaming_comparison['Tipo'] = streaming_comparison.apply(
    lambda x: f"TV: {x['StreamingTV']}, Movies: {x['StreamingMovies']}", axis=1)
    
    fig_compare = px.bar(streaming_comparison, x='Tipo', y=['Yes', 'No'], 
                title='Comparação entre Streaming TV e Filmes',
                labels={'value': 'Número de Clientes', 'variable': 'Evasão'},
                barmode='group', **px_defaults)
st.plotly_chart(fig_compare, use_container_width=True)
st.dataframe(streaming_comparison)




