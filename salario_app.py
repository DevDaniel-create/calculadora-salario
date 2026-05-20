import streamlit as st

st.title("Calculadora de Salário")

valor_hora = st.number_input("Valor da hora (R$):", min_value=0.0)
horas_mes = st.number_input("Horas trabalhadas no mês:", min_value=0)

if st.button("Calcular"):
    salario_sem_acrescimo = valor_hora * horas_mes
    salario_com_acrescimo = ((10 / 100) * salario_sem_acrescimo) + salario_sem_acrescimo
    st.success(f"Salário bruto: R${salario_sem_acrescimo:.2f}")
    st.success(f"Acréscimo (10%): R${salario_sem_acrescimo * 0.10:.2f}")
    st.success(f"Total a pagar: R${salario_com_acrescimo:.2f}")
    
