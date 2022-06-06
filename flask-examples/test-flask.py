from flask import Flask
print("Hola desde python")

app=Flask(__name__)

@app.route('/')
def index():
    return "Hola desde flask"

@app.route('/route1')
def route1():
    return "Esto es una ruta 1"
def route2():
    return "Esto es una ruta 2"

app.add_url_rule('/route2','route2', route2)

if __name__=="__main__":
    app.run(host="localhost", port=3000, debug=True)