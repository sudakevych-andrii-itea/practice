from flask import request, jsonify, Blueprint, Response
from sqlite_context_manager import SQLite


subjects_blueprint = Blueprint('subjects_blueprint', __name__)


subject_structure = [
    "id",
    "name"
]


def get_subjects():
    with SQLite('students.db') as cur:
        cur.execute("SELECT * FROM subjects")
        return [dict(zip(subject_structure, values)) for values in cur.fetchall()]


def create_subject(*data):
    with SQLite('students.db') as cur:
        cur.execute("CREATE TABLE if not exists subjects("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                    "name VARCHAR NOT NULL)")
        cur.execute("INSERT INTO subjects(name) "
                    "VALUES(?)", (*data,))


def update_subject(subject_id, *data):
    with SQLite('students.db') as cur:
        cur.execute("UPDATE subjects SET name=? WHERE id=?", (*data, subject_id))


def delete_subject(subject_id):
    with SQLite('students.db') as cur:
        cur.execute("DELETE FROM subject WHERE id=?", (subject_id,))
        return Response(status=200)


@subjects_blueprint.route('/subjects', methods=['GET', 'POST'])
@subjects_blueprint.route('/subjects/<string:subject_id>', methods=['PUT', 'DELETE'])
def subject(subject_id=None):
    if request.method == 'GET':
        data = get_subjects()
        return jsonify(data)
    elif request.method == 'POST':
        create_subject(*request.json.values())
        return request.json
    elif request.method == 'PUT':
        update_subject(subject_id, *request.json.values())
        return Response(status=200)
    elif request.method == 'DELETE':
        delete_subject(subject_id)
        return Response(status=200)
