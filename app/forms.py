from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from .db_connection import get_user, validate_user_password

class AddTodoForm(FlaskForm):
    description = StringField("Descripción", validators=[DataRequired()])
    submit = SubmitField("Crear")

class ToDoOptionsForm(FlaskForm):
    description = StringField(validators=[DataRequired()]) 
    delete = SubmitField("Borrar")
    update = SubmitField("Actualizar estado")
    edit = SubmitField("Editar")
    save = SubmitField("Guardar")

class LogInForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Iniciar sesión")

    def validate_username(self, username):
        if not get_user(username.data):
            raise ValidationError("No existe ningún usuario registrado con ese nombre.")

    def validate_password(self, password):
        if get_user(self.username.data) and not validate_user_password(self.username.data, password.data):
            raise ValidationError("Contraseña incorrecta, por favor inténtelo de nuevo.")

class SignUpForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired(), EqualTo("confirm_password", message="Las contraseñas no coinciden.")])
    confirm_password = PasswordField("Confirmar contraseña", validators=[DataRequired(), EqualTo("password", message="Las contraseñas no coinciden.")])
    submit = SubmitField("Registrar")

    def validate_username(self, username):
        if get_user(username.data):
            raise ValidationError("El nombre de usuario ingresado ya ha sido registrado.")

