# Fase 3: Creando nuestro entorno para estructurar los Datos
## Link al repositorio: https://github.com/Trabajo-gruupal-empresa/Fase3.git
### Enunciado del problema:
#### El objetivo consiste en mostrar cómo una aplicación puede tener una interfaz web, una interfaz gráfica y además, compartir los datos. La aplicación que vamos a diseñar tiene como objetivo mostrar un formulario de contacto y registrar los datos en una base de datos relacional.
Esta misma aplicación se desarrollará para permitir reutilizar el modelo de datos para la creación de una interfaz gráfica. Las tres aplicaciones utilizarán la misma base de datos.

Además de la implementación de Pyramid o del FrontEnd elegido, este tiempo se dedicará para realizar:

·    el modelo de objetos: 5 objetos, es decir 5 clases,

·    un formulario,

·    la modificación del controlador del índice y de la plantilla asociada,

·    la creación de cuatro controladores,

·    la creación de dos plantillas.

 

La aplicación, en su globalidad, es un simple formulario de contacto.

https://recursospython.com/codigos-de-fuente/formulario-de-contacto-via-cgi/

La solución web que os propongo utilizar es Pyramid, un framework web que utiliza distintos módulos de Python bien contrastados y sobre los que se basa para ofrecer una solución fiable, pero flexible, pues en todo momento es posible remplazar alguno de los módulos por otro (por ejemplo, cambiar el módulo que gestiona el templating, o el que gestiona la autenticación, o incluso el que gestiona el enrutado...). El desacople de estos módulos es una de las ventajas de este framework.

https://atmantree.com/posts/introduccion-a-pyramid/

La solución para gestionar la persistencia que vamos a utilizar es PostgreSQL.

Otra opción propuesta es la utilización del framework Django. Este último es un framework full-stack, es decir, que integra en su seno todos los componentes elementales (ya no es necesario utilizar proyectos complementarios para realizar las tareas básicas y, por otro lado, el desarrollar ya no tiene restricciones). La gran ventaja de Django es que dispone de una galaxia impresionante de módulos externos, que permiten realizar tareas complejas con muy poco esfuerzo. Django es uno de los productos de referencia de la Web y contribuye en gran medida a la popularidad de Python.

https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Forms

otra buena alternativa es:

https://j2logo.com/tutorial-flask-leccion-3-formularios-wtforms/

Destacaremos que es posible utilizar el ORM SQLAlchemy con Django, ya que se ha presentado en este libro, y que también es posible utilizar otro sistema de plantillas diferente al que se provee de base.

https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/databases.html

A contrario que Django, Pyramid es un framework minimalista. Para construir una aplicación es necesario agregar varios componentes Python independientes. La ventaja es que cada uno es intercambiable. Se trata de un framework muy ligero llamado light-stack.
