import streamlit as st
from models.questao import Questao
import data.questions_data as data_questions
import numpy as np
import matplotlib.pyplot as plt


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

lista_questoes = []

# Informações do cliente
nome_client = st.text_input(label='Nome')
telefone_client = st.text_input(label='Telefone / Email')

# Questão 1
st.markdown('')
st.markdown('Questão 1')

opcoes1 = [data_questions.opcao1_1,
           data_questions.opcao1_2,
           data_questions.opcao1_3]

questao1 = Questao(enunciado=data_questions.enunciado1,
                   opcoes=opcoes1,
                   questao_key='questao1',
                   slider_key='intensidade1',
                   valor='MERECIMENTO')
questao1.gerar_questao()
lista_questoes.append(questao1)
st.markdown('---')

# Questão 2
st.markdown('Questão 2')

opcoes2 = [data_questions.opcoes2_1,
           data_questions.opcoes2_2,
           data_questions.opcoes2_3]

questao2 = Questao(enunciado=data_questions.enunciado2,
                   opcoes=opcoes2,
                   questao_key='questao2',
                   slider_key='intensidade2',
                   valor='AUTOPERCEPÇÃO')

questao2.gerar_questao()
lista_questoes.append(questao2)
st.markdown('---')

# Questão 3
st.markdown('Questão 3')

opcoes3 = [data_questions.opcoes3_1,
           data_questions.opcoes3_2,
           data_questions.opcoes3_3]

questao3 = Questao(enunciado=data_questions.enunciado3,
                   opcoes=opcoes3,
                   questao_key='questao3',
                   slider_key='intensidade3',
                   valor='AUTORRESPONSABILIDADE')
questao3.gerar_questao()
lista_questoes.append(questao3)
st.markdown('---')

# Questão 4
st.markdown('Questão 4')

opcoes4 = [data_questions.opcoes4_1,
           data_questions.opcoes4_2,
           data_questions.opcoes4_3]

questao4 = Questao(enunciado=data_questions.enunciado4,
                   opcoes=opcoes4,
                   questao_key='questao4',
                   slider_key='intensidade4',
                   valor='AÇÃO CONSCIENTE')
questao4.gerar_questao()
lista_questoes.append(questao4)
st.markdown('---')

# Questão 5
st.markdown('Questão 5')

opcoes5 = [data_questions.opcoes5_1,
           data_questions.opcoes5_2,
           data_questions.opcoes5_3]

questao5 = Questao(enunciado=data_questions.enunciado5,
                   opcoes=opcoes5,
                   questao_key='questao5',
                   slider_key='intensidade5',
                   valor='FOCO')
questao5.gerar_questao()
lista_questoes.append(questao5)
st.markdown('---')

# Questão 6
st.markdown('Questão 6')

opcoes6 = [data_questions.opcoes6_1,
           data_questions.opcoes6_2,
           data_questions.opcoes6_3]

questao6 = Questao(enunciado=data_questions.enunciado6,
                   opcoes=opcoes6,
                   questao_key='questao6',
                   slider_key='intensidade6',
                   valor='ENFRENTAMENTO')
questao6.gerar_questao()
lista_questoes.append(questao6)
st.markdown('---')

# Questão 7
st.markdown('Questão 7')

opcoes7 = [data_questions.opcoes7_1,
           data_questions.opcoes7_2,
           data_questions.opcoes7_3]

questao7 = Questao(enunciado=data_questions.enunciado7,
                   opcoes=opcoes7,
                   questao_key='questao7',
                   slider_key='intensidade7',
                   valor='AÇÃO')
questao7.gerar_questao()
lista_questoes.append(questao7)
st.markdown('---')

# Questão 8
st.markdown('Questão 8')

opcoes8 = [data_questions.opcoes8_1,
           data_questions.opcoes8_2,
           data_questions.opcoes8_3]

questao8 = Questao(enunciado=data_questions.enunciado8,
                   opcoes=opcoes8,
                   questao_key='questao8',
                   slider_key='intensidade8',
                   valor='AÇÃO CONTÍNUA')
questao8.gerar_questao()
lista_questoes.append(questao8)
st.markdown('---')

# Questão 9
st.markdown('Questão 9')

opcoes9 = [data_questions.opcoes9_1,
           data_questions.opcoes9_2,
           data_questions.opcoes9_3]
questao9 = Questao(enunciado=data_questions.enunciado9,
                   opcoes=opcoes9,
                   questao_key='questao9',
                   slider_key='intensidade9',
                   valor='RESILIÊNCIA')
questao9.gerar_questao()
lista_questoes.append(questao9)
st.markdown('---')

respostas = st.button(label='Enviar respostas',
                      use_container_width=True,
                      args=[lista_questoes],
                      type='primary',
                      key='respostas')

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
        angulos_list.append(2 * np.pi / N)

    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    radii = respostas['intensidades']
    width = angulos_list

    ax = plt.subplot(111, projection='polar')
    bars = ax.bar(theta, radii, width=width, bottom=0.0)

    # Use custom colors and opacity
    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.viridis(r / 10.))
        bar.set_alpha(0.5)

    st.pyplot(plt.gcf(), use_container_width=False)

else:
    respostas = None
