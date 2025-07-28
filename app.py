
import streamlit as st
import joblib
import numpy as np

# Carregar modelo
modelo = joblib.load('modelo.pkl')

st.title("🏥 Sistema de Previsão de Obesidade")
st.write("Preencha os dados abaixo para obter uma previsão:")

# Entradas do usuário
gender = st.selectbox("Gênero", ["Male", "Female"])
age = st.slider("Idade", 10, 100, 25)
height = st.number_input("Altura (em metros)", 1.0, 2.5, 1.70)
weight = st.number_input("Peso (kg)", 30.0, 200.0, 70.0)
family_history = st.selectbox("Histórico familiar de obesidade?", ["yes", "no"])
favc = st.selectbox("Consome alimentos calóricos com frequência?", ["yes", "no"])
fcvc = st.slider("Frequência de vegetais (0 a 3)", 0.0, 3.0, 2.0)
ncp = st.slider("Nº de refeições por dia", 1, 5, 3)
caec = st.selectbox("Come entre as refeições?", ["no", "Sometimes", "Frequently", "Always"])
smoke = st.selectbox("Fuma?", ["yes", "no"])
ch2o = st.slider("Água por dia (0 a 3)", 0.0, 3.0, 2.0)
scc = st.selectbox("Controla calorias?", ["yes", "no"])
faf = st.slider("Atividade física (0 a 3)", 0.0, 3.0, 1.0)
ter = st.slider("Tempo com tecnologia (0 a 3)", 0.0, 3.0, 2.0)
calc = st.selectbox("Frequência de álcool", ["no", "Sometimes", "Frequently", "Always"])
mtrans = st.selectbox("Meio de transporte", ["Public_Transportation", "Walking", "Automobile", "Motorbike", "Bike"])

if st.button("🔍 Prever"):
    entrada = np.array([[
        1 if gender == "Male" else 0,
        age,
        height,
        weight,
        1 if family_history == "yes" else 0,
        1 if favc == "yes" else 0,
        fcvc,
        ncp,
        ["no", "Sometimes", "Frequently", "Always"].index(caec),
        1 if smoke == "yes" else 0,
        ch2o,
        1 if scc == "yes" else 0,
        faf,
        ter,
        ["no", "Sometimes", "Frequently", "Always"].index(calc),
        ["Public_Transportation", "Walking", "Automobile", "Motorbike", "Bike"].index(mtrans)
    ]])
    resultado = modelo.predict(entrada)
    st.success(f"Nível de Obesidade Previsto: {resultado[0]}")
