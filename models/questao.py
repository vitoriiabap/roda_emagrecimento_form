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
                 valor,
                 alternativa_escolhida='',
                 intensidade=0):
        self.enunciado = enunciado
        self.alternativa_escolhida = alternativa_escolhida
        self.intensidade = intensidade
        self.opcoes = opcoes
        self.slider_key = slider_key,
        self.questao_key = questao_key
        self.valor = valor

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
        st.write(self.alternativa_escolhida[0])

        intensidade = st.slider(label=label,
                                min_value=min_value,
                                max_value=max_value,
                                key=self.slider_key,
                                value=min_value)
        self.intensidade = intensidade

        return intensidade
