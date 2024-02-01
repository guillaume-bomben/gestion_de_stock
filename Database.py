import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connect_posible = False
        self.try_connect()


    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()

    def executeQuery(self, query, params=None):
        self.connect()
        self.cursor.execute(query, params or ())
        self.connection.commit()
        self.disconnect()

    def fetch(self, query, params=None):
        self.connect()
        self.cursor.execute(query, params or ())
        result = self.cursor.fetchall()
        self.disconnect()
        return result
    
    def try_connect(self):
        try:
            self.connect()
            print("Connexion réussie à la base de données.")
            self.connect_posible = True
            self.disconnect()
        except mysql.connector.Error as err:
            print(f"Erreur de connexion à la base de données: {err}")