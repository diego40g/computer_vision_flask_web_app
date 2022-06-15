import datetime
from flask import Blueprint,request,jsonify,Flask,Markup,render_template
from firebase_admin import db

labels=[
    'Altitud Metros', 'Calidad Aire PPM', 'Humedad Relativa', 'Presion Pascal', 'Temperatura C BMP', 'Temperatura-C-DHT11', 'Velocidad Viento km/h', 'Velocidad Maxima Viento km/h'
]
colors=[
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"
]

#Fecha
def fechaD():
    fecha=[]  
    user_dicc=user_Ref.get()
    for value in user_dicc.items():
        for v in value:
            if(type(v)==type({})):
                for va in v.items():
                    if va[0]=="Fecha":
                        fecha.append(va[1])
    return fecha
#Calidad-Aire-PPM
def calidadAirePPMD():
    calidadAirePPM=[]
    user_dicc=user_Ref.get()
    for value in user_dicc.items():
        for v in value:
            if(type(v)==type({})):
                for va in v.items():
                    if va[0]=="Calidad-Aire-PPM":
                        calidadAirePPM.append(va[1])
    return calidadAirePPM
#Humedad-Relativa
def humedadRelativaD():
    humedadRelativa=[]
    user_dicc=user_Ref.get()
    for value in user_dicc.items():
        for v in value:
            if(type(v)==type({})):
                for va in v.items():
                    if va[0]=="Humedad-Relativa":
                        humedadRelativa.append(va[1])
    return humedadRelativa
#Presion-Pascal                  
def presionPascalD():
    presionPascal=[]
    user_dicc=user_Ref.get()
    for value in user_dicc.items():
        for v in value:
            if(type(v)==type({})):
                for va in v.items():
                    if va[0]=="Presion-Pascal":
                        presionPascal.append(va[1])
    return presionPascal
#Temperatura-C-BMP
def temperaturaBMPD():
    temperaturaCBMP=[]
    user_dicc=user_Ref.get()
    for value in user_dicc.items():
        for v in value:
            if(type(v)==type({})):
                for va in v.items():
                    if va[0]=="Temperatura-C-BMP":
                        temperaturaCBMP.append(va[1])
    return temperaturaCBMP
#Temperatura-C-DHT11
def temperaturaDHTD():
    temperaturaCDHT11=[]
    user_dicc=user_Ref.get()
    for value in user_dicc.items():
        for v in value:
            if(type(v)==type({})):
                for va in v.items():
                    if va[0]=="Temperatura-C-DHT11":
                        temperaturaCDHT11.append(va[1])
    return temperaturaCDHT11
#Velocidad_Maxima_Viento_km-h
def velocidadMaxVientoD():
    velocidadMaximaVientoKmH=""
    user_dicc=user_Ref.get()
    for value in user_dicc.items():
        for v in value:
            if(type(v)==type({})):
                for va in v.items():
                    if va[0]=="Velocidad_Maxima_Viento_km-h":
                        velocidadMaximaVientoKmH=str(va[1])
    return velocidadMaximaVientoKmH
#Velocidad_Viento_km-h      
def velocidadVientoD():
    velocidadVientoKmH=[]
    user_dicc=user_Ref.get()
    for value in user_dicc.items():
        for v in value:
            if(type(v)==type({})):
                for va in v.items():
                    if va[0]=="Velocidad_Viento_km-h":
                        if va[1]<0:
                            velocidadVientoKmH.append(0)
                        else:
                            velocidadVientoKmH.append(va[1])
    return velocidadVientoKmH
#Altitud-Metros
def altitudMetrosD():
    altitudMetros=[]
    user_dicc=user_Ref.get()
    for value in user_dicc.items():
        for v in value:
            if(type(v)==type({})):
                for va in v.items():
                    if va[0]=="Altitud-Metros":
                        altitudMetros.append(va[1])
    return altitudMetros
            
def data():
    user_dicc=user_Ref.get()
    for value in user_dicc.items():
        for v in value:
            if(type(v)==type({})):
                #v.get('name')
                for va in v.items():
                    #print(va[0])
                    #print(type(va[1]))
                    if va[0]=="Altitud-Metros":
                        altitudMetros.append(va[1])
                    if va[0]=="Calidad-Aire-PPM":
                        calidadAirePPM.append(va[1])
                    if va[0]=="Fecha":
                        fecha.append(va[1])
                    if va[0]=="Humedad-Relativa":
                        humedadRelativa.append(va[1])
                    if va[0]=="Presion-Pascal":
                        presionPascal.append(va[1])
                    if va[0]=="Temperatura-C-BMP":
                        temperaturaCBMP.append(va[1])
                    if va[0]=="Temperatura-C-DHT11":
                        temperaturaCDHT11.append(va[1])
                    if va[0]=="Velocidad_Maxima_Viento_km-h":
                        velocidadMaximaVientoKmH=str(va[1])
                    if va[0]=="Velocidad_Viento_km-h":
                        velocidadVientoKmH.append(va[1])
    
    print("/******Altitud Metros***********/")
    print(altitudMetros)
    """print("/******Calidad Aire PPM*********/")
    print(calidadAirePPM)"""
    print("/************Fecha**************/")
    print(fecha)
    """print("/*******Humedad Relativa********/")
    print(humedadRelativa)
    print("/*********Presion Pascal********/")
    print(presionPascal)
    print("/*******Temperatura CBMP********/")
    print(temperaturaCBMP)
    print("/******Temperatura DHT11********/")
    print(temperaturaCDHT11)
    print("/********Velocidad Max**********/")
    print(velocidadMaximaVientoKmH)
    print("/************Viento*************/")
    print(velocidadVientoKmH)"""

