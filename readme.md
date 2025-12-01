# 📘 README — Análise OLAP dos Microdados do ENEM 2023

## 🎓 **Descrição do Trabalho**

O Exame Nacional do Ensino Médio (ENEM) é uma das principais avaliações educacionais do Brasil, utilizado como critério de acesso ao ensino superior e como indicador de qualidade do ensino. Seus microdados fornecem um conjunto abrangente de informações sobre os participantes, incluindo notas por área de conhecimento, dados demográficos e características socioeconômicas.

### 📌 **Situação Problema**

Você faz parte do Ministério da Educação e precisa realizar análises estratégicas a partir dos Microdados do ENEM 2023. Essas análises devem apoiar decisões relacionadas ao processo de aplicação da prova e a programas educacionais vinculados.

### 🎯 **Objetivo Geral**

Desenvolver um **modelo OLAP** baseado nos microdados do ENEM 2023. A partir dos dados disponibilizados em formato **OLTP**, será necessário transformá-los em um **modelo multidimensional**, que posteriormente será implementado e explorado no **Microsoft Power BI**.


                        +----------------+
                        |  DIM_REGIAO    |
                        +--------+-------+
                                 |
                                 |
               +-----------------+------------------+
               |                                    |
       +-------+--------+                  +--------+--------+
       |   DIM_ESTADO   |                  |  DIM_MUNICIPIO  |
       +-----------------+                  +-----------------+
               |                                    |
               +-----------------+------------------+
                                 |
                                 |
                         +-------+-------+
                         |   FAT_NOTAS   |
                         +---------------+
                                 |
     +---------------------------+------------------------------+
     |           |                 |                |           |
    +----+----+ +---+----+ +------+-----+ +------+-----+ +--+-----+
    | DIM_ESC | | DIM_SEXO | | DIM_RACA | | DIM_FAIXA | | DIM_SOC |
    +---------+ +-----------+ +-----------+ +-----------+ +--------+



### 🗂️ **Base de Dados Utilizada**

* **Fonte:** Microdados do ENEM
* **Acesso:** [https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem)

Os microdados incluem informações detalhadas sobre milhões de participantes, permitindo análises profundas e indicadores relevantes para políticas públicas.

---

## 📊 **Lista de Tarefas / Análises Obrigatórias**

A seguir estão as análises que deverão ser produzidas a partir do modelo OLAP:

### 1. 📍 **Desempenho médio dos alunos por Estado**

Cálculo da média das notas das áreas de conhecimento para cada Unidade Federativa.

### 2. 🌎 **Desempenho médio dos alunos por região**

Comparação entre Norte, Nordeste, Centro-Oeste, Sudeste e Sul.

### 3. 💰 **Desempenho médio dos alunos por faixa socioeconômica**

Agrupamento conforme classificação socioeconômica definida pelo questionário.

### 4. 📝 **Distribuição das maiores notas de redação por estado e município**

Identificação dos locais com os melhores desempenhos em redação.

### 5. 🗺️ **Distribuição geográfica das maiores notas por área de conhecimento**

Mapeamento espacial dos destaques em cada área: LC, MT, CH, CN e Redação.

### 6. 👥 **Distribuição das notas por gênero e situação socioeconômica**

Avaliação segmentada considerando sexo e contexto econômico.

### 7. 🎂 **Distribuição das notas por faixa etária**

Criação de faixas de idade e análise comparativa das notas.

### 8. 🎨 **Distribuição das notas por raça/cor**

Agrupamento segundo a classificação do IBGE presente no ENEM.

### 9. 🏙️ **Diferenças nas médias de notas entre alunos de capitais e do interior**

Comparação entre municípios classificados como capitais ou não.

### 10. ⚖️ **Comparação das notas por gênero em cada área de conhecimento**

Análise da variação de desempenho masculino x feminino.

### 11. 🏫 **Média de notas entre alunos de escolas públicas e privadas por área de conhecimento**

Comparação das redes escolar pública e privada considerando LC, MT, CH, CN e Redação.

---

## 🛠️ **Entrega Esperada**

* Modelo multidimensional criado a partir dos microdados.
* ETL completo documentado.
* Dashboard no Power BI contendo todas as análises listadas.
* README explicando metodologia, dados utilizados e indicadores.

---

## 👨‍💻 **Tecnologias Sugeridas**

* Python (Pandas, NumPy)
* Power BI
