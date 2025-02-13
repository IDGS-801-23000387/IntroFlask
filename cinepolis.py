from flask import Flask, render_template, request  

app = Flask(__name__)  

class Cinepolis:  
    precioBoleto = 12  

    def calcular_total(self, boletos, tiene_tarjeta):  
        subtotal = boletos * self.precioBoleto  
        descuento = 0  
        if 3 <= boletos <= 5:  
            descuento += 0.10   
        elif boletos > 5:  
            descuento += 0.15       
        if tiene_tarjeta == "si":  
            descuento += 0.10   
        total = subtotal - (subtotal * descuento)  
        return round(total, 2)  

    def validar_boletos(self, compradores, boletos):  
        return boletos <= compradores * 7  

@app.route('/', methods=["GET", "POST"])  
def index():  
    totalPagar = 0
    alertaError = ""
    cinepolis = Cinepolis()  
    if request.method == "POST":  
        nombre = request.form.get("nombre")  
        compradores = request.form.get("compradores")  
        boletos = request.form.get("boletos")  
        tiene_tarjeta = request.form.get("cineco")   
        compradores = int(compradores)  
        boletos = int(boletos)  
        if not cinepolis.validar_boletos(compradores, boletos):  
                alertaError = "Solo puedes comprar 7 Boletos por personas Por favor cambie el numero de personas "  
        else:  
                totalPagar = cinepolis.calcular_total(boletos, tiene_tarjeta)  
    return render_template("Cinepolis.html",totalPagar=totalPagar,alertaError=alertaError,)  

if __name__ == "__main__":  
    app.run(debug=True, port=3000)