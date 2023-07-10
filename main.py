import streamlit as st
from models.question import Question
import data.questions_data as data_questions
import numpy as np
import matplotlib.pyplot as plt
import result_report


def gerar_objeto_questao(pergunta, indice):
    pergunta = Question(
        wording=pergunta['enunciado'],
        options=pergunta['opções'],
        question_key=f'questao{indice}',
        slider_key=f'intensidade{indice}',
        concept=pergunta['valor']
    )
    pergunta.generate_question()
    return pergunta


def normalizar_intensidades(intensidade):
    return intensidade / len(lista_indices_questoes)


def gerar_grafico_roda_emagrecimento(questoes):
    conceitos = np.array(list(map(lambda questao: questao.concept, questoes)))
    intensidades = np.array(list(map(lambda questao: questao.intensity, questoes)))

    quantidade_conceitos = len(conceitos)

    figure, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(10, 10), dpi=300)

    larguras_cones = np.fromiter((2 * np.pi / quantidade_conceitos for _ in range(9)), dtype='float64')
    posicoes_cones = np.linspace(0.0, 2 * np.pi, quantidade_conceitos, endpoint=False)
    my_cmap = plt.get_cmap('tab10')

    ax.bar(x=posicoes_cones,
           height=10,
           width=larguras_cones,
           edgecolor='white',
           zorder=1,
           alpha=0.1,
           color=my_cmap(normalizar_intensidades(lista_indices_questoes)))

    ax.bar(x=posicoes_cones,
           height=intensidades,
           width=larguras_cones,
           edgecolor='white',
           zorder=1,
           alpha=1,
           color=my_cmap(normalizar_intensidades(lista_indices_questoes)))

    for posicao_cone, valor in zip(posicoes_cones, conceitos):
        angulo_do_texto = np.degrees(posicao_cone)
        if posicao_cone < np.pi:
            angulo_do_texto -= 90
        elif posicao_cone == np.pi:
            angulo_do_texto += 90
        else:
            angulo_do_texto += 90

        ax.text(posicao_cone, 11, valor, ha='center', va='center', rotation=angulo_do_texto,
                rotation_mode='anchor', fontsize=14)
    ax.set_xticks([])
    yticks_labels = [escala_intensidade for escala_intensidade in range(11)]
    ax.set_yticks(ticks=yticks_labels, labels=yticks_labels, color='black')

    ax.grid(alpha=0.9, color='white', lw=3)
    ax.spines['polar'].set_visible(False)
    plt.ylim(0, 10)
    plt.tight_layout()

    return figure


# Configuração da página
st.set_page_config(page_title='Roda do Emagrecimento',
                   layout='wide',
                   initial_sidebar_state='collapsed',
                   menu_items=None, )

# Título do formulário
st.markdown('## Roda do emagrecimento')
st.markdown('Orientações a respeito do preenchimento do formulário')
st.markdown('- Orientação 1 \n'
            '- Orientação 2\n'
            '- Orientação 3')

st.markdown('###### Vamos iniciar...')

# Informações do cliente
nome_client = st.text_input(label='Nome')
telefone_client = st.text_input(label='Telefone / Email')

# Criando formulário
banco_dados_questoes = data_questions.perguntas
quantidade_questoes = len(banco_dados_questoes)
lista_indices_questoes = np.arange(1, quantidade_questoes + 1, 1)
lista_questoes = list(map(gerar_objeto_questao, data_questions.perguntas.values(), lista_indices_questoes))

# Botão para enviar respostas
botao_enviar_respostas = st.button(label='Enviar respostas',
                                   use_container_width=True,
                                   type='primary',
                                   key='respostas')

# Mensagem após preenchimento
if st.session_state['respostas']:
    if telefone_client != '':
        # st.success('Obrigado por responder, suas respostas foram enviadas para o email informado.')
        fig = gerar_grafico_roda_emagrecimento(lista_questoes)
        result_report.create_template(client_name=nome_client)
        with open('resultado.pdf', 'rb') as pdf_file:
            PDFbyte = pdf_file.read()

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.pyplot(fig)
            gerar_pdf = st.download_button(label='Baixe seu resultado...',
                                           data=PDFbyte,
                                           args=[fig],
                                           file_name='test.pdf',
                                           mime='application/octet-stream',
                                           use_container_width=True)
    else:
        st.warning('Por favor preencha seu email')
else:
    botao_enviar_respostas = None
