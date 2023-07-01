import streamlit as st


class Questao:
    conditions = {
        'A': 'Qual a intensidade da sua resposta, de 0 a 3',
        'B': 'Qual a intensidade da sua resposta, de 4 a 6',
        'C': 'Qual a intensidade da sua resposta, de 7 a 10'
    }

    def __init__(self,
                 enunciado,
                 opcoes,
                 slider_key,
                 questao_key,
                 alternativa_escolhida='',
                 intensidade=0):
        self.enunciado = enunciado
        self.alternativa_escolhida = alternativa_escolhida
        self.intensidade = intensidade
        self.opcoes = opcoes
        self.slider_key = slider_key,
        self.questao_key = questao_key

    def gerar_questao(self):
        container = st.container()
        with container:
            st.markdown(self.enunciado)
            alternativa_marcada = st.radio(label='',
                                           options=self.opcoes, label_visibility='collapsed',
                                           key=self.questao_key)
            self.alternativa_escolhida = alternativa_marcada
            self.mostrar_seletor_intensidade()

    def mostrar_seletor_intensidade(self):
        label = Questao.conditions.get(self.alternativa_escolhida[0])
        values = label.split('de')[-1].strip().split('a')
        min_value = int(values[0].strip())
        max_value = int(values[1].strip())

        intensidade = st.slider(label=label,
                                min_value=min_value,
                                max_value=max_value,
                                key=self.slider_key)
        self.intensidade = intensidade

        return intensidade

st.write('Roda do emagrecimento')
st.write('Formulário - 1')


# Questão 1
enunciado1 = "###### MERECIMENTO: é o que torna alguém ou algo digno de mérito"

opcao1_1 = "A. Sempre senti que eu não sou digna de ter tudo na vida, e todas as vezes que alguma coisa começa a " \
           "se organizar na minha vida, outra desanda."
opcao1_2 = "B. Me enxergar como merecedora de uma vida equilibrada é difícil, mas pensando bem acredito que mereça" \
           " sim."
opcao1_3 = "C. Eu tenho certeza absoluta que sou merecedora de ter tudo que eu desejo nessa vida."
opcoes1 = [opcao1_1, opcao1_2, opcao1_3]

questao1 = Questao(enunciado=enunciado1,
                   opcoes=opcoes1,
                   questao_key='questao1',
                   slider_key='intensidade1')
questao1.gerar_questao()
st.markdown('---')

# Questão 2

enunciado2 = "###### AUTOPERCEPÇÃO: Reconhecer sua reação diante de cada emoção e situação, ou seja, como as emoções" \
             " se manifestam em sua vida. Percebendo o que deve ser trabalhado para a mudança e reconhecendo o que" \
             " deve ser valorizado."

opcoes2_1 = "A. Todas as vezes que eu estou estressada acabo descontando meu estresse na comida ou em pessoas que " \
            "estão sempre junto á mim. Estou sempre irritada e perceber essa irritação ou estresse é muito difícil" \
            " para mim."
opcoes2_2 = "B. É habitual eu estar estressada ou irritada e descontar nas pessoas e na comida minhas emoções. Apesar" \
            " disso, algumas vezes eu consigo perceber que os problemas estão nas minhas emoções, mas nunca consigo" \
            " controlar."
opcoes2_3 = "C. Eu tenho total consciência de como eu reajo as emoções, e toda vez que me percebo emocionalmente" \
            " abalada consigo aos poucos me acalmar e me recompor, me colocando em um estado mais equilibrado."

opcoes2 = [opcoes2_1, opcoes2_2, opcoes2_3]

questao2 = Questao(enunciado=enunciado2,
                   opcoes=opcoes2,
                   questao_key='questao2',
                   slider_key='intensidade2')

questao2.gerar_questao()
st.markdown('---')