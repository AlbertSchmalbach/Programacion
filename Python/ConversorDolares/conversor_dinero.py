import streamlit as st
import requests

st.title("Conversión de Dólares a Pesos")

dolares = st.number_input(
    "Ingrese la cantidad de dólares (USD)",
    min_value=0.0,
    step=1.0
)

if st.button("Convertir"):
    try:
        url = "https://open.er-api.com/v6/latest/USD"
        response = requests.get(url)
        data = response.json()

        tasa = data["rates"]["COP"]
        pesos = dolares * tasa

        st.success(f"""
        💱 **Tasa actual:** 1 USD = {tasa:,.2f} COP  
        💵 **{dolares:.2f} USD** equivalen a  
        💰 **{pesos:,.2f} COP**
        """)

    except Exception as e:
        st.error("No se pudo obtener la tasa de cambio.")
