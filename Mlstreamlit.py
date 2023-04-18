import streamlit as st
from PIL import Image
import pandas as pd
import typing
from main import *

st.set_page_config(
    page_title="Les represento mi App!",
    page_icon="😎",
    layout="wide"
)


# Crear un título para la aplicación
st.title('Streaming Services')

# Cargar los datos en la app
consul=pd.read_csv("DataPlataformas.csv",sep=";")

#cargo los datos del modelo de recomendacion
recomendacion=pd.read_csv("Recomendacion.csv",sep=",",index_col=0)
similarityMachinePeli = pd.read_csv('similarityMachinePeli.csv') 
MachinePeli = pd.read_csv('MachinePeli.csv')

# Definir las funciones para las consultas
# Query 1: Duracion maxima
#-------------------------------------------------------------------------------
#1) Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.
#-------------------------------------------------------------------------------
def get_max_duration(year:int, plataforma:str, duration_type:str):
    #Lectura de la base de datos:
   
    # Verificar que la plataforma sea una de las opciones válidas
    consul1=consul[(consul['release_year']==year) &
       (consul["plataforma"]==plataforma) &
       (consul["duration_type"]==duration_type)].sort_values(by='duration_int', ascending=False).head(1)

    return consul1["title"]


#-------------------------------------------------------------------------------
# Query 2:
#2) Cantidad de películas por plataforma con un puntaje mayor a XX en
#  determinado año (la función debe llamarse get_score_count(platform, scored, year))
#-------------------------------------------------------------------------------
def get_score_count(plataforma : str, scored : float, release_year: int):

    # plataformas validas que se pueden elegir 
    if plataforma is not None and plataforma.lower() not in ['disney', 'amazon', 'hulu', 'netflix']:
        raise ValueError("opciones válidas: disney, amazon, hulu o netflix.")
    # seleccionamos las peliculas por año y puntaje especifico
    a=consul["title"][(consul["type"]=='movie') &
                (consul["plataforma"]==plataforma) & 
                (consul["scored"]>scored) & #----De 3.72 a 3.34
                (consul['release_year']==release_year)].count()
    a=float(a)#--> el valor arrojado en entero 
    return a

#-------------------------------------------------------------------------------
# Query 3:
#3) Cantidad de películas por plataforma con filtro de PLATAFORMA. 
# (La función debe llamarse get_count_platform(platform))
#-------------------------------------------------------------------------------
def get_count_platform(plataforma: str):
   
    # plataformas validas que se pueden elegir  
    a=consul["title"][(consul["type"]=='movie') &
                (consul["plataforma"]==plataforma)].count()

    #a=float(a)#--> el valor arrojado en entero 
    return a

#-------------------------------------------------------------------------------   
#4) Actor que más se repite según plataforma y año. 
# (La función debe llamarse get_actor(platform, year))
#-------------------------------------------------------------------------------
def get_actor(platform:str,year:int):
      
        lista=[]
        cc=pd.DataFrame()

        a=pd.DataFrame(consul["cast"][(consul["plataforma"]==platform) & 
                    (consul["release_year"]==year)])
        a_=a["cast"].str.split(",",expand=True)

        
        for ind, col in enumerate(a_.columns):
           lista.extend(a_[col].tolist())

        cc["actores"]=pd.DataFrame(lista)
        a=cc.groupby(["actores"]).size().reset_index(name="cant").sort_values(by="cant",ascending=False)
        
        try:
           z=a[a["cant"]==cc["actores"].value_counts(ascending=False).max()]
        except:
            z=(f"Las opciones {platform} y {year} no registran actores")
        return z

#------------------------------------------------------------------------------- 
#5) La cantidad de contenidos/productos según tipo,pais y año. 
#La función debe llamarse prod_per_county(tipo,pais,anio) 
#------------------------------------------------------------------------------- 
def prod_per_county(tipo:str,pais:str,anio:int):
   a=consul["id"][(consul["country"]==pais ) &
         (consul["release_year"]==anio) &
         (consul["type"]==tipo)].count()

   return {"tipo":tipo,"pais":pais,"año":anio,"peliculas":a}


