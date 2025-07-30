
# Importação de bibliotecas necessárias
import streamlit as st
import joblib
import pandas as pd

# Carregar modelo treinado
modelo = joblib.load('modelo.pkl')

# Título do app
st.title("🏥 Sistema Preditivo de Obesidade")
st.markdown("Este aplicativo utiliza um modelo de Machine Learning para prever o nível de obesidade de um paciente com base em informações pessoais e comportamentais.")

# Campos de entrada
gender = st.selectbox("Gênero", ["Male", "Female"])
age = st.slider("Idade", 10, 100, 25)
height = st.number_input("Altura (em metros)", min_value=1.0, max_value=2.5, step=0.01, value=1.70)
weight = st.number_input("Peso (em kg)", min_value=30.0, max_value=200.0, step=0.1, value=70.0)
family_history = st.selectbox("Histórico familiar de obesidade?", ["yes", "no"])
favc = st.selectbox("Consome alimentos calóricos com frequência?", ["yes", "no"])
fcvc = st.slider("Frequência de vegetais na dieta (0 a 3)", 0.0, 3.0, 2.0)
ncp = st.slider("Nº de refeições principais por dia", 1, 5, 3)
caec = st.selectbox("Come entre as refeições?", ["no", "Sometimes", "Frequently", "Always"])
smoke = st.selectbox("Fuma?", ["yes", "no"])
ch2o = st.slider("Consumo de água por dia (0 a 3)", 0.0, 3.0, 2.0)
scc = st.selectbox("Controla ingestão calórica?", ["yes", "no"])
faf = st.slider("Frequência de atividade física (0 a 3)", 0.0, 3.0, 1.0)
ter = st.slider("Tempo com tecnologia (0 a 3)", 0.0, 3.0, 2.0)
calc = st.selectbox("Frequência de consumo de álcool", ["no", "Sometimes", "Frequently", "Always"])
mtrans = st.selectbox("Meio de transporte", ["Public_Transportation", "Walking", "Automobile", "Motorbike", "Bike"])

# Botão de previsão
if st.button("🔍 Prever Nível de Obesidade"):
    entrada = pd.DataFrame([{
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "family_history": family_history,
        "FAVC": favc,
        "FCVC": fcvc,
        "NCP": ncp,
        "CAEC": caec,
        "SMOKE": smoke,
        "CH2O": ch2o,
        "SCC": scc,
        "FAF": faf,
        "TUE": ter,
        "CALC": calc,
        "MTRANS": mtrans
    }])

    predicao = modelo.predict(entrada)
    st.success(f"Nível de Obesidade Previsto: **{predicao[0]}**")
