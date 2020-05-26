from sqlite_context_manager import SQLite


class User:
    def __init__(self, db_name='students.db'):
        self.db_name = db_name

    def get_all_students(self):
        with SQLite(self.db_name) as cur:
            cur.execute("SELECT student_identifier, student_name FROM students;")
            return cur.fetchall()

    def get_student_by_id(self, student_identifier):
        with SQLite(self.db_name) as cur:
            cur.execute("SELECT * FROM students "
                        "INNER JOIN faculties ON (students.faculty_id = faculties.id) "
                        "INNER JOIN classes ON (students.class_id = classes.id) "
                        "WHERE student_identifier = ?", (student_identifier,))
            return cur.fetchone()

    def get_all_students_info(self):
        with SQLite(self.db_name) as cur:
            cur.execute("SELECT students.id, students.student_identifier, students.student_name, "
                        "faculties.faculty_name, classes.class_name, GROUP_CONCAT(marks.mark) "
                        "FROM students "
                        "INNER JOIN faculties ON (students.faculty_id = faculties.id)"
                        "INNER JOIN classes ON (students.class_id = classes.id)"
                        "INNER JOIN marks ON (students.id = marks.student_id)"
                        "GROUP BY(students.id) ")
            return cur.fetchall()

    def get_excellent_students(self):
        with SQLite(self.db_name) as cur:
            cur.execute("SELECT students.id, students.student_identifier, "
                        "students.student_name "
                        "FROM students "
                        "INNER JOIN marks ON (students.id = marks.student_id)"
                        "GROUP BY(students.id)"
                        "HAVING(AVG(marks.mark) >= 90)")
            return cur.fetchall()


class Admin:
    def __init__(self, db_name='students.db'):
        self.db_name = db_name

    def _create_faculties_table(self):
        with SQLite(self.db_name) as cur:
            cur.execute("CREATE TABLE if not exists faculties("
                        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                        "faculty_name VARCHAR NOT NULL)")

    def add_faculty(self, faculty_name):
        self._create_faculties_table()
        with SQLite(self.db_name) as cur:
            cur.execute("INSERT INTO faculties(faculty_name) VALUES(?)", (faculty_name,))

    def _create_classes_table(self):
        with SQLite(self.db_name) as cur:
            cur.execute("CREATE TABLE if not exists classes("
                        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                        "class_name VARCHAR NOT NULL,"
                        "faculty_id INTEGER, "
                        "FOREIGN KEY(faculty_id) REFERENCES faculties(id))")

    def add_class(self, class_name, faculty_id):
        self._create_classes_table()
        with SQLite(self.db_name) as cur:
            cur.execute("INSERT INTO classes(class_name, faculty_id) VALUES(?,?)", (class_name, faculty_id))

    def _create_subjects_table(self):
        with SQLite(self.db_name) as cur:
            cur.execute("CREATE TABLE if not exists subjects("
                        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                        "subject_name VARCHAR NOT NULL)")

    def add_subject(self, subject_name):
        self._create_subjects_table()
        with SQLite(self.db_name) as cur:
            cur.execute("INSERT INTO subjects(subject_name) VALUES(?)", (subject_name,))

    def _create_students_table(self):
        with SQLite(self.db_name) as cur:
            cur.execute("CREATE TABLE if not exists students("
                        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                        "student_identifier VARCHAR NOT NULL, "
                        "student_name VARCHAR NOT NULL, "
                        "faculty_id INTEGER, "                        
                        "class_id INTEGER, "
                        "FOREIGN KEY(faculty_id) REFERENCES faculties(id), "
                        "FOREIGN KEY(class_id) REFERENCES classes(id))")

    def add_student(self, student_id, student_name, faculty_id, class_id):
        self._create_students_table()
        with SQLite(self.db_name) as cur:
            cur.execute("INSERT INTO students("
                        "student_identifier, student_name, faculty_id, class_id)"
                        "VALUES(?,?,?,?)",
                        (student_id, student_name, faculty_id, class_id))

    def _create_marks_table(self):
        with SQLite(self.db_name) as cur:
            cur.execute("CREATE TABLE if not exists marks("
                        "mark_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                        "subject VARCHAR NOT NULL, "
                        "mark TINYINT NOT NULL,"
                        "student_id INTEGER,"
                        "FOREIGN KEY(student_id) REFERENCES students(id))")

    def add_mark(self, subject, mark, student_id):
        self._create_marks_table()
        with SQLite(self.db_name) as cur:
            cur.execute("INSERT INTO marks("
                        "subject, mark, student_id)"
                        "VALUES(?,?,?)",
                        (subject, mark, student_id))


if __name__ == '__main__':
    user = User()
    print(user.get_all_students())
    print(user.get_student_by_id('MN-12'))
    print(user.get_all_students_info())
    print(user.get_excellent_students())
