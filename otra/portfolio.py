import streamlit as st
from streamlit_extras.app_logo import add_logo

# Configuración de la página
st.set_page_config(
    page_title="Portafolio de Proyectos",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Logo y título principal
#add_logo("assets/codingisfun_logo.png", height=150)
st.title(" PORTFOLIO")
st.markdown("<p style='text-align: center; font-size: 20px;'>Explora mis notebooks de GitHub directamente desde aquí.</p>", unsafe_allow_html=True)

# Sidebar - Selección de proyectos y sección About Me
st.sidebar.title("📂 Proyectos")
option = st.sidebar.radio(
    "Selecciona un proyecto:",
    ("Proyecto 1", "Proyecto 2", "Proyecto 3", "Proyecto 4")
)

st.sidebar.title("📄 Sobre mi")
st.sidebar.image("./assets/1perfil.JPG", width=200)
st.sidebar.write("**Haidel Valera**")
st.sidebar.write("Analista de Datos, apoyando a empresas mediante el soporte de la toma de decisiones basada en datos.")
st.sidebar.write("---")
st.sidebar.subheader("Experiencia en el sector TI")
st.sidebar.write(
    """
    - 7 años de experiencia extrayendo insights accionables de datos
    - Sólida experiencia práctica y conocimientos en Python
    - Buen entendimiento de principios estadísticos y sus respectivas aplicaciones
    """
)
st.sidebar.subheader("Habilidades")
st.sidebar.write(
    """
    - Programación: Python (Pandas, Seaborn, Matplotlib)
    - Visualización de datos: Tableau, Plotly
    - Bases de datos: SQLSERVER, MySQL
    """
)

# Mostrar enlaces directos a los notebooks de GitHub
if option == "Proyecto 1":
    st.write("## 📍 Airbnb Project - Análisis de Datos")
    st.markdown("## Localizar el perfil (o perfiles) de inmuebles que maximizan el potencial comercial en el mercado del alquiler turístico y las principales zonas donde buscarlos.")
    st.markdown("[🔗 Ver Notebook en GitHub] (https://github.com/haidelous/Portfolio/tree/main/Airbnb_project)")
    

elif option == "Proyecto 2":
    st.write("## 💡 Energia Renovable - Análisis de Datos ")
    st.markdown("## Analizar los datos disponibles para intentar intuir donde pueden estar los problemas y si es necesario desplazar o no a un equipo de ingenieros a las plantas.")
    st.markdown("[🔗 Ver Notebook en GitHub] (https://github.com/haidelous/Portfolio/tree/main/Paneles_Solar_project)")

elif option == "Proyecto 3":
    st.write("## 🌐 Ecommerce - Análisis de Datos")
    st.markdown(
        """
        ## Analizar los datos transaccionales para intentar potenciales acciones CRO que incrementen visitas, conversiones y ticket medio, y por tanto incrementar la facturación global del ecommerce.  
        Crear activos analíticos avanzados como una segmentación RFM y un sistema de recomendación que impulsen la consecución del objetivo.
        """
    )
    st.markdown("[🔗 Ver Notebook en GitHub] (https://github.com/haidelous/Portfolio/tree/main/E-commerce_project)")

elif option == "Proyecto 4":
    st.write("## 📊 DREAM RESORT HOTEL - DASHBOARD")
    st.markdown(
        """
        ## Creación de un dashboard para que la dirección pueda tomar mejores decisiones a la hora de gestionar las instalaciones del hotel con un foco DATA-DRIVEN. 
        """
    )
    st.markdown("[🔗 Ver Tableau ] (https://public.tableau.com/shared/8HJJNXHKX?:display_count=n&:origin=viz_share_link")
# Pie de página
st.divider()
st.markdown(
    """
    <style>
        .footer {text-align: center; font-size: 14px; color: grey;}
    </style>
    <p class="footer">Desarrollado por [Data Analyst, Haidel Valera] | © 2024</p>
    """,
    unsafe_allow_html=True
)
