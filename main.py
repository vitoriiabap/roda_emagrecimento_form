import streamlit as st
from models.question import Question
import data.questions_data as data_questions
import numpy as np
import matplotlib.pyplot as plt
import re
import datetime


def generate_question_object(question, indice):
    question = Question(
        wording=question['enunciado'],
        options=question['opções'],
        question_key=f'questao{indice}',
        slider_key=f'intensidade{indice}',
        concept=question['valor']
    )
    question.generate_question()
    return question


def normalize_intensity(intensity):
    return intensity / len(index_questions)


def generate_slimming_circle_plot(questions):
    concepts = np.array(list(map(lambda question: question.concept, questions)))
    intensidades = np.array(list(map(lambda question: question.intensity, questions)))

    number_of_concepts = len(concepts)

    figure, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(10, 10), dpi=300)

    cones_width = np.fromiter((2 * np.pi / number_of_concepts for _ in range(9)), dtype='float64')
    cones_positions = np.linspace(0.0, 2 * np.pi, number_of_concepts, endpoint=False)
    my_cmap = plt.get_cmap('tab10')

    ax.bar(x=cones_positions,
           height=10,
           width=cones_width,
           edgecolor='white',
           zorder=1,
           alpha=0.1,
           color=my_cmap(normalize_intensity(index_questions)))

    ax.bar(x=cones_positions,
           height=intensidades,
           width=cones_width,
           edgecolor='white',
           zorder=1,
           alpha=1,
           color=my_cmap(normalize_intensity(index_questions)))

    for cone_position, concept in zip(cones_positions, concepts):
        text_angle = np.degrees(cone_position)
        if cone_position < np.pi:
            text_angle -= 90
        elif cone_position == np.pi:
            text_angle += 90
        else:
            text_angle += 90

        ax.text(cone_position, 11, concept, ha='center', va='center', rotation=text_angle,
                rotation_mode='anchor', fontsize=14)
    ax.set_xticks([])
    yticks_labels = [intensity_scale for intensity_scale in range(11)]
    ax.set_yticks(ticks=yticks_labels, labels=yticks_labels, color='black')

    ax.grid(alpha=0.9, color='white', lw=3)
    ax.spines['polar'].set_visible(False)
    plt.ylim(0, 10)
    plt.tight_layout()

    return figure


def validate_email(string):
    regex_email_pattern = re.compile(r'^[\w\-\.]+@([\w-]+\.)+[\w-]{2,4}$')
    match = re.match(regex_email_pattern, string)
    return match


def get_answers(*argv):
    questions = argv[0]
    client_data = argv[1]
    name = client_data['client_name']
    email = client_data['client_email']
    answers = []
    for question in questions:
        answer = {
            'Data / Hora': datetime.datetime.today().now(),
            'Nome': name,
            'Email': email,
            'Questão': question.question_key,
            'Conceito': question.concept,
            'Alternativa escolhida': question.chosen_option,
            'Intensidade escolhida': question.intensity
        }
        answers.append(answer)
        return answers


# Configuração da página
st.set_page_config(page_title='TISDE',
                   layout='wide',
                   initial_sidebar_state='collapsed',
                   menu_items=None, )

# Título do formulário
st.markdown('## Teste de Identificação de Sabotadores de Emagrecimento - TISDE')
st.markdown('#### Orientações')
st.markdown('1. Leia cada questão com muita atenção aos detalhes;')
st.markdown('2. Escolha a alternativa que mais se adequar ao seu momento; e')
st.markdown('3. Escolha o nível da sua afirmação arrastando o cursor do mouse de acordo com a classificação indicada')

# Informações do cliente
client_name = st.text_input(label='Nome completo')
client_email = st.text_input(label='Telefone / Email')

if client_name == '' and not validate_email(client_email):
    st.warning(body='Digite seu nome e um email válido, por favor.')
elif client_name == '' and validate_email(client_email):
    st.warning(body='Digite seu nome, por favor.')
elif client_name != '' and not validate_email(client_email):
    st.warning(body='Digite um email válido, por favor')
else:
    st.success(body='Obrigado por preencher seus dados, agora vamos continuar com o questionário.')

# Criando formulário
banco_dados_questoes = data_questions.perguntas
quantidade_questoes = len(banco_dados_questoes)
index_questions = np.arange(1, quantidade_questoes + 1, 1)
lista_questoes = list(map(generate_question_object, data_questions.perguntas, index_questions))

# Botão para enviar respostas
botao_enviar_respostas = st.button(label='Gerar resultado',
                                   use_container_width=True,
                                   type='primary',
                                   key='respostas',
                                   on_click=get_answers,
                                   args=(lista_questoes, {'client_name': client_name,
                                                          'client_email': client_email}))

# Mensagem após preenchimento
if st.session_state['respostas']:

    st.success(body=f"Parabéns, {client_name}! Seu resultado foi enviado para o email informado. Se nao estiver na "
                    f"sua Caixa de Entrada, por favor verifique na Caixa de Spans ;)")

    # st.markdown('\n')
    # st.markdown(f'Parabéns {client_name}!')
    # st.markdown('Este exercício identificou possíveis **atitude que podem estar atrapalhando e interrompendo '
    #             'a evolução do seu emagrecimento**.')
    # st.markdown('Ao longo desse processo de transformação física, **é preciso primeiramente conhecer e '
    #             'desenvolver suas ações comportamentais!**. Dessa forma, você só não conseguirá atingir o seu'
    #             ' objetivo, mas também defini-lo e mantê-lo.')
    # st.markdown('Vamos para os próximos passos? [Sim eu quero evoluir!](https://www.google.com.br)')

    fig = generate_slimming_circle_plot(lista_questoes)
    fig.savefig(f'resultados/resultado_{client_name.lower().strip().replace(" ", "_")}.png')

    # result_report.create_template(client_name=client_name)

    # with open('resultado.pdf', 'rb') as pdf_file:
    #     PDFbyte = pdf_file.read()

    # col1, col2, col3 = st.columns([1.2, 2, 1.2])
    # nome_client_para_arquivo_pdf = client_name.lower().replace(' ', '_').strip()
    # with col2:
    # st.pyplot(fig)
    # gerar_pdf = st.download_button(label='Baixe seu resultado...',
    #                                data=PDFbyte,
    #                                file_name=f'resultado_{nome_client_para_arquivo_pdf}.pdf',
    #                                mime='application/octet-stream',
    #                                use_container_width=True)

else:
    botao_enviar_respostas = None
