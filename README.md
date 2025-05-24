# 📊 Análisis de Violencia en Tunja - 2024

Este proyecto es una aplicación interactiva desarrollada con [Streamlit](https://streamlit.io/) que permite analizar los casos de violencia reportados en la ciudad de **Tunja, Colombia**, durante el año 2024. Utiliza visualizaciones gráficas para facilitar la comprensión de los patrones sociodemográficos y espaciales relacionados con la violencia.

---

## 📁 Estructura del Proyecto

```
📦violencia-tunja-2024
├── 📂data
│   └── violencia.csv             # Dataset principal con los casos reportados
├── 📄 app.py                     # Aplicación principal de Streamlit
├── 📄 README.md                  # Documentación del proyecto
└── 📄 requirements.txt           # Dependencias necesarias
```

---

## 🚀 Cómo ejecutar la aplicación

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/violencia-tunja-2024.git
cd violencia-tunja-2024
```

### 2. Crea un entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate      # En Linux/macOS
venv\Scripts\activate         # En Windows
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecuta la app

```bash
streamlit run app.py
```

---

## 🧪 Funcionalidades

- **Filtros dinámicos** por sexo y estrato socioeconómico.
- **Indicadores generales** como total de casos, edad promedio y fecha del último caso.
- Visualizaciones:
  - 📊 Histograma por edad
  - 🏘️ Casos por barrio (Top 10)
  - 👤 Relación con el agresor
  - 📍 Ámbito o lugar del hecho
- Manejo de errores para evitar fallos cuando los filtros no retornan resultados.

---

## 📦 Requisitos

El archivo `requirements.txt` debe incluir las siguientes librerías:

```txt
streamlit
pandas
seaborn
matplotlib
plotly
```

Instálalas con:

```bash
pip install -r requirements.txt
```

---

## 📌 Notas

- Asegúrate de tener el archivo `violencia.csv` en la carpeta `data/`, con codificación `latin-1`.
- El nombre de las columnas del CSV será normalizado automáticamente (mayúsculas, sin espacios).
- Las fechas serán convertidas correctamente con formato `día/mes/año`.

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

---

## 🤝 Autor

**Luis M.**  
*Proyecto académico de análisis de datos con enfoque social*
