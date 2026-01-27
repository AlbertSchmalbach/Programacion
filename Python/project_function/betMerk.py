import streamlit as st
import pandas as pd

def calcular_subtotal(name_product, price, cantidad):
    subtotal = float(price) * float(cantidad)
    nueva_fila = {"producto": name_product, "precio": price, "cantidad": cantidad, "subtotal":subtotal}
    print('execute')
    st.session_state.table_data = pd.concat([st.session_state.table_data, pd.DataFrame([nueva_fila])], ignore_index=True)

if "table_data" not in st.session_state:
    st.session_state.table_data= pd.DataFrame(columns=["producto", "precio", "cantidad", "subtotal"])

st.title("Supermercados BetMerk")

with st.form("producto_form"):
    product_name = st.text_input("Ingrese el nombre del producto")
    product_price = st.number_input("Ingrese el precio")
    product_cant = st.number_input("Ingrese la cantidad")

    subtotal_button = st.form_submit_button("Comprar Producto")
    
    if subtotal_button:
        calcular_subtotal(product_name, product_price, product_cant)

st.dataframe(st.session_state.table_data)

if st.button("Calcular Total"):
    if len(st.session_state.table_data) > 0:
        total = (st.session_state.table_data["precio"]*st.session_state.table_data["cantidad"]).sum()

        st.subheader("El Precio Total")
        st.write("El precio total es: " + str(total))