#------------------------------------------------------------------------------- 
#6) La cantidad total de contenidos/productos según rating y devolver entero. 
#La función debe llamarse lamarse get_contents(rating) 
#------------------------------------------------------------------------------- 

def get_contents(rating):
   return  consul['id'][consul['rating']==rating].count()

# a=consul["id"][consul["rating"]==rating].count()
# f"El  rating  {rating} , tiene una cantidad de  {a} peliculas"

#-----------------------------------------------------------------------------
# Crear un título para la aplicación
#------------------------------------------------------------------------------
st.title('Consultas de películas y series')

image = Image.open("crs/Presentación1.png")

st.image(image, caption='PLataforma streaming')

# Opciones de consulta
options = ['Inicio','Duración máxima', 'Títulos por puntuación', 'Títulos por plataforma', 'Actor con más apariciones',"La cantidad de contenidos/productos","cantidad de contenido por rating","Modelo de recomendacion"]
query = st.sidebar.selectbox('Seleccione una consulta', options)

import streamlit as st

if query == 'Inicio':
         st.write('Bienvenido a la aplicación de consultas en el catálogo de servicios de streaming')
         st.subheader("Top 10 de las mejores peliculas calificadas")
         st.write(recomendacion[recomendacion["ratings"]>240].sort_values(by="Prome_Raitings",ascending=False).head(10))

# Consulta 1: Duración máxima
if query == 'Duración máxima':
    st.subheader('Película con mayor duración por año, plataforma y tipo de duracion.')
    year = st.number_input('Año', min_value=2000, max_value=2023, value=2020, step=1)
    platform = st.selectbox('Seleccione una plataforma', ['disney','hulu','netflix',"amazon"])
    duration_type = st.selectbox('Tipo de duración', ['min', 'season'])
    if st.button('Consultar'):
        result = get_max_duration(year, platform, duration_type)
        if isinstance(result, str):
            st.write(f'La duración máxima en {duration_type.lower()}s en {year} en {platform} es: {result}.')
        else:
            st.write(result)


# Consulta 2: Títulos por puntuación
if query == 'Títulos por puntuación':
    st.subheader('Títulos con una puntuación dada en una plataforma y año determinados')
    plataforma = st.selectbox('Seleccione una plataforma', ['amazon','disney','hulu','netflix'])
    scored = st.selectbox('Puntuación mínima',[3.34, 3.35, 3.37, 3.38, 3.39, 3.4 , 3.41, 3.42, 3.43, 3.44, 3.45,
                                                3.46, 3.47, 3.48, 3.49, 3.5 , 3.51, 3.52, 3.53, 3.54, 3.55, 3.56,
                                                3.57, 3.58, 3.59, 3.6 , 3.61, 3.62, 3.63, 3.64, 3.65, 3.66, 3.67,
                                                3.68, 3.69, 3.7 , 3.71])

    release_year = st.number_input('Año', min_value=2000, max_value=2023, value=2020, step=1)
    if st.button('Consultar'):
        result = get_score_count(plataforma, scored, release_year)
        st.write(f"Hay {result}  títulos en   {plataforma}  con una puntuación de mayor a  {scored}   o más en  {release_year}")


# Consulta 3: Títulos por plataforma
if query == 'Títulos por plataforma':
    st.subheader('Número de títulos en una plataforma dada')
    plataforma = st.selectbox('Seleccione una plataforma', ['amazon','disney','hulu','netflix'])
    if st.button('Consultar'):
        result = get_count_platform(plataforma)
        st.write(f"Hay {result} títulos en {plataforma}.")

