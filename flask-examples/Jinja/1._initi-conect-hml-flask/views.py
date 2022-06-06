from flask import render_template

def index():
    return "Bienvenido a la pagina de inicio"

def index_tem():
    return render_template('index.html')