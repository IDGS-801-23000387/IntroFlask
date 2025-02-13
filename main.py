from flask import Flask,render_template, request

app=Flask(__name__)

@app.route("/")
def index():
    titulo="IDGS801"
     
    return render_template("index.html",titulo=titulo)

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

app.route("/ejemplo2")
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
def username(id,username):
    return f"<h1>Hola, {username}! Tu ID es: {id}</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"<h1>La suma es: {n1+n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="juan"):
    return f"<h1>Hola, {param}</h1>"

@app.route("/operas")
def operas():
    return '''
 <form action="">
        <label for="">Name</label>
        <input type="text" id="name" name="name" required>

        <label for="">APaterno</label>
        <input type="text" id="APaterno" name="APaterno" required>
    </form>
           '''
           
if __name__== "__main__":
    app.run(debug=True, port=3000)
    