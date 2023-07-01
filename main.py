import streamlit as st
from models.questao import Questao

# Configuração da página
st.set_page_config(page_title='Roda do Emagrecimento',
                   layout='wide',
                   initial_sidebar_state='collapsed',
                   menu_items=None)

# Título do formulário
st.markdown('### Roda do emagrecimento')
st.markdown('[x] - Olá meninas')

# Questão 1
st.markdown('Questão 1')
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
st.markdown('Questão 2')
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

# Questão 3
st.markdown('Questão 3')
enunciado3 = "###### AUTORESPONSABILIDADE: Ter a capacidade de assumir para si mesma seus resultados, " \
             "independente se positivos ou negativos. Consciência de que é nossa responsabilidade tudo " \
             "que nos acontece."

opcoes3_1 = "A. A culpa da minha vida estar como está hoje não é minha, pessoas que passaram ou estão na minha " \
            "vida sempre dificultam tudo. Minha rotina e trabalho são estressantes e acabo não tendo tempo " \
            "para pensar e cuidar de mim."

opcoes3_2 = "B.  Acho que as pessoas que convivem comigo poderiam facilitar algumas coisas para me " \
            "ajudar a emagrecer e ser mais calma."

opcoes3_3 = "C. Acredito que eu sou a única responsável por meus fracassos e por minhas conquistas."

opcoes3 = [opcoes3_1, opcoes3_2, opcoes3_3]
questao3 = Questao(enunciado=enunciado3,
                   opcoes=opcoes3,
                   questao_key='questao3',
                   slider_key='intensidade3')
questao3.gerar_questao()
st.markdown('---')

# Questão 4
st.markdown('Questão 4')
enunciado4 = "###### AÇÃO CONSCIENTE: Sair do automático, ter comportamentos através de escolhas " \
             "conscientes dos seus resultados e consequências."
opcoes4_1 = "A. Eu nunca penso antes de comer, quando vejo já me entreguei a compulsão ou aquele " \
            "doce que eu amo, ou a pizza do final de semana. Nunca me questiono sobre esses " \
            "comportamentos."
opcoes4_2 = "B. Às vezes eu penso antes de comer, vejo se aquilo vai ser prejudicial para mim, mesmo " \
            "não conseguindo me controlar."
opcoes4_3 = 'C. Eu SEMPRE penso antes de comer, mesmo que às vezes eu “escorregue”.'

opcoes4 = [opcoes4_1, opcoes4_2, opcoes4_3]
questao4 = Questao(enunciado=enunciado4,
                   opcoes=opcoes4,
                   questao_key='questao4',
                   slider_key='intensidade4')
questao4.gerar_questao()
st.markdown('---')

# Questão 5
st.markdown('Questão 5')
enunciado5 = "###### Foco: Direcionar sua atenção naquilo que realmente importa, naquilo que realmente é " \
             "importante na sua vida. Somente pessoas com foco são capazes de grandes realizações e " \
             "conquistas."
opcoes5_1 = "A. Eu sou uma pessoa que nunca foca em nada, estou sempre com mil coisas na cabeça, e " \
            "por isso, ir até o fim nas coisas que eu começo é muito difícil."
opcoes5_2 = "B. Às vezes consigo ter foco, mantenho por um tempinho curto, mas depois de pouco tempo " \
            "já me vejo abandonando tudo para trás."
opcoes5_3 = "C. Meu foco está totalmente voltado para emagrecer, faço tudo que está ao meu alcance " \
            "para conquistar o que eu tanto sonho."

opcoes5 = [opcoes5_1, opcoes5_2, opcoes5_3]
questao5 = Questao(enunciado=enunciado5,
                   opcoes=opcoes5,
                   questao_key='questao5',
                   slider_key='intensidade5')
questao5.gerar_questao()
st.markdown('---')

# Questão 6
st.markdown('Questão 5')
enunciado6 = "###### ENFRENTAMENTO Não mascarar o quanto essa vida no automático te custa. Enfrentar a dor " \
            "da mudança."
