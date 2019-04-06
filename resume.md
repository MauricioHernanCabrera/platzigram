
<!-- Abrir debbuger -->
import pdb
pdb.set_trace()

tocando c se cierra el debugger
<!--  -->



## Comandos de django
python manage.py runserver -> levantar servidor

python manage.py startapp posts -> 

python manage.py migrate -> correr migraciones
python manage.py makemigrations -> levantar ultima migracion

python manage.py shell -> shell de python con todas las cosas de django disponibles
python manage.py createsuperuser -> crear super usuario




## Glosario
**ORM:** Object-relational mapping. Es el encargado de permitir el acceso y control de una base de datos relacional a través de una abstracción a clases y objetos.

**Templates:** Archivos HTML que permiten la inclusión y ejecución de lógica especial para la presentación de datos.

**Modelo:** Parte de un proyecto de Django que se encarga de estructurar las tablas y propiedades de la base de datos a través de clases de Python.

**Vista:** Parte de un proyecto de Django que se encarga de la lógica de negocio y es la conexión entre el template y el modelo.

**App:** Conjunto de código que se encarga de resolver una parte muy específica del proyecto, contiene sus modelos, vistas, urls, etc.

**Patrón de diseño:** Solución común a un problema particular.
