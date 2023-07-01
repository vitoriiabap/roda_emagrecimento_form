import streamlit as st
from models.questao import Questao
import data.questions_data as data_questions

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

# Questão 1
st.markdown('')
st.markdown('Questão 1')

opcoes1 = [data_questions.opcao1_1,
           data_questions.opcao1_2,
           data_questions.opcao1_3]

questao1 = Questao(enunciado=data_questions.enunciado1,
                   opcoes=opcoes1,
                   questao_key='questao1',
                   slider_key='intensidade1')
questao1.gerar_questao()
st.markdown('---')

# Questão 2
st.markdown('Questão 2')

opcoes2 = [data_questions.opcoes2_1,
           data_questions.opcoes2_2,
           data_questions.opcoes2_3]

questao2 = Questao(enunciado=data_questions.enunciado2,
                   opcoes=opcoes2,
                   questao_key='questao2',
                   slider_key='intensidade2')

questao2.gerar_questao()
st.markdown('---')

# Questão 3
st.markdown('Questão 3')

opcoes3 = [data_questions.opcoes3_1,
           data_questions.opcoes3_2,
           data_questions.opcoes3_3]

questao3 = Questao(enunciado=data_questions.enunciado3,
                   opcoes=opcoes3,
                   questao_key='questao3',
                   slider_key='intensidade3')
questao3.gerar_questao()
st.markdown('---')

# Questão 4
st.markdown('Questão 4')

opcoes4 = [data_questions.opcoes4_1,
           data_questions.opcoes4_2,
           data_questions.opcoes4_3]

questao4 = Questao(enunciado=data_questions.enunciado4,
                   opcoes=opcoes4,
                   questao_key='questao4',
                   slider_key='intensidade4')
questao4.gerar_questao()
st.markdown('---')

# Questão 5
st.markdown('Questão 5')

opcoes5 = [data_questions.opcoes5_1,
           data_questions.opcoes5_2,
           data_questions.opcoes5_3]

questao5 = Questao(enunciado=data_questions.enunciado5,
                   opcoes=opcoes5,
                   questao_key='questao5',
                   slider_key='intensidade5')
questao5.gerar_questao()
st.markdown('---')

# Questão 6
st.markdown('Questão 5')

opcoes6 = [data_questions.enunciado6,
           data_questions.enunciado6,
           data_questions.enunciado6]

questao6 = Questao(enunciado=data_questions.enunciado6,
                   opcoes=opcoes6,
                   questao_key='questao6',
                   slider_key='intensidade6')
questao6.gerar_questao()
st.markdown('---')

# Questão 7
st.markdown('Questão 7')

opcoes7 = [data_questions.opcoes7_1,
           data_questions.opcoes7_2,
           data_questions.opcoes7_3]

questao7 = Questao(enunciado=data_questions.enunciado7,
                   opcoes=opcoes7,
                   questao_key='questao7',
                   slider_key='intensidade7')
questao7.gerar_questao()
st.markdown('---')

# Questão 8
st.markdown('Questão 8')

opcoes8 = [data_questions.opcoes8_1,
           data_questions.opcoes8_2,
           data_questions.opcoes8_3]

questao8 = Questao(enunciado=data_questions.enunciado8,
                   opcoes=opcoes8,
                   questao_key='questao8',
                   slider_key='intensidade8')
questao8.gerar_questao()
st.markdown('---')

# Questão 9
st.markdown('Questão 9')

opcoes9 = [data_questions.opcoes9_1,
           data_questions.opcoes9_2,
           data_questions.opcoes9_3]
questao9 = Questao(enunciado=data_questions.enunciado9,
                   opcoes=opcoes9,
                   questao_key='questao9',
                   slider_key='intensidade9')
questao9.gerar_questao()
st.markdown('---')


def get_answers():
    return st.write('Respostas')


st.button(label='Enviar respostas', use_container_width=True, on_click=get_answers())
