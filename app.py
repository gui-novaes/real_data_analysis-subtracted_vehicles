import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster

df = pd.read_excel("VeiculosSubtraidos_2025.xlsx", engine='openpyxl')

st.title('Dados de Veículos Subtraídos no Estado de São Paulo em 2025')

# DELETE NaN
df = df.dropna(subset=['LATITUDE', 'LONGITUDE'], how='any')

# def coordinates default of map
map = folium.Map(location=[-23.54, -46.63], zoom_start=6.3)
coordinates = list(zip(df.LATITUDE, df.LONGITUDE))

# HEATMAP SUBTRACTED VEHICLES
heatMap = HeatMap(coordinates, radius=10, blur=10)
map.add_child(heatMap)

# Show HeatMap
st.header("Mapa de Calor de Veículos Subtraídos")
st.components.v1.html(folium.Figure().add_child(map).render(), height=500)

st.divider()

# Show Counter Subtracted Map
map = folium.Map(location=[-23.54, -46.63], zoom_start=6.3)
mapCounter = MarkerCluster(coordinates)
map.add_child(mapCounter)

# Show CounterMap
st.header("Contagem de Veículos Subtraídos")
st.components.v1.html(folium.Figure().add_child(map).render(), height=500)

st.divider()

st.title('Veículos com mais índices de Roubo/Furto')

# count of most subtracted vehicles
df_vehicles = df.groupby('DESCR_MARCA_VEICULO').agg({
    'DESCR_MARCA_VEICULO': 'count',
    'DESCR_TIPO_VEICULO': 'first'
}).rename(columns={
    'DESCR_MARCA_VEICULO': 'N° de Ocorrências',
    'DESCR_TIPO_VEICULO': 'Tipo de Veículo'
}).sort_values(by='N° de Ocorrências', ascending=False)

df_vehicles.index.name = None
df_vehicles_formatted = df_vehicles.reset_index()
df_vehicles_formatted.index += 1
df_vehicles_formatted.columns = ['Marca e Modelo do Veículo', 'N° de Ocorrências', 'Tipo de Veículo']

st.write(df_vehicles_formatted)
