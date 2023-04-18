<p align=center><img src=https://assets.soyhenry.com/logos/LOGO-HENRY-04.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>
*Cristian Andres Contreras*  
*Negociante internacional*  
*Data Sciencie(In progress)*

<p align="center">
<img src="https://cosasdedevs.com/media/sections/images/fastapi.png"height=180>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1k9eb0ZrfvW_VQoiim4y4NBPnvQXmCGQbMw&usqp=CAU"  height=100>
</p>
<p align="right">
<img src="https://seeklogo.com/images/S/streamlit-logo-B405F7E2FC-seeklogo.com.png"height=200>
</p>

<hr>  


# <h2 align=center>**`Extración, transformación y Carga (ETL)`**</h2>



<p align="center">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXVWET0vYFMDJn92VOuXpkONKjS4F-KamSBQ&usqp=CAU"height=120>
<img src=""  height=180>
</p>


<hr>

Este trabajo está basado en realizar un proceso de extracción, transformación y carga (ETL) con diversos dataset, con la fin de entregar datos estandarizados y de buena calidad (limpios), también se realizó un proceso de Machine Learnig, con el fin pueda generar recomendaciones a los usuarios, estudiaron los datos para que así se puedan procesar a través de nuestra Application Programming Interface (API), la cual va estar trabajando desde un modo de producción desde un servidor llamado Render.

Una API o interfaz de programación de aplicaciones, con un protocolo que se usa para diseñar e integrar el software de las aplicaciones.
Es una herramienta muy versátil y fundamental para la creación de App web, sitios estáticos entre otras formas de uso, esta permite realizar una sinnúmero de operaciones para vincular con una plataforma Web.

Hoy en día contamos con **FastAPI** y **Flask** entre muchas otras, son framework modernos y de alto rendimiento para construir APIs con Python.
<p align=center>
<img src = "https://tekla.io/wp-content/uploads/2022/06/QueEsAPIRest-Recurso-01.jpg" height=250><p>

<hr>

## **Tecnologías**

Para la elaboración de este proyecto se utilizaron las siguiente tecnologías:

* Fastapi
* Visual studio code
* Jupyter
* Python
* Pandas
* Uvicorn
* Render
* Streamlit
* scikit-learn
* Github
<hr>

## **Pasos para la elaboración del proyecto**


<p align=center>
<img src = 'https://images.jifo.co/53775302_1581003928973.jpg' height=250><p>

**1.** **EDA** 

Se realiza un análisis exploratorio con el objetivo de verificar el estado los datos de entrada, para lograr detallar que están cargados correctamente, lo cual permite poder tomar decisiones en la limpieza de estos; los archivos orginales fueron suministrados en formato *csv*, estos se cargaron de la siguiente manera:

