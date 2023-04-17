from fastapi import FastAPI
import pandas as pd
#from coneccion import consul
from typing import Optional
import uvicorn


app=FastAPI(title="Api de consultas en Plataformas striming",
            description="Esta Api realiza cosultas en las plataformas Amazon,Hulu, Netflix y Disney",
            version="V1.0")


consul=pd.read_csv("DataPlataformas.csv",sep=";")

# introduccion
@app.get("/docs")
def presentacion():
    return {"PI 01 - Cristian Andres Contreras"}

@app.get("/contacto")
def contacto():
    return "Email: cristos34_9@hotmail.com / Github: cristos34"

#-------------------------------------------------------------------------------
#1) Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.
#-------------------------------------------------------------------------------
@app.get("/get_max_duration/{year}/{plataforma}/{duration_type}")
def get_max_duration(year: Optional[int] = None, plataforma: Optional[str] = None, duration_type: Optional[str] = 'min'):
    #Lectura de la base de datos:
   
    # Verificar que la plataforma sea una de las opciones válidas
    if plataforma is not None and plataforma.lower() not in ['disney', 'amazon', 'hulu', 'netflix']:
        raise ValueError("opciones válidas: Disney, Amazon, Hulu o Netflix.")
    if duration_type is not None and duration_type not in ['min', 'season']:
        return('Los valores validos son: min, season')

    consul1=consul[(consul['release_year']==year) &
       (consul["plataforma"]==plataforma) &
       (consul["duration_type"]==duration_type)].sort_values(by='duration_int', ascending=False).head(1)

    return consul1["title"].to_json(orient="records")

#-------------------------------------------------------------------------------
#2) Cantidad de películas por plataforma con un puntaje mayor a XX en
#  determinado año (la función debe llamarse get_score_count(platform, scored, year))
#-------------------------------------------------------------------------------
@app.get("/Cantidad de películas por plataforma - get_score_count/{plataforma}/{scored}/{release_year}")
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
    return {a}
#-------------------------------------------------------------------------------
#3) Cantidad de películas por plataforma con filtro de PLATAFORMA. 
# (La función debe llamarse get_count_platform(platform))
#-------------------------------------------------------------------------------
@app.get("/Cantidad de películas por plataforma - get_count_platform/{plataforma}")
def get_count_platform(plataforma: str):
   

    # plataformas validas que se pueden elegir 
    if plataforma is not None and plataforma.lower() not in ['disney', 'amazon', 'hulu', 'netflix']:
        raise ValueError("Opciones válidas: disney, amazon, hulu, netflix.")
    
    a=consul["title"][(consul["type"]=='movie') &
                (consul["plataforma"]==plataforma)].count()

    a=float(a)#--> el valor arrojado en entero 
    return {a}
#-------------------------------------------------------------------------------   
#4) Actor que más se repite según plataforma y año. 
# (La función debe llamarse get_actor(platform, year))
#-------------------------------------------------------------------------------
@app.get("/actor que más se repite - get_actor(plataforma, year")
def get_actor(platform:str,year:int):
       #creo una lista y un dataframe vacio para gurdar los datos
        lista=[]
        cc=pd.DataFrame()

        #Realizo el filtro de la cosulta tal como solicitan, segun requerimiento
        #la comvierto en dataframe y  la guardo en una variable
        a=pd.DataFrame(consul["cast"][(consul["plataforma"]==platform) & 
                    (consul["release_year"]==year)])

        #Divido la columna "cast" de la cosulta en varios columnas con el fin 
        #de aplanar la columna la division la hago atravez de una split
        a_=a["cast"].str.split(",",expand=True)

        #Itero cada columna creada por la divicion de la columna "cast"
        # con el fin de extraer cada valor de todas las columnas y meterla en una sola 
        # pero ya uno por uno pero antes las envio a una lista 
        for ind, col in enumerate(a_.columns):
           lista.extend(a_[col].tolist())

        #Convierto la lista en un dataframe   
        cc["actores"]=pd.DataFrame(lista)
        #cc["actores"].value_counts(ascending=False).max()#-->Realizo el conteo de cada 
        # valor y extraigo el valor maximo

        #despues de creado el dataframe realizo una agrupacion de los datos de la columna 
        #"Actores" donde uso size para contarlos Reset_index para no crear indices y name para 
        #crear una nueva columna cor sort_values(by= "cant") organizo por cantidad de forma decendente
        a=cc.groupby(["actores"]).size().reset_index(name="cant").sort_values(by="cant",ascending=False)

        #realizo la condicion que me traiga todos los valores maximos 
        z=a[a["cant"]==int(cc["actores"].value_counts(ascending=False).max())]
        #Se crea un dicionario con los parametros ya que la sonsulta si lo solicita
       
        z=dict(z)
        di=dict([('plataforma', platform), ('año', year)])
        z.update(di)
        c=pd.DataFrame(z)
        
        return c.to_dict("records")

#------------------------------------------------------------------------------- 
#5) La cantidad de contenidos/productos según tipo,pais y año. 
#La función debe llamarse prod_per_county(tipo,pais,anio) 
#------------------------------------------------------------------------------- 
@app.get("/La cantidad de contenidos/productos - prod_per_county(tipo,pais,anio)")
def prod_per_county(tipo:str,pais:str,anio:int):
   a=consul["id"][(consul["country"]=="canada" ) &
         (consul["release_year"]==2020) &
         (consul["type"]=="movie")].count()

   #return {"tipo":"movie","pais":"canada","año":2020,"peliculas":a}
   a=float(a)#--> el valor arrojado en entero 
   return {a}
#------------------------------------------------------------------------------- 
#6) La cantidad total de contenidos/productos según rating y devolver entero. 
#La función debe llamarse lamarse get_contents(rating) 
#------------------------------------------------------------------------------- 
@app.get("/La cantidad de contenidos/productos - get_contents(rating)")
def get_contents(rating):
   return  f"El  rating  {rating} , tiene una cantidad de   {consul['id'][consul['rating']==rating].count()} peliculas"
            
if __name__ == "__main__":
   uvicorn.run("main:app", host="0.0.0.0", port=8080)

   #link
#para EJECUTAR la api
# https://fastapi-platafomas-streaming.onrender.com/docs
    
#python -m venv venv #--> crear el ambiente virtual desde la terminal
#crear el main.py #--> crear un archivo en el ambinete virtual
#cd
#.\venv\
#Set-ExecutionPolicy -ExecutionPolicy Remotesigned -Scope process
#.\Scripts\
#.\activate
#cd ..
#cd ..
#uvicorn main:app
#uvicorn main:app --reload  #---> para que quede cocorriendo mientras dse programa
#http://localhost:8000
#http://localhost:8000/docs 
#Para hacer del deploy --> renderizar 
#pip list
#uvicorn main:app --host 0.0.0.0 --port 8080  
# environment environment variables--> key:PIP_VERSION   value:22.3.1 #-->version
# pip install --upgrade scikit-learn
#pip freeze > requirements.txt