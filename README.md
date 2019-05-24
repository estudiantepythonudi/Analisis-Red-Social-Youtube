# PROPUESTA DE RECOPILACIÓN Y ANÁLISIS DE DATOS EN REDES SOCIALES - ANALÍSIS DE COMUNIDADES EN LA RED SOCIAL YOUTUBE.

Autor: Ricardo Amaya Infante

Director: Jonathan Ramos Chaux

Universidad: Universidad de Investigación y Desarrollo

Correo: ramaya1@udi.edu.co

# IMPORTANTE: 

En orden para correr el código dentro de las herramientas que se usaran para abordar el problema, es necesario tener unas librerias instaladas. En el directorio base del repositorio se encuentra un archivo de texto de nombre $requerimentos.txt$ que contiene todas estas librerias. Si se encuentra en un sistema operativo Linux es tan sencillo como descargar el archivo y correr el siguiente comando donde hayamos descargado el archivo de texto

    $ pip install -r requerimentos.txt

Si se desea evitar la instalación de librerias en alguna máquina, tendremos un link de descarga para unos Jupyter notebooks ejecutados en Colaboratory. Google Colaboratory brinda un servicio en la nube gratuito construido sobre Jupyter Notebooks que puede correr en GPUS. Colaboratory se presenta como una gran herramienta para mejorar nuestras habilidades de programación y además permite a cualquier persona tener acceso a unas buenas computadoras y ahorra tiempo en la gran mayoría de ocasiones debido a que estas computadores ya tienen algunas de las librerias más importantes instaladas.

Algunas de las especificaciones y limitaciones de las máquinas en las que podemos ejecutar nuestros algoritmos son:

<img src="https://cdn-images-1.medium.com/max/1000/0*6ElaVC0Cf4OndZKi.png">

- n1-highmem-2 instance
- 2vCPU @ 2.2GHz
- 13GB RAM
- 33GB Espacio para almacenamiento
- 90 minutos como máximo sin hacer nada
- Maximo de 12 horas en ejecución
- GPU Mejorada hasta 350 GB

## Utilizar los notebooks en Google Colaboratory:

En el directorio base del repositorio encontrar un zip con nombre Networks.zip. Este contiene los notebooks preparados para correr en Google Colaboratory. Para correr estos notebooks en Colaboratory es necesario ingresar a una cuenta de Google Drive y en el Directorio Root (el principal, donde se guarda todo) crear una carpeta de nombre Networks y subir el contenido del Networks.zip desempaquetado. Una vez subidos los notebooks, podrás abrir cada uno dando click derecho y seleccionando abrir con -> Colaboratory.

# Entendiendo el problema

El crecimiento poblacional exponencial que se vive actualmente y la gran acogida de las herramientas tecnológicas y dispositivos que se encuentran conectados a diferentes tipos de redes y principalmente la internet, ha despertado el interés y la necesidad de estar cada vez más interconectados entre si y conocer en tiempo real todo lo que ocurre en el mundo.

Los datos de cada una de las personas que usan de forma directa o indirecta los dispositivos tecnológicos para acceder a plataformas virtuales, páginas web o en general todo lo que concierne a algún tipo de interacción o interconexión mediante una red social, son propios y el acceso a ellos es limitado acorde a las regulaciones de ley impuestas por la soberanía de cada nación.

La meta es identificar los circulos sociales de una persona. Cada circulo es un subconjunto de sus amigos. Esto significa que podemos formular el problema de detección de circulos como un problema de agrupamiento de su ego-network. En la siguiente figura se muestra un único usuario u* y formamos una red con sus amigos *vi. Nos referiremos al usuario u* como *ego y a sus nodos vi como alters. La tarea es identificar los circulos a que cada vi pertenece.

<img src="https://i.imgur.com/Ist45yG.png">

# Abordando el problema

El “Análisis de Redes Sociales” es una técnica que permite estudiar y representar gráficamente las relaciones establecidas entre determinados participantes (nodos) junto con la estructura que estas determinan, ésta técnica puede ser utilizada bajo dos tipos de enfoque: exploratorio y confirmatorio. El primero abarca la visualización y manipulación de la información, mientras que el segundo consiste en pruebas de hipótesis y distribuciones de probabilidad.

Escogimos tres algoritmos, cada uno de estos puede ser ejecutado en un Jupyter notebook o en Python scripts:

1. Un algoritmo de agrupación guiado por centralidad, utilizando Centralidad por intermediación.
2. Un algoritmo basado en agrupación: KMeans.
3. Un algoritmo basado en densidad: DBSCAN.

Los notebooks los usaremos como una herramienta interactiva para la visualización los datos, el analísis de estos y para mostrar conclusiones. Por otro lado, los Python scripts seran usados para interactuar con los algoritmos, esto con el fin de entender como es que estos funcionan y las variaciones frente a sus respectivos hiperparametros y cantidad de datos con el que estos se entrenan.