* Para visualizar la limpieza completa se pueden remitir a [Limpieza y extacion](https://github.com/cristos34/PI-01-DT09---DATA-ENGINEER/blob/4debca816103fd2a251a3f1ed7badedf590356f6/Proyecto_PI_ETL_Uno.ipynb).

* Para visualizar el modelo de recomendación se pueden remitir a [Modelo de recomendacion](https://github.com/cristos34/PI-01-DT09---DATA-ENGINEER/blob/ec2b5ef3dda8eddc97f378c6c6c7d83852ea036d/MLrecomeinda.ipynb).


## **2.** **Creación de la API**

Para crear la API se utilizó el framework [FastApi](https://fastapi.tiangolo.com/), que está catalogado en el momento como el framework de más alto procesamiento y de mayor facilidad de uso.
            
La API llamanda **platafomas-streaming** permite conocer diferentes datos de las platafromas Amazon, Hulu, Disney, Netflix, esta se trabajó en un archivo llamado **main.py** y se inició de la siguiente manera:

Para ver el código completo donde están todas las funciones que de la API se pueden remitir a [main.py](https://github.com/cristos34/PI-01-DT09---DATA-ENGINEER/blob/main/main.py).
            
También se realizó una API con el framework [Flask](https://flask.palletsprojects.com/en/2.2.x/), que está catalogado también como un framework con mucha facilidad para trabajar Pandas y muchas otras bases de datos. Además, que presta muchos de los servicios que brinda FastApi.
            
La API, llamada  **mainFlask** permite conocer diferentes datos de las plataformas  Amazon, Hulu, Disney, Netflix, esta se trabajó en un archivo llamado **mainFlask.py**, pero no se le pudo hacer el deploying, debido a que no se encontró información que sirviera de guía y que funcionaran su procedimiento.

Para ver el código completo donde están todas las funciones de esta API, se pueden remitir a [mainFlask.py](https://github.com/cristos34/PI-Flask-app-Plataforrmas/blob/01070124cf76e0849ccfaffbafd719161ddadd27/mainFlask.py).

Asimismo, se realizó la misma API, pero con el framework [Streamlit](https://streamlit.io/) mucho más amigable; en cuanto a la documentación y el uso, la interfacez es muy fácil de armar y el deploy no tiene comparación, esta API permite conocer diferentes datos de las plataformas  Amazon, Hulu, Disney, Netflix; además, realiza sugerencias a los usuarios y presenta el top 10 de las películas mejor calificadas, esta se trabajó en un archivo llamado **Mlstreamlit.py**

Para ver el código completo donde están todas las funciones de esta APP, se pueden remitir a [Mlstreamlit.py](https://github.com/cristos34/PI-01-DT09---DATA-ENGINEER/blob/main/Mlstreamlit.py).


* Datos para requiremensts.txt :
```Python
     * pip
     * colorama
     * decorator
     * fastapi
     * gitdb
     * GitPython
     * ipykernel
     * ipython
     * matplotlib
     * matplotlib-inline
     * metrics
     * numpy
     * packaging
     * pandas
     * prompt-toolkit
     * requests
     * scikit-learn
     * scipy
     * seaborn
     * sklearn
     * streamlit
     * typing
     * uvicorn
```
## **2.1** **Pasos para crear el ambiente virtual**

* Crear el ambiente virtual desde la terminal con la siguiente línea de código nombre de la carpeta venvv, pero antes deben ubicarse en la carpeta raíz.
            
            **python -m venv venvv** 
           
* Crear un archivo principal, normalmente llamado Main.py o App.py
           
             ** main.py** 
            
* Se dirijen a la carpeta \venvv\ con el comando cd y tab
            
            **cd + tab**
            **.\venvv\**
            
* Copiar la siguiente línea de código y se pega en la ruta de \ven
            
            **Set-ExecutionPolicy -ExecutionPolicy Remotesigned -Scope process**
            
* Se dirijen a la carpeta \Scripts\ con el comando cd y tab
            
            **cd + tab**
                        
* Copiar la siguiente línea de código y se pega en la ruta de \Scrip
            
            **\activate**
            
* Se dirijen a la carpeta raíz, o sea que salen del \venvv\ y \Scripts\  con el comando cd espacio 2 puntos cd ..
            
            **cd ..**
            **cd ..**
            
* Crear un archivo llamado .gitignore, con el fin que ignorar el ambiente virtual cuando se suba al GitHub, este debe tener el nombre del ambiente virtual más el **/**            
           ``` Venvv/```
            
* Crear un archivo llamado requirements.txt, para especificar las librerías que se están usando con su versión actual, ingresando el siguiente comando y se puede actualizar que el mismo comando
            
           **pip frezze>requirements.txt**
## <h2>**`Instalado nuestro entorno virtual podemos continuar con nuestra API`**</h2>         
            
## **2.2** **Ejecutar la API creada en FastApi localmente**
* El siguiente comando es para correr nuestra API
              **uvicorn main:app**
* El siguiente comando es para mantener corriendo nuestra API, mientras está en desarrollo
              **uvicorn main:app --reload**
* Rutas para colocar en el navegador después de ejecutar nuestra API de FastApi y poder observar el funcionamiento de la misma.
             #http://localhost:8000 
             #http://localhost:8000/docs
             #127.0.0.1:8000/docs
             #0.0.0.0:8000/docs
             
## **2.3** **Pasos crear un repositorio en GitHub**     
* Deben estar **Registrado en GitHub**
* Entrar a su **Cuenta de GitHub**
* Dar clic en **Repositories**
* Dar clic en **NEW**
* Colocar el **nombre al Repositorio** 
* Dar una **breve Descripcion** del repo
* Dar clic en **Create Repository**
* Seguir los pasos del punto **2.4** del presente **README.md**
    
## **2.4** **Pasos para cargar el archivo a gitHub**     
* Ir a la carpeta donde se encuentra el archivo 
* Dar clic derecho 
* Escoger Git Bash Here - 
**Aparece una consola donde deben ingresar los siguientes comandos:**
* git init
* git status
* git add . ``` todos los archivos ```
* git add README.md  ```opcional```
* git add nombre del archivo ```opcional```
* git commit -m ``` "nombre de la carga del repositorio" ejemplo  “first commit”```
* git branch -M main
* git remote add origin ```https://ruta del repositorio donde se alojara el proyecto ```
* git push -u origin main

## **2.5** **Pasos realizar el deploying a la API con FastAPI**
*  Ingresar a Render.com
*  Dar clic en **GET STARTED FOR FREE**
*  Se registran en Render 
*  Muestra la opcción para ingresar. Ejemplo: por medio de **Github**
*  Dar clic en **NEW+**
*  Dar Clic en **Web service**
*  Dar clic en **Connect**
       -Colocar el nombre que deseemos
*  Ir a **Stard Command**
       colocar esta sentencia verificar el host y el port
       **-uvicorn main:app --host 0.0.0.0 --port 10000**
*  Dar clic en **Create Web Service**  --> **Environment Variables** --> **Add Environment Variables**  
    ```
       * Key: PIP_VERSION 
       * Value:22.3.1 -->Esta es la version del pip se debe consultar puede ser con **pip list** 
    ```
*  Dar clic en Save changes
*  Ir **Logs**
*  Dar clic en **Manual Deploy**  
      - Dar clic en **Deploy Latest Commit**
*  Esperar un rato a que cargue (el proceso demora un poco)
*  Copiar la dirección **URL** y se le agrega **/docs**
*  **Ejemplo https://fastapi-platafomas-streaming-009.onrender.com/docs**
 
## **2.6** **Paso a paso para ejecutar la API de forma remota con el deploy en Render**

Paso a paso para ejecutar la API, se tiene que ingresar al siguiente link que se conecta con el servidor **[FastApi_Recomienda](https://fastapi-platafomas-streaming-009.onrender.com/docs)**

```
Una vez encendido ingresados al link ya podemos utilizar nuestras consultas en la API, como son:

* Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))

* Se realiza la verificación los valores mínimos y máximos del dataframe

* Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))

* Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))

* La cantidad de contenidos/productos según tipo,pais y año. (La función debe llamarse prod_per_county(tipo,pais,anio))

* La cantidad total de contenidos/productos según rating y devolver entero. (La función debe llamarse lamarse get_contents(rating)) 

* Modelo de recomandación. (La función debe llamarse lamarse get_recommendation(titulo))

```
## **2.7** **Ejecutar la App creada en Streamlit localmente**
* El siguiente comando es para correr nuestra App, 
              **streamlit run Mlstreamlit.py**

* El comando genera una ruta donde sólo se debe dar clic y queda ejecutandose hasta que cierran con: **Control + c** en la terminal

## **2.8** **Pasos realizar el deploying de Streamlit (APP), en Streamlit.io**
* Ingresar a la página oficial de Streamlit **streamlit.io**
* Dar clic en **Sign up for Streamlit Community Cloud**
* Escoger la forma de ingrasar Ejemplo **Github**
* Dar clic en **Get Started**
* Dar Clic en **New app**
* Escoger el repositorio en caso de ser con Github
* Colocar el **main** en caso de el archivo a ejecutar sea el main
* Escoger el archivo principal Ejemplo **Mlstreamlit.py**
* Dar clic a **Deploy**
* esperar un rato mientras se carga completamante 
* Copiar el link y se finaliza

## **2.9** **Paso a paso para ejecutar la App de Streamlit de forma remota con el deploy en Streamlit.io**

* Paso a paso para ejecutar la APP, se tiene que ingresar al siguiente link que se conecta con el servidor:
 **[Streamlit_Recomienda](https://cristos34-pi-01-dt09---data-engineer-mlstreamlit-8gqh60.streamlit.app/)**  
* Una vez encendido ingresados al link, se pueden realizar las consultas en la APP de Streamlit, las cuales son las mismas del punto **2.6**

**Video de presentación**
 **([https://drive.google.com/file/d/1QDk4qe1-GVL1jOaTSR7OPoSB2ERB6usp/view?usp=share_link](https://drive.google.com/file/d/1vZMK-M0V41zpkx1y0-gEn2aKHFe0mqE3/view?usp=sharing))**

Fecha de inicio 10/04/2023  
Fecha de finalización 19/04/2023

###### **Gracias por su visita.**
