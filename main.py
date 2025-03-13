from flask import Flask, render_template, request
from datetime import datetime
import forms
from flask import g
from flask import flash
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.secret_key="1234567890"
csrf=CSRFProtect()
@app.route("/")
def index():
    
    return render_template("index.html" )

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/OperasBas", methods=["GET", "POST"])
def operas1():
    resultado = 0
    if request.method == "POST":
        n1 = float(request.form.get("n1"))
        n2 = float(request.form.get("n2"))
        seleccion = request.form.get("seleccion")

        if seleccion == "suma":
            resultado = f"La suma de {n1} + {n2} es {n1 + n2}"
        elif seleccion == "resta":
            resultado = f"La resta de {n1} - {n2} es {n1 - n2}"
        elif seleccion == "multiplicacion":
            resultado = f"La multiplicación de {n1} * {n2} es {n1 * n2}"
        elif seleccion == "division":
            resultado = f"La división de {n1} / {n2} es {n1 / n2}"

    return render_template("OperasBas.html", resultado=resultado)

@app.route("/Alumnos", methods=["GET", "POST"])
def alumnos():
    mat = ""
    nom = ""
    ape = ""
    email = ""
    alumno_clas = forms.UserForm(request.form)
    if request.method == "POST" and alumno_clas.validate():
        mat = alumno_clas.matricula.data
        nom = alumno_clas.nombre.data
        ape = alumno_clas.apellido.data
        email = alumno_clas.correo.data
        mensaje="Bienvenido {}".format(nom )	
        flash(mensaje)

    return render_template("Alumnos.html", form=alumno_clas, mat=mat, nom=nom, ape=ape, email=email)

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/hola")
def hola():
    return "<h1>Hola, Mundo!</h1>"

@app.route("/user/<string:user>")
def user(user):
    return f"<h1>Hola, {user}!</h1>"

@app.route("/numero/<int:numero>")
def number(numero):
    return f"<h1>El numero es {numero}!</h1>"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"<h1>Hola, {username}! Tu ID es: {id}</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"<h1>La suma es: {n1 + n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="juan"):
    return f"<h1>Hola, {param}</h1>"

@app.route("/operas", methods=["GET"])
def operas():
    return '''
    <form action="">
        <label for="">Name</label>
        <input type="text" id="name" name="name" required>
        <label for="">APaterno</label>
        <input type="text" id="APaterno" name="APaterno" required>
    </form>
    '''

 

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    print("beforer 1")

@app.after_request
def after_request(response):
    print("afterr 3")
    return response
# main.py
@app.route('/ZodiacoChino', methods=['GET', 'POST'])
def zodiaco_chino():
    nombre = ""
    apellidoP =""
    apellidoM = ""
    signo = ""
    imagen =""
    edad = 0
    dia =0
    mes = 0
    sexo = ""
    signos_chinos = [
        ("Mono", "mono.png"),
        ("Gallo", "gallo.png"),
        ("Perro", "perro.png"),
        ("Cerdo", "cerdo.png"),
        ("Rata", "rata.png"),
        ("Buey", "buey.png"),
        ("Tigre", "tigre.png"),
        ("Conejo", "conejo.png"),
        ("Dragón", "dragon.png"),
        ("Serpiente", "serpiente.png"),
        ("Caballo", "caballo.png"),
        ("Cabra", "cabra.png")
    ]

    zodiaco_form = forms.ZodiacoForm(request.form)
    

    if request.method == 'POST' and zodiaco_form.validate():
        nombre = zodiaco_form.nombre.data
        apellidoP = zodiaco_form.apellidoP.data
        apellidoM = zodiaco_form.apellidoM.data
        anio = zodiaco_form.anio.data
        dia = zodiaco_form.dia.data
        mes = zodiaco_form.mes.data
        sexo = zodiaco_form.sexo.data

        añoPresente = datetime.now().year
        edad = añoPresente - anio
        signoInfo = signos_chinos[anio % 12]
        signo = signoInfo[0]
        imagen = f"static/img/{signoInfo[1]}"

    return render_template('ZodiacoChino.html', form=zodiaco_form, nombre=nombre, apellidoP=apellidoP, apellidoM=apellidoM, signo=signo, imagen=imagen, edad=edad, dia=dia, mes=mes, sexo=sexo)
if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)