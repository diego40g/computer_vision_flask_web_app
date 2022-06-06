from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Pagina principal index"

#variable rules
@app.route('/<name>')
def variable(name):
    return 'This is variable {}'.format(name)

@app.route('/blog/<int:blogid>')
def blog(blogid):
    return "El id del blog es {}".format(blogid)

@app.route('/weight/<float:w>')
def weight(w):
    return "Su ancho es %s"%w


if __name__=="__main__":
    app.run(debug=True,port=3000)