#db=firestore.client()
#user_Ref=db.collection('user')

user_Ref=db.reference('/esp32/DiegoPaz/Sensores')
"""ref.push({
    'name':'Diego Paz',
    'age': 24
})"""

userAPI=Blueprint('userAPI',__name__)

@userAPI.route('/add',methods=['POST'])
def create():
    try:
        ##user_Ref.push(id.hex).set(request.json)
        user_Ref.push(request.json)
        ##modificar un dato
        user_Upd=user_Ref.child('-N4FkKESOAvrg8OUCEaF')
        user_Upd.update({'name':'NaN'})
        return jsonify({"succesfull":True}),200
    except Exception as e:
        return f"An Error Occurred: {e}"

#localhost:3030/data/altitud_metros
@userAPI.route('/altitud_metros',methods=['GET'])
def getAltMetro():
    line_labels=[]
    line_values=[]
    try:
        line_labels=fechaD()
        line_values=altitudMetrosD()
        print(len(line_labels))
        print(len(line_values))
        return render_template('line_chart.html', title='Altitud en metros', max=max(line_values), values=line_values, labels=line_labels)
    except Exception as e:
        return f"Error por: {e}"
    
#localhost:3030/data/calidad_aire
@userAPI.route('/calidad_aire',methods=['GET'])
def getCalAire():
    line_labels=[]
    line_values=[]
    try:
        line_labels=fechaD()
        line_values=calidadAirePPMD()
        print(len(line_labels))
        print(len(line_values))
        return render_template('line_chart.html', title='Calidad del aire PPM', max=max(line_values), values=line_values, labels=line_labels)
    except Exception as e:
        return f"Error por: {e}" 

#localhost:3030/data/humedad_relativa
@userAPI.route('/humedad_relativa',methods=['GET'])
def getHumRelativa():
    line_labels=[]
    line_values=[]
    try:
        line_labels=fechaD()
        line_values=humedadRelativaD()
        print(len(line_labels))
        print(len(line_values))
        return render_template('line_chart.html', title='Humedad Relativa', max=max(line_values), values=line_values, labels=line_labels)
    except Exception as e:
        return f"Error por: {e}" 

#localhost:3030/data/presion_atmosferica
@userAPI.route('/presion_atmosferica',methods=['GET'])
def getPreAtmosferica():
    line_labels=[]
    line_values=[]
    try:
        line_labels=fechaD()
        line_values=presionPascalD()
        print(len(line_labels))
        print(len(line_values))
        return render_template('line_chart.html', title='Presion atmosferica Pascales', max=max(line_values), values=line_values, labels=line_labels)
    except Exception as e:
        return f"Error por: {e}" 

#localhost:3030/data/temperatura_BMP
@userAPI.route('/temperatura_BMP',methods=['GET'])
def getTemperaturaBMP():
    line_labels=[]
    line_values=[]
    try:
        line_labels=fechaD()
        line_values=temperaturaBMPD()
        print(len(line_labels))
        print(len(line_values))
        return render_template('line_chart.html', title='Temperatura BMP', max=max(line_values), values=line_values, labels=line_labels)
    except Exception as e:
        return f"Error por: {e}" 
    
#localhost:3030/data/temperatura_DHT
@userAPI.route('/temperatura_DHT',methods=['GET'])
def getTemperaturaDHT():
    line_labels=[]
    line_values=[]
    try:
        line_labels=fechaD()
        line_values=temperaturaDHTD()
        print(len(line_labels))
        print(len(line_values))
        return render_template('line_chart.html', title='Temperatura DHT', max=max(line_values), values=line_values, labels=line_labels)
    except Exception as e:
        return f"Error por: {e}" 
    
#localhost:3030/data/vel_max_viento
@userAPI.route('/vel_max_viento',methods=['GET'])
def getMaxViento():
    try:
        date=datetime.datetime.now()
        value=velocidadMaxVientoD()
        return render_template('index.html', title='Velocidad Maxima del Viento', value=value, date=date)
    except Exception as e:
        return f"Error por: {e}"
    
#localhost:3030/data/vel_viento
@userAPI.route('/vel_viento',methods=['GET'])
def getVelViento():
    line_labels=[]
    line_values=[]
    try:
        line_labels=fechaD()
        line_values=velocidadVientoD()
        print(len(line_labels))
        print(len(line_values))
        return render_template('line_chart.html', title='Velocidad del Viento', max=max(line_values), values=line_values, labels=line_labels)
    except Exception as e:
        return f"Error por: {e}" 