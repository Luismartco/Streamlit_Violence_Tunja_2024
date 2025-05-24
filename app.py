import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Violencia en Tunja 2024", layout="wide")

st.title("📊 Análisis de Violencia en Tunja - 2024")
st.markdown("Este panel interactivo permite analizar los casos de violencia reportados en Tunja durante el año 2024, usando herramientas de visualización de datos para comprender patrones clave.")

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv("Data/violencia.csv", encoding="latin-1", dayfirst=True)
    df.columns = df.columns.str.strip().str.replace(" ", "_").str.upper()
    df['FECHA__DEL__HECHO'] = pd.to_datetime(df['FECHA__DEL__HECHO'], errors='coerce', dayfirst=True)
    return df

df = load_data()

# SIDEBAR - Filtros
st.sidebar.header("🎛️ Filtros")
sexo_victima = st.sidebar.multiselect("Sexo de la víctima", df['SEXO__DE__LA__VICTIMA'].unique(), default=df['SEXO__DE__LA__VICTIMA'].unique())
estrato = st.sidebar.multiselect("Estrato socioeconómico", df['ESTRATO_SOCIECONOMICO__DE__LA__VICTIMA'].unique(), default=df['ESTRATO_SOCIECONOMICO__DE__LA__VICTIMA'].unique())

df_filtrado = df[
    (df['SEXO__DE__LA__VICTIMA'].isin(sexo_victima)) &
    (df['ESTRATO_SOCIECONOMICO__DE__LA__VICTIMA'].isin(estrato))
]

st.markdown("### 📈 Indicadores Generales")
colA, colB, colC = st.columns(3)

if df_filtrado.empty:
    colA.metric("Total de Casos", "0")
    colB.metric("Edad Promedio", "N/A")
    colC.metric("Último Caso Registrado", "N/A")
else:
    total_casos = len(df_filtrado)
    prom_edad = df_filtrado['EDAD__DE__LA__VICTIMA'].mean()
    fecha_mas_reciente = df_filtrado['FECHA__DEL__HECHO'].max()

    colA.metric("Total de Casos", total_casos)
    colB.metric("Edad Promedio", f"{prom_edad:.1f} años")
    colC.metric("Último Caso Registrado", fecha_mas_reciente.strftime("%Y-%m-%d"))

st.markdown("---")
st.markdown("### 🔍 Visualización de Datos")

# GRÁFICOS 2x2
col1, col2 = st.columns(2)

# Gráfico 1: Histograma de edades
with col1:
    st.markdown("#### 📊 Distribución por Edad")
    if not df_filtrado.empty:
        fig, ax = plt.subplots(figsize=(4, 2))
        sns.histplot(df_filtrado["EDAD__DE__LA__VICTIMA"], bins=10, ax=ax, color='steelblue')
        ax.set_xlabel("Edad")
        ax.set_ylabel("Número de casos")
        ax.tick_params(labelsize=8)
        st.pyplot(fig)
    else:
        st.info("No hay datos para mostrar en este gráfico.")

# Gráfico 2: Casos por barrio (Top 10)
with col2:
    st.markdown("#### 🏘️ Casos por Barrio (Top 10)")
    if not df_filtrado.empty:
        top_barrios = df_filtrado['BARRIO__DE__LA__VICTIMA'].value_counts().head(10)
        fig = px.bar(
            x=top_barrios.values,
            y=top_barrios.index,
            orientation='h',
            labels={"x": "Casos", "y": "Barrio"},
            color_discrete_sequence=["#6a0dad"]
        )
        fig.update_layout(height=250, margin=dict(t=20, b=20))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No hay datos para mostrar en este gráfico.")

# Gráfico 3: Relación con el agresor
with col1:
    st.markdown("#### 👤 Relación con el Agresor")
    if not df_filtrado.empty:
        top_relaciones = df_filtrado['REALCION__CON__LA__VICTIMA'].value_counts().head(7)
        fig = px.bar(
            x=top_relaciones.values,
            y=top_relaciones.index,
            orientation='h',
            labels={"x": "Casos", "y": "Relación"},
            color_discrete_sequence=["#d62728"]
        )
        fig.update_layout(height=250, margin=dict(t=20, b=20))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No hay datos para mostrar en este gráfico.")

# Gráfico 4: Ámbito o lugar del hecho
with col2:
    st.markdown("#### 📍 Ámbito o Lugar del Hecho")
    if not df_filtrado.empty:
        ambito_data = df_filtrado['AMBITO__O__LUGAR'].value_counts(normalize=True).sort_values(ascending=True) * 100

        fig, ax = plt.subplots(figsize=(4, 2))
        bars = ax.barh(ambito_data.index, ambito_data.values, color=sns.color_palette("pastel"))
        ax.set_xlabel("Porcentaje (%)")
        ax.set_xlim(0, 100)

        for bar in bars:
            width = bar.get_width()
            ax.text(width + 1, bar.get_y() + bar.get_height()/2,
                    f'{width:.1f}%', va='center', fontsize=7)

        ax.tick_params(labelsize=7)
        st.pyplot(fig)
    else:
        st.info("No hay datos para mostrar en este gráfico.")