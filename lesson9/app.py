from flask import Flask

from faculties.faculties import faculties_blueprint
from classes.classes import classes_blueprint
from curators.curators import curators_blueprint
from students.students import students_blueprint
from subjects.subjects import subjects_blueprint
from marks.marks import marks_blueprint

app = Flask(__name__)
app.register_blueprint(faculties_blueprint)
app.register_blueprint(classes_blueprint)
app.register_blueprint(curators_blueprint)
app.register_blueprint(students_blueprint)
app.register_blueprint(subjects_blueprint)
app.register_blueprint(marks_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
