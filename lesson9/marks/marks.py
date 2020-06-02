from flask import request, jsonify, Blueprint, Response
from sqlite_context_manager import SQLite

marks_blueprint = Blueprint('marks_blueprint', __name__)


def create_mark(*data):
    with SQLite('students.db') as cur:
        cur.execute("CREATE TABLE if not exists marks("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "mark TINYINT NOT NULL, "
                    "subject_id VARCHAR NOT NULL,"                    
                    "student_id INTEGER,"
                    "FOREIGN KEY(subject_id) REFERENCES subjects(id), "
                    "FOREIGN KEY(student_id) REFERENCES students(id))")
        cur.execute("INSERT INTO classes(name, faculty_id) VALUES(?,?)", (*data,))


def update_mark(mark_id, *data):
    with SQLite('students.db') as cur:
        cur.execute("UPDATE marks SET mark=?, subject_id=?, student_id=? WHERE id=?", (*data, mark_id))


def delete_class(mark_id):
    with SQLite('students.db') as cur:
        cur.execute("DELETE FROM marks WHERE id=?", (mark_id,))
        return Response(status=200)


@marks_blueprint.route('/marks/<string:mark_id>', methods=['POST', 'PUT', 'DELETE'])
def classes(mark_id=None):
    if request.method == 'POST':
        create_mark(*request.json.values())
        return request.json
    elif request.method == 'PUT':
        update_mark(mark_id, *request.json.values())
        return Response(status=200)
    elif request.method == 'DELETE':
        delete_class(mark_id)
        return Response(status=200)
