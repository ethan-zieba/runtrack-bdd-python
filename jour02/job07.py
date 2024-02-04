import mariadb

plateforme_database = mariadb.connect(
    host="localhost",
    user="root",
    password="Maria13Pad!"
)

cur = plateforme_database.cursor()
cur.execute("USE entreprise;")

class Database:
    def __init__(self):
        self.__host = "localhost"
        self.__user = "root"
        with open("password.txt", "r") as passwordtxt:
            self.__pw = passwordtxt.read()
            self.__database = "Entreprise"
        self.__connect()

    def __connect(self):
        self.database = mariadb.connect(
            host=self.__host,
            user=self.__user,
            password=self.__pw,
            autocommit=False,
            database=self.__database
        )

    def request(self, request, updates=False):
        database, cursor = self.database, self.database.cursor()
        cursor.execute(request)
        database.commit()
        if not updates:
            sel = cursor.fetchall()
            print(sel)
        cursor.close()
        database.close()

class Entreprise(Database):
    def __init__(self):
        super().__init__()

    def create_service(self, name):
        self.request(f"INSERT INTO service (nom) VALUES (\'{name}\')", updates=True)

    def get_services(self):
        result = self.request("SELECT * FROM service")
        print("")
        for row in result:
            print(row)

entreprise = Entreprise()
entreprise.get_services()