opcoes6_1 = "A. É muito sofrido me olhar no espelho e subir na balança, prefiro não saber como estou " \
            "hoje porque isso me dói e eu prefiro evitar esse confronto com o que me machuca, por isso " \
            "prefiro usar “uma venda nos olhos para não encarar a realidade”."
opcoes6_2 = "B. Ver o ponto que eu cheguei me faz mal, às vezes eu me coloco de frente com a triste " \
            "realidade que estou vivendo, mas isso me machuca e acabo colocando de volta “a venda " \
            "nos olhos” para não sofrer mais."
opcoes6_3 = "C. Por mais difícil que seja, eu tenho o hábito de parar e me analisar, perceber o que eu " \
            "venho fazendo que está me colocando na vida que hoje me faz mal. Já arranquei a venda " \
            "dos meus olhos."

opcoes6 = [opcoes6_1, opcoes6_2, opcoes6_3]
questao6 = Questao(enunciado=enunciado6,
                   opcoes=opcoes6,
                   questao_key='questao6',
                   slider_key='intensidade6')
questao6.gerar_questao()
st.markdown('---')

# Questão 7
st.markdown('Questão 7')
enunciado7 = "###### AÇÃO: É ela que gera os resultados que te realizam."
opcoes7_1 = "A. Sou hoje uma pessoa que não faz nada para emagrecer."
opcoes7_2 = "B. Sou o tipo de pessoa que enrola para começar uma dieta e a fazer exercício, e depois de " \
            "algum tempo abandono."
opcoes7_3 = "C. Sou uma pessoa decidida, sei o que preciso fazer para emagrecer e entro em ação para " \
            "conquistar esse objetivo."

opcoes7 = [opcoes7_1, opcoes7_2, opcoes7_3]
questao7 = Questao(enunciado=enunciado7,
                   opcoes=opcoes7,
                   questao_key='questao7',
                   slider_key='intensidade7')
questao7.gerar_questao()
st.markdown('---')

# Questão 8
st.markdown('Questão 8')
enunciado8 = "###### AÇÃO CONTÍNUA: É a capacidade de sustentar seus comportamentos por um longo período."
opcoes8_1 = "A. Eu nem começo a fazer alguma coisa pelo meu emagrecimento"
opcoes8_2 = "B. Toda vez que eu comecei, uma dieta em menos de uma semana já estava abandonando."
opcoes8_3 = "C. Sou o tipo de pessoa que não para até chegar no objetivo. Sei que o sucesso é " \
            "questão de tempo e não vou parar até conquistar."

opcoes8 = [opcoes8_1, opcoes8_2, opcoes8_3]
questao8 = Questao(enunciado=enunciado8,
                   opcoes=opcoes8,
                   questao_key='questao8',
                   slider_key='intensidade8')
questao8.gerar_questao()
st.markdown('---')

# Questão 9
st.markdown('Questão 9')
enunciado9 = "###### RESILIÊNCIA: Capacidade de se recobrar facilmente ou se adaptar à má sorte ou às mudanças.."
opcoes9_1 = "A. Sou o tipo de pessoa que quando acontece alguma coisa que me deixa triste não consigo " \
            "lidar com isso, desconto sempre na comida minhas frustrações, fico sempre ruminando o acontecimento"
opcoes9_2 = "B. Sou o tipo de pessoa que quando acontece alguma coisa que me deixa triste eu demoro " \
            "muito tempo para conseguir absorver o que aconteceu. Mas depois até que eu consigo " \
            "seguir em frente."
opcoes9_3 = "C. Sou o tipo de pessoa que quando acontece alguma coisa que me deixa triste eu consigo " \
            "me reerguer pois sei que mesmo levando pancada da vida ela precisa continuar, e isso não " \
            "me para."

opcoes9 = [opcoes9_1, opcoes9_2, opcoes9_3]
questao9 = Questao(enunciado=enunciado9,
                   opcoes=opcoes9,
                   questao_key='questao9',
                   slider_key='intensidade9')
questao9.gerar_questao()
st.markdown('---')
