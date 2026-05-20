import streamlit as st

st.title("Calculadora de Salário")

valor_hora = st.number_input("Valor da hora (R$):", min_value=0.0)
horas_mes = st.number_input("Horas trabalhadas no mês:", min_value=0)

if st.button("Calcular"):
    salario_sem_acrescimo = valor_hora * horas_mes
    salario_com_acrescimo = ((10 / 100) * salario_sem_acrescimo) + salario_sem_acrescimo
    st.success(f"O valor a ser pago ao funcionário é: R${salario_com_acrescimo:.2f}")

    