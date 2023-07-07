import streamlit as st
from models.questao import Questao
import data.questions_data as data_questions
import numpy as np
import matplotlib.pyplot as plt


def gerar_objeto_questao(pergunta, indice):
    pergunta = Questao(
        enunciado=pergunta['enunciado'],
        opcoes=pergunta['opções'],
        questao_key=f'questao{indice}',
        slider_key=f'intensidade{indice}',
        valor=pergunta['valor']
    )
    pergunta.gerar_questao()
    return pergunta


def normalizar_intensidades(intensidade):
    return intensidade / len(lista_indices_questoes)

def gerar_grafico_roda_emagrecimento(questoes):
    conceitos = np.array(list(map(lambda questao: questao.valor, questoes)))
    intensidades = np.array(list(map(lambda questao: questao.intensidade, questoes)))

    quantidade_conceitos = len(conceitos)

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(10, 10))

    larguras_cones = np.array([2 * np.pi / quantidade_conceitos for conceito in conceitos])
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

    return fig


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

# Criando formulário
banco_dados_questoes = data_questions.perguntas
quantidade_questoes = len(banco_dados_questoes)
lista_indices_questoes = np.arange(1, quantidade_questoes + 1, 1)
lista_questoes = list(map(gerar_objeto_questao, data_questions.perguntas.values(), lista_indices_questoes))

# Botão para enviar respostas
respostas = st.button(label='Enviar respostas',
                      use_container_width=True,
                      type='primary',
                      key='respostas')

# Gerando a Roda
if st.session_state['respostas']:
    grafico_roda_emagrecimento = gerar_grafico_roda_emagrecimento(lista_questoes)

    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    col1, col2, col3 = st.columns([1, 0.3, 2])
    with col1:
        st.pyplot(grafico_roda_emagrecimento)
    with col3:
        st.markdown("#### Vamos analisar seus resultados...")

else:
    respostas = None
