from flask import request, jsonify, Blueprint, Response
from sqlite_context_manager import SQLite


faculties_blueprint = Blueprint('faculties_blueprint', __name__)


faculties_structure = [
    "id",
    "name",
    "description"
]

faculty_structure = [
    "id",
    "name",
    "description",
    "classes_id",
    "classes_name"
]


def get_faculties():
    with SQLite('students.db') as cur:
        cur.execute("SELECT * FROM faculties")
        return [dict(zip(faculties_structure, values)) for values in cur.fetchall()]


def get_faculty(faculty_id):
    with SQLite('students.db') as cur:
        cur.execute("SELECT faculties.id, faculties.name, "
                    "faculties.description, GROUP_CONCAT(classes.id), GROUP_CONCAT(classes.name) "
                    "FROM faculties "
                    "INNER JOIN classes ON (classes.faculty_id = faculties.id) "
                    "WHERE faculties.id = ?", (faculty_id,))
        result = dict(zip(faculty_structure, cur.fetchone()))
        result['classes_id'] = [int(item) for item in result['classes_id'].split(',')]
        result['classes_name'] = result['classes_name'].split(',')
        result['classes'] = dict(zip(result['classes_id'], result['classes_name']))
        result.pop('classes_id')
        result.pop('classes_name')
        return result


def create_faculty(*data):
    with SQLite('students.db') as cur:
        cur.execute("CREATE TABLE if not exists faculties("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "name VARCHAR NOT NULL, "
                    "description VARCHAR)")
        cur.execute("INSERT INTO faculties(name, description) VALUES(?,?)", (*data,))


def update_faculty(faculty_id, *data):
    with SQLite('students.db') as cur:
        cur.execute("UPDATE faculties SET name=?, description=? WHERE id=?", (*data, faculty_id))


def delete_faculty(faculty_id):
    with SQLite('students.db') as cur:
        cur.execute("DELETE FROM faculties WHERE id=?", (faculty_id,))


@faculties_blueprint.route('/faculties', methods=['GET', 'POST'])
@faculties_blueprint.route('/faculties/<string:faculty_id>', methods=['GET', 'PUT', 'DELETE'])
def faculties(faculty_id=None):
    if request.method == 'GET':
        data = get_faculties()
        if faculty_id:
            data = get_faculty(faculty_id)
        return jsonify(data)
    elif request.method == 'POST':
        create_faculty(*request.json.values())
        return jsonify(request.json)
    elif request.method == 'PUT':
        update_faculty(faculty_id, *request.json.values())
        return Response(status=200)
    elif request.method == 'DELETE':
        delete_faculty(faculty_id)
        return Response(status=200)
