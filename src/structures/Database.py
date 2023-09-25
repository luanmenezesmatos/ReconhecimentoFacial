import mysql.connector as mysql

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        self.connection = mysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        print("Conectado ao banco de dados!")

    def disconnect(self):
        self.connection.close()

    def insert(self, name, image):
        self.connect()
        self.cursor.execute(
            "INSERT INTO faces (name, image) VALUES (%s, %s)", (name, image))
        self.connection.commit()
        self.disconnect()

    def select(self, name):
        self.connect()
        self.cursor.execute("SELECT image FROM faces WHERE name = %s", (name,))
        result = self.cursor.fetchone()
        self.disconnect()
        return result[0] if result else None

    def selectAll(self):
        self.connect()
        self.cursor.execute("SELECT name, image FROM faces")
        result = self.cursor.fetchall()
        self.disconnect()
        return result

    def delete(self, name):
        self.connect()
        self.cursor.execute("DELETE FROM faces WHERE name = %s", (name,))
        self.connection.commit()
        self.disconnect()
    
    def deleteAll(self):
        self.connect()
        self.cursor.execute("DELETE FROM faces")
        self.connection.commit()
        self.disconnect()

    def update(self, name, image):
        self.connect()
        self.cursor.execute(
            "UPDATE faces SET image = %s WHERE name = %s", (image, name))
        self.connection.commit()
        self.disconnect()