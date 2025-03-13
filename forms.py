from wtforms import Form, validators, StringField, EmailField, IntegerField, RadioField
from datetime import datetime  # Importa datetime para usar en la validación del año

class UserForm(Form):
    matricula = StringField("Matricula", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=3, max=10, message="3-10 Caracteres")
    ])
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido")
    ])
    apellido = StringField("Apellido", [
        validators.DataRequired(message="El campo es requerido")
    ])
    correo = EmailField("Correo", [
        validators.DataRequired(message="El campo es requerido")
    ])

class ZodiacoForm(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido")
    ])
    apellidoP = StringField("Apellido Paterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    apellidoM = StringField("Apellido Materno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    anio = IntegerField("Año de Nacimiento", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1900, max=datetime.now().year, message="El año debe ser válido")
    ])
    dia = IntegerField("Día", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, max=31, message="El día debe ser válido")
    ])
    mes = IntegerField("Mes", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, max=12, message="El mes debe ser válido")
    ])
    sexo = RadioField("Sexo", choices=[
        ("Masculino", "Masculino"),
        ("Femenino", "Femenino")
    ], validators=[validators.DataRequired(message="El campo es requerido")])