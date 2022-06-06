from flask import render_template

def index():
    return "Bienvenido a la pagina de inicio"

def index_tem(name,age):
    #age=17
    return render_template('index.html',name=name,age=age)