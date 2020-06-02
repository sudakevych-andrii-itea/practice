from flask import request, jsonify, Blueprint, Response
from sqlite_context_manager import SQLite


curators_blueprint = Blueprint('curators_blueprint', __name__)


curator_structure = [
    "id",
    "name",
    "last_name"
]


def get_curators():
    with SQLite('students.db') as cur:
        cur.execute("SELECT * FROM curators")
        return [dict(zip(curator_structure, values)) for values in cur.fetchall()]


def get_curator(curator_id):
    with SQLite('students.db') as cur:
        cur.execute("SELECT * FROM curators WHERE id = ?", (curator_id,))
        return [dict(zip(curator_structure, cur.fetchone()))]


def create_curator(*data):
    with SQLite('students.db') as cur:
        cur.execute("CREATE TABLE if not exists curators("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "name VARCHAR NOT NULL, "
                    "last_name VARCHAR NOT NULL)")
        cur.execute("INSERT INTO curators(name, last_name) VALUES(?,?)", (*data,))


def update_curator(curator_id, *data):
    with SQLite('students.db') as cur:
        cur.execute("UPDATE curators SET passport_id=?, name=?, surname=? WHERE id=?", (*data, curator_id))


def delete_curator(curator_id):
    with SQLite('students.db') as cur:
        cur.execute("DELETE FROM curators WHERE id=?", (curator_id,))


@curators_blueprint.route('/curators', methods=['GET', 'POST'])
@curators_blueprint.route('/curators/<string:curator_id>', methods=['GET', 'PUT', 'DELETE'])
def curators(curator_id=None):
    if request.method == 'GET':
        data = get_curators()
        if curator_id:
            data = get_curator(curator_id)
        return jsonify(data)
    elif request.method == 'POST':
        create_curator(*request.json.values())
        return request.json
    elif request.method == 'PUT':
        update_curator(curator_id, *request.json.values())
        return Response(status=200)
    elif request.method == 'DELETE':
        delete_curator(curator_id)
        return Response(status=200)