Los Jupyter notebooks se encuentran en el directorio base de este repositorio, mientras que los Python scripts se encuentran en el directorio scripts y pueden ser ejecutados en una terminal. Si se desea, se pueden hacer uso de algunas banderas para no tener que editar estos scripts. Los python scripts se corren de la siguiente manera:

Abrimos un terminal y navegamos hasta la carpeta scripts. Una vez allá escribimos lo siguiente:

### Algoritmo de agrupación guiado por centralidad, betweenness centrality.

Su único parametro es la cantidad de nodos que le ingresamos

    $ python CGC.py --nodes=1000

### Algoritmo KMeans.

Tiene un parametro que es la cantidad de nodos que le ingresamos y un hiperparametro que es la cantidad de clusters

    $ python Kmeans.py --nodes=1000 --n_clusters=10

### Algoritmo DBSCAN.

Tiene un parametro que es la cantidad de nodos que le ingresamos y un hiperparametro que es la tolerancia (epsilon)

    $ python DBSCAN.py --nodes=1000 --epsilon=0.001

### Una vez ejecutemos los python scripts. Estos guardaran el grafo en la carpeta graphs con el siguiente formato para el nombre: ALGORITMO_NODOS_HIPERPARAMETRO.png. Si no se coloca ninguna bandera, la ejecución se llevará acabo con los valores por defecto de cada parametro e hiperparametro.

# Observaciones

- El algoritmo de centralidad por intermediación calcula el camino más corto entre cada par de nodos en un grafo conectado. Cada nodo recibe una calificación basado en la cantidad de caminos cortos que pasan a través de este. Los nodos que frecuentemente estan en caminos cortos tienen una calificación más alta.

- El algoritmo KMeans agrupa los nodos al intentar separarlos en n grupos de igual varianza, minimizando un criterio conocido como la inercia o la suma de cuadrados dentro de un cluster.

- La inercia en el KMeans hace la suposición de que los grupos son convexos e isotropicos, lo cual no siempre es el caso. Esto responde de mala manera a clusters alargados o datos de forma irregular.

- Dandole el tiempo necesario, el algoritmo KMeans siempre converge, aunque a veces puede converger a un mínimo local.

- El algoritmo DBSCAN ve los clusters como areas de alta densidad, separadas por areas de baja densidad. Debido a esta visión generica, los clusters encontrados por el DBSCAN pueden ser de cualquier forma, contrario al k-means que asume que los clusters tienen una forma convexa.

- La mínima cantidad de nodos y epsilon en el DBSCAN, definen formalmente la densidad. A mayor mínima cantidad de nodos para agrupar y menor epsilon, más densidad es necesaria para formar un cluster

- Cuando escogemos un valor bajo para epsilon en el DBSCAN, la gran mayoría de datos no estarán agrupados y serán clasificados como ruido. Por el contrario, cuando utilizamos un valor alto para epsilon ocasionara que todos los nodos esten agrupados.

# Conclusiones

- Después de correr nuestros datos en la misma muestra de datos nos damos cuenta que esta investigación esta límitada por el hardware en que se corran los experimentos. Se necesita de bastante memoria y buen procesador para visualizar y entrenar datasets grandes.

- Para grafos largos, el algoritmo de centralidad por intermediación no es practico y no nos dice mucho del problema que estamos tratando.

- El algoritmo KMeans mantiene un buen tiempo de ejecución a medida que se entrena con una mayor cantidad de datos.

- El algoritmo KMeans es mucho más rápido que el DBSCAN.

- El algoritmo DBSCAN es deterministico, siempre genera los mismos clusters cuando se le dan los datos en el mismo orden.

- DBScan es mas amigable porque no necesita el numero de clusters como parametro, mientras el KMeans si lo necesita.

- Cuando no se conoce la cantidad de clusters escondidos en un dataset y no hay manera de visualizarlo, es una buena decisión utilizar el DBSCAN.

- DBSCAN no trabaja muy bien en clusters con diferentes densidades y necesita una selección cuidadosa de sus parametros.

- El algoritmo de centralidad por intermediación hace la suposición de que todas las comunicaciones entre nodos pasan por un camino más corto y con la misma frecuencia, esto no es un caso de la vida real, lo que nos lleva a pensar que no nos da una buena vista de los nodos más influyentes en un grafo, si no una buena representación.

- A pesar de tener un tiempo mayor de ejecución que el algoritmo de centralidad por intermediación y el KMeans, escogemos el DBSCAN como el algoritmo ideal para un analisis de las redes sociales. La razón principal es porque estamos tratando con grandes cantidades de datos, díficiles de visualizar y por lo tanto, de manera intuitiva, no podemos hacer una selección cuidadosa de un parametro como el número de clusters en el KMeans.