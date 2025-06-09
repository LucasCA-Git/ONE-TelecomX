# ONE-TelecomX
## Analise de evasão de clientes

### Análise por Tipo de Contrato
- Clientes com contrato mensal (Month-to-month) tendem a evadir mais.
- Contratos de um ou dois anos (One year / Two year) mostram uma taxa de retenção maior, indicando que contratos mais longos reduzem a evasão.
![tipo de contrato](/static/distribuição%20de%20tipos%20de%20contrato.png)
![tipo de contrato](/static/evasão%20por%20contrato.png
)
### Análise por Forma de Pagamento
- Clientes que utilizam pagamento eletrônico (Electronic check) apresentam maior evasão.
- Pagamentos automáticos por cartão de crédito ou débito parecem ter menor evasão, o que sugere que métodos com débito automático reduzem o churn.
![tipo de contrato](/static/evasão%20por%20forma%20de%20pagamento.png)

### Análise por Tipo de Internet
- Usuários sem serviço de internet ("No") têm uma evasão significativamente menor — talvez porque tenham serviços básicos ou são clientes com serviços estáticos.
- Já clientes com Fiber optic apresentam maior taxa de evasão, possivelmente por conta de insatisfação com qualidade, preço ou concorrência.
![tipo de contrato](/static/evasão%20por%20tipo%20de%20internet.png)

### Streaming TV e Filmes
- O uso de Streaming TV e Movies está ligado à presença de internet, e clientes com esses serviços apresentam maior propensão à evasão.
- Isso pode sugerir que o perfil mais digital do cliente também é mais exigente, e talvez mais sensível a problemas ou preços.
![comparativo tipo filme](/static/streaming.png)

### Comparação Streaming TV vs Filmes
- A comparação cruzada mostra que usuários que usam ambos (TV e Movies) têm uma taxa alta de evasão, indicando que consumidores que contratam mais serviços também são os mais voláteis.
![comparativo tipo filme](/static/tipofilme.png)

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```
### 2. Instale as dependencias
```bash
pip install streamlit pandas plotly
```
### 3. Rode o script 
- o script serve para transformar o json em csv
```bash
python convert.py
```
### 4. rode o app no streamlit 
```bash
streamlit run app.py
```