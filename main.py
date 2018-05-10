
from bottle import request, route, run, template

##L

##localhost:8000/
@route('/')
def index():
    return template('index')  #muestra la vista index en views/index.tpl <- aqui va html


##localhost:8000/hola/*cualquier cosa*
@route('/hola/<nombre>')
def hola(nombre):  #El parametro es el que se pasa por la ruta. Ej: Para la ruta "/hola/juan" nombre valdra 'juan'
    return template('hola',nombre1=nombre)  #le pasa la variable nombre al archivo views/hola, en ese archivo se muestra el valor de la variable

##localhost::8000/post
@route('/post')
def postView():
    return template('post') #Para mostrar la vista post.tpl, este envia un form por post a la ruta /post (la de abajo)



@route('/post', method="POST")  #
def post():
    nombre=request.forms.get('nombre')  ##Obtiene el valor 'nombre' del form
    return template('hola',nombre1=nombre)  #Lo muestra en la vista hola

@route('/mostrar')
def mostrar():
    datos={
        'nombre': 'Alexander',
        'apellidos': 'Apaza Torres',
        'edad':20,
        'universidad':'UNSA'
    }
    return template('mostrar',datos=datos)   ##Pasar varios datos en un diccionario para mostrar en vista


##Como es un ejemplo supongamos que tenemos una base de datos asi
datos=[
        {
            'nombre': 'Alexander',
            'apellidos': 'Apaza Torres',
            'edad':20,
            'universidad':'UNSA'
        },
        {
            'nombre': 'Juan',
            'apellidos': 'Perez Cornejo',
            'edad':21,
            'universidad':'UNSA'
        },        
        {
            'nombre': 'Pedro',
            'apellidos': 'Rodriguez Lapa',
            'edad':22,
            'universidad':'UNSA'
        },        
        {
            'nombre': 'Luis',
            'apellidos': 'Turpo Cuevas',
            'edad':23,
            'universidad':'UNSA'
        },
    ]


@route('/todos')
def todos(datos=datos):
    return template('todos',datos=datos)  #Pasa todos los datos para mostrarlos en una tabla


@route('/mostrar/<nombre>')
def mostrarNombre(nombre,datos=datos):  #Muestra una persona en especifico, buscado por el nombre
    for i in datos: #Buscaremos en el diccionario si se encuentra a la persona
        if i["nombre"]==nombre:
            return template('mostrar',datos=i)  #Se puede reusar la vista en la que se muestra cada persona
    return template('mostrar',datos={'nombre':'','apellidos':'','edad':'','universidad':''})  #Si no lo encuentra manda datos vacios








run(host="localhost",port=8000,debug=True,reloader=True)
