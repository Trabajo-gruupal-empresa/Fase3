# Importar los módulos necesarios de Pyramid
from pyramid.config import Configurator
from pyramid.view import view_config
from pyramid.response import Response

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Contacto(Base):
    __tablename__ = 'contactos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    email = Column(String)
    telefono = Column(String)
    mensaje = Column(String)

engine = create_engine('postgresql://usuario:contraseña@localhost:5432/nombre_basedatos')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)

@view_config(route_name='home', renderer='formulario.pt')
def home(request):
    return {}

@view_config(route_name='guardar_contacto', request_method='POST')
def guardar_contacto(request):
    nombre = request.params.get('nombre')
    email = request.params.get('email')
    telefono = request.params.get('telefono')
    mensaje = request.params.get('mensaje')

    contacto = Contacto(nombre=nombre, email=email, telefono=telefono, mensaje=mensaje)

    db_session = DBSession()
    db_session.add(contacto)
    db_session.commit()

    return Response('Contacto registrado correctamente')

# Configurar las rutas de la aplicación
config = Configurator()
config.add_route('home', '/')
config.add_route('guardar_contacto', '/guardar_contacto')
config.scan()

# Iniciar la aplicación Pyramid
app = config.make_wsgi_app()