# Consulta 4: Actor con más apariciones
if query == 'Actor con más apariciones':
    st.subheader('Actor con más apariciones en una plataforma y año determinados')
    platform = st.selectbox('Seleccione una plataforma', ['amazon','disney','hulu','netflix'])
    year = st.number_input('Año', min_value=2000, max_value=2022, value=2020, step=1)
    if st.button('Consultar'):
        result = get_actor(platform, year)
        if isinstance(result, str):
            st.write(result)
        else:
            if len(result)==0:
               st.write(f"Las opciones {platform} y {year}, no registran actores; por favor cambiar de año o plataforma")
            if len(result)!=0:
               st.write(f"El actor con más apariciones en {platform} en el año {year} son:")
               st.write(result)

# Consulta 5: La cantidad de contenidos
if query == "La cantidad de contenidos/productos":
    listaa=list(consul["country"].unique())
    st.subheader('Títulos con una puntuación dada en una plataforma y año determinados')
    tipo = st.selectbox('Seleccione una plataforma',['movie', 'tv show'])
    pais = st.selectbox('Puntuación mínima',['canada', 'india', 'united states', 'united kingdom', 'france',
                                                        'spain', 'italy', 'france','germany', 'japan',
                                                        'china','denmark', 'czech republic', 'netherlands',
                                                        'ireland','thailand', 'brazil','switzerland,'
                                                        'germany', 'australia', 'belgium',
                                                        'chile', 'argentina','mexico',
                                                        'sweden','new zealand',
                                                        'portugal','egypt', 'austria','russia','spain',
                                                        'croatia', 'slovenia','serbia','montenegro', 'south korea', 'indonesia',
                                                        'arab emirates', 'jordan'])
    anio = st.number_input('Año', min_value=2000, max_value=2023, value=2020, step=1)
    if st.button('Consultar'):
        result = prod_per_county(tipo,pais,anio)
        st.write(f"En el pais {pais}, año {anio} y con el tipo {tipo} tenemos la siguiente:")
        st.write(result)
   
if query =="cantidad de contenido por rating":
    st.subheader('Cantidad de contenido por rating')
    rating = st.selectbox('Seleccione el tipode Ratings', ['G', '13+', 'all', '18+', 'r', 'tv-y', 'tv-y7', 'nr', '16+',
                                                            'tv-pg', '7+', 'tv-14', 'tv-nr', 'tv-g', 'pg-13', 'tv-ma', 'g',
                                                            'pg', 'nc-17', 'unrated', '16', 'ages_16_', 'ages_18_', 'all_ages',
                                                            'not_rate', 'tv-y7-fv', 'not rated', '2 seasons', '93 min',
                                                            '4 seasons', '136 min', '91 min', '85 min', '98 min', '89 min',
                                                            '94 min', '86 min', '3 seasons', '121 min', '88 min', '101 min',
                                                            '1 season', '83 min', '100 min', '95 min', '92 min', '96 min',
                                                            '109 min', '99 min', '75 min', '87 min', '67 min', '104 min',
                                                            '107 min', '84 min', '103 min', '105 min', '119 min', '114 min',
                                                            '82 min', '90 min', '130 min', '110 min', '80 min', '6 seasons',
                                                            '97 min', '111 min', '81 min', '49 min', '45 min', '41 min',
                                                            '73 min', '40 min', '36 min', '39 min', '34 min', '47 min',
                                                            '65 min', '37 min', '78 min', '102 min', '129 min', '115 min',
                                                            '112 min', '61 min', '106 min', '76 min', '77 min', '79 min',
                                                            '157 min', '28 min', '64 min', '7 min', '5 min', '6 min',
                                                            '127 min', '142 min', '108 min', '57 min', '118 min', '116 min',
                                                            '12 seasons', '71 min', '74 min', '66 min', 'ur'])
    if st.button('Consultar'):
        result = get_contents(rating)
        st.write(f"El  rating  {rating} , tiene una cantidad de {result} peliculas")

