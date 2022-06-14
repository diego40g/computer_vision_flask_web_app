from flask import render_template

def index():
    return "Bienvenido a la pagina de inicio"

def index_tem(name,age):
    return render_template('index.html',name=name,age=age)

def index_for():
    data = {
        'statistics':70,
        'machine learning':55,
        'deep learning':35.5,
        'python':82.1
    }
    return render_template("index_for.html",data=data)