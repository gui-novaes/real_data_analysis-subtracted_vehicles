# 🚗 Análise de Ocorrências de Roubo e Furto de Veículos em São Paulo

Este projeto consiste em uma aplicação web interativa desenvolvida com Streamlit e Python para analisar dados de ocorrências de roubo e furto de veículos no estado de São Paulo, a partir de uma base de dados em Excel fornecida pelo governo estadual. A aplicação oferece visualizações geográficas e análises estatísticas para identificar padrões e tendências nos dados.

---

## 🛠️ Funcionalidades Atuais

A aplicação atualmente oferece as seguintes funcionalidades:

* **Mapa de Calor:** Visualização da intensidade das ocorrências em diferentes áreas geográficas utilizando a biblioteca Folium.
* **Mapa de Contagem de Casos:** Visualização do número total de ocorrências por região no mapa, também utilizando Folium.
* **Ranking de Veículos:** Classificação dos veículos com o maior número de ocorrências de roubo/furto, apresentada de forma decrescente utilizando Pandas.

---

## 🚀 Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias e bibliotecas Python:

* **[Streamlit](https://streamlit.io/)**: Framework Python para criar aplicativos web interativos de forma rápida e fácil.
* **[Pandas](https://pandas.pydata.org/)**: Biblioteca para manipulação e análise de dados tabulares.
* **[Folium](https://python-visualization.github.io/folium/)**: Biblioteca para criação de mapas interativos com Leaflet.js.

---

## ⚙️ Como Executar (Instruções Gerais - Adaptar conforme sua necessidade)

1.  **Certifique-se de ter o Python instalado** na sua máquina.
2.  **Instale as bibliotecas necessárias:**
    ```bash
    pip install streamlit pandas folium
    ```
3.  **Salve a base de dados em Excel** (fornecida pelo governo de SP)[Base de Dados](https://www.ssp.sp.gov.br/estatistica/consultas) no mesmo diretório do seu script Python ou ajuste o caminho no código.
4.  **Execute o aplicativo Streamlit** a partir do terminal, navegando até o diretório do seu projeto e rodando o seguinte comando:
    ```bash
    streamlit run seu_script.py
    ```
    (Substitua `seu_script.py` pelo nome do seu arquivo Python).

---

## 🎯 Objetivo

O principal objetivo deste projeto é demonstrar habilidades em análise de dados, visualização de informações geográficas e desenvolvimento de aplicações web interativas utilizando Python e suas bibliotecas. Este projeto visa evidenciar a capacidade de transformar dados brutos em *insights* valiosos.

---

## 🔗 Link da Aplicação

[https://dataanalysis-subtractedvehicles.streamlit.app/](https://dataanalysis-subtractedvehicles.streamlit.app/)

---

## 🧑‍💻 Contribuições

Contribuições para o projeto são bem-vindas! Se você tiver ideias para novas funcionalidades, melhorias no código ou na interface, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

---