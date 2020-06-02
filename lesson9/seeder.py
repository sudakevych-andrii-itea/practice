import random

from sqlite_context_manager import SQLite

names_list = ['Taonga', 'Makensie', 'Lasse', 'Oryn', 'Sambrid', 'Eiddon', 'Jahy', 'Heyden', 'Abir', 'Celik', 'Gurwinder', 'Meko', 'Vasyl', 'Haider', 'Musse', 'Phoenix', 'Lucais', 'Antonyo', 'Riccardo', 'Ahmad', 'Abubakar', 'Micah', 'Jamaal', 'Gian', 'Aazaan', 'Seane', 'Madison-Jake', 'Bo', 'Antonyo', 'Eli', 'Marcquis', 'Kasey', 'Lukmaan', 'Nick', 'Paolo', 'Marko', 'Zak', 'Lang', 'Dean', 'Blake', 'Kjae', 'Joseph', 'Zachariya', 'Ainslie', 'Kristoffer', 'Kristoffer', 'Inan', 'Iestyn', 'Bryn', 'Marcello', 'Milos', 'Tymon', 'Benoit', 'Kinnon', 'Allesandro', 'Kian-James', 'Filippo', 'Sandro', 'Marcquis', 'Ciann', 'Klevis', 'Kingston', 'Al-Hassan', 'Kaylum', 'Zakaria', 'Bobby', 'Jian', 'Ryan-Lee', 'Atal', 'Harnek', 'Kailin', 'Aaron', 'Jordy', 'Roan', 'Rylan', 'Mati', 'Salvador', 'Ryleigh', 'Ricco', 'Karthikeya', 'Caedyn', 'Calean', 'Bjorn', 'Kyle-Derek', 'Darrel', 'Nicki', 'Tomas', 'Lenyn', 'Marco', 'Uzair', 'Eljon', 'Kruz', 'Yusef', 'Denny', 'Arrham', 'Kelvan', 'Oskar', 'Brydon', 'Kieron', 'Aarman', 'Erik', 'Adie', 'Julian', 'Emmet', 'Dean', 'Malachi', 'Owyn', 'Easton', 'Junior', 'Ambanimoh', 'Darcy', 'Kealan', 'Kal-el', 'Kenan', 'Eason', 'Areez', 'Bailey', 'Cillian', 'Roan', 'Jia', 'Meshach', 'Carl', 'Corey-James', 'Azzedine', 'Hamad', 'Jakub', 'Joojo', 'Eli', 'Mikee', 'Jayhan', 'Shaun', 'Shyam', 'Chrismedi', 'Orrin', 'Cullen', 'Daryn', 'Simon', 'Hendri', 'Maxwell', 'Braydon', 'Walid', 'Keaton', 'Savin', 'Abdisalam', 'Cody-Lee', 'Xin', 'Khevien', 'Chaitanya', 'Axel', 'Kasey', 'Lawrence', 'Lachlainn', 'Lockey', 'Francesco', 'Tisloh', 'Gene', 'Bully', 'Conner', 'Curtis', 'Ahmed', 'Leydon', 'Loukas', 'Han', 'Amrinder', 'Uchenna', 'Aryan', 'Flint', 'Laughlan', 'Coben', 'Aryankhan', 'Rahim', 'Kinnon', 'Sinai', 'Billy', 'Cory', 'Kaidan', 'Rio', 'Zakaria', 'Bailey', 'Caden', 'James-Paul', 'Bailie', 'Kenzi', 'Ronald', 'Devin', 'Ash', 'Darrell', 'Siddharth', 'Maryk', 'Guerin', 'Lincoln-John', 'Cody-Lee', 'Ihtisham', 'Walid', 'Zaki', 'Olivier', 'Hansen', 'Solomon', 'Aryan', 'Moayd']
last_names_list = ['Molina', 'Welch', 'Travis', 'York', 'Kent', 'Pratt', 'Santana', 'Berry', 'King', 'Howe', 'Trujillo', 'Sheppard', 'Dominguez', 'Workman', 'Farley', 'Sweeney', 'Briggs', 'Moore', 'Douglas', 'Myers', 'Kaufman', 'Gomez', 'Fitzgerald', 'Mejia', 'Ayala', 'Moore', 'Riggs', 'Hernandez', 'Vang', 'Leach', 'Green', 'Huber', 'Davis', 'Petersen', 'Horn', 'Butler', 'Houston', 'Pate', 'Young', 'Mooney', 'Brennan', 'Chaney', 'Moses', 'Knox', 'Henderson', 'Hoover', 'Wiley', 'Pace', 'Rivas', 'Blanchard', 'Ward', 'Roman', 'Olsen', 'Snyder', 'Randolph', 'Hogan', 'Sweet', 'Armstrong', 'Yates', 'Moore', 'Patton', 'Everett', 'Ratliff', 'Zimmerman', 'Riley', 'Nash', 'Jimenez', 'Carlson', 'Black', 'Dickerson', 'Mejia', 'Cobb', 'Dalton', 'Randolph', 'Weaver', 'Paul', 'Hall', 'Kirk', 'Brewer', 'Mcintosh', 'Conrad', 'Cline', 'Reese', 'Wallace', 'Taylor', 'Nguyen', 'Wallace', 'Schneider', 'Morse', 'Middleton', 'Fowler', 'Day', 'Park', 'Sears', 'Jones', 'Cline', 'Hopkins', 'Daniels', 'Cabrera', 'Greer', 'Wolf', 'Solomon', 'Banks', 'Blanchard', 'Berg', 'Morse', 'Buchanan', 'Reid', 'Craig', 'Hood', 'Conrad', 'Rice', 'Ayers', 'Mcconnell', 'Sandoval', 'Boone', 'Rollins', 'Preston', 'Justice', 'Briggs', 'Lee', 'Booth', 'Heath', 'Armstrong', 'Fernandez', 'Burt', 'Serrano', 'Baxter', 'Quinn', 'Dawson', 'Gilliam', 'Chan', 'Mckinney', 'Gomez', 'Torres', 'Caldwell', 'Bryant', 'Green', 'Chase', 'Stanton', 'Whitney', 'Gould', 'Duran', 'Espinoza', 'Mcclure', 'Terrell', 'Zimmerman', 'Ellison', 'Floyd', 'Bray', 'Giles', 'Odonnell', 'Wyatt', 'Spears', 'Oneill', 'Leach', 'Delacruz', 'Nichols', 'Boone', 'Jackson', 'Mcbride', 'Williamson', 'Barr', 'Floyd', 'Pruitt', 'Roman', 'Black', 'Larson', 'Taylor', 'Powell', 'Mann', 'Wilkerson', 'Rose', 'Whitley', 'Porter', 'Simmons', 'Villarreal', 'Vinson', 'Chambers', 'Jefferson', 'Watts', 'Nunez', 'Dodson', 'Lane', 'Salas', 'Shannon', 'Foley', 'Briggs', 'Harrell', 'Chen', 'White', 'Snider', 'Allen', 'Mack', 'Steele', 'Burke', 'Holden', 'Herrera', 'Cotton', 'Castaneda']


