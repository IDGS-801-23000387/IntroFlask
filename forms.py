from wtforms import Form
from wtforms import validators

from wtforms import StringField,  PasswordField, BooleanField, SubmitField, SelectField, RadioField, DateField, IntegerField, DecimalField,EmailField
class UserForm(Form):
    
    matricula = StringField("Matricula",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3,max=10,message="3-10 Caracteres")
    ])
    nombre = StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido")
    ])
    apellido = StringField("Apellido",[
        validators.DataRequired(message="El campo es requerido")
    ])
    correo = EmailField("Correo",[
        validators.DataRequired(message="El campo es requerido")
    ])