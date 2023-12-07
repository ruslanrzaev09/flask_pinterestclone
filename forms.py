from flask_wtf.form import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import Length, DataRequired, EqualTo
from flask_wtf.file import FileField, FileAllowed


class RegistrationForm(FlaskForm):
    username = StringField(
        "Имя пользователя", validators=[DataRequired(), Length(min=5, max=30)]
    )
    password = PasswordField(
        "Пароль", validators=[DataRequired(), Length(min=5, max=30)]
    )
    confirm_password = PasswordField(
        "Подтверждение пароля", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Зарегестрироваться")


class LoginForm(FlaskForm):
    username = StringField(
        "Имя пользователя", validators=[DataRequired(), Length(min=5, max=30)]
    )
    password = PasswordField(
        "Пароль", validators=[DataRequired(), Length(min=5, max=30)]
    )
    submit = SubmitField("Войти")


class UploadImage(FlaskForm):
    image = FileField(
        "Выберите изображение",
        validators=[FileAllowed(["jpg", "png", "jpeg"], "Only Images!")],
    )
    description = TextAreaField("Описание")
    tags = StringField("Теги")
