from codigo_de_ejecucion import *
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_echarts import st_echarts

#CONFIGURACION DE LA PÁGINA
st.set_page_config(
     page_title = 'Modelo probabilidad ataque cardiaco',
     page_icon = 'chaval.png',
     layout = 'wide')
     
     
#SIDEBAR
with st.sidebar:
    st.image('revision.jpg')
    
    #INPUTS DE LA APLICACION   
    edad = st.number_input('Edad', 1, 100)
    sexo = st.selectbox('Sexo: 0-Mujer 1-Hombre ', ['0','1'])
    tipo_dolor_toracico = st.radio('Dolor torácico: 1-Angina típica, 2-Angina atípica 3-Dolor no angina 4-Asintomático', ['1','2','3','4'])
    presion_arterial_sangre = st.slider('Presión arterial', 50, 250)
    colesterol_serico = st.slider('Colesterol sérico', 100, 500)
    presion_arterial_reposo = st.radio('Presión arterial reposo', ['0','1','2'])
    angina_inducida_ejercicio = st.selectbox('Angina inducida ejercicio: 1-Si 0-No', ['0','1'])
    pico_anterior = st.number_input('Pico anterior', 0.00, 10.00)
    segmento_st_ejercio_maximo = st.selectbox('Segmento ejercicio máximo: 1-Ascendente 2-Plano 3-Descendente', ['0','1','2'])
    num_vasos_coloreados_fluoroscopia = st.selectbox('Número de vasos coloreados', ['0','1','2','3'])
    talasemia = st.selectbox('Talasemia: 1-Normal 2-Defecto fijo 7-Defecto reversible', ['1','2','3'])

#MAIN
st.title('MODELO ANÁLISIS ATAQUE CARDIACO')


#CALCULAR

#Crear el registro
registro = pd.DataFrame({'edad':edad,
                         'sexo':sexo,
                         'tipo_dolor_toracico':tipo_dolor_toracico,
                         'presion_arterial_sangre':presion_arterial_sangre,
                         'colesterol_serico':colesterol_serico,
                         'presion_arterial_reposo':presion_arterial_reposo,
                         'angina_inducida_ejercicio':angina_inducida_ejercicio,
                         'pico_anterior':pico_anterior,
                         'segmento_st_ejercio_maximo':segmento_st_ejercio_maximo,
                         'num_vasos_coloreados_fluoroscopia':num_vasos_coloreados_fluoroscopia,
                         'talasemia':talasemia}
                        ,index=[0])

#CALCULAR PROBABILIDAD
if st.sidebar.button('CALCULAR PROBABILIDAD'):
    #Ejecutar el modelo
    scoring = ejecutar_modelos(registro)
    
    #Calcular los kpis
    kpi_ataque = int(scoring * 100)
    
    #Velocimetros
    #Codigo de velocimetros tomado de https://towardsdatascience.com/5-streamlit-components-to-build-better-applications-71e0195c82d4
    ataque_options = {
            "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
            "series": [
                {
                    "name": "ATAQUE",
                    "type": "gauge",
                    "axisLine": {
                        "lineStyle": {
                            "width": 10,
                        },
                    },
                    "progress": {"show": "true", "width": 10},
                    "detail": {"valueAnimation": "true", "formatter": "{value}"},
                    "data": [{"value": kpi_ataque, "name": "ATAQUE"}],
                }
            ],
        }
 
#Representarlos en la app
    col1,col2,col3 = st.columns(3)
    with col2:
        st_echarts(options=ataque_options, width="110%", key=1)
        st.write('La probabilidad de que el paciente tenga un ataque de corazón es:')
        st.metric(label="PROBABILIDAD", value = kpi_ataque) #Metido en estático por simplicidad
 
#Prescripcion
    #col1,col2,col3 = st.columns(3)
    #with col2:
        #st.write('La probabilidad de que el paciente tenga un ataque de corazón es:')
        #st.metric(label="PROBABILIDAD", value = kpi_ataque) #Metido en estático por simplicidad
else:
    st.write('DEFINE LOS PARÁMETROS DEL PACIENTE Y HAZ CLICK EN CALCULAR PROBABILIDAD') 
