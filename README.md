# Ejercicio creación de ML pipelines y puesta en producción

Este es un ejercicio academico de la Maestría en Inteligencia Artificial de la universidad Sergio Arboleda el cuál consiste en poner en marcha un modelo de ML en todo el ciclo de vida del desarrollo. 

El dataset utilizado es el siguiente: https://www.kaggle.com/datasets/jimschacko/10-years-diabetes-dataset 

Con este dataset se busca crear un modelo de ML que nos ayude a predecir si una persona puede recaer e ir de nuevo al hospital. |`Target`:`['readmitted']`| 

## Desarrollo de notebooks

Este proyecto obedece el siguiente flujo (Google collab):

1. Análisis de datos
2. Selección de características (PCA)
3. Evaluación de diferentes modelos de entrenamiento
4. Generación de Pipelines de entrenamiento
5. Exportación de trabajo .joblib y .pkl para puesta en producción

*USA EDA proyecto Electiva 2 DSI*
https://colab.research.google.com/drive/1F4cWyBLVkNhIPKMZI94irC9pSbuK0udH

*Pipeline Diabetes Dataset*
https://colab.research.google.com/drive/1296Jz5JR_IrnAE_JA_aWc4j6xv3vy2td

## Desarrollo de puesta en producción

### Conexión con servicio cloud

Una vez analizados el dataset y los pipelines se decide llevar a cabo la puesta en producción usando las siguientes tecnologías: (Google cloud platform, servicio google storage)
En este storage se implementa DVC como versionador el cuál adquiere los datos y los pipelines para el entrenamiento. 

* 1. Creación de bucket en plataforma cloud
* 2. Obtención de llaves de acceso
* 3. Instalación de librerías necesarias DVC para versionamiento
* 4. Conexión de bucket con DVC
* 4. Creación de trakers remotos


### Desempaquetado de modelos

Se procede a extraer el código de los notebooks a python con los siguientes módulos:

* - prepare.py: Lectura de bucket de datos raw y eliminación de variables previamente analizadas. Creación de csv para entrenamiento
* - train.py  : Configuración de Pipelines de entrenamiento
* - utils.py  : Exportación de trabajo formatos .jblib, .pkl

### Creación de API

Se crea una API usando la librería FastAPI el cual conecta el modelo generado con un endpoint, se desarrollan los test. Encuentre este código en el repositorio. 