class CuratorsSeeder:
    def __init__(self, names, last_names):
        self.names = names
        self.last_names = last_names

    @staticmethod
    def _create_curators_table():
        with SQLite('students.db') as cur:
            cur.execute("CREATE TABLE if not exists curators("
                        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                        "name VARCHAR NOT NULL, "
                        "last_name VARCHAR NOT NULL)")

    def create_curators_data(self, count):
        self._create_curators_table()
        for _ in range(count):
            with SQLite('students.db') as cur:
                cur.execute("INSERT INTO curators(name, last_name) VALUES(?,?)",
                            (random.choice(self.names), random.choice(self.last_names),))


class StudentsSeeder:
    def __init__(self, names, last_names):
        self.names = names
        self.last_names = last_names

    @staticmethod
    def _get_faculties():
        with SQLite('students.db') as cur:
            cur.execute("SELECT id FROM faculties")
            return [item for sub in cur.fetchall() for item in sub]

    @staticmethod
    def _get_faculties_classes(faculty_id):
        with SQLite('students.db') as cur:
            cur.execute("SELECT GROUP_CONCAT(classes.id) "
                        "FROM faculties "
                        "INNER JOIN classes ON(classes.faculty_id = faculties.id) "
                        "WHERE faculties.id=?", (faculty_id,))
            return [int(item) for sub in cur.fetchone() for item in sub.split(',')]

    @staticmethod
    def _get_curators():
        with SQLite('students.db') as cur:
            cur.execute("SELECT id FROM curators")
            return [item for sub in cur.fetchall() for item in sub]

    @staticmethod
    def _create_students_table():
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

    def create_students_data(self, count):
        self._create_students_table()
        for _ in range(count):
            faculty_id = random.choice(self._get_faculties())
            class_id = random.choice(self._get_faculties_classes(faculty_id))
            curator_id = random.choice(self._get_curators())
            with SQLite('students.db') as cur:
                cur.execute("INSERT INTO students("
                            "name, last_name, "
                            "faculty_id, class_id, curator_id) "
                            "VALUES(?,?,?,?,?)",
                            (random.choice(self.names), random.choice(self.last_names),
                             faculty_id, class_id, curator_id))


class MarksSeeder:
    @staticmethod
    def _get_students():
        with SQLite('students.db') as cur:
            cur.execute("SELECT id FROM students")
            return [item for sub in cur.fetchall() for item in sub]

    @staticmethod
    def _create_table_marks():
        with SQLite('students.db') as cur:
            cur.execute("CREATE TABLE if not exists marks("
                        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                        "mark TINYINT NOT NULL, "
                        "subject_id VARCHAR NOT NULL,"
                        "student_id INTEGER,"
                        "FOREIGN KEY(subject_id) REFERENCES subjects(id), "
                        "FOREIGN KEY(student_id) REFERENCES students(id))")

    def create_marks_data(self, subject_id):
        self._create_table_marks()
        for i in self._get_students():
            mark = random.randrange(10, 101)
            with SQLite('students.db') as cur:
                cur.execute("INSERT INTO marks("
                            "mark, subject_id, student_id)"
                            "VALUES(?,?,?)",
                            (mark, subject_id, i))
