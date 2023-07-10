import streamlit as st


class Question:
    intensity_labels = {
        'A': 'Qual a intensidade da sua resposta, de 0 a 3',
        'B': 'Qual a intensidade da sua resposta, de 4 a 6',
        'C': 'Qual a intensidade da sua resposta, de 7 a 10'
    }

    def __init__(self,
                 wording,
                 options,
                 slider_key,
                 question_key,
                 concept):
        self.wording = wording
        self.chosen_option = None
        self.intensity = None
        self.options = options
        self.slider_key = slider_key,
        self.question_key = question_key
        self.concept = concept

    def generate_question(self):
        container = st.container()
        with container:
            st.markdown(f'*Questão - {self.question_key[-1]}*')
            st.markdown(self.wording)
            chosen_option = st.radio(label='',
                                     options=self.options, label_visibility='collapsed',
                                     key=self.question_key)
            self.chosen_option = chosen_option

        intensity_slider_label = Question.intensity_labels.get(self.chosen_option[0])
        intensity_values = intensity_slider_label.split('de')[-1].strip().split('a')
        min_intensity_value = int(intensity_values[0].strip())
        max_intensity_value = int(intensity_values[1].strip())

        chosen_intensity = st.slider(label=intensity_slider_label,
                                     min_value=min_intensity_value,
                                     max_value=max_intensity_value,
                                     key=self.slider_key,
                                     value=min_intensity_value)
        self.intensity = chosen_intensity
        st.markdown('---')

