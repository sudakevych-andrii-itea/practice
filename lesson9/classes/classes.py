from flask import request, jsonify, Blueprint, Response
from sqlite_context_manager import SQLite

classes_blueprint = Blueprint('classes_blueprint', __name__)


classes_structure = [
    "id",
    "name",
    "faculty_id"
]


class_structure = [
    "id",
    "name",
    "faculty_id",
    "students_id",
    "students_last_name"
]


def get_classes():
    with SQLite('students.db') as cur:
        cur.execute("SELECT * FROM classes")
        return [dict(zip(classes_structure, values)) for values in cur.fetchall()]


def get_class(class_id):
    with SQLite('students.db') as cur:
        cur.execute("SELECT classes.id, classes.name, classes.faculty_id, "
                    "GROUP_CONCAT(students.id), GROUP_CONCAT(students.last_name) "
                    "FROM classes "
                    "INNER JOIN students ON (students.class_id = classes.id) "
                    "WHERE classes.id=?", (class_id,))
        result = dict(zip(class_structure, cur.fetchone()))
        result['students_id'] = [int(item) for item in result['students_id'].split(',')]
        result['students_last_name'] = result['students_last_name'].split(',')
        result['students'] = dict(zip(result['students_id'], result['students_last_name']))
        result.pop('students_id')
        result.pop('students_last_name')
        return result


def create_class(*data):
    with SQLite('students.db') as cur:
        cur.execute("CREATE TABLE if not exists classes("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "name VARCHAR NOT NULL,"
                    "faculty_id INTEGER, "
                    "FOREIGN KEY(faculty_id) REFERENCES faculties(id))")
        cur.execute("INSERT INTO classes(name, faculty_id) VALUES(?,?)", (*data,))


def update_class(class_id, *data):
    with SQLite('students.db') as cur:
        cur.execute("UPDATE classes SET name=?, faculty_id=? WHERE id=?", (*data, class_id))


def delete_class(class_id):
    with SQLite('students.db') as cur:
        cur.execute("DELETE FROM classes WHERE id=?", (class_id,))
        return Response(status=200)


@classes_blueprint.route('/classes', methods=['GET', 'POST'])
@classes_blueprint.route('/classes/<string:class_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def classes(class_id=None):
    if request.method == 'GET':
        data = get_classes()
        if class_id:
            data = get_class(class_id)
        return jsonify(data)
    elif request.method == 'POST':
        create_class(*request.json.values())
        return request.json
    elif request.method == 'PUT':
        update_class(class_id, *request.json.values())
        return Response(status=200)
    elif request.method == 'DELETE':
        delete_class(class_id)
        return Response(status=200)
