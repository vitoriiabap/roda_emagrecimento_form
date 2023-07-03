import streamlit as st
from models.questao import Questao
import data.questions_data as data_questions
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(page_title='Roda do Emagrecimento',
                   layout='wide',
                   initial_sidebar_state='collapsed',
                   menu_items=None)

# Título do formulário
st.markdown('### Roda do emagrecimento')
st.markdown('Orientações a respeito do preenchimento do formulário')
st.markdown('- Orientação 1 \n'
            '- Orientação 2\n'
            '- Orientação 3')

st.markdown('###### Vamos iniciar...')

# Informações do cliente
nome_client = st.text_input(label='Nome')
telefone_client = st.text_input(label='Telefone / Email')

# Gerando questões
lista_questoes = []
count = 0
for pergunta in data_questions.perguntas.values():
    questao_key = f'questao{count}'
    slider_key = f'intensidade{count}'

    questao = Questao(enunciado=pergunta['enunciado'],
                      opcoes=pergunta['opções'],
                      questao_key=questao_key,
                      slider_key=slider_key,
                      valor=pergunta['valor'])
    count += 1

    st.markdown(f'Questão - {count}')
    questao.gerar_questao()
    lista_questoes.append(questao)
    st.markdown('---')

# Botão para enviar respostas
respostas = st.button(label='Enviar respostas',
                      use_container_width=True,
                      args=[lista_questoes],
                      type='primary',
                      key='respostas')

# Gerando a Roda
if st.session_state['respostas']:

    valor_list = []
    intensidade_list = []

    for questao in lista_questoes:
        valor_list.append(questao.valor)
        intensidade_list.append(questao.intensidade)
    respostas = {
        'valor': valor_list,
        'intensidades': intensidade_list
    }

    valores, intensidades = respostas.values()

    # Compute pie slices
    N = len(intensidade_list)
    angulos_list = []
    for i in range(N):
        angulos_list.append(360 / N)

    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    radii = respostas['intensidades']
    width = angulos_list

    c = ['#FFB52B', '#C8C8C8', 'black', 'blue', 'orange', 'yellow', 'black', 'blue', 'orange']
    fig = go.Figure()
    fig.add_trace(go.Barpolar(
        r=radii,
        theta=np.linspace(0.0, 360.0, N, endpoint=False),
        width=width,
        marker_color=['green', 'blue', 'black', 'orange', 'purple', 'grey', 'brown', '#ffb52b', '#c8c8c8'],
        marker_line_color="white",
        marker_line_width=2,
        opacity=0.8,

    ))


    fig.update_layout(
        template=None,
        polar=dict(
            radialaxis=dict(range=[0, 5], showticklabels=False, ticks=''),
            angularaxis=dict(showticklabels=False, ticks='')
        ),
    width=800,
    height=800)


    st.plotly_chart(fig, use_container_width=True)



else:
    respostas = None
