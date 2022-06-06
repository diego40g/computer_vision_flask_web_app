from flask import Flask
import views

app = Flask(__name__)

#create rule (uri)
app.add_url_rule('/','index',views.index)

app.add_url_rule('/template/<name>/<int:age>','index_template',views.index_tem)

#run flask app
if __name__=="__main__":
    app.run(debug=True, port=3000)