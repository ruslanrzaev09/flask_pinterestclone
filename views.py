from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, current_user, logout_user
from app import app, bcrypt, db
from forms import RegistrationForm, LoginForm, UploadImage
from models import User, Image


@app.route("/", methods=["GET", "POST"])
@login_required
def home():
    images = Image.query.all()

    return render_template("home.html", images=images, current_user=current_user)


@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    form = UploadImage()

    if form.validate_on_submit():
        image = form.image.data
        filename = image.filename
        description = form.description.data
        tags = form.tags.data

        image.save(f"static/uploads/{filename}")

        new_image = Image(
            filename=filename,
            description=description,
            user_id=current_user.id,
            tags=tags,
        )

        db.session.add(new_image)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html", form=form)


@app.route("/search", methods=["GET", "POST"])
def search():
    tags = request.form.get("name")
    images = Image.query.filter(Image.tags.like(f"%{tags}%")).all()

    return render_template("search.html", images=images)


@app.route("/post/<int:id>")
def post(id):
    post = Image.query.get_or_404(id)

    return render_template("post.html", post=post)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(username=form.username.data, password=hashed_password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)

            return redirect(url_for("home"))
        else:
            flash(
                "Имя пользователя или пароль неверный. Проверьте значения и попробуйте еще раз."
            )

            return redirect(url_for("login"))

    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()

    return redirect(url_for("register"))


@app.errorhandler(404)
def not_found(e):
    return redirect(url_for("home"))


@app.errorhandler(403)
def not_found(e):
    return redirect(url_for("home"))
