from flask import request, jsonify, Blueprint, Response
from sqlite_context_manager import SQLite


students_blueprint = Blueprint('students_blueprint', __name__)


students_structure = [
    "id",
    "name",
    "last_name",
    "faculty_id",
    "class_id",
    "curator_id"
]


student_structure = [
    "id",
    "name",
    "last_name",
    "faculty_id",
    "faculty_name",
    "class_id",
    "class_name",
    "curator_id",
    "marks"
]


def get_students():
    with SQLite('students.db') as cur:
        cur.execute("SELECT * FROM students")
        return [dict(zip(students_structure, values)) for values in cur.fetchall()]


def get_excellent_students():
    with SQLite('students.db') as cur:
        cur.execute("SELECT students.id, students.name, students.last_name,"
                    "faculties.id, faculties.name, "
                    "classes.id, classes.name, "
                    "curators.id, GROUP_CONCAT(marks.mark) "
                    "FROM students "
                    "INNER JOIN faculties ON (students.faculty_id = faculties.id) "
                    "INNER JOIN classes ON (students.class_id = classes.id)"
                    "INNER JOIN curators ON (students.curator_id = curators.id)"
                    "INNER JOIN marks ON (students.id = marks.student_id) "
                    "GROUP BY(students.id)"
                    "HAVING(AVG(marks.mark) >= 80)")
        return [dict(zip(student_structure, values)) for values in cur.fetchall()]


def get_student(student_id):
    with SQLite('students.db') as cur:
        cur.execute("SELECT students.id, students.name, students.last_name,"
                    "faculties.id, faculties.name, "
                    "classes.id, classes.name, "
                    "curators.id, GROUP_CONCAT(marks.mark) "
                    "FROM students "
                    "INNER JOIN faculties ON (students.faculty_id = faculties.id) "
                    "INNER JOIN classes ON (students.class_id = classes.id)"
                    "INNER JOIN curators ON (students.curator_id = curators.id)"
                    "INNER JOIN marks ON (students.id = marks.student_id) "
                    "WHERE students.id = ?", (student_id,))
        return dict(zip(student_structure, cur.fetchone()))


def create_student(*data):
    with SQLite('students.db') as cur:
        cur.execute("CREATE TABLE if not exists students("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "name VARCHAR NOT NULL, "
                    "last_name VARCHAR NOT NULL, "
                    "faculty_id INTEGER NOT NULL, "
                    "class_id INTEGER NOT NULL, "
                    "curator_id INTEGER NOT NULL, "
                    "FOREIGN KEY(faculty_id) REFERENCES faculties(id), "
                    "FOREIGN KEY(class_id) REFERENCES classes(id), "
                    "FOREIGN KEY(curator_id) REFERENCES curators(id))")
        cur.execute("INSERT INTO students("
                    "name, last_name, "
                    "faculty_id, class_id, curator_id) "
                    "VALUES(?,?,?,?,?)", (*data,))


def update_student(student_id, *data):
    with SQLite('students.db') as cur:
        cur.execute("UPDATE students SET name=?, last_name=?, faculty_id=?, class_id=?, curator_id=? WHERE id=?", (*data, student_id))


def delete_student(student_id):
    with SQLite('students.db') as cur:
        cur.execute("DELETE FROM students WHERE id=?", (student_id,))
        return Response(status=200)


@students_blueprint.route('/students', methods=['GET', 'POST'])
@students_blueprint.route('/students/<string:student_id>', methods=['GET', 'PUT', 'DELETE'])
def students(student_id=None):
    if request.method == 'GET':
        data = get_students()
        if student_id:
            data = get_student(student_id)
        return jsonify(data)
    elif request.method == 'POST':
        create_student(*request.json.values())
        return request.json
    elif request.method == 'PUT':
        update_student(student_id, *request.json.values())
        return Response(status=200)
    elif request.method == 'DELETE':
        delete_student(student_id)
        return Response(status=200)


@students_blueprint.route('/excellent_students', methods=['GET'])
def excellent_students():
    if request.method == 'GET':
        data = get_excellent_students()
        return jsonify(data)