#----------------------------------------------------------------------------------------
#Modelo de Recomendacion
#----------------------------------------------------------------------------------------
def modelo_RecomendacionID(titul:str):
    reco=recomendacion.copy()
    tituloUno=[titul]
    tituloDos=""
    grupo=""

    if len(tituloUno)!=0:
        titUno='|'.join(tituloUno)
        return reco[reco["title"].str.contains(titUno, case=False, na=True, regex=True)]

def modelo_RecomendacionTitulo(movid:str):
        reco=recomendacion.copy()
        tituloDos=movid
        categoria=list(reco["listed_in"][reco["title"]==tituloDos])
        cat='|'.join(categoria)
        a=reco[["movieId","title","listed_in","Prome_Raitings"]][(reco["listed_in"].str.contains(cat, case=False, na=True, regex=True)) &
                                                    (reco["ratings"]>200) &
                                                    (reco["Prome_Raitings"]>4)]
        return a[a["movieId"]!=tituloDos].head(7)
#---------------------------------------------------------------------------------------------------------
# Consulta modelo de recomendacion
def get_recommendation(title: str):
    
    arr = similarityMachinePeli.to_numpy()
    try:
        #Ubicamos el indice del titulo pasado como parametro en la columna 'title' del dts user_item
        indice = np.where(MachinePeli['title'] == title)[0][0]
        #Encontramos los indices de las puntuaciones y caracteristicas similares del titulo 
        puntuaciones_similitud = arr[indice,:]
        #Ordenamos los indices de menor a mayor
        puntuacion_ordenada = np.argsort(puntuaciones_similitud)[::-1]
        #seleccionamos solo 5 
        top_indices = puntuacion_ordenada[:5]
        #retornamos los 5 items con sus titulos como una lista
        a=MachinePeli.loc[top_indices, 'title'].reset_index(drop=True)
        return a
        #Si el titulo dado no se encuentra damos un aviso
    except IndexError:
        print(f"El título '{title}' no se encuentra en la base de datos. Intente con otro título.")
 
           
def modelo_RecomendacionTitulo(movid:str):
        reco=recomendacion.copy()
        tituloDos=movid
        categoria=list(reco["listed_in"][reco["title"]==tituloDos])
        cat='|'.join(categoria)
        a=reco[["movieId","title","listed_in","Prome_Raitings"]][(reco["listed_in"].str.contains(cat, case=False, na=True, regex=True)) &
                                                    (reco["ratings"]>200) &
                                                    (reco["Prome_Raitings"]>4)]
        return a[a["movieId"]!=tituloDos].reset_index(drop=True).head(5)
#---------------------------------------------------------------------------------------------------------
# Consulta modelo de recomendacion con ML y sin ML
#---------------------------------------------------------------------------------------------------------

if query == 'Modelo de recomendacion':
    st.subheader('Peliculas y series recomendadas')
    title = st.selectbox("Escoja la pelicula por su nombre",options=recomendacion.apply(lambda  i: i["title"],axis=1))
    #title = st.selectbox("Escoja la pelicula por su nombre",options=recomendacion.apply(lambda  i: i["title"],axis=1))
    #movid = st.selectbox("Escoja la pelicula su identificador",options=recomendacion.apply(lambda  i: i["movieId"],axis=1))
    
    if st.button('Consultar'):
           
           result = get_recommendation(title)
           st.subheader("A otros usuarios tambien les gustaron estas peliculas con ML.")
           st.write(result)
           
           result = modelo_RecomendacionTitulo(title)
           st.subheader("A otros usuarios tambien les gustaron estas peliculas sin ML.")
           st.write(result) 
           st.write("")
           st.write("Para cambiar de Streamlit a FastApi usa el siguiente enlace:")
           st.write("https://fastapi-platafomas-streaming-009.onrender.com/docs")
           st.write("BY Cristian Andres Contreras")  

#para arrankar streamlit
#streamlit run Mlstreamlit.py
