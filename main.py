import streamlit as st


def switch_question(argument):
    conditions = {
        'A': ['Qual a intensidade da sua resposta, de 0 a 3'],
        'B': ['Qual a intensidade da sua resposta, de 4 a 6'],
        'C': ['Qual a intensidade da sua resposta, de 7 a 10']
    }
    label = conditions.get(argument)[0]
    values = label.split('de')[-1].strip().split('a')
    min_value = int(values[0].strip())
    max_value = int(values[1].strip())
    return st.slider(label=label,
                     min_value=min_value,
                     max_value=max_value)


st.write('Roda do emagrecimento')

form = st.form(key='form', clear_on_submit=False)

st.write('Formulário - 1')

questao1 = st.container()
with questao1:
    alternativa = st.radio(label='Emagrecimento...', options=['A', 'B', 'C'])
    switch_question(alternativa)