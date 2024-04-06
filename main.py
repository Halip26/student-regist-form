from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# URI stands for Uniform Resource Indetifier
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.sqlite3"
app.config["SECRET_KEY"] = "ABC987"
db = SQLAlchemy(app)


# create a table
class students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Age = db.Column(db.Integer)
    dob = db.Column(db.String(100))
    Gender = db.Column(db.String(10))

    def __init__(self, name, age, dob, gender):
        self.Name = name
        self.Age = age
        self.dob = dob
        self.Gender = gender


@app.route("/", methods=["GET", "POST"])
def add_students():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        dob = request.form["dob"]
        gender = request.form["gender"]
        student = students(name, age, dob, gender)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for("successfully"))

    return render_template("add_students.html")


@app.route("/successfully")
def successfully():
    return render_template("successfully.html")


@app.route("/show_details")
def show_details():
    # fetch all student records from the db
    all_students = students.query.all()
    return render_template("show_details.html", students=all_students)


@app.route("/clear_database", methods=["GET", "POST"])
def clear_database():
    if request.method == "POST":
        # delete all records from the students table
        db.session.query(students).delete()
        db.session.commit()

        # redirect to the show_details
        return redirect(url_for("successfully"))
    # render a template for confirmation
    return render_template("clear_database.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port="8